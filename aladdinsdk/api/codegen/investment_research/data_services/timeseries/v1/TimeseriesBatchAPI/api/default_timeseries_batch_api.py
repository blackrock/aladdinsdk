# coding: utf-8

"""
    Timeseries Batch

    Timeseries Batch offers the capability to retrieve, filter, and upload more than one timeseries at once.  # noqa: E501

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

from typing import Any, Dict

from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.models.timeseries_batch_api_cancel_longrunning_operation_request import TimeseriesBatchAPICancelLongrunningOperationRequest
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.models.v1_longrunning_operation import V1LongrunningOperation
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.models.v1_upload_timeseries_batches_request import V1UploadTimeseriesBatchesRequest
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.models.v1_upload_timeseries_batches_response import V1UploadTimeseriesBatchesResponse

from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.api_client import ApiClient
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.api_response import ApiResponse
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesBatchAPI.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultTimeseriesBatchAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def timeseries_batch_api_cancel_longrunning_operation(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="The id of the operation resource to be cancelled.")], body : TimeseriesBatchAPICancelLongrunningOperationRequest, **kwargs) -> object:  # noqa: E501
        """Starts asynchronous cancellation on a long-running operation  # noqa: E501

        Starts asynchronous cancellation on a long-running operation.  The server makes a best effort to cancel the operation, but success is not guaranteed.  If the server doesn't support this method, it returns `Code.UNIMPLEMENTED`.  Clients can use [LongrunningOperationAPI.GetOperation] or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error][.Operation.error] value with a [Status.code] of 1, corresponding to `Code.CANCELLED`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_cancel_longrunning_operation(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: The id of the operation resource to be cancelled. (required)
        :type id: str
        :param body: (required)
        :type body: TimeseriesBatchAPICancelLongrunningOperationRequest
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
            raise ValueError("Error! Please call the timeseries_batch_api_cancel_longrunning_operation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.timeseries_batch_api_cancel_longrunning_operation_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, body, **kwargs)  # noqa: E501

    @validate_arguments
    def timeseries_batch_api_cancel_longrunning_operation_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="The id of the operation resource to be cancelled.")], body : TimeseriesBatchAPICancelLongrunningOperationRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Starts asynchronous cancellation on a long-running operation  # noqa: E501

        Starts asynchronous cancellation on a long-running operation.  The server makes a best effort to cancel the operation, but success is not guaranteed.  If the server doesn't support this method, it returns `Code.UNIMPLEMENTED`.  Clients can use [LongrunningOperationAPI.GetOperation] or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error][.Operation.error] value with a [Status.code] of 1, corresponding to `Code.CANCELLED`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_cancel_longrunning_operation_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: The id of the operation resource to be cancelled. (required)
        :type id: str
        :param body: (required)
        :type body: TimeseriesBatchAPICancelLongrunningOperationRequest
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
            'id',
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
                    " to method timeseries_batch_api_cancel_longrunning_operation" % _key
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
            '400': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '401': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '403': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '404': "TimeseriesBatchAPIGetLongrunningOperation400Response",
        }

        return self.api_client.call_api(
            '/longRunningOperations/{id}:cancel', 'POST',
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
    def timeseries_batch_api_get_longrunning_operation(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Id of the LongrunningOperation")], **kwargs) -> V1LongrunningOperation:  # noqa: E501
        """Gets the state of a long-running operation  # noqa: E501

        Clients can use this method to poll the operation result at intervals as recommended by the API service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_get_longrunning_operation(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Id of the LongrunningOperation (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1LongrunningOperation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the timeseries_batch_api_get_longrunning_operation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.timeseries_batch_api_get_longrunning_operation_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, **kwargs)  # noqa: E501

    @validate_arguments
    def timeseries_batch_api_get_longrunning_operation_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Id of the LongrunningOperation")], **kwargs) -> ApiResponse:  # noqa: E501
        """Gets the state of a long-running operation  # noqa: E501

        Clients can use this method to poll the operation result at intervals as recommended by the API service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_get_longrunning_operation_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Id of the LongrunningOperation (required)
        :type id: str
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
        :rtype: tuple(V1LongrunningOperation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'vnd_com_blackrock_request_id',
            'vnd_com_blackrock_origin_timestamp',
            'id'
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
                    " to method timeseries_batch_api_get_longrunning_operation" % _key
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
            '200': "V1LongrunningOperation",
            '400': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '401': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '403': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '404': "TimeseriesBatchAPIGetLongrunningOperation400Response",
        }

        return self.api_client.call_api(
            '/longRunningOperations/{id}', 'GET',
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
    def timeseries_batch_api_upload_timeseries_batches(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1UploadTimeseriesBatchesRequest, **kwargs) -> V1UploadTimeseriesBatchesResponse:  # noqa: E501
        """Upload TimeseriesBatch  # noqa: E501

        Upload TimeseriesBatch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_upload_timeseries_batches(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1UploadTimeseriesBatchesRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: V1UploadTimeseriesBatchesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the timeseries_batch_api_upload_timeseries_batches_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.timeseries_batch_api_upload_timeseries_batches_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, **kwargs)  # noqa: E501

    @validate_arguments
    def timeseries_batch_api_upload_timeseries_batches_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], body : V1UploadTimeseriesBatchesRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Upload TimeseriesBatch  # noqa: E501

        Upload TimeseriesBatch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.timeseries_batch_api_upload_timeseries_batches_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, body, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param body: (required)
        :type body: V1UploadTimeseriesBatchesRequest
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
        :rtype: tuple(V1UploadTimeseriesBatchesResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method timeseries_batch_api_upload_timeseries_batches" % _key
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
            '200': "V1UploadTimeseriesBatchesResponse",
            '400': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '401': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '403': "TimeseriesBatchAPIGetLongrunningOperation400Response",
            '404': "TimeseriesBatchAPIGetLongrunningOperation400Response",
        }

        return self.api_client.call_api(
            '/timeseriesBatches:upload', 'POST',
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
