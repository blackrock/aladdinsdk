# coding: utf-8

"""
    Portfolio Configuration Record For Accounting

    Configurations API for Aladdin Accounting allows you to access accounting configuration attributes for process types that portfolios are setup on. Data can be sourced in aggregate and filtered to improve oversight and scale of configuration monitoring. This API allows for retrieval of key data points for portfolio configurations by various parameters, including portfolio tickers, processCodes, and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1PortfolioConfigurationAttribute(BaseModel):
    """
    V1PortfolioConfigurationAttribute
    """
    accounting_attribute_name: Optional[StrictStr] = Field(None, alias="accountingAttributeName", description="It defines the attribute name.")
    accounting_attribute_value: Optional[StrictStr] = Field(None, alias="accountingAttributeValue", description="It defines attribute value.")
    effective_date: Optional[date] = Field(None, alias="effectiveDate", description="It defines attribute's effective date.")
    modifier: Optional[StrictStr] = Field(None, description="It defines who last modified the attribute.")
    modification_time: Optional[datetime] = Field(None, alias="modificationTime", description="It defines when the attribute was modified.")
    is_default: Optional[StrictBool] = Field(None, alias="isDefault", description="It defines attribute if attirbute has this value by default or it is a modified value.")
    category: Optional[StrictStr] = Field(None, description="It defines category in which the attribute belong in accounting portal.")
    __properties = ["accountingAttributeName", "accountingAttributeValue", "effectiveDate", "modifier", "modificationTime", "isDefault", "category"]

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
    def from_json(cls, json_str: str) -> V1PortfolioConfigurationAttribute:
        """Create an instance of V1PortfolioConfigurationAttribute from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PortfolioConfigurationAttribute:
        """Create an instance of V1PortfolioConfigurationAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PortfolioConfigurationAttribute.parse_obj(obj)

        _obj = V1PortfolioConfigurationAttribute.parse_obj({
            "accounting_attribute_name": obj.get("accountingAttributeName"),
            "accounting_attribute_value": obj.get("accountingAttributeValue"),
            "effective_date": obj.get("effectiveDate"),
            "modifier": obj.get("modifier"),
            "modification_time": obj.get("modificationTime"),
            "is_default": obj.get("isDefault"),
            "category": obj.get("category")
        })
        return _obj
