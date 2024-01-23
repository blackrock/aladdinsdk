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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_custom_evaluation_metric.models.v1_risk_custom_evaluation_metric import V1RiskCustomEvaluationMetric

class V1ListRiskCustomEvaluationMetricResponse(BaseModel):
    """
    V1ListRiskCustomEvaluationMetricResponse
    """
    risk_custom_evaluation_metrics: Optional[conlist(V1RiskCustomEvaluationMetric)] = Field(None, alias="riskCustomEvaluationMetrics")
    total: Optional[StrictInt] = None
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["riskCustomEvaluationMetrics", "total", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1ListRiskCustomEvaluationMetricResponse:
        """Create an instance of V1ListRiskCustomEvaluationMetricResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in risk_custom_evaluation_metrics (list)
        _items = []
        if self.risk_custom_evaluation_metrics:
            for _item in self.risk_custom_evaluation_metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['riskCustomEvaluationMetrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListRiskCustomEvaluationMetricResponse:
        """Create an instance of V1ListRiskCustomEvaluationMetricResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListRiskCustomEvaluationMetricResponse.parse_obj(obj)

        _obj = V1ListRiskCustomEvaluationMetricResponse.parse_obj({
            "risk_custom_evaluation_metrics": [V1RiskCustomEvaluationMetric.from_dict(_item) for _item in obj.get("riskCustomEvaluationMetrics")] if obj.get("riskCustomEvaluationMetrics") is not None else None,
            "total": obj.get("total"),
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

