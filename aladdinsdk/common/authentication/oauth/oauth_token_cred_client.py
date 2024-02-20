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

import requests
import logging
from aladdinsdk.common.blkutils.blkutils import DEFAULT_WEB_SERVER, SDK_HELP_MESSAGE_SUFFIX
from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
from aladdinsdk.config import user_settings

_logger = logging.getLogger(__name__)


def get_access_token_and_ttl_from_oauth_server(client_id=None, client_secret=None, refresh_token=None, scopes=None,
                                               auth_flow_type=None, auth_server_proxy=None, auth_server_url=None):
    """
    Client for communicating with oauth server to fetch a fresh access token to be used for api calls

    Args:
        client_id (_type_, required): Client Id for Oauth Application
        client_secret (_type_, required): Client Secret for Oauth Application
        refresh_token (_type_, required): Refresh token for user already signed into Application being used to make api calls
        scopes (_type_, required): List of scopes to correctly permission the access token based on api end point call
        auth_flow_type (_type_, required): Auth flow to use to fetch access token (Client Credentials/Refresh Token)
        auth_server_proxy (_type_, optional): Proxy to use when fetching access token
        auth_server_url (_type_, optional): Auth server url to use when fetching access token

    Returns:
        pair(access_token, token_expiry): Pair of access token and its expiry time
    """
    access_token_ttl_tuple = None, None
    try:
        if (client_id and client_secret) is None and auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS:
            raise AsdkOAuthException("Missing Oauth value(s): "
                                     f"client-id/client-secret for auth flow type = client credentials. {SDK_HELP_MESSAGE_SUFFIX}")
        if (client_id and client_secret and refresh_token) is None and auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN:
            raise AsdkOAuthException("Missing Oauth value(s): "
                                     f"client-id/client-secret/refresh-token for auth flow type = refresh token. {SDK_HELP_MESSAGE_SUFFIX}")
        if (refresh_token == "<no value>") and auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN:
            raise AsdkOAuthException("Missing refresh token. "
                                     f"Please login to studio application to create refresh token. {SDK_HELP_MESSAGE_SUFFIX}")

        access_token_ttl_tuple = _retrieve_token_details(client_id, client_secret, refresh_token, auth_flow_type,
                                                         scopes, auth_server_proxy, auth_server_url)
    except AsdkOAuthException as e:
        _logger.debug(f"Failed to retrieve access token from oauth server. Error: {e}")
    return access_token_ttl_tuple


def _retrieve_token_details(client_id, client_secret, refresh_token, auth_flow_type, scopes=None, auth_server_proxy=None, auth_server_url=None):
    """
    Given oauth client and user secrets, make a request to the auth server for an access token
    If not already present 'offline_access' is added to scopes list

    Args:
        client_id (_type_, required): Client Id for Oauth Application
        client_secret (_type_, required): Client Secret for Oauth Application
        refresh_token (_type_, required): Refresh token for user already signed into Application being used to make api calls
        scopes (_type_, required): List of scopes to correctly permission the access token based on api end point call
        auth_flow_type (_type_, required): Auth flow to use to fetch access token (Client Credentials/Refresh Token)
        auth_server_proxy (_type_, optional): Proxy to use when fetching access token
        auth_server_url (_type_, optional): Auth server url to use when fetching access token

    Raises:
        AsdkOAuthException: _description_

    Returns:
        pair(access_token, token_expiry): Pair of access token and its expiry time
    """
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }

    if scopes is None:
        scopes = []

    data = _construct_data_for_token_request(auth_flow_type, client_id, client_secret, refresh_token, scopes)
    url = _get_token_url_for_auth_server(auth_server_url)
    _proxies = _get_proxy_for_auth_server(auth_server_proxy)

    try:
        response = requests.post(url, headers=headers, params=data, verify=True, proxies=_proxies)
        if response.status_code == 200:
            return _get_oauth_access_token_and_ttl_from_response(response.json())
        else:
            raise AsdkOAuthException('OAuth token retrieval failed', response.content)
    except (requests.exceptions.RequestException) as e:
        raise AsdkOAuthException('Problem connecting to authentication server', e)


def _get_oauth_access_token_and_ttl_from_response(response_json):
    """
    Given the response from the oauth server, parse it to determine the access token and expires in values

    Args:
        response_json (_type_, required): Response json from auth server

    Raises:
        AsdkOAuthException: _description_

    Returns:
        pair(access_token, token_expiry): Pair of access token and its expiry time
    """
    try:
        return response_json['access_token'], response_json['expires_in']
    except (AttributeError, KeyError) as e:
        raise AsdkOAuthException('Failed to retrieve oauth access token and token expiry time from server', e)


def _get_token_url_for_auth_server(auth_server_url=None):
    """
    Method for constructing the token auth url based on the client environment the aladdinsdk is currently being run in

    Args:
        auth_server_url (_type_, optional): Auth server url

    Returns:
        String: OAuth server url
    """
    user_settings_token_auth_url_pattern = '{}/v1/token'
    if auth_server_url is not None:
        return user_settings_token_auth_url_pattern.format(auth_server_url)
    user_setting_auth_url = user_settings.get_api_oauth_auth_server_url()
    if user_setting_auth_url is not None:
        return user_settings_token_auth_url_pattern.format(user_setting_auth_url)

    token_auth_url_pattern = '{}/api/oauth2/default/v1/token'
    return token_auth_url_pattern.format(DEFAULT_WEB_SERVER)


def _get_proxy_for_auth_server(auth_server_proxy=None):
    """
    Method for constructing the auth server proxy list

    Args:
        auth_server_url (_type_, optional): Auth server url

    Returns:
        String: OAuth server url
    """
    _proxies = {}
    configured_oauth_proxy = user_settings.get_api_oauth_auth_server_proxy()
    if configured_oauth_proxy is not None:
        # if user provided proxy through config
        _proxies["https"] = configured_oauth_proxy
    if auth_server_proxy is not None:
        # if user provided proxy from api client
        _proxies["https"] = auth_server_proxy
    return _proxies


def _construct_data_for_token_request(auth_flow_type, client_id, client_secret, refresh_token=None, scopes=[]):
    """
    Given oauth client and user secrets, construct a request for an access token

    Args:
        auth_flow_type (_type_, required): Auth flow to use to fetch access token (Client Credentials/Refresh Token)
        client_id (_type_, required): Client Id for Oauth Application
        client_secret (_type_, required): Client Secret for Oauth Application
        refresh_token (_type_, required): Refresh token for user already signed into Application being used to make api calls
        scopes (_type_, required): List of scopes to correctly permission the access token based on api end point call

    Returns:
        map: request data
    """
    data = {
        'grant_type': auth_flow_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'scopes': scopes
    }
    if auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN and refresh_token is not None:
        data['refresh_token'] = refresh_token
    if auth_flow_type is None and refresh_token is not None:
        data['grant_type'] = user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN
    return data
