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
from pydantic import BaseModel, conlist
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_security_cash_flow import V1SecurityCashFlow

class V1SecurityCashFlowsList(BaseModel):
    """
    V1SecurityCashFlowsList
    """
    values: Optional[conlist(V1SecurityCashFlow)] = None
    __properties = ["values"]

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
    def from_json(cls, json_str: str) -> V1SecurityCashFlowsList:
        """Create an instance of V1SecurityCashFlowsList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SecurityCashFlowsList:
        """Create an instance of V1SecurityCashFlowsList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SecurityCashFlowsList.parse_obj(obj)

        _obj = V1SecurityCashFlowsList.parse_obj({
            "values": [V1SecurityCashFlow.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None
        })
        return _obj
