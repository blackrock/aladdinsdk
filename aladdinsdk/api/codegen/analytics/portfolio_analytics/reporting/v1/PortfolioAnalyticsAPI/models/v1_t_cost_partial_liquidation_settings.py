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
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_partial_liquidation_strategy import V1PartialLiquidationStrategy

class V1TCostPartialLiquidationSettings(BaseModel):
    """
    V1TCostPartialLiquidationSettings
    """
    liquidation_strategy: Optional[V1PartialLiquidationStrategy] = Field(None, alias="liquidationStrategy")
    nav_percent: Optional[StrictInt] = Field(None, alias="navPercent")
    max_transaction_cost: Optional[StrictInt] = Field(None, alias="maxTransactionCost")
    max_market_impact: Optional[StrictInt] = Field(None, alias="maxMarketImpact")
    max_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maxRatio")
    __properties = ["liquidationStrategy", "navPercent", "maxTransactionCost", "maxMarketImpact", "maxRatio"]

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
    def from_json(cls, json_str: str) -> V1TCostPartialLiquidationSettings:
        """Create an instance of V1TCostPartialLiquidationSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TCostPartialLiquidationSettings:
        """Create an instance of V1TCostPartialLiquidationSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TCostPartialLiquidationSettings.parse_obj(obj)

        _obj = V1TCostPartialLiquidationSettings.parse_obj({
            "liquidation_strategy": obj.get("liquidationStrategy"),
            "nav_percent": obj.get("navPercent"),
            "max_transaction_cost": obj.get("maxTransactionCost"),
            "max_market_impact": obj.get("maxMarketImpact"),
            "max_ratio": obj.get("maxRatio")
        })
        return _obj

