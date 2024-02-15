# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class V1SECLiquiditySettings(BaseModel):
    """
    V1SECLiquiditySettings
    """
    default_reasonably_anticipated_trading_size: Optional[StrictBool] = Field(None, alias="defaultReasonablyAnticipatedTradingSize")
    nav_percent: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="navPercent")
    __properties = ["defaultReasonablyAnticipatedTradingSize", "navPercent"]

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
    def from_json(cls, json_str: str) -> V1SECLiquiditySettings:
        """Create an instance of V1SECLiquiditySettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SECLiquiditySettings:
        """Create an instance of V1SECLiquiditySettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SECLiquiditySettings.parse_obj(obj)

        _obj = V1SECLiquiditySettings.parse_obj({
            "default_reasonably_anticipated_trading_size": obj.get("defaultReasonablyAnticipatedTradingSize"),
            "nav_percent": obj.get("navPercent")
        })
        return _obj
