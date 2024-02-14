# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_optimization_case_group import V2OptimizationCaseGroup

class V2CreateLongRunningOptimizationCaseGroupRequest(BaseModel):
    """
    V2CreateLongRunningOptimizationCaseGroupRequest
    """
    optimization_case_group: Optional[V2OptimizationCaseGroup] = Field(None, alias="optimizationCaseGroup")
    __properties = ["optimizationCaseGroup"]

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
    def from_json(cls, json_str: str) -> V2CreateLongRunningOptimizationCaseGroupRequest:
        """Create an instance of V2CreateLongRunningOptimizationCaseGroupRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of optimization_case_group
        if self.optimization_case_group:
            _dict['optimizationCaseGroup'] = self.optimization_case_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2CreateLongRunningOptimizationCaseGroupRequest:
        """Create an instance of V2CreateLongRunningOptimizationCaseGroupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2CreateLongRunningOptimizationCaseGroupRequest.parse_obj(obj)

        _obj = V2CreateLongRunningOptimizationCaseGroupRequest.parse_obj({
            "optimization_case_group": V2OptimizationCaseGroup.from_dict(obj.get("optimizationCaseGroup")) if obj.get("optimizationCaseGroup") is not None else None
        })
        return _obj

