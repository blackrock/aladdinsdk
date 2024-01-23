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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.optimization.models.soft_bound_objective_soft_bound_type import SoftBoundObjectiveSoftBoundType

class V2SoftBoundObjective(BaseModel):
    """
    V2SoftBoundObjective
    """
    penalty_slope: Union[StrictFloat, StrictInt] = Field(..., alias="penaltySlope")
    soft_bound_type: Optional[SoftBoundObjectiveSoftBoundType] = Field(None, alias="softBoundType")
    __properties = ["penaltySlope", "softBoundType"]

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
    def from_json(cls, json_str: str) -> V2SoftBoundObjective:
        """Create an instance of V2SoftBoundObjective from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2SoftBoundObjective:
        """Create an instance of V2SoftBoundObjective from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2SoftBoundObjective.parse_obj(obj)

        _obj = V2SoftBoundObjective.parse_obj({
            "penalty_slope": obj.get("penaltySlope"),
            "soft_bound_type": obj.get("softBoundType")
        })
        return _obj

