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
import logging
import uuid
from aladdinsdk.common.authentication.basicauth import basicauthutil
from aladdinsdk.common.authentication.oauth import oauth_token_cred_client, okta_sidecar_client
from aladdinsdk.common.blkutils.blkutils import DEFAULT_WEB_SERVER
from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.common.secrets import fsutil
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload

_logger = logging.getLogger(__name__)
_HEADER_KEY_REQUEST_ID = "VND.com.blackrock.Request-ID"
_HEADER_KEY_ORIGIN_TIMESTAMP = "VND.com.blackrock.Origin-Timestamp"
_AUTHORIZATION_HEADER = "Authorization"
_BEARER_TOKEN_VALUE = "Bearer {}"
_GET_API_OAUTH_CONFIG_VALUE_FROM_USER_SETTINGS = 'user_settings.get_api_oauth_{}()'
_GET_API_OAUTH_CONFIG_FILEPATH_VALUE_FROM_USER_SETTINGS = 'user_settings.get_api_oauth_{}_filepath()'


class ApiAuthUtil():
    """
    API Auth Util class for Aladdin Graph API calls
    """

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def __init__(self,
                 default_web_server=None,
                 configuration=None,
                 token_ttl=None,
                 **kwargs):
        """
        Instantiate an APIAuthUtil instance for a given API call.
        User may pass in optional parameters to override default values or values derived from configured user settings.

        Priority order:
        - Value passed in API Client instantiation
        - Value set as environment variable
        - Value set in user settings file

        Args:
            default_web_server (_type_, optional): Default web server. Defaults to os.environ.get("defaultWebServer").
            api_key (_type_, optional): API Key. Defaults to value set as "ASDK_API__TOKEN" environment variable, or "api.token" in settings yaml,
                None if not configured.
            configuration (_type_, optional): API confiuration. Defaults to value None if not configured.
            auth_type (_type_, optional): API Authentication Type. Must be in ["Basic Auth", "OAuth"]. Defaults to value set as "ASDK_API__AUTH_TYPE"
                or "api.auth_type" in settings yaml.
            auth_flow_type (_type_, optional): : API Authentication Type. Must be in ["refresh_token", "client_credentials"]. Defaults to value set
                as "ASDK_API__AUTH_FLOW_TYPE" or "api.auth_flow_type" in settings yaml.
            username (_type_, optional): Username. Defaults to value set as "ASDK_USER_CREDENTIALS__USERNAME" environment variable, or
                "user_credentials.username" in settings yaml, None if not configured.
            password (_type_, optional): Password. Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD" environment variable, or
                "user_credentials.password" in settings yaml, None if not configured.
            client_id (_type_, optional): Client Id for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_ID" environment variable, or
                "oauth.client_id" in settings yaml, None if not configured.
            client_secret (_type_, optional): Client Secret for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_SECRET" environment
                variable, or "oauth.client_secret" in settings yaml, None if not configured.
            refresh_token (_type_, optional): Refresh token to use for oauth token uri. Defaults to value set as "ASDK_OAUTH__REFRESH_TOKEN"
                environment variable, or "oauth.refresh_token" in settings yaml, None if not configured.
            api_access_token (_type_, optional): Access token to use for oauth. Defaults to None
            token_ttl (_type_, optional): Token TTL for oauth access token. Defaults to None
            auth_server_proxy (_type_, optional): API Auth Server Proxy for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_PROXY"
                environment variable, or "oauth.auth_server_proxy" in settings yaml, None if not configured.
            auth_server_url (_type_, optional): API Auth Server URL for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_URL" environment
                variable, or "oauth.auth_server_url" in settings yaml, None if not configured.
            password_filepth (_type_, optional): Basic Auth Password Filepath. Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH"
                environment variable, or "user_credentials.password_filepath" settings yaml, None is not configured.
            encrypted_password_filepath (_type_, optional): Basic Auth Password Filepath. Defaults to value set as
                "ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH" environment variable, or "user_credentials.encrypted_password_filepath"
                settings yaml, None is not configured.
            encryption_filepath (_type_, optional): Basic Auth Encryption Filepath. Defaults to value set as
                "ASDK_USER_CREDENTIALS__ENCRYPTION_FILEPATH" environment variable, or "user_credentials.encryption_filepath" settings yaml,
                None is not configured.
        """
        default_web_server = DEFAULT_WEB_SERVER if default_web_server is None else default_web_server
        self.default_web_server = default_web_server
        self.configuration = configuration
        self.token_ttl = token_ttl
        self._set_api_fields(**kwargs)

        if self.auth_type not in [user_settings.CONF_API_AUTH_TYPE_BASIC_AUTH, user_settings.CONF_API_AUTH_TYPE_OAUTH]:
            _logger.warning("No valid auth mechanism configured")

        if self.configuration is None:
            _logger.warning("Python code generated API client configuration object must be provided. Required for adding mandatory auth headers.")

        if self.api_key is None and self.auth_type == user_settings.CONF_API_AUTH_TYPE_BASIC_AUTH:
            _logger.warning("API Key not provided. API calls may not succeed.")

        # check if user has provided access token inline or via user settings yaml file
        self.user_provided_api_access_token = self._fetch_oauth_param(self.api_access_token, 'access_token') \
            if self.auth_type == user_settings.CONF_API_AUTH_TYPE_OAUTH else None

    def _set_api_fields(self, **kwargs):
        api_key = kwargs['api_key'] if 'api_key' in kwargs else None
        auth_type = kwargs['auth_type'] if 'auth_type' in kwargs else None
        auth_flow_type = kwargs['auth_flow_type'] if 'auth_flow_type' in kwargs else None
        username = kwargs['username'] if 'username' in kwargs else None
        password = kwargs['password'] if 'password' in kwargs else None
        client_id = kwargs['client_id'] if 'client_id' in kwargs else None
        client_secret = kwargs['client_secret'] if 'client_secret' in kwargs else None
        refresh_token = kwargs['refresh_token'] if 'refresh_token' in kwargs else None
        api_access_token = kwargs['api_access_token'] if 'api_access_token' in kwargs else None
        auth_server_proxy = kwargs['auth_server_proxy'] if 'auth_server_proxy' in kwargs else None
        auth_server_url = kwargs['auth_server_url'] if 'auth_server_url' in kwargs else None
        password_filepath = kwargs['password_filepath'] if 'password_filepath' in kwargs else None
        encrypted_password_filepath = kwargs['encrypted_password_filepath'] if 'encrypted_password_filepath' in kwargs else None
        encryption_filepath = kwargs['encryption_filepath'] if 'encryption_filepath' in kwargs else None

        self.api_key = api_key
        self.auth_type = auth_type
        self.auth_flow_type = auth_flow_type
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.api_access_token = api_access_token
        self.auth_server_proxy = auth_server_proxy
        self.auth_server_url = auth_server_url
        self.password_filepath = password_filepath
        self.encrypted_password_filepath = encrypted_password_filepath
        self.encryption_filepath = encryption_filepath

    @dynamic_asdk_config_reload
    def add_auth_details_to_header_and_config(self, scopes=None):
        """
        Method for adding api key to config and adding auth details for api call based on auth type: basic/oauth and returns the api headers.
        In case of basic auth: adding api key header to configuration + adding basic auth details to configuration + return basic auth headers.
        In case of oauth: adding api key header to configuration + add oauth api access token to auth header + return oauth headers.

        Args:
            scopes (_type_, optional): list of scopes for the api endpoint being called

        Returns:
            Map: request headers for the api call
        """
        request_headers = build_request_headers()

        # Note: api key will be phased out eventually by agraph team
        add_api_key_header_to_configuration(self.configuration, self.api_key)

        if self.auth_type == user_settings.CONF_API_AUTH_TYPE_BASIC_AUTH:
            _logger.debug("Basic Auth Configured for APIs.")
            if self.password is None:
                _logger.debug("Password not provided during API client initialization, fetching from configuration file.")
                self.password = basicauthutil.fetch_password_from_user_settings(self.password_filepath,
                                                                                self.encrypted_password_filepath,
                                                                                self.encryption_filepath)
            basicauthutil.add_basic_auth_details_to_configuration(self.configuration,
                                                                  username=self.username,
                                                                  password=self.password)
        elif self.auth_type == user_settings.CONF_API_AUTH_TYPE_OAUTH:
            access_token = self._fetch_oauth_token_for_api_call(scopes)
            request_headers[_AUTHORIZATION_HEADER] = _BEARER_TOKEN_VALUE.format(access_token)

        return request_headers

    def _fetch_oauth_token_for_api_call(self, scopes=None):
        """
        Method for fetching oauth access token to be used for making api calls
        In case access token is provided by the user: proceed with that token and return its value
        In case access token is not provided by the user: request oauth access token from oauth server or okta-sidecar (if running in compute mode)

        Args:
            scopes (_type_, optional): list of scopes for the api endpoint being called

        Returns:
            String: Oauth Access Token to be used for api calls
        """
        token = None

        if self.user_provided_api_access_token is not None:
            _logger.debug("Utilizing OAuth access token provided by user.")
            token = self.user_provided_api_access_token
        else:
            _logger.debug("Fetching OAuth access token from auth server.")
            new_oauth_access_token_tuple = self._request_oauth_access_token_tuple(scopes)
            self._update_oauth_access_token(new_oauth_access_token_tuple)
            token = self.api_access_token

        if token is None:
            raise AsdkOAuthException("No valid access token for OAuth found!!!")
        else:
            return token

    def _update_oauth_access_token(self, oauth_access_token_resp_tuple):
        """
        Method for updating the api oauth access token.

        Args:
            oauth_access_token_resp_tuple (_type_, required): tuple containing access token and its expiry in
        """
        if oauth_access_token_resp_tuple is None or len(oauth_access_token_resp_tuple) < 2 or oauth_access_token_resp_tuple == (None, None):
            _logger.warning("Incomplete/inaccurate access token details received from auth server. API calls may fail.")
            self.token_ttl = None
            self.api_access_token = None
            return

        # update access token
        self.api_access_token = oauth_access_token_resp_tuple[0]

        # update ttl
        oauth_response_ttl = oauth_access_token_resp_tuple[1]
        if oauth_response_ttl is not None and isinstance(oauth_response_ttl, int):
            # ttl from auth server is seconds until expiry
            curr_timestamp = datetime.datetime.utcnow()
            self.token_ttl = curr_timestamp + datetime.timedelta(seconds=oauth_response_ttl)
        elif oauth_response_ttl is not None and isinstance(oauth_response_ttl, datetime.datetime):
            # ttl from auth server is expiry timestamp
            self.token_ttl = oauth_response_ttl
        else:
            self.token_ttl = None

    def _request_oauth_access_token_tuple(self, scopes):
        """
        Method for fetching oauth params required that are used to get an api access token from the oauth server
        In case any of following are none: (client_id, client_secret, refresh_token) then attempt requesting access token from okta-sidecar
        If access token is not available via either mechanism, raise appropriate AsdkOAuthException

        Args:
            scopes (_type_, optional): Scopes for the api endpoint (used for fetching oauth access token)

        Returns:
            Tuple: Tuple containing the oauth access token and token ttl
        """
        client_id = self._fetch_oauth_param(self.client_id, 'client_id')
        client_secret = self._fetch_oauth_param(self.client_secret, 'client_secret')
        refresh_token = self._fetch_oauth_param(self.refresh_token, 'refresh_token')

        access_token_ttl_tuple_from_auth_server = oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server(client_id,
                                                                                                                     client_secret,
                                                                                                                     refresh_token,
                                                                                                                     scopes,
                                                                                                                     self.auth_flow_type,
                                                                                                                     self.auth_server_proxy,
                                                                                                                     self.auth_server_url)
        if access_token_ttl_tuple_from_auth_server != (None, None):
            _logger.debug("Access token retrieved from OAuth server")
            return access_token_ttl_tuple_from_auth_server

        _logger.debug("Unable to fetch access token from oauth server. Attempting to fetch access token from okta-sidecar server.")
        access_token_ttl_tuple_from_okta_sidecar = okta_sidecar_client.get_access_token_ttl_from_okta_sidecar(scopes)
        if access_token_ttl_tuple_from_okta_sidecar != (None, None):
            _logger.debug("Access token retrieved from okta-sidecar")
            return access_token_ttl_tuple_from_okta_sidecar

        _logger.debug("Unable to fetch access token from either oauth server or okta-sidecar server. Refer to debug logs for more information.")
        return None, None

    @dynamic_asdk_config_reload
    def _fetch_oauth_param(self, param_value, param_name):
        """
        Method for fetching an oauth param for API Oauth Type (responsible for fetching client id/client secret/refresh token/oauth access token)
        First the method checks for inline/params values passed in by user when initializing the API client
        Next the method checks for values set in the config by the user
        Last the method check for a filepath set in the config by the user
        This method assumes the DYNACONF user settings get methods for fetching a config key value follows the format:
            get_api_oauth_OAUTH_PARAM_NAME_HERE()
        This method also assumes the DYNACONF user settings get methods for fetching a config key value filepath follows the format:
            get_api_oauth_OAUTH_PARAM_NAME_HERE_filepath()

        Args:
            param_value (_type_, required): oauth param value
            param_name (_type_, required): oauth param name

        Returns:
            Tuple: Tuple containing the oauth access token and token ttl
        """
        if param_value is not None:
            _logger.debug(f"Providing oauth ::{param_name} from user input")
            return param_value

        if param_value is None:
            _logger.debug(f"Checking oauth ::{param_name} from config file value")
            string_val = _GET_API_OAUTH_CONFIG_VALUE_FROM_USER_SETTINGS.format(param_name)
            param_value = eval(string_val)

        if param_value is None:
            _logger.debug(f"Checking oauth ::{param_name} from config file filepath value")
            if param_name == "client_id" or param_name == "client_secret":
                string_val = _GET_API_OAUTH_CONFIG_FILEPATH_VALUE_FROM_USER_SETTINGS.format("client_details")
            else:
                string_val = _GET_API_OAUTH_CONFIG_FILEPATH_VALUE_FROM_USER_SETTINGS.format(param_name)
            if eval(string_val) is not None:
                # secret file yaml structure contains following keys: id, secret, token, <url, encryption>
                if "_" in param_name:
                    # if param_name is client_id, client_secret, refresh_token
                    key = param_name.split("_")[-1]
                else:
                    key = param_name
                param_value = fsutil.read_secret_from_yaml_file(eval(string_val), key)
        return param_value


