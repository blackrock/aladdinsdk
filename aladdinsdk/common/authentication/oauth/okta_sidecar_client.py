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

import os
import requests
import importlib
import logging

_logger = logging.getLogger(__name__)

STREAMLIT_MODULE_NAME = "streamlit"
STREAMLIT_WEBSOCKET_HEADER_MODULE_NAME = "streamlit.web.server.websocket_headers"
HTTP_HEADER_KEY_DEVELOPER_UID = "Developer-Uid"
_COMPUTE_APP_TYPE = os.environ.get("COMPUTE_APP_TYPE")
OKTA_SIDECAR_SERVER = os.environ.get("OKTA_SIDECAR_SERVER_URL", "http://localhost:8081")
OKTA_SIDECAR_PING_ENDPOINT = f"{OKTA_SIDECAR_SERVER}/v1/ping"
OKTA_SIDECAR_ACCESS_TOKEN_ENDPOINT = f"{OKTA_SIDECAR_SERVER}/v1/access-token"


def get_access_token_ttl_from_okta_sidecar(scopes=None):
    """
    Client for communicating with okta-sidecar server running in aladdin-compute run mode
    If streamlit modules are available, this method will fetch the 'Developer-Uid' from the websocket headers,
    and make a request to Okta Sidecar server to get access token for the user.
    If either of the following are unavailable - streamlit modules / websocket headers / okta-sidecar server - this method will return None

    Args:
        scopes (_type_, required): List of scopes to correctly permission the access token based on api end point call

    Returns:
        access_token: OAuth access token or None
    """
    if scopes is None:
        scopes = []

    developer_uid_from_header = ""
    if _COMPUTE_APP_TYPE == "streamlit":
        developer_uid_from_header = _retrieve_streamlit_websocket_header_developer_uid()
    elif _COMPUTE_APP_TYPE == "dash":
        developer_uid_from_header = _retrieve_dash_header_developer_uid()

    _sidecar_running = _is_okta_sidecar_running()
    if _sidecar_running and developer_uid_from_header is not None:
        access_token, expires_at = _fetch_access_token_from_okta_sidecar(developer_uid=developer_uid_from_header, scopes=scopes)
        return access_token, expires_at

    if developer_uid_from_header is None:
        _logger.debug("Compute App http headers and/or Developer-Uid unavailable. Can not fetch access token from okta-sidecar server.")
    if not _sidecar_running:
        _logger.debug("Unable to ping okta-sidecar server. Can not fetch access token from okta-sidecar server.")

    return None, None


def _retrieve_streamlit_websocket_header_developer_uid():
    """
    Retrieve the 'Developer-Uid' from the streamlit websocket headers if available.
    If streamlit modules or websocket headers are unavailable, return None.

    Returns:
        _type_: developer uid from websocket header or None
    """
    try:
        importlib.import_module(STREAMLIT_MODULE_NAME)
        _websocket_headers_module = importlib.import_module(STREAMLIT_WEBSOCKET_HEADER_MODULE_NAME)
        _streamlit_request_headers = _websocket_headers_module._get_websocket_headers()
        if HTTP_HEADER_KEY_DEVELOPER_UID in _streamlit_request_headers:
            return _streamlit_request_headers[HTTP_HEADER_KEY_DEVELOPER_UID]
    except Exception:
        _logger.debug("Streamlit modules and/or websocket headers not available.")
    return None


def _retrieve_dash_header_developer_uid():
    """
    Retrieve the 'Developer-Uid' from the dash header if available.
    If flask modules or dash header are unavailable, return None.

    Returns:
        _type_: developer uid from dash header or None
    """
    try:
        flask_module = importlib.import_module("flask")
        _dash_request_headers = flask_module.request.headers
        if HTTP_HEADER_KEY_DEVELOPER_UID in _dash_request_headers:
            return _dash_request_headers[HTTP_HEADER_KEY_DEVELOPER_UID]
    except Exception:
        _logger.debug("Dash modules and/or http headers not available.")
    return None


def _is_okta_sidecar_running():
    """
    Check if okta-sidecar server is running

    Returns:
        boolean: True is okta-sidecar server is running, False otherwise
    """
    try:
        response = requests.get(OKTA_SIDECAR_PING_ENDPOINT)
        if response.status_code == 200:
            return True
    except (requests.exceptions.RequestException):
        _logger.debug("Okta-sidecar server not available.")
    return False


def _fetch_access_token_from_okta_sidecar(developer_uid, scopes=[]):
    """
    Fetch access token from okta-sidecar server

    Args:
        developer_uid (string): Developer UID from streamlit websocket headers
        scopes (list): List of scopes

    Raises:
        AsdkOAuthException: Raised when access token retrieval fails

    Returns:
        string: OAuth access token
    """
    params = {
        "developerUid": developer_uid,
        "scopes": ",".join(scopes),
        }
    try:
        response = requests.get(OKTA_SIDECAR_ACCESS_TOKEN_ENDPOINT, params=params)
        response_json = response.json()
        if response.status_code == 200 and 'expiresAt' in response_json and 'accessToken' in response_json:
            return response_json['accessToken'], response_json['expiresAt']
        elif response.status_code == 200 and 'accessToken' in response_json:
            return response_json['accessToken'], None
        else:
            _logger.debug(f'OAuth token retrieval failed. Response:{response.content}')
    except (requests.exceptions.RequestException) as e:
        _logger.debug(f'Problem connecting to authentication server. Error: {e}')
    return None, None
