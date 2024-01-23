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
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_workflow.models.v1_risk_workflow_activity import V1RiskWorkflowActivity
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_workflow.models.v1_risk_workflow_priority import V1RiskWorkflowPriority

class V1RiskWorkflow(BaseModel):
    """
    Representation of Risk Workflow.
    """
    id: Optional[StrictStr] = None
    workflow_activity: Optional[V1RiskWorkflowActivity] = Field(None, alias="workflowActivity")
    exception_id: Optional[StrictStr] = Field(None, alias="exceptionId")
    workflow_description: Optional[StrictStr] = Field(None, alias="workflowDescription")
    workflow_priority: Optional[V1RiskWorkflowPriority] = Field(None, alias="workflowPriority")
    workflow_failure_message: Optional[StrictStr] = Field(None, alias="workflowFailureMessage")
    workflow_available_actions: Optional[conlist(StrictStr)] = Field(None, alias="workflowAvailableActions")
    rule_id: StrictStr = Field(..., alias="ruleId")
    scope_id: StrictStr = Field(..., alias="scopeId")
    scope_type: StrictStr = Field(..., alias="scopeType")
    __properties = ["id", "workflowActivity", "exceptionId", "workflowDescription", "workflowPriority", "workflowFailureMessage", "workflowAvailableActions", "ruleId", "scopeId", "scopeType"]

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
    def from_json(cls, json_str: str) -> V1RiskWorkflow:
        """Create an instance of V1RiskWorkflow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "workflow_failure_message",
                            "workflow_available_actions",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of workflow_activity
        if self.workflow_activity:
            _dict['workflowActivity'] = self.workflow_activity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RiskWorkflow:
        """Create an instance of V1RiskWorkflow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RiskWorkflow.parse_obj(obj)

        _obj = V1RiskWorkflow.parse_obj({
            "id": obj.get("id"),
            "workflow_activity": V1RiskWorkflowActivity.from_dict(obj.get("workflowActivity")) if obj.get("workflowActivity") is not None else None,
            "exception_id": obj.get("exceptionId"),
            "workflow_description": obj.get("workflowDescription"),
            "workflow_priority": obj.get("workflowPriority"),
            "workflow_failure_message": obj.get("workflowFailureMessage"),
            "workflow_available_actions": obj.get("workflowAvailableActions"),
            "rule_id": obj.get("ruleId"),
            "scope_id": obj.get("scopeId"),
            "scope_type": obj.get("scopeType")
        })
        return _obj

