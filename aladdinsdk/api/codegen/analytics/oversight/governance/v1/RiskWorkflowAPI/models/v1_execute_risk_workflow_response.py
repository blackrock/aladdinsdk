# coding: utf-8

"""
    Risk Governance - Workflows

    Retrieve, update, and transition Workflow items as surfaced in Risk Radar.  # noqa: E501

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
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskWorkflowAPI.models.v1_risk_workflow import V1RiskWorkflow

class V1ExecuteRiskWorkflowResponse(BaseModel):
    """
    V1ExecuteRiskWorkflowResponse
    """
    workflow_items: Optional[conlist(V1RiskWorkflow)] = Field(None, alias="workflowItems")
    __properties = ["workflowItems"]

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
    def from_json(cls, json_str: str) -> V1ExecuteRiskWorkflowResponse:
        """Create an instance of V1ExecuteRiskWorkflowResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_items (list)
        _items = []
        if self.workflow_items:
            for _item in self.workflow_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workflowItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ExecuteRiskWorkflowResponse:
        """Create an instance of V1ExecuteRiskWorkflowResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ExecuteRiskWorkflowResponse.parse_obj(obj)

        _obj = V1ExecuteRiskWorkflowResponse.parse_obj({
            "workflow_items": [V1RiskWorkflow.from_dict(_item) for _item in obj.get("workflowItems")] if obj.get("workflowItems") is not None else None
        })
        return _obj

