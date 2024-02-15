# coding: utf-8

"""
    Aladdin User Group Permission

    API contains operations on Aladdin User Group Permission resource. Note: This is not intended to be used for Authorization.  # noqa: E501

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

from pydantic import Field, StrictInt, StrictStr

from typing import Any, Dict, Optional

from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.models.user_group_permission_api_batch_create_user_group_permissions_request import UserGroupPermissionAPIBatchCreateUserGroupPermissionsRequest
from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.models.user_group_permission_api_batch_delete_user_group_permission_request import UserGroupPermissionAPIBatchDeleteUserGroupPermissionRequest
from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.models.v1_batch_create_user_group_permissions_response import V1BatchCreateUserGroupPermissionsResponse
from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.models.v1_list_user_group_permissions_response import V1ListUserGroupPermissionsResponse

from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.api_client import ApiClient
from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.platform.access.permission.v1.UserGroupPermissionAPI.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultUserGroupPermissionAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def user_group_permission_api_batch_create_user_group_permissions(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to add permissions to.")], body : UserGroupPermissionAPIBatchCreateUserGroupPermissionsRequest, **kwargs) -> V1BatchCreateUserGroupPermissionsResponse:  # noqa: E501
        """Add Permissions to a User Group  # noqa: E501

        Prerequisite: You must have permission to add User Group permissions. You must have the Aladdin Permission PERMS_GROUP_MOD_perm or MOD_PERMS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_batch_create_user_group_permissions(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to add permissions to. (required)
        :type parent: str
        :param body: (required)
        :type body: UserGroupPermissionAPIBatchCreateUserGroupPermissionsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1BatchCreateUserGroupPermissionsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the user_group_permission_api_batch_create_user_group_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.user_group_permission_api_batch_create_user_group_permissions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, **kwargs)  # noqa: E501

    @validate_arguments
    def user_group_permission_api_batch_create_user_group_permissions_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to add permissions to.")], body : UserGroupPermissionAPIBatchCreateUserGroupPermissionsRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Add Permissions to a User Group  # noqa: E501

        Prerequisite: You must have permission to add User Group permissions. You must have the Aladdin Permission PERMS_GROUP_MOD_perm or MOD_PERMS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_batch_create_user_group_permissions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to add permissions to. (required)
        :type parent: str
        :param body: (required)
        :type body: UserGroupPermissionAPIBatchCreateUserGroupPermissionsRequest
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
        :rtype: tuple(V1BatchCreateUserGroupPermissionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'parent',
            'body'
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
                    " to method user_group_permission_api_batch_create_user_group_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['parent']:
            _path_params['parent'] = _params['parent']


        # process the query parameters
        _query_params = []
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
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "V1BatchCreateUserGroupPermissionsResponse",
            '400': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '401': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '403': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '404': "UserGroupPermissionAPIListUserGroupPermissions400Response",
        }

        return self.api_client.call_api(
            '/userGroups/{parent}/userGroupPermissions:batchCreate', 'POST',
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
    def user_group_permission_api_batch_delete_user_group_permission(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to remove permissions from.")], body : UserGroupPermissionAPIBatchDeleteUserGroupPermissionRequest, **kwargs) -> object:  # noqa: E501
        """Remove Permissions from a User Group  # noqa: E501

        Prerequisite: You must have permission to remove User Group permissions. You must have the Aladdin Permission PERMS_GROUP_MOD_perm or MOD_PERMS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_batch_delete_user_group_permission(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to remove permissions from. (required)
        :type parent: str
        :param body: (required)
        :type body: UserGroupPermissionAPIBatchDeleteUserGroupPermissionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the user_group_permission_api_batch_delete_user_group_permission_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.user_group_permission_api_batch_delete_user_group_permission_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, **kwargs)  # noqa: E501

    @validate_arguments
    def user_group_permission_api_batch_delete_user_group_permission_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to remove permissions from.")], body : UserGroupPermissionAPIBatchDeleteUserGroupPermissionRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Remove Permissions from a User Group  # noqa: E501

        Prerequisite: You must have permission to remove User Group permissions. You must have the Aladdin Permission PERMS_GROUP_MOD_perm or MOD_PERMS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_batch_delete_user_group_permission_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to remove permissions from. (required)
        :type parent: str
        :param body: (required)
        :type body: UserGroupPermissionAPIBatchDeleteUserGroupPermissionRequest
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'parent',
            'body'
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
                    " to method user_group_permission_api_batch_delete_user_group_permission" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['parent']:
            _path_params['parent'] = _params['parent']


        # process the query parameters
        _query_params = []
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
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['APIKeyHeader', 'OAuth2ClientCredentials', 'basicAuth', 'OAuth2AccessCode', 'ClientKeyHeader']  # noqa: E501

        _response_types_map = {
            '200': "object",
            '400': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '401': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '403': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '404': "UserGroupPermissionAPIListUserGroupPermissions400Response",
        }

        return self.api_client.call_api(
            '/userGroups/{parent}/userGroupPermissions:batchDelete', 'POST',
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
    def user_group_permission_api_list_user_group_permissions(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to retrieve its permissions.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of Permissions to return. The service may return fewer than this value. If unspecified, at most 1000 Permissions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous 'ListUserGroupPermissions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'ListUserGroupPermissions' must match the call that provided the page token.")] = None, **kwargs) -> V1ListUserGroupPermissionsResponse:  # noqa: E501
        """List User Group Permissions  # noqa: E501

        Returns all permissions in the specified User Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_list_user_group_permissions(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, page_size, page_token, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to retrieve its permissions. (required)
        :type parent: str
        :param page_size: The maximum number of Permissions to return. The service may return fewer than this value. If unspecified, at most 1000 Permissions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
        :type page_size: int
        :param page_token: A page token, received from a previous 'ListUserGroupPermissions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'ListUserGroupPermissions' must match the call that provided the page token.
        :type page_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1ListUserGroupPermissionsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the user_group_permission_api_list_user_group_permissions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.user_group_permission_api_list_user_group_permissions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, page_size, page_token, **kwargs)  # noqa: E501

    @validate_arguments
    def user_group_permission_api_list_user_group_permissions_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], parent : Annotated[StrictStr, Field(..., description="The name of the User Group to retrieve its permissions.")], page_size : Annotated[Optional[StrictInt], Field(description="The maximum number of Permissions to return. The service may return fewer than this value. If unspecified, at most 1000 Permissions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A page token, received from a previous 'ListUserGroupPermissions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'ListUserGroupPermissions' must match the call that provided the page token.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List User Group Permissions  # noqa: E501

        Returns all permissions in the specified User Group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_group_permission_api_list_user_group_permissions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, parent, page_size, page_token, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param parent: The name of the User Group to retrieve its permissions. (required)
        :type parent: str
        :param page_size: The maximum number of Permissions to return. The service may return fewer than this value. If unspecified, at most 1000 Permissions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
        :type page_size: int
        :param page_token: A page token, received from a previous 'ListUserGroupPermissions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'ListUserGroupPermissions' must match the call that provided the page token.
        :type page_token: str
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
        :rtype: tuple(V1ListUserGroupPermissionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'parent',
            'page_size',
            'page_token'
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
                    " to method user_group_permission_api_list_user_group_permissions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['parent']:
            _path_params['parent'] = _params['parent']


        # process the query parameters
        _query_params = []
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        if _params.get('page_token') is not None:  # noqa: E501
            _query_params.append(('pageToken', _params['page_token']))

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
            '200': "V1ListUserGroupPermissionsResponse",
            '400': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '401': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '403': "UserGroupPermissionAPIListUserGroupPermissions400Response",
            '404': "UserGroupPermissionAPIListUserGroupPermissions400Response",
        }

        return self.api_client.call_api(
            '/userGroups/{parent}/userGroupPermissions', 'GET',
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