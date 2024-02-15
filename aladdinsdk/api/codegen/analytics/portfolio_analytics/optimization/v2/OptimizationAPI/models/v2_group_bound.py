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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.group_bound_bound import GroupBoundBound
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_bound_relaxation import V2BoundRelaxation
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.v2_soft_bound_objective import V2SoftBoundObjective

class V2GroupBound(BaseModel):
    """
    V2GroupBound
    """
    bounds: Optional[conlist(GroupBoundBound)] = None
    relaxation_pair: Optional[V2BoundRelaxation] = Field(None, alias="relaxationPair")
    soft_objective: Optional[V2SoftBoundObjective] = Field(None, alias="softObjective")
    __properties = ["bounds", "relaxationPair", "softObjective"]

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
    def from_json(cls, json_str: str) -> V2GroupBound:
        """Create an instance of V2GroupBound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bounds (list)
        _items = []
        if self.bounds:
            for _item in self.bounds:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bounds'] = _items
        # override the default output from pydantic by calling `to_dict()` of relaxation_pair
        if self.relaxation_pair:
            _dict['relaxationPair'] = self.relaxation_pair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of soft_objective
        if self.soft_objective:
            _dict['softObjective'] = self.soft_objective.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2GroupBound:
        """Create an instance of V2GroupBound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2GroupBound.parse_obj(obj)

        _obj = V2GroupBound.parse_obj({
            "bounds": [GroupBoundBound.from_dict(_item) for _item in obj.get("bounds")] if obj.get("bounds") is not None else None,
            "relaxation_pair": V2BoundRelaxation.from_dict(obj.get("relaxationPair")) if obj.get("relaxationPair") is not None else None,
            "soft_objective": V2SoftBoundObjective.from_dict(obj.get("softObjective")) if obj.get("softObjective") is not None else None
        })
        return _obj
