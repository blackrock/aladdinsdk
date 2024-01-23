# coding: utf-8

"""
    Risk Governance - Rule Evaluation

    Trigger Rule evaluations for Rules created and subscribed to within Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.evaluator_analytics.models.v1_portfolio_analytics_benchmark_config import V1PortfolioAnalyticsBenchmarkConfig

class V1EvaluatePortfolioRequest(BaseModel):
    """
    V1EvaluatePortfolioRequest
    """
    portfolio_id: StrictStr = Field(..., alias="portfolioId")
    as_of_date: date = Field(..., alias="asOfDate")
    benchmark_config: Optional[V1PortfolioAnalyticsBenchmarkConfig] = Field(None, alias="benchmarkConfig")
    __properties = ["portfolioId", "asOfDate", "benchmarkConfig"]

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
    def from_json(cls, json_str: str) -> V1EvaluatePortfolioRequest:
        """Create an instance of V1EvaluatePortfolioRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of benchmark_config
        if self.benchmark_config:
            _dict['benchmarkConfig'] = self.benchmark_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EvaluatePortfolioRequest:
        """Create an instance of V1EvaluatePortfolioRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EvaluatePortfolioRequest.parse_obj(obj)

        _obj = V1EvaluatePortfolioRequest.parse_obj({
            "portfolio_id": obj.get("portfolioId"),
            "as_of_date": obj.get("asOfDate"),
            "benchmark_config": V1PortfolioAnalyticsBenchmarkConfig.from_dict(obj.get("benchmarkConfig")) if obj.get("benchmarkConfig") is not None else None
        })
        return _obj

