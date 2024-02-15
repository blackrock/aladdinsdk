# coding: utf-8

"""
    Risk Governance - Custom Evaluation Metric

    Upload or Retreive Custom Evaluation Metric to be used for Rule evaluation in Risk Radar.  # noqa: E501

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
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskCustomEvaluationMetricAPI.models.v1_risk_custom_evaluation_metric import V1RiskCustomEvaluationMetric

class V1CreateRiskCustomEvaluationMetricRequest(BaseModel):
    """
    V1CreateRiskCustomEvaluationMetricRequest
    """
    as_of_date: date = Field(..., alias="asOfDate")
    risk_custom_evaluation_metric: Optional[V1RiskCustomEvaluationMetric] = Field(None, alias="riskCustomEvaluationMetric")
    __properties = ["asOfDate", "riskCustomEvaluationMetric"]

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
    def from_json(cls, json_str: str) -> V1CreateRiskCustomEvaluationMetricRequest:
        """Create an instance of V1CreateRiskCustomEvaluationMetricRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of risk_custom_evaluation_metric
        if self.risk_custom_evaluation_metric:
            _dict['riskCustomEvaluationMetric'] = self.risk_custom_evaluation_metric.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateRiskCustomEvaluationMetricRequest:
        """Create an instance of V1CreateRiskCustomEvaluationMetricRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateRiskCustomEvaluationMetricRequest.parse_obj(obj)

        _obj = V1CreateRiskCustomEvaluationMetricRequest.parse_obj({
            "as_of_date": obj.get("asOfDate"),
            "risk_custom_evaluation_metric": V1RiskCustomEvaluationMetric.from_dict(obj.get("riskCustomEvaluationMetric")) if obj.get("riskCustomEvaluationMetric") is not None else None
        })
        return _obj