# GENERIC API HELPERS
def build_request_headers():
    """
    Unique request headers for each request.
    The timestamp and request-ID are generated at the time of making a request

    Returns:
        JSON: Request headers with unique Request-ID and Origin-Timestamp
    """
    unique_request_origin_id = str(uuid.uuid1())
    curr_timestamp = datetime.datetime.utcnow().replace(microsecond=0).replace(tzinfo=datetime.timezone.utc).isoformat()
    api_request_headers = {
        _HEADER_KEY_REQUEST_ID: unique_request_origin_id,
        _HEADER_KEY_ORIGIN_TIMESTAMP: curr_timestamp,
    }
    return api_request_headers


def add_api_key_header_to_configuration(configuration, api_key=None):
    """
    Given an API instance configuration, set APIKeyHeader.

    Priority order:
    - Key set in API Client instantiation
    - Key set as environment variable config
    - Key set in user settings file

    Args:
        configuration (_type_): _description_

    Raises:
        Exception: _description_
        Exception: _description_
    """
    if api_key is not None:
        configuration.api_key = {
            'APIKeyHeader': api_key
        }


def inflate_api_kwargs(kwargs):
    """
    Given API/ADC initialization kwargs, fill in any missing values from user settings
    The resulting kwargs will be used to initialize the API client object

    Args:
        kwargs (_type_): _description_

    Returns:
        _type_: _description_
    """
    _inflate_api_basic_auth_kwargs(kwargs)
    _inflate_api_oauth_kwargs(kwargs)
    if 'api_key' not in kwargs and user_settings.get_api_token() is not None:
        kwargs['api_key'] = user_settings.get_api_token()
    if 'auth_type' not in kwargs and user_settings.get_api_auth_type() is not None:
        kwargs['auth_type'] = user_settings.get_api_auth_type()
    if 'username' not in kwargs and user_settings.get_username() is not None:
        kwargs['username'] = user_settings.get_username()

    if kwargs['auth_type'] == user_settings.CONF_API_AUTH_TYPE_OAUTH and 'auth_flow_type' not in kwargs:
        kwargs['auth_flow_type'] = user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN

    return kwargs


