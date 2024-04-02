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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_portfolio_configuration_attribute import V1PortfolioConfigurationAttribute

class V1PortfolioConfigurationRecord(BaseModel):
    """
    V1PortfolioConfigurationRecord
    """
    id: Optional[StrictStr] = Field(None, description="It is the unique identifier for this record.")
    portfolio_ticker: Optional[StrictStr] = Field(None, alias="portfolioTicker", description="It is the ticker or portfolio name.")
    process_code: Optional[StrictStr] = Field(None, alias="processCode", description="It is the process code like W,D etc.")
    configuration_attributes: Optional[conlist(V1PortfolioConfigurationAttribute)] = Field(None, alias="configurationAttributes", description="It is the list of attributes for the configuration record.")
    keys: Optional[conlist(StrictStr)] = Field(None, description="It contains the list of key attributes for one configuration record.")
    __properties = ["id", "portfolioTicker", "processCode", "configurationAttributes", "keys"]

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
    def from_json(cls, json_str: str) -> V1PortfolioConfigurationRecord:
        """Create an instance of V1PortfolioConfigurationRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in configuration_attributes (list)
        _items = []
        if self.configuration_attributes:
            for _item in self.configuration_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['configurationAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PortfolioConfigurationRecord:
        """Create an instance of V1PortfolioConfigurationRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PortfolioConfigurationRecord.parse_obj(obj)

        _obj = V1PortfolioConfigurationRecord.parse_obj({
            "id": obj.get("id"),
            "portfolio_ticker": obj.get("portfolioTicker"),
            "process_code": obj.get("processCode"),
            "configuration_attributes": [V1PortfolioConfigurationAttribute.from_dict(_item) for _item in obj.get("configurationAttributes")] if obj.get("configurationAttributes") is not None else None,
            "keys": obj.get("keys")
        })
        return _obj
