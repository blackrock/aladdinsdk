# coding: utf-8

"""
    Risk Governance - Configuration

    Retrieve, update, and create configurations which drive Risk Governance behaviours and Risk Radar UI choices.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskConfigAPI.models.v1_custom_evaluation_metric_config import V1CustomEvaluationMetricConfig

class V1CustomEvaluationMetricConfigRecord(BaseModel):
    """
    V1CustomEvaluationMetricConfigRecord
    """
    custom_metric_configs: Optional[conlist(V1CustomEvaluationMetricConfig)] = Field(None, alias="customMetricConfigs")
    __properties = ["customMetricConfigs"]

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
    def from_json(cls, json_str: str) -> V1CustomEvaluationMetricConfigRecord:
        """Create an instance of V1CustomEvaluationMetricConfigRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in custom_metric_configs (list)
        _items = []
        if self.custom_metric_configs:
            for _item in self.custom_metric_configs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customMetricConfigs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomEvaluationMetricConfigRecord:
        """Create an instance of V1CustomEvaluationMetricConfigRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomEvaluationMetricConfigRecord.parse_obj(obj)

        _obj = V1CustomEvaluationMetricConfigRecord.parse_obj({
            "custom_metric_configs": [V1CustomEvaluationMetricConfig.from_dict(_item) for _item in obj.get("customMetricConfigs")] if obj.get("customMetricConfigs") is not None else None
        })
        return _obj
