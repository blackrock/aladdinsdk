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
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.tax_rate_tax_rate_type import TaxRateTaxRateType

class TaxModelTaxRate(BaseModel):
    """
    TaxModelTaxRate
    """
    tax_rate_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="taxRateValue")
    tax_rate_lag: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="taxRateLag")
    tax_rate_type: Optional[TaxRateTaxRateType] = Field(None, alias="taxRateType")
    __properties = ["taxRateValue", "taxRateLag", "taxRateType"]

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
    def from_json(cls, json_str: str) -> TaxModelTaxRate:
        """Create an instance of TaxModelTaxRate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaxModelTaxRate:
        """Create an instance of TaxModelTaxRate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaxModelTaxRate.parse_obj(obj)

        _obj = TaxModelTaxRate.parse_obj({
            "tax_rate_value": obj.get("taxRateValue"),
            "tax_rate_lag": obj.get("taxRateLag"),
            "tax_rate_type": obj.get("taxRateType")
        })
        return _obj

