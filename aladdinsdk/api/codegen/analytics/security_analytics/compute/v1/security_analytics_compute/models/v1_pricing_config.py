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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.security_analytics_compute.models.pricing_config_pricing_input_type import PricingConfigPricingInputType

class V1PricingConfig(BaseModel):
    """
    V1PricingConfig
    """
    pricing_input_type: Optional[PricingConfigPricingInputType] = Field(None, alias="pricingInputType")
    price_input: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="priceInput")
    price_shortcut: Optional[StrictStr] = Field(None, alias="priceShortcut")
    __properties = ["pricingInputType", "priceInput", "priceShortcut"]

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
    def from_json(cls, json_str: str) -> V1PricingConfig:
        """Create an instance of V1PricingConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PricingConfig:
        """Create an instance of V1PricingConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PricingConfig.parse_obj(obj)

        _obj = V1PricingConfig.parse_obj({
            "pricing_input_type": obj.get("pricingInputType"),
            "price_input": obj.get("priceInput"),
            "price_shortcut": obj.get("priceShortcut")
        })
        return _obj

