# coding: utf-8

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

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

from typing import Optional

from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.models.v1_corporate_action import V1CorporateAction
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.models.v1_filter_corporate_actions_request import V1FilterCorporateActionsRequest
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.models.v1_filter_corporate_actions_response import V1FilterCorporateActionsResponse

from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.api_client import ApiClient
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultCorporateActionAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def corporate_action_api_filter_corporate_actions(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1FilterCorporateActionsRequest, **kwargs) -> V1FilterCorporateActionsResponse:  # noqa: E501
        """Filters corporateActions  # noqa: E501

        Filters corporate actions based on search criteria. Search must be made using at-least any one of these: ids, externalCorporateActionIds, start/endProcessingDate, start/endExpirationDate, start/endModifyTime, assetIds. These can be clubbed (if required) with all available search parameters. Both start and end date must be provided if making a search using any date/time field. From the body container, fields that are not required for making a search can be removed from corporateActionQuery object only. Pagination not supported currently. pagesize & pageToken have to be left as they are.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.corporate_action_api_filter_corporate_actions(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1FilterCorporateActionsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1FilterCorporateActionsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the corporate_action_api_filter_corporate_actions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.corporate_action_api_filter_corporate_actions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, **kwargs)  # noqa: E501

    @validate_arguments
    def corporate_action_api_filter_corporate_actions_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1FilterCorporateActionsRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Filters corporateActions  # noqa: E501

        Filters corporate actions based on search criteria. Search must be made using at-least any one of these: ids, externalCorporateActionIds, start/endProcessingDate, start/endExpirationDate, start/endModifyTime, assetIds. These can be clubbed (if required) with all available search parameters. Both start and end date must be provided if making a search using any date/time field. From the body container, fields that are not required for making a search can be removed from corporateActionQuery object only. Pagination not supported currently. pagesize & pageToken have to be left as they are.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.corporate_action_api_filter_corporate_actions_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1FilterCorporateActionsRequest
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
        :rtype: tuple(V1FilterCorporateActionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
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
                    " to method corporate_action_api_filter_corporate_actions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            '200': "V1FilterCorporateActionsResponse",
            '400': "CorporateActionAPIGetCorporateAction400Response",
            '401': "CorporateActionAPIGetCorporateAction400Response",
            '403': "CorporateActionAPIGetCorporateAction400Response",
            '404': "CorporateActionAPIGetCorporateAction400Response",
        }

        return self.api_client.call_api(
            '/corporateActions:filter', 'POST',
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
    def corporate_action_api_get_corporate_action(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Corporate action Id.")], corporate_action_view : Annotated[Optional[StrictStr], Field(description="View of corporate action resource. If not specified, then this parameter will default to the 'CORPORATE_ACTION_VIEW_FULL' value. (-- api-linter: core::0131::request-unknown-fields=disabled  aip.dev/not-precedent: We need to do this because we need to specify view  of the resource... --).   - CORPORATE_ACTION_VIEW_UNSPECIFIED: The default/unset value at API level. The GetCorporateActions API defaults to FULL and FilterCorporateActions API defaults to DESC_ONLY on cam-server side.  - CORPORATE_ACTION_VIEW_FULL: Includes full contents of the resource.")] = None, **kwargs) -> V1CorporateAction:  # noqa: E501
        """Gets a corporateAction  # noqa: E501

        Gets a corporate action based on corporate action Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.corporate_action_api_get_corporate_action(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, corporate_action_view, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Corporate action Id. (required)
        :type id: str
        :param corporate_action_view: View of corporate action resource. If not specified, then this parameter will default to the 'CORPORATE_ACTION_VIEW_FULL' value. (-- api-linter: core::0131::request-unknown-fields=disabled  aip.dev/not-precedent: We need to do this because we need to specify view  of the resource... --).   - CORPORATE_ACTION_VIEW_UNSPECIFIED: The default/unset value at API level. The GetCorporateActions API defaults to FULL and FilterCorporateActions API defaults to DESC_ONLY on cam-server side.  - CORPORATE_ACTION_VIEW_FULL: Includes full contents of the resource.
        :type corporate_action_view: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1CorporateAction
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the corporate_action_api_get_corporate_action_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.corporate_action_api_get_corporate_action_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, corporate_action_view, **kwargs)  # noqa: E501

    @validate_arguments
    def corporate_action_api_get_corporate_action_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Corporate action Id.")], corporate_action_view : Annotated[Optional[StrictStr], Field(description="View of corporate action resource. If not specified, then this parameter will default to the 'CORPORATE_ACTION_VIEW_FULL' value. (-- api-linter: core::0131::request-unknown-fields=disabled  aip.dev/not-precedent: We need to do this because we need to specify view  of the resource... --).   - CORPORATE_ACTION_VIEW_UNSPECIFIED: The default/unset value at API level. The GetCorporateActions API defaults to FULL and FilterCorporateActions API defaults to DESC_ONLY on cam-server side.  - CORPORATE_ACTION_VIEW_FULL: Includes full contents of the resource.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Gets a corporateAction  # noqa: E501

        Gets a corporate action based on corporate action Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.corporate_action_api_get_corporate_action_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, corporate_action_view, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Corporate action Id. (required)
        :type id: str
        :param corporate_action_view: View of corporate action resource. If not specified, then this parameter will default to the 'CORPORATE_ACTION_VIEW_FULL' value. (-- api-linter: core::0131::request-unknown-fields=disabled  aip.dev/not-precedent: We need to do this because we need to specify view  of the resource... --).   - CORPORATE_ACTION_VIEW_UNSPECIFIED: The default/unset value at API level. The GetCorporateActions API defaults to FULL and FilterCorporateActions API defaults to DESC_ONLY on cam-server side.  - CORPORATE_ACTION_VIEW_FULL: Includes full contents of the resource.
        :type corporate_action_view: str
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
        :rtype: tuple(V1CorporateAction, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'id',
            'corporate_action_view'
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
                    " to method corporate_action_api_get_corporate_action" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('corporate_action_view') is not None:  # noqa: E501
            _query_params.append(('corporateActionView', _params['corporate_action_view'].value))

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
            '200': "V1CorporateAction",
            '400': "CorporateActionAPIGetCorporateAction400Response",
            '401': "CorporateActionAPIGetCorporateAction400Response",
            '403': "CorporateActionAPIGetCorporateAction400Response",
            '404': "CorporateActionAPIGetCorporateAction400Response",
        }

        return self.api_client.call_api(
            '/corporateActions/{id}', 'GET',
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
