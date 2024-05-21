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
import re
import asyncio
import json
import inspect
import jsonpath_ng
from urllib.parse import urljoin
from collections import namedtuple
from aladdinsdk.api.registry import get_api_details
from aladdinsdk.common.authentication.api import _HEADER_KEY_ORIGIN_TIMESTAMP, _HEADER_KEY_REQUEST_ID, ApiAuthUtil
from aladdinsdk.common.blkutils.blkutils import DEFAULT_WEB_SERVER
from aladdinsdk.common.authentication.api import inflate_api_kwargs
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.common.error.asdkerrors import AsdkApiException
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload
from aladdinsdk.common.datatransformation import json_to_pandas
from aladdinsdk.common.retry.api_retry import api_retry
import logging

_logger = logging.getLogger(__name__)

_ASDK_USER_AGENT_PATTERN = 'AladdinSDK-{}/1.0.0/python'
_DEFAULT_SDK_USER_AGENT_SUFFIX = 'Core'

_HttpEndpointDescription = namedtuple("EndpointDescription", ["http_endpoint", "http_method"])

# Switch to enable/disable scopes to be picked from AGraph specs
_api_oauth_scopes_enabled = os.environ.get("AGRAPH_SCOPES_ENABLED", "False").lower() in ('true', '1', 't')


def update_domain_sdk_user_agent_suffix(domain_sdk_suffix):
    """
    Helper method to append domain specific user agent suffix
    """
    global _DEFAULT_SDK_USER_AGENT_SUFFIX
    regex = r"^[a-zA-Z0-9\.\/]+$"
    if re.match(regex, domain_sdk_suffix) is not None and len(domain_sdk_suffix) > 0 and len(domain_sdk_suffix) <= 15:
        _DEFAULT_SDK_USER_AGENT_SUFFIX = domain_sdk_suffix
        _logger.debug(f"Updating SDK user agent to {_ASDK_USER_AGENT_PATTERN.format(_DEFAULT_SDK_USER_AGENT_SUFFIX)}")
    else:
        raise AsdkApiException("User Agent suffix should be alphanumeric string of max length 15.")


