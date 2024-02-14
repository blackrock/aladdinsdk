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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_look_through_config import V1LookThroughConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_portfolio_analytics_benchmark_config import V1PortfolioAnalyticsBenchmarkConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_portfolio_analytics_breakdown_config import V1PortfolioAnalyticsBreakdownConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_portfolio_analytics_column_set_config import V1PortfolioAnalyticsColumnSetConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_portfolio_analytics_filter_config import V1PortfolioAnalyticsFilterConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_split_position_config import V1SplitPositionConfig
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.PortfolioAnalyticsAPI.models.v1_time_series_period_setting import V1TimeSeriesPeriodSetting

class V1ComputePortfolioTimeSeriesAnalyticsRequest(BaseModel):
    """
    V1ComputePortfolioTimeSeriesAnalyticsRequest
    """
    portfolio_ticker: Optional[StrictStr] = Field(None, alias="portfolioTicker")
    time_series_period_setting: Optional[V1TimeSeriesPeriodSetting] = Field(None, alias="timeSeriesPeriodSetting")
    reporting_currency_code: Optional[StrictStr] = Field(None, alias="reportingCurrencyCode")
    benchmark_config: Optional[V1PortfolioAnalyticsBenchmarkConfig] = Field(None, alias="benchmarkConfig")
    breakdown_config: Optional[V1PortfolioAnalyticsBreakdownConfig] = Field(None, alias="breakdownConfig")
    column_config: Optional[V1PortfolioAnalyticsColumnSetConfig] = Field(None, alias="columnConfig")
    split_position_config: Optional[V1SplitPositionConfig] = Field(None, alias="splitPositionConfig")
    look_through_config: Optional[V1LookThroughConfig] = Field(None, alias="lookThroughConfig")
    filter_configs: Optional[conlist(V1PortfolioAnalyticsFilterConfig)] = Field(None, alias="filterConfigs")
    calendar: Optional[StrictStr] = None
    bypass_caching: Optional[StrictBool] = Field(None, alias="bypassCaching", description="bypass Explore level caching. Default value is false.")
    __properties = ["portfolioTicker", "timeSeriesPeriodSetting", "reportingCurrencyCode", "benchmarkConfig", "breakdownConfig", "columnConfig", "splitPositionConfig", "lookThroughConfig", "filterConfigs", "calendar", "bypassCaching"]

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
    def from_json(cls, json_str: str) -> V1ComputePortfolioTimeSeriesAnalyticsRequest:
        """Create an instance of V1ComputePortfolioTimeSeriesAnalyticsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of time_series_period_setting
        if self.time_series_period_setting:
            _dict['timeSeriesPeriodSetting'] = self.time_series_period_setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of benchmark_config
        if self.benchmark_config:
            _dict['benchmarkConfig'] = self.benchmark_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of breakdown_config
        if self.breakdown_config:
            _dict['breakdownConfig'] = self.breakdown_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of column_config
        if self.column_config:
            _dict['columnConfig'] = self.column_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of split_position_config
        if self.split_position_config:
            _dict['splitPositionConfig'] = self.split_position_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of look_through_config
        if self.look_through_config:
            _dict['lookThroughConfig'] = self.look_through_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filter_configs (list)
        _items = []
        if self.filter_configs:
            for _item in self.filter_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filterConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ComputePortfolioTimeSeriesAnalyticsRequest:
        """Create an instance of V1ComputePortfolioTimeSeriesAnalyticsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ComputePortfolioTimeSeriesAnalyticsRequest.parse_obj(obj)

        _obj = V1ComputePortfolioTimeSeriesAnalyticsRequest.parse_obj({
            "portfolio_ticker": obj.get("portfolioTicker"),
            "time_series_period_setting": V1TimeSeriesPeriodSetting.from_dict(obj.get("timeSeriesPeriodSetting")) if obj.get("timeSeriesPeriodSetting") is not None else None,
            "reporting_currency_code": obj.get("reportingCurrencyCode"),
            "benchmark_config": V1PortfolioAnalyticsBenchmarkConfig.from_dict(obj.get("benchmarkConfig")) if obj.get("benchmarkConfig") is not None else None,
            "breakdown_config": V1PortfolioAnalyticsBreakdownConfig.from_dict(obj.get("breakdownConfig")) if obj.get("breakdownConfig") is not None else None,
            "column_config": V1PortfolioAnalyticsColumnSetConfig.from_dict(obj.get("columnConfig")) if obj.get("columnConfig") is not None else None,
            "split_position_config": V1SplitPositionConfig.from_dict(obj.get("splitPositionConfig")) if obj.get("splitPositionConfig") is not None else None,
            "look_through_config": V1LookThroughConfig.from_dict(obj.get("lookThroughConfig")) if obj.get("lookThroughConfig") is not None else None,
            "filter_configs": [V1PortfolioAnalyticsFilterConfig.from_dict(_item) for _item in obj.get("filterConfigs")] if obj.get("filterConfigs") is not None else None,
            "calendar": obj.get("calendar"),
            "bypass_caching": obj.get("bypassCaching")
        })
        return _obj

