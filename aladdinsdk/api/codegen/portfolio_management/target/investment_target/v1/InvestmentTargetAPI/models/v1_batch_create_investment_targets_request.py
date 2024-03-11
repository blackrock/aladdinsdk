# coding: utf-8

"""
    Aladdin Investment Target

    This service provides advance capabilities to create and manage all types of Aladdin Investment Targets and their associated subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictBool, conlist
from aladdinsdk.api.codegen.portfolio_management.target.investment_target.v1.InvestmentTargetAPI.models.v1_investment_target import V1InvestmentTarget

class V1BatchCreateInvestmentTargetsRequest(BaseModel):
    """
    V1BatchCreateInvestmentTargetsRequest
    """
    investment_targets: conlist(V1InvestmentTarget) = Field(..., alias="investmentTargets")
    new_version: StrictBool = Field(..., alias="newVersion")
    __properties = ["investmentTargets", "newVersion"]

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
    def from_json(cls, json_str: str) -> V1BatchCreateInvestmentTargetsRequest:
        """Create an instance of V1BatchCreateInvestmentTargetsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in investment_targets (list)
        _items = []
        if self.investment_targets:
            for _item in self.investment_targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['investmentTargets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchCreateInvestmentTargetsRequest:
        """Create an instance of V1BatchCreateInvestmentTargetsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchCreateInvestmentTargetsRequest.parse_obj(obj)

        _obj = V1BatchCreateInvestmentTargetsRequest.parse_obj({
            "investment_targets": [V1InvestmentTarget.from_dict(_item) for _item in obj.get("investmentTargets")] if obj.get("investmentTargets") is not None else None,
            "new_version": obj.get("newVersion")
        })
        return _obj

