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


from typing import List, Optional
from pydantic import BaseModel, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_liquidity_asset_model_selection import V1LiquidityAssetModelSelection

class V1LiquidityAdvancedSetting(BaseModel):
    """
    V1LiquidityAdvancedSetting
    """
    models: Optional[conlist(V1LiquidityAssetModelSelection)] = None
    __properties = ["models"]

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
    def from_json(cls, json_str: str) -> V1LiquidityAdvancedSetting:
        """Create an instance of V1LiquidityAdvancedSetting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in models (list)
        _items = []
        if self.models:
            for _item in self.models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['models'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LiquidityAdvancedSetting:
        """Create an instance of V1LiquidityAdvancedSetting from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LiquidityAdvancedSetting.parse_obj(obj)

        _obj = V1LiquidityAdvancedSetting.parse_obj({
            "models": [V1LiquidityAssetModelSelection.from_dict(_item) for _item in obj.get("models")] if obj.get("models") is not None else None
        })
        return _obj

