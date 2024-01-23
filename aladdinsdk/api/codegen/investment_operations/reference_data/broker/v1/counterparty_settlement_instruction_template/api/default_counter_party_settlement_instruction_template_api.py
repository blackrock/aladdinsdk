# coding: utf-8

"""
    Counter Party Settlement Instruction Template

    API contains operations on Counter Party Settlement Instruction Template resource.  # noqa: E501

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

from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.counterparty_settlement_instruction_template.models.v1_counter_party_settlement_instruction_template import V1CounterPartySettlementInstructionTemplate

from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.counterparty_settlement_instruction_template.api_client import ApiClient
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.counterparty_settlement_instruction_template.api_response import ApiResponse
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.counterparty_settlement_instruction_template.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultCounterPartySettlementInstructionTemplateAPI(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Delivery method.  The method of delivery. E.g. fax. Please see decode named BRKR_DELIV_T.")], **kwargs) -> V1CounterPartySettlementInstructionTemplate:  # noqa: E501
        """Get Counter Party Settlement Instruction Template  # noqa: E501

        Gets Counter Party Settlement Instruction template by delivery method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Delivery method.  The method of delivery. E.g. fax. Please see decode named BRKR_DELIV_T. (required)
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
        :rtype: V1CounterPartySettlementInstructionTemplate
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, **kwargs)  # noqa: E501

    @validate_arguments
    def counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template_with_http_info(self, vnd_com_blackrock_request_id : Annotated[StrictStr, Field(..., description="A unique identifier for this request.")], vnd_com_blackrock_origin_timestamp : Annotated[datetime, Field(..., description="Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231.")], id : Annotated[StrictStr, Field(..., description="Delivery method.  The method of delivery. E.g. fax. Please see decode named BRKR_DELIV_T.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Counter Party Settlement Instruction Template  # noqa: E501

        Gets Counter Party Settlement Instruction template by delivery method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template_with_http_info(vnd_com_blackrock_request_id, vnd_com_blackrock_origin_timestamp, id, async_req=True)
        >>> result = thread.get()

        :param vnd_com_blackrock_request_id: A unique identifier for this request. (required)
        :type vnd_com_blackrock_request_id: str
        :param vnd_com_blackrock_origin_timestamp: Timestamp assigned to this request at origin, in \"HTTP-date\" format as defined by RFC 7231. (required)
        :type vnd_com_blackrock_origin_timestamp: datetime
        :param id: Delivery method.  The method of delivery. E.g. fax. Please see decode named BRKR_DELIV_T. (required)
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
        :rtype: tuple(V1CounterPartySettlementInstructionTemplate, status_code(int), headers(HTTPHeaderDict))
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
                    " to method counter_party_settlement_instruction_template_api_get_counter_party_settlement_instruction_template" % _key
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
            '200': "V1CounterPartySettlementInstructionTemplate",
            '400': "CounterPartySettlementInstructionTemplateAPIGetCounterPartySettlementInstructionTemplate400Response",
            '401': "CounterPartySettlementInstructionTemplateAPIGetCounterPartySettlementInstructionTemplate400Response",
            '403': "CounterPartySettlementInstructionTemplateAPIGetCounterPartySettlementInstructionTemplate400Response",
            '404': "CounterPartySettlementInstructionTemplateAPIGetCounterPartySettlementInstructionTemplate400Response",
        }

        return self.api_client.call_api(
            '/counterPartySettlementInstructionTemplates/{id}', 'GET',
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