def _inflate_api_basic_auth_kwargs(kwargs):
    """
    Helper to fill in any missing values for basic auth related kwargs

    Args:
        kwargs (_type_): _description_
    """
    if 'password' not in kwargs and user_settings.get_user_password() is not None:
        kwargs['password'] = user_settings.get_user_password()
    if 'password_filepath' not in kwargs and user_settings.get_password_filepath() is not None:
        kwargs['password_filepath'] = user_settings.get_password_filepath()
    if 'encrypted_password_filepath' not in kwargs and user_settings.get_encrypted_password_filepath() is not None:
        kwargs['encrypted_password_filepath'] = user_settings.get_encrypted_password_filepath()
    if 'encryption_filepath' not in kwargs and user_settings.get_encryption_filepath() is not None:
        kwargs['encryption_filepath'] = user_settings.get_encryption_filepath()


def _inflate_api_oauth_kwargs(kwargs):
    """
    Helper to fill in any missing values for oauth related kwargs

    Args:
        kwargs (_type_): _description_
    """
    if 'auth_flow_type' not in kwargs and user_settings.get_api_auth_flow_type() is not None:
        kwargs['auth_flow_type'] = user_settings.get_api_auth_flow_type()
    if 'client_id' not in kwargs and user_settings.get_api_oauth_client_id() is not None:
        kwargs['client_id'] = user_settings.get_api_oauth_client_id()
    if 'client_secret' not in kwargs and user_settings.get_api_oauth_client_secret() is not None:
        kwargs['client_secret'] = user_settings.get_api_oauth_client_secret()
    if 'refresh_token' not in kwargs and user_settings.get_api_oauth_refresh_token() is not None:
        kwargs['refresh_token'] = user_settings.get_api_oauth_refresh_token()
    if 'api_access_token' not in kwargs and user_settings.get_api_oauth_access_token() is not None:
        kwargs['api_access_token'] = user_settings.get_api_oauth_access_token()
    if 'auth_server_proxy' not in kwargs and user_settings.get_api_oauth_auth_server_proxy() is not None:
        kwargs['auth_server_proxy'] = user_settings.get_api_oauth_auth_server_proxy()
    if 'auth_server_url' not in kwargs and user_settings.get_api_oauth_auth_server_url():
        kwargs['auth_server_url'] = user_settings.get_api_oauth_auth_server_url()
