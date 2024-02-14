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
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_override_date_multi_period_column_option import V1OverrideDateMultiPeriodColumnOption
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_override_date_time_series_date_range_column_option import V1OverrideDateTimeSeriesDateRangeColumnOption
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_override_date_time_series_fixed_column_option import V1OverrideDateTimeSeriesFixedColumnOption

class V1OverrideDateColumnOption(BaseModel):
    """
    V1OverrideDateColumnOption
    """
    multi_period: Optional[V1OverrideDateMultiPeriodColumnOption] = Field(None, alias="multiPeriod")
    time_series_date_range: Optional[V1OverrideDateTimeSeriesDateRangeColumnOption] = Field(None, alias="timeSeriesDateRange")
    time_series_fixed: Optional[V1OverrideDateTimeSeriesFixedColumnOption] = Field(None, alias="timeSeriesFixed")
    __properties = ["multiPeriod", "timeSeriesDateRange", "timeSeriesFixed"]

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
    def from_json(cls, json_str: str) -> V1OverrideDateColumnOption:
        """Create an instance of V1OverrideDateColumnOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of multi_period
        if self.multi_period:
            _dict['multiPeriod'] = self.multi_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_series_date_range
        if self.time_series_date_range:
            _dict['timeSeriesDateRange'] = self.time_series_date_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_series_fixed
        if self.time_series_fixed:
            _dict['timeSeriesFixed'] = self.time_series_fixed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1OverrideDateColumnOption:
        """Create an instance of V1OverrideDateColumnOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1OverrideDateColumnOption.parse_obj(obj)

        _obj = V1OverrideDateColumnOption.parse_obj({
            "multi_period": V1OverrideDateMultiPeriodColumnOption.from_dict(obj.get("multiPeriod")) if obj.get("multiPeriod") is not None else None,
            "time_series_date_range": V1OverrideDateTimeSeriesDateRangeColumnOption.from_dict(obj.get("timeSeriesDateRange")) if obj.get("timeSeriesDateRange") is not None else None,
            "time_series_fixed": V1OverrideDateTimeSeriesFixedColumnOption.from_dict(obj.get("timeSeriesFixed")) if obj.get("timeSeriesFixed") is not None else None
        })
        return _obj

