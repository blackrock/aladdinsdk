# coding: utf-8

"""
    Token

    For pre-registered OAuth applications such as ADC Studio, Handles the Authorization Code Flow and Repository for OAuth AccessTokens.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import datetime

from pydantic import Field, StrictStr

from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.models.v1_authorization_url import V1AuthorizationUrl
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.models.v1_check_token_exists_response import V1CheckTokenExistsResponse
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.models.v1_token import V1Token

from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.api_client import ApiClient
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.infrastructure.token.v1.token.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultTokenAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def token_api_check_token_exists(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], user : Annotated[StrictStr, Field(..., description="user is the user of the requestor of a token.")], **kwargs) -> V1CheckTokenExistsResponse:  # noqa: E501
        """CheckTokenExists checks whether a token is stored  # noqa: E501

        CheckTokenExists returns whether a token is stored by the token service for a specific user (-- api-linter: aladdin::9002::wordslist-custom-method-rpc=disabled  aip.dev/not-precedent: We need to do this because check keyword used previous to wordlist --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because check keyword used previous to wordlist --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_check_token_exists(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, user, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param user: user is the user of the requestor of a token. (required)
        :type user: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1CheckTokenExistsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the token_api_check_token_exists_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.token_api_check_token_exists_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, user, **kwargs)  # noqa: E501

    @validate_arguments
    def token_api_check_token_exists_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], user : Annotated[StrictStr, Field(..., description="user is the user of the requestor of a token.")], **kwargs) -> ApiResponse:  # noqa: E501
        """CheckTokenExists checks whether a token is stored  # noqa: E501

        CheckTokenExists returns whether a token is stored by the token service for a specific user (-- api-linter: aladdin::9002::wordslist-custom-method-rpc=disabled  aip.dev/not-precedent: We need to do this because check keyword used previous to wordlist --) (-- api-linter: aladdin::9002::wordslist-custom-method-http=disabled  aip.dev/not-precedent: We need to do this because check keyword used previous to wordlist --)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_check_token_exists_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, user, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param user: user is the user of the requestor of a token. (required)
        :type user: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V1CheckTokenExistsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'application_name',
            'user'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method token_api_check_token_exists" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('application_name') is not None:  # noqa: E501
            _query_params.append(('applicationName', _params['application_name']))

        if _params.get('user') is not None:  # noqa: E501
            _query_params.append(('user', _params['user']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['vnd_com_blackrock_request_id']:
            _header_params['VND.com.blackrock.Request-ID'] = _params['vnd_com_blackrock_request_id']

        if _params['vnd_com_blackrock_origin_timestamp']:
            _header_params['VND.com.blackrock.Origin-Timestamp'] = _params['vnd_com_blackrock_origin_timestamp']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1CheckTokenExistsResponse",
            '400': "TokenAPIGenerateAuthorizationUrl400Response",
            '401': "TokenAPIGenerateAuthorizationUrl400Response",
            '403': "TokenAPIGenerateAuthorizationUrl400Response",
            '404': "TokenAPIGenerateAuthorizationUrl400Response",
        }

        return self.api_client.call_api(
            '/token:checkTokenExists', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def token_api_generate_authorization_url(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], redirect_uri : Annotated[StrictStr, Field(..., description="redirect_uri is the URI to be redirected to after authorization is complete.")], user : Annotated[StrictStr, Field(..., description="user is the user of the requestor of a token. user parameter field is temporary until bms header modifier is added to go")], **kwargs) -> V1AuthorizationUrl:  # noqa: E501
        """GenerateAuthorizationUrl retrieves an Okta authorization URL  # noqa: E501

        AuthorizationUrl is the Okta authorization URL for a user to consent to applications being able to access third-party services. Follow the AuthorizationUrl in the response to authenticate, providing consent to the application. The resultant access+refresh token will then be available via GenerateToken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_generate_authorization_url(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, redirect_uri, user, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param redirect_uri: redirect_uri is the URI to be redirected to after authorization is complete. (required)
        :type redirect_uri: str
        :param user: user is the user of the requestor of a token. user parameter field is temporary until bms header modifier is added to go (required)
        :type user: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1AuthorizationUrl
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the token_api_generate_authorization_url_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.token_api_generate_authorization_url_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, redirect_uri, user, **kwargs)  # noqa: E501

    @validate_arguments
    def token_api_generate_authorization_url_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], redirect_uri : Annotated[StrictStr, Field(..., description="redirect_uri is the URI to be redirected to after authorization is complete.")], user : Annotated[StrictStr, Field(..., description="user is the user of the requestor of a token. user parameter field is temporary until bms header modifier is added to go")], **kwargs) -> ApiResponse:  # noqa: E501
        """GenerateAuthorizationUrl retrieves an Okta authorization URL  # noqa: E501

        AuthorizationUrl is the Okta authorization URL for a user to consent to applications being able to access third-party services. Follow the AuthorizationUrl in the response to authenticate, providing consent to the application. The resultant access+refresh token will then be available via GenerateToken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_generate_authorization_url_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, redirect_uri, user, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param redirect_uri: redirect_uri is the URI to be redirected to after authorization is complete. (required)
        :type redirect_uri: str
        :param user: user is the user of the requestor of a token. user parameter field is temporary until bms header modifier is added to go (required)
        :type user: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V1AuthorizationUrl, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'application_name',
            'redirect_uri',
            'user'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method token_api_generate_authorization_url" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('application_name') is not None:  # noqa: E501
            _query_params.append(('applicationName', _params['application_name']))

        if _params.get('redirect_uri') is not None:  # noqa: E501
            _query_params.append(('redirectUri', _params['redirect_uri']))

        if _params.get('user') is not None:  # noqa: E501
            _query_params.append(('user', _params['user']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['vnd_com_blackrock_request_id']:
            _header_params['VND.com.blackrock.Request-ID'] = _params['vnd_com_blackrock_request_id']

        if _params['vnd_com_blackrock_origin_timestamp']:
            _header_params['VND.com.blackrock.Origin-Timestamp'] = _params['vnd_com_blackrock_origin_timestamp']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1AuthorizationUrl",
            '400': "TokenAPIGenerateAuthorizationUrl400Response",
            '401': "TokenAPIGenerateAuthorizationUrl400Response",
            '403': "TokenAPIGenerateAuthorizationUrl400Response",
            '404': "TokenAPIGenerateAuthorizationUrl400Response",
        }

        return self.api_client.call_api(
            '/authorizationUrl:generate', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def token_api_generate_token(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], **kwargs) -> V1Token:  # noqa: E501
        """GenerateToken retrieves a token  # noqa: E501

        Retrieves an access token for the authorized user. If no access token is available, complete the \"Authorization Code Flow\" beginning w/ GenerateAuthorizationUrl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_generate_token(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1Token
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the token_api_generate_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.token_api_generate_token_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, **kwargs)  # noqa: E501

    @validate_arguments
    def token_api_generate_token_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], application_name : Annotated[StrictStr, Field(..., description="application_name is an OAuth2 *application* client.")], **kwargs) -> ApiResponse:  # noqa: E501
        """GenerateToken retrieves a token  # noqa: E501

        Retrieves an access token for the authorized user. If no access token is available, complete the \"Authorization Code Flow\" beginning w/ GenerateAuthorizationUrl  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_api_generate_token_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, application_name, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param application_name: application_name is an OAuth2 *application* client. (required)
        :type application_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(V1Token, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'application_name'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method token_api_generate_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('application_name') is not None:  # noqa: E501
            _query_params.append(('applicationName', _params['application_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['vnd_com_blackrock_request_id']:
            _header_params['VND.com.blackrock.Request-ID'] = _params['vnd_com_blackrock_request_id']

        if _params['vnd_com_blackrock_origin_timestamp']:
            _header_params['VND.com.blackrock.Origin-Timestamp'] = _params['vnd_com_blackrock_origin_timestamp']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1Token",
            '400': "TokenAPIGenerateAuthorizationUrl400Response",
            '401': "TokenAPIGenerateAuthorizationUrl400Response",
            '403': "TokenAPIGenerateAuthorizationUrl400Response",
            '404': "TokenAPIGenerateAuthorizationUrl400Response",
        }

        return self.api_client.call_api(
            '/token:generate', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
