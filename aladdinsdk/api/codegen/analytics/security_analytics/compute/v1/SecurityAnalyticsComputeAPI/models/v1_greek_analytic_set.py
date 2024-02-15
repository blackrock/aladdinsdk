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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class V1GreekAnalyticSet(BaseModel):
    """
    V1GreekAnalyticSet
    """
    value_delta: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueDelta")
    value_gamma: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueGamma")
    value_phi: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valuePhi")
    value_rho: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueRho")
    value_theta: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueTheta")
    value_vanna: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueVanna")
    value_vega: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueVega")
    value_volga: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueVolga")
    __properties = ["valueDelta", "valueGamma", "valuePhi", "valueRho", "valueTheta", "valueVanna", "valueVega", "valueVolga"]

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
    def from_json(cls, json_str: str) -> V1GreekAnalyticSet:
        """Create an instance of V1GreekAnalyticSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1GreekAnalyticSet:
        """Create an instance of V1GreekAnalyticSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1GreekAnalyticSet.parse_obj(obj)

        _obj = V1GreekAnalyticSet.parse_obj({
            "value_delta": obj.get("valueDelta"),
            "value_gamma": obj.get("valueGamma"),
            "value_phi": obj.get("valuePhi"),
            "value_rho": obj.get("valueRho"),
            "value_theta": obj.get("valueTheta"),
            "value_vanna": obj.get("valueVanna"),
            "value_vega": obj.get("valueVega"),
            "value_volga": obj.get("valueVolga")
        })
        return _obj
