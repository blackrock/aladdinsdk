"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
import importlib
import logging
import os

import requests

_logger = logging.getLogger(__name__)

STREAMLIT_MODULE_NAME = "streamlit"
STREAMLIT_WEBSOCKET_HEADER_MODULE_NAME = "streamlit.web.server.websocket_headers"
HTTP_HEADER_KEY_SESSION_ID = "X-Session-Id"
_COMPUTE_APP_TYPE = os.environ.get("COMPUTE_APP_TYPE")
LOCAL_TOKEN_SERVER = os.environ.get("ASDK_LOCAL_TOKEN_SERVER_URL", "http://127.0.0.1:9091")
LOCAL_TOKEN_SERVER_LIVENESS_ENDPOINT = f"{LOCAL_TOKEN_SERVER}/v1/liveness"
LOCAL_TOKEN_SERVER_TOKEN_ENDPOINT = f"{LOCAL_TOKEN_SERVER}/token"


def get_access_token_ttl_from_local_token_server(scopes=None):
    """
    Client for communicating with the gateway's local token server running in aladdin-compute run mode.
    The gateway middleware injects the 'X-Session-Id' header on every proxied request; this client
    reads that header from the incoming streamlit/dash request and forwards it to the local token
    server to fetch the session's current access token.

    If either of the following are unavailable - streamlit/flask modules / X-Session-Id header /
    local token server - this method will return (None, None).

    :param scopes: List of scopes to validate against the gateway's configured OAuth scope allow-list,
        defaults to None
    :type scopes: list, optional
    :returns: OAuth access token and expiration time, or (None, None) if unavailable
    :rtype: tuple[str, datetime.datetime] or tuple[None, None]
    """
    if scopes is None:
        scopes = []

    session_id_from_header = ""
    if _COMPUTE_APP_TYPE == "streamlit":
        session_id_from_header = _retrieve_streamlit_websocket_header_session_id()
    elif _COMPUTE_APP_TYPE == "dash":
        session_id_from_header = _retrieve_dash_header_session_id()

    _server_running = _is_local_token_server_running()
    if _server_running and session_id_from_header is not None:
        access_token, expires_at = _fetch_access_token_from_local_token_server(session_id=session_id_from_header, scopes=scopes)
        return access_token, expires_at

    if session_id_from_header is None:
        _logger.debug("Compute App http headers and/or X-Session-Id unavailable. Can not fetch access token from local token server.")
    if not _server_running:
        _logger.debug("Unable to ping local token server. Can not fetch access token from local token server.")

    return None, None


def _retrieve_streamlit_websocket_header_session_id():
    """
    Retrieve the 'X-Session-Id' from the streamlit context headers if available.
    If streamlit modules or context headers are unavailable, return None.

    :returns: session id from context headers or None
    :rtype: str or None
    """
    # Preferred path: Streamlit >= 1.37 public context headers API.
    try:
        streamlit_module = importlib.import_module(STREAMLIT_MODULE_NAME)
        context = getattr(streamlit_module, "context", None)
        headers = getattr(context, "headers", None) if context is not None else None
        if headers and HTTP_HEADER_KEY_SESSION_ID in headers:
            return headers[HTTP_HEADER_KEY_SESSION_ID]
    except Exception:
        _logger.debug("Streamlit modules and/or context headers not available.")

    # Fallback path: older Streamlit private websocket headers API.
    try:
        importlib.import_module(STREAMLIT_MODULE_NAME)
        websocket_headers_module = importlib.import_module(STREAMLIT_WEBSOCKET_HEADER_MODULE_NAME)
        streamlit_request_headers = websocket_headers_module._get_websocket_headers()
        if streamlit_request_headers and HTTP_HEADER_KEY_SESSION_ID in streamlit_request_headers:
            return streamlit_request_headers[HTTP_HEADER_KEY_SESSION_ID]
    except Exception:
        _logger.debug("Legacy streamlit websocket headers not available.")

    return None


def _retrieve_dash_header_session_id():
    """
    Retrieve the 'X-Session-Id' from the dash header if available.
    If flask modules or dash header are unavailable, return None.

    :returns: session id from dash header or None
    :rtype: str or None
    """
    try:
        flask_module = importlib.import_module("flask")
        _dash_request_headers = flask_module.request.headers
        if HTTP_HEADER_KEY_SESSION_ID in _dash_request_headers:
            return _dash_request_headers[HTTP_HEADER_KEY_SESSION_ID]
    except Exception:
        _logger.debug("Dash modules and/or http headers not available.")
    return None


def _is_local_token_server_running():
    """
    Check if the local token server is running by pinging its liveness endpoint.

    :returns: True if local token server is running, False otherwise
    :rtype: bool
    """
    try:
        response = requests.get(LOCAL_TOKEN_SERVER_LIVENESS_ENDPOINT)
        if response.status_code == 200:
            return True
    except (requests.exceptions.RequestException) as e:
        _logger.debug("Local token server not available: %r", e)
    return False


def _fetch_access_token_from_local_token_server(session_id, scopes=[]):
    """
    Fetch access token from the gateway's local token server.

    :param session_id: Session id read from the incoming request's X-Session-Id header
    :type session_id: str
    :param scopes: List of scopes, defaults to []
    :type scopes: list, optional
    :returns: OAuth access token and expiration time, or (None, None) if retrieval fails
    :rtype: tuple[str, datetime.datetime] or tuple[None, None]
    """
    headers = {HTTP_HEADER_KEY_SESSION_ID: session_id}
    params = {}
    if scopes:
        params["scopes"] = ",".join(scopes)
    try:
        response = requests.get(LOCAL_TOKEN_SERVER_TOKEN_ENDPOINT, params=params, headers=headers)
        if response.status_code != 200:
            _logger.debug(f'OAuth token retrieval failed. Response:{response.content}')
            return None, None
        response_json = response.json()
        access_token = response_json.get('access_token')
        if not access_token:
            _logger.debug(f'OAuth token retrieval response missing access_token. Response:{response.content}')
            return None, None
        expires_at_raw = response_json.get('expires_at')
        expires_at = _parse_expires_at(expires_at_raw) if expires_at_raw else None
        return access_token, expires_at
    except (requests.exceptions.RequestException) as e:
        _logger.debug(f'Problem connecting to authentication server. Error: {e}')
    return None, None


def _parse_expires_at(expires_at_raw):
    """
    Parse the RFC3339 expires_at value returned by the local token server.

    :param expires_at_raw: RFC3339 timestamp string
    :type expires_at_raw: str
    :returns: parsed datetime or None
    :rtype: datetime.datetime or None
    """
    try:
        # Python 3.7+ fromisoformat does not accept a trailing 'Z'; normalize it.
        normalized = expires_at_raw.replace('Z', '+00:00') if isinstance(expires_at_raw, str) else expires_at_raw
        # Go marshals time.Time with nanosecond precision (up to 9 fractional digits),
        # but Python < 3.11 fromisoformat only supports up to 6 (microseconds).
        # Truncate fractional seconds to 6 digits for compatibility.
        import re
        normalized = re.sub(r'(\.\d{6})\d+', r'\1', normalized)
        return datetime.datetime.fromisoformat(normalized)
    except (TypeError, ValueError):
        _logger.debug(f'Unable to parse expires_at value from local token server: {expires_at_raw}')
        return None
