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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.custom_aggregation_column_option_column_weight_type import CustomAggregationColumnOptionColumnWeightType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.custom_aggregation_column_option_weight_type import CustomAggregationColumnOptionWeightType
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_custom_aggregation_limit import V1CustomAggregationLimit
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_custom_aggregation_subtotal_type import V1CustomAggregationSubtotalType

class V1CustomAggregationColumnOption(BaseModel):
    """
    V1CustomAggregationColumnOption
    """
    subtotal_type: Optional[V1CustomAggregationSubtotalType] = Field(None, alias="subtotalType")
    custom_aggregation_limit: Optional[V1CustomAggregationLimit] = Field(None, alias="customAggregationLimit")
    exclude_null_value: Optional[StrictBool] = Field(None, alias="excludeNullValue")
    weight_type: Optional[CustomAggregationColumnOptionWeightType] = Field(None, alias="weightType")
    column_weight_type: Optional[CustomAggregationColumnOptionColumnWeightType] = Field(None, alias="columnWeightType")
    __properties = ["subtotalType", "customAggregationLimit", "excludeNullValue", "weightType", "columnWeightType"]

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
    def from_json(cls, json_str: str) -> V1CustomAggregationColumnOption:
        """Create an instance of V1CustomAggregationColumnOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of custom_aggregation_limit
        if self.custom_aggregation_limit:
            _dict['customAggregationLimit'] = self.custom_aggregation_limit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomAggregationColumnOption:
        """Create an instance of V1CustomAggregationColumnOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomAggregationColumnOption.parse_obj(obj)

        _obj = V1CustomAggregationColumnOption.parse_obj({
            "subtotal_type": obj.get("subtotalType"),
            "custom_aggregation_limit": V1CustomAggregationLimit.from_dict(obj.get("customAggregationLimit")) if obj.get("customAggregationLimit") is not None else None,
            "exclude_null_value": obj.get("excludeNullValue"),
            "weight_type": obj.get("weightType"),
            "column_weight_type": obj.get("columnWeightType")
        })
        return _obj

