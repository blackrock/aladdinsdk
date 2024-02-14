# coding: utf-8

"""
    Risk Governance - Tasks

    Retrieve Tasks, as surfaced in Risk Radar, which are aggregates that comprise of related Exceptions, Rules, and Workflow items.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_evaluation_state import V1EvaluationState
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_limit import V1Limit
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskTaskAPI.models.v1_threshold import V1Threshold

class V1SectorResult(BaseModel):
    """
    V1SectorResult
    """
    sector: Optional[StrictStr] = None
    last_threshold_crossed: Optional[V1Threshold] = Field(None, alias="lastThresholdCrossed")
    evaluation_state: Optional[V1EvaluationState] = Field(None, alias="evaluationState")
    actual_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="actualValue")
    limit: Optional[V1Limit] = None
    __properties = ["sector", "lastThresholdCrossed", "evaluationState", "actualValue", "limit"]

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
    def from_json(cls, json_str: str) -> V1SectorResult:
        """Create an instance of V1SectorResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of limit
        if self.limit:
            _dict['limit'] = self.limit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SectorResult:
        """Create an instance of V1SectorResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SectorResult.parse_obj(obj)

        _obj = V1SectorResult.parse_obj({
            "sector": obj.get("sector"),
            "last_threshold_crossed": obj.get("lastThresholdCrossed"),
            "evaluation_state": obj.get("evaluationState"),
            "actual_value": obj.get("actualValue"),
            "limit": V1Limit.from_dict(obj.get("limit")) if obj.get("limit") is not None else None
        })
        return _obj

