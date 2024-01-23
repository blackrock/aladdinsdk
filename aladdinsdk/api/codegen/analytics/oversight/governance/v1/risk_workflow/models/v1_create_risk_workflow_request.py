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


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_workflow.models.v1_risk_workflow import V1RiskWorkflow

class V1CreateRiskWorkflowRequest(BaseModel):
    """
    V1CreateRiskWorkflowRequest
    """
    risk_workflow: Optional[V1RiskWorkflow] = Field(None, alias="riskWorkflow")
    __properties = ["riskWorkflow"]

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
    def from_json(cls, json_str: str) -> V1CreateRiskWorkflowRequest:
        """Create an instance of V1CreateRiskWorkflowRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of risk_workflow
        if self.risk_workflow:
            _dict['riskWorkflow'] = self.risk_workflow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CreateRiskWorkflowRequest:
        """Create an instance of V1CreateRiskWorkflowRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CreateRiskWorkflowRequest.parse_obj(obj)

        _obj = V1CreateRiskWorkflowRequest.parse_obj({
            "risk_workflow": V1RiskWorkflow.from_dict(obj.get("riskWorkflow")) if obj.get("riskWorkflow") is not None else None
        })
        return _obj

