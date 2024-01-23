# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.security_analytics_compute.models.v1_compute_analytics_request import V1ComputeAnalyticsRequest
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.security_analytics_compute.models.v1_security_cash_flows_request_config import V1SecurityCashFlowsRequestConfig

class V1ComputeBatchCashFlowsRequest(BaseModel):
    """
    V1ComputeBatchCashFlowsRequest
    """
    requests: conlist(V1ComputeAnalyticsRequest) = Field(...)
    cashflows_request_config: Optional[V1SecurityCashFlowsRequestConfig] = Field(None, alias="cashflowsRequestConfig")
    __properties = ["requests", "cashflowsRequestConfig"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> V1ComputeBatchCashFlowsRequest:
        """Create an instance of V1ComputeBatchCashFlowsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of cashflows_request_config
        if self.cashflows_request_config:
            _dict['cashflowsRequestConfig'] = self.cashflows_request_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ComputeBatchCashFlowsRequest:
        """Create an instance of V1ComputeBatchCashFlowsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ComputeBatchCashFlowsRequest.parse_obj(obj)

        _obj = V1ComputeBatchCashFlowsRequest.parse_obj({
            "requests": [V1ComputeAnalyticsRequest.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None,
            "cashflows_request_config": V1SecurityCashFlowsRequestConfig.from_dict(obj.get("cashflowsRequestConfig")) if obj.get("cashflowsRequestConfig") is not None else None
        })
        return _obj