class AladdinAPI():
    """
    API Client for Aladdin Graph API calls
    """

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def __init__(self,
                 api_name,
                 default_web_server=DEFAULT_WEB_SERVER,
                 **kwargs):
        """
        Instantiate an API client instance for a given API name.
        User may pass in optional parameters to override default or configured values.

        Priority order:
        - Value passed in API Client instantiation
        - Value set as environment variable
        - Value set in user settings file

        Args:
            api_name (string): Name of the API
            default_web_server (string, optional): Default web server. Defaults to os.environ.get("defaultWebServer").
            auth_flow_type (string, optional): Auth Flow type for oauth token generation. Defaults to user_settings.get_auth_flow_type().
            api_key (string, optional): API Key. Defaults to value set as "ASDK_API__TOKEN" environment variable, or "api.token" in settings yaml,
                None if not configured.
            auth_type (string, optional): API Authentication Type. Must be in [BASIC_AUTH, OAUTH]
            username (string, optional): Username. Defaults to value set as "ASDK_USER_CREDENTIALS__USERNAME" environment variable,
                or "user_credentials.username" in settings yaml, None if not configured.
            password (string, optional): Password. Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD" environment variable,
                or "user_credentials.password" in settings yaml, None if not configured.
            client_id (string, optional): Client Id for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_ID" environment variable,
                or "oauth.client_id" in settings yaml, None if not configured.
            client_secret (string, optional): Client Secret for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_SECRET" environment variable,
                or "oauth.client_secret" in settings yaml, None if not configured.
            refresh_token (string, optional): Refresh token to use for oauth token uri. Defaults to value set as "ASDK_OAUTH__REFRESH_TOKEN"
                environment variable, or "oauth.refresh_token" in settings yaml, None if not configured.
            api_access_token (string, optional): API Authentication token for Oauth. Defaults to None. If no access token provided,
                AladdinSDK will look to client id, secret and refresh token values for fetching access token
            auth_server_proxy (string, optional): API Auth Server Proxy for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_PROXY"
                environment variable, or "oauth.auth_server_proxy" in settings yaml, None if not configured.
            auth_server_url (string, optional): API Auth Server URL for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_URL"
                environment variable, or "oauth.auth_server_url" in settings yaml, None if not configured.
            password_filepath (string, optional): Password filepath (Basic Auth). Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH"
                environment variable, or "user_credentials.password_filepath" in settings yaml, None if not configured.
            encrypted_password_filepath (string, optional): Encrypted Password filepath (Basic Auth). Defaults to value set as
                "ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH" environment variable, or "user_credentials.encrypted_password_filepath" in
                settings yaml, None if not configured.
            encryption_filepath (string, optional): Encryption filepath. Defaults to value set as "ASDK_USER_CREDENTIALS__ENCRYPTED_FILEPATH"
                environment variable, or "user_credentials.encryption_filepath" in settings yaml, None if not configured.
        """
        # Fetch details from registry
        self._details = get_api_details(api_name=api_name)

        # Build API instance from openapi codegen
        configuration = self._details.api_configuration(
            host=urljoin(default_web_server, self._details.host_url_path),
        )
        self.instance = self._build_api_client_instance(configuration)
        self._api_auth_util = ApiAuthUtil(configuration=configuration, **inflate_api_kwargs(kwargs))

        # Prepare additional details for wrapper functionality
        _endpoint_method_mappings = self._generate_swagger_mappings()
        self._endpoint_path_to_method_mappings = _endpoint_method_mappings[0]
        self._endpoint_to_scope_mappings = _endpoint_method_mappings[1]

    def _build_api_client_instance(self, configuration):
        """
        Create and return an instance of the API class

        Args:
            configuration: Codegen API Client Configuration object

        Returns:
            _type_: _description_ - API Class
        """
        # Enter a context with an instance of the API client
        api_client = self._details.api_client(configuration)

        # Update user agent for client
        api_client.user_agent = _ASDK_USER_AGENT_PATTERN.format(_DEFAULT_SDK_USER_AGENT_SUFFIX)

        # Create an instance of the API class
        api_instance = self._details.api_default_class(api_client)

        return api_instance

    def _is_valid_transformation_option(self, asdk_transformation_option):
        """
        Validate transformation options
        """
        is_valid = False
        if asdk_transformation_option is not None and ('type' and 'flatten' in asdk_transformation_option):
            if asdk_transformation_option['type'] in ('json', 'dataframe'):
                is_valid = True
        return is_valid

    def _response_transformation(self, api_response, asdk_transformation_option):
        """
        Handle the mappings to the accurate transformation utilities and perform the transformation
        """
        if asdk_transformation_option['type'] == 'dataframe':
            if not isinstance(api_response, str) and hasattr(api_response, 'json'):
                api_response = api_response.json()
            api_response = json_to_pandas.convert(api_response, asdk_transformation_option['flatten'])
        return api_response

    def _generate_swagger_mappings(self):
        """
        Utility method to parse API swagger file and generate useful maps for the wrapper:
        - swagger_path_to_api_method_map - endpoint path and http method type in swagger maps to API method name in codegen class
        - api_method_to_scopes_map - API method name in codegen class maps to corresponding OAuth scope

        Returns:
            _type_: _description_
        """
        swagger_path_to_api_method_map = {}
        api_method_to_scopes_map = {}

        json_object = self._read_swagger_json()
        operation_id_objects = jsonpath_ng.parse('$.paths..operationId').find(json_object)

        # Create interim map for methods to swagger endpoint paths
        end_point_op_ids = {}
        for obj in operation_id_objects:
            end_point_op_ids[obj.value.replace("_", "").lower()] = _HttpEndpointDescription(str(obj.full_path.left.left.right).strip("'"),
                                                                                            str(obj.full_path.left.right).strip("'"))

        # For each endpoint method, populate appropriate mappings
        for method in self._details.api_class_methods:
            k = method.replace("_", "")
            if (k in end_point_op_ids.keys()):
                # map swagger endpoint path to API method from codegen client
                swagger_path_to_api_method_map[end_point_op_ids[k]] = method
                # map API method from codegen client to OAuth API scope
                api_method_to_scopes_map[method] = [] if not _api_oauth_scopes_enabled else \
                    self._fetch_scopes_from_swagger(json_object, end_point_op_ids[k])
            else:
                _logger.debug(f"Unable to map [{method}]. Method may not be callable via REST endpoint wrappers.")
        return swagger_path_to_api_method_map, api_method_to_scopes_map

    def _fetch_scopes_from_swagger(self, swagger_json_object, ep_path):
        scope_values = []

        if self._api_auth_util.auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN:
            _json_path_to_scopes = f'$.paths."{ep_path.http_endpoint}".{ep_path.http_method}.security.[*].OAuth2AccessCode'
        elif self._api_auth_util.auth_flow_type == user_settings.CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS:
            _json_path_to_scopes = f'$.paths."{ep_path.http_endpoint}".{ep_path.http_method}.security.[*].OAuth2ClientCredentials'
        else:
            return []

        path_security_list = jsonpath_ng.parse(_json_path_to_scopes).find(swagger_json_object)
        for _scope_datum_in_context in path_security_list:
            for _scope in _scope_datum_in_context.value:
                scope_values.append(_scope)

        _logger.debug(f"Fetching scope from swagger file for ({ep_path.http_method} - {ep_path.http_endpoint}): {scope_values}")
        return scope_values

    def _read_swagger_json(self):
        swagger_string = ""
        swagger_file_path = self._details.swagger_file_path

        if not swagger_file_path.exists():
            raise AsdkApiException(f"API [{self._details.api_name}] is mapped to invalid swagger path [{swagger_file_path}] .")
        with swagger_file_path.open(encoding='utf-8') as swagger_file:
            swagger_string = swagger_file.read()
        json_object = None
        try:
            json_object = json.loads(swagger_string)
        except Exception as e:
            _logger.error(e)
            raise AsdkApiException("Invalid json")
        return json_object

    def get_api_endpoint_methods(self):
        return self._details.api_class_methods

    def get_api_endpoint_path_tuples(self):
        return [(ep_path.http_endpoint, ep_path.http_method) for ep_path in self._endpoint_path_to_method_mappings.keys()]

    @asdk_exception_handler
    def get_api_endpoint_signature(self, endpoint_method_name: str):
        """
        Get the signature of an API endpoint method

        Args:
            endpoint_method_name (str): API endpoint method name

        Raises:
            AsdkApiException: If method name passed is not valid

        Returns:
            signature: Signature of the API endpoint method
        """
        if endpoint_method_name not in self._details.api_class_methods:
            raise AsdkApiException("Incorrect endpoint path/method passed")
        endpoint_method = getattr(self.instance, endpoint_method_name)
        signature = inspect.signature(endpoint_method)
        return signature

    def get(self, endpoint_path, *args, **kwargs):
        """
        Wrapper method for making a GET API call using generated client code from Aladdin Graph swagger specification.
        Calls self.call_api with provided args and kwargs
        """
        return self.call_api((endpoint_path, "get"), *args, **kwargs)

    def put(self, endpoint_path, *args, **kwargs):
        """
        Wrapper method for making a PUT API call using generated client code from Aladdin Graph swagger specification.
        Calls self.call_api with provided args and kwargs
        """
        return self.call_api((endpoint_path, "put"), *args, **kwargs)

    def post(self, endpoint_path, *args, **kwargs):
        """
        Wrapper method for making a POST API call using generated client code from Aladdin Graph swagger specification.
        Calls self.call_api with provided args and kwargs
        """
        return self.call_api((endpoint_path, "post"), *args, **kwargs)

    def delete(self, endpoint_path, *args, **kwargs):
        """
        Wrapper method for making a DELETE API call using generated client code from Aladdin Graph swagger specification.
        Calls self.call_api with provided args and kwargs
        """
        return self.call_api((endpoint_path, "delete"), *args, **kwargs)

    def patch(self, endpoint_path, *args, **kwargs):
        """
        Wrapper method for making a PATCH API call using generated client code from Aladdin Graph swagger specification.
        Calls self.call_api with provided args and kwargs
        """
        return self.call_api((endpoint_path, "patch"), *args, **kwargs)

    @asdk_exception_handler
    @api_retry
    @dynamic_asdk_config_reload
    def call_api(self, api_endpoint_name, request_body=None, _oauth_scopes=None, _deserialize_to_object=True,
                 asdk_transformation_option={'type': "json", 'flatten': None}, **params):
        """
        Wrapper method for making an API call using generated client code from Aladdin Graph swagger specification

        Args:
            api_endpoint_name (_type_): Swagger path, or (Swagger path, http method) tuple, or python Codegen API method name
            request_body (_type_, optional): Request body for API call. Defaults to None.
            _oauth_scopes (_type_, optional): Scopes for OAuth. Defaults to None.
            _deserialize_to_object (bool, optional): Deserialize response to python Codegen API response object. Defaults to True.
            asdk_transformation_option (dict, optional): Transformation options to dictate response transformation (EXPERIMENTAL).
                Defaults to {'type': "json", 'flatten': None}.

        Raises:
            AsdkApiException: _description_

        Returns:
            _type_: _description_
        """
        api_endpoint_name = self._endpoint_path_mapping_helper(api_endpoint_name)
        if api_endpoint_name not in self.get_api_endpoint_methods():
            raise AsdkApiException("Incorrect endpoint path/method passed")

        if _oauth_scopes is None or len(_oauth_scopes) == 0:
            _oauth_scopes = self._endpoint_to_scope_mappings.get(api_endpoint_name, None)

        request_headers = self._api_auth_util.add_auth_details_to_header_and_config(_oauth_scopes)

        endpoint_to_call = getattr(self.instance, f"{api_endpoint_name}_with_http_info")

        sig = self.get_api_endpoint_signature(api_endpoint_name)

        if 'body' in sig.parameters.keys():
            api_response = endpoint_to_call(
                vnd_com_blackrock_request_id=request_headers[_HEADER_KEY_REQUEST_ID],
                vnd_com_blackrock_origin_timestamp=request_headers[_HEADER_KEY_ORIGIN_TIMESTAMP],
                body=request_body,
                _headers=request_headers,
                _preload_content=_deserialize_to_object,
                **params
            )
        else:
            api_response = endpoint_to_call(
                vnd_com_blackrock_request_id=request_headers[_HEADER_KEY_REQUEST_ID],
                vnd_com_blackrock_origin_timestamp=request_headers[_HEADER_KEY_ORIGIN_TIMESTAMP],
                _headers=request_headers,
                _preload_content=_deserialize_to_object,
                **params
            )

        if _deserialize_to_object:
            if hasattr(api_response, "data"):
                api_response = api_response.data
        else:
            # disabled deserialization and response validation - for to obtain raw response
            if hasattr(api_response, "raw_data"):
                api_response = json.loads(api_response.raw_data)

        if self._is_valid_transformation_option(asdk_transformation_option):
            api_response = self._response_transformation(api_response, asdk_transformation_option)

        return api_response

    async def _poll_lro_status(self, check_lro_status_endpoint, lro_id, _deserialize_to_object=True, status_check_interval=None):
        """
        Helper method to poll on an LRO call

        Args:
            check_lro_status_endpoint (_type_): Endpoint for API instance to be used for checking the status of Long Running Operation
            lro_id (_type_): Long Running Operation ID
            status_check_interval (_type_, optional): Time duration between status checks. Defaults to 10 (based on user configuration).

        Returns:
            _type_: Result of a successfully completed Long Running Operation
        """
        attempt = 1
        status_check_result = self.call_api(check_lro_status_endpoint, _deserialize_to_object=_deserialize_to_object,
                                            id=lro_id)
        _logger.debug(f"LRO status check attempt #{attempt}, result: {status_check_result}")
        while (not (status_check_result.done if _deserialize_to_object else status_check_result['done'])):
            await asyncio.sleep(status_check_interval)
            status_check_result = self.call_api(check_lro_status_endpoint,
                                                _deserialize_to_object=_deserialize_to_object, id=lro_id)
            attempt += 1
            _logger.debug(f"LRO status check attempt #{attempt}, result: {status_check_result}")
        return status_check_result

    async def call_lro_status_api(self, check_lro_status_endpoint, lro_id, _deserialize_to_object=True,
                                  status_check_interval=None, timeout: int = None):
        """
        Helper method to poll on an LRO call

        Args:
            check_lro_status_endpoint (_type_): Endpoint for API instance to be used for checking the status of Long Running Operation
            lro_id (_type_): Long Running Operation ID
            status_check_interval (_type_, optional): Time duration between status checks. Defaults to 10 (based on user configuration).
            timeout (int, optional): Timeout in seconds for LRO operation. Defaults to 300 (based on user configuration).

        Returns:
            _type_: Result of a successfully completed Long Running Operation
        """
        if status_check_interval is None:
            status_check_interval = user_settings.get_api_lro_status_check_interval()

        if timeout is None:
            timeout = user_settings.get_api_lro_status_check_timeout()

        try:
            lro_completion_response = await asyncio.wait_for(
                self._poll_lro_status(check_lro_status_endpoint, lro_id,
                                      _deserialize_to_object=_deserialize_to_object,
                                      status_check_interval=status_check_interval), timeout=timeout)
        except asyncio.TimeoutError:
            raise AsdkApiException(f"Long running operation timed out. LRO hasn't finished in {timeout} seconds.")

        return lro_completion_response

    async def call_lro_api(self, start_lro_endpoint, check_lro_status_endpoint, status_check_interval=None, callback_func=None,
                           request_body=None, _deserialize_to_object=True, timeout: int = None, **params):
        """
        API Wrapper for Long Running Operation calls.

        Args:
            start_lro_endpoint (_type_): Endpoint for API instance to be used for starting a Long Running Operation
            check_lro_status_endpoint (_type_): Endpoint for API instance to be used for checking the status of Long Running Operation
            status_check_interval (_type_, optional): Time duration between status checks. Defaults to 10 (based on user configuration).
            callback_func (_type_, optional): Optional callback function to be invoked with LRO endpoint response once the operation is done.
                Defaults to None - returns LRO response as is.
            request_body (_type_, optional): Request payload for start_lro_endpoint. Defaults to None.
            timeout (int, optional): Timeout in seconds for LRO operation. Defaults to 300 (based on user configuration).

        Raises:
            AsdkApiException: If LRO response is empty, then operation ID and status are not available for LRO utility to perform status checks

        Returns:
            If callback function is not provided, returns LRO endpoint response as is
            else, invokes callback function with LRO response and returns result of callback function
        """
        # Commence LRO
        start_lro_response = self.call_api(start_lro_endpoint, request_body, _deserialize_to_object=_deserialize_to_object, **params)
        if start_lro_response is None:
            raise AsdkApiException("Long running operation response is empty, unable to get operation ID or status.")

        # Check if operation is done in first attempt, else begin polling with status check endpoint
        lro_completion_response = None
        if start_lro_response.done if _deserialize_to_object else start_lro_response['done']:
            lro_completion_response = start_lro_response
        else:
            lro_id = start_lro_response.id if _deserialize_to_object else start_lro_response['id']
            lro_completion_response = await self.call_lro_status_api(check_lro_status_endpoint, lro_id,
                                                                     _deserialize_to_object=_deserialize_to_object,
                                                                     status_check_interval=status_check_interval,
                                                                     timeout=timeout)
        # process LRO response - invoke callback function if given
        if callback_func is not None:
            return callback_func(lro_completion_response)
        return lro_completion_response

    def _endpoint_path_mapping_helper(self, user_input_endpoint):
        """
        Helper method to map user input for API endpoint to appropriate API class method

        Args:
            user_input_endpoint (str/tuple): endpoint path or python method name OR tuple (http path, http method)

        Returns:
            _type_: python API class method name
        """
        if isinstance(user_input_endpoint, str) and not user_input_endpoint.startswith("/"):
            # user may have provided endpoint method name directly
            return user_input_endpoint

        if isinstance(user_input_endpoint, str) and user_input_endpoint.startswith("/"):
            # user provided a path from swagger json
            return self._endpoint_path_string_input_mapping_helper(user_input_endpoint)

        if isinstance(user_input_endpoint, tuple) or isinstance(user_input_endpoint, _HttpEndpointDescription):
            # user has provided a tuple
            http_endpoint = user_input_endpoint[0]
            http_method = user_input_endpoint[1].lower()
            return self._endpoint_path_to_method_mappings.get(_HttpEndpointDescription(http_endpoint, http_method), None)

    def _endpoint_path_string_input_mapping_helper(self, user_input_endpoint):
        _matched_endpoint_method = None
        _matched_http_methods = []
        for httpmethod in ["get", "put", "post", "delete", "patch"]:
            endpoint_method = self._endpoint_path_to_method_mappings.get(_HttpEndpointDescription(user_input_endpoint, httpmethod), None)
            if endpoint_method is not None and len(_matched_http_methods) == 0:
                _matched_endpoint_method = self._endpoint_path_to_method_mappings.get(_HttpEndpointDescription(user_input_endpoint, httpmethod), None)
            if endpoint_method is not None:
                _matched_http_methods.append(httpmethod)
        if len(_matched_http_methods) > 1:
            _logger.warning(f"Multiple methods map to path {user_input_endpoint}. Input may need to be more "
                            f"specific - provide a tuple with (path, method) where method is one of {_matched_http_methods}")
        return _matched_endpoint_method
