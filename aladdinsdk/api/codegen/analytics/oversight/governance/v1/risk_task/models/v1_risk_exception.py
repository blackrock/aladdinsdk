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

from datetime import date, datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_task.models.v1_condition_result import V1ConditionResult
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_task.models.v1_evaluation_state import V1EvaluationState

class V1RiskException(BaseModel):
    """
    Representation of Risk Exception, its available fields and the flexible one \"exceptionDetail\" to store more specific details.
    """
    id: Optional[StrictStr] = None
    external_id: StrictStr = Field(..., alias="externalId")
    valid_begin_date: Optional[date] = Field(None, alias="validBeginDate")
    valid_end_date: Optional[date] = Field(None, alias="validEndDate")
    entry_time: Optional[datetime] = Field(None, alias="entryTime")
    expiry_time: Optional[datetime] = Field(None, alias="expiryTime")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    modifier: Optional[StrictStr] = None
    workflow_id: Optional[StrictStr] = Field(None, alias="workflowId")
    scope_id: StrictStr = Field(..., alias="scopeId")
    scope_type: StrictStr = Field(..., alias="scopeType")
    scope: Optional[StrictStr] = None
    entity_id: StrictStr = Field(..., alias="entityId")
    entity_type: StrictStr = Field(..., alias="entityType")
    entity: Optional[StrictStr] = None
    evaluation_state: Optional[V1EvaluationState] = Field(None, alias="evaluationState")
    rule_priority: Optional[StrictInt] = Field(None, alias="rulePriority")
    rule_id: StrictStr = Field(..., alias="ruleId")
    rule_version: StrictStr = Field(..., alias="ruleVersion")
    exception_tier: Optional[StrictStr] = Field(None, alias="exceptionTier")
    evaluation_results: Optional[conlist(V1ConditionResult)] = Field(None, alias="evaluationResults")
    exception_details: Optional[Dict[str, StrictStr]] = Field(None, alias="exceptionDetails")
    __properties = ["id", "externalId", "validBeginDate", "validEndDate", "entryTime", "expiryTime", "createTime", "modifier", "workflowId", "scopeId", "scopeType", "scope", "entityId", "entityType", "entity", "evaluationState", "rulePriority", "ruleId", "ruleVersion", "exceptionTier", "evaluationResults", "exceptionDetails"]

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
    def from_json(cls, json_str: str) -> V1RiskException:
        """Create an instance of V1RiskException from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in evaluation_results (list)
        _items = []
        if self.evaluation_results:
            for _item in self.evaluation_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['evaluationResults'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RiskException:
        """Create an instance of V1RiskException from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RiskException.parse_obj(obj)

        _obj = V1RiskException.parse_obj({
            "id": obj.get("id"),
            "external_id": obj.get("externalId"),
            "valid_begin_date": obj.get("validBeginDate"),
            "valid_end_date": obj.get("validEndDate"),
            "entry_time": obj.get("entryTime"),
            "expiry_time": obj.get("expiryTime"),
            "create_time": obj.get("createTime"),
            "modifier": obj.get("modifier"),
            "workflow_id": obj.get("workflowId"),
            "scope_id": obj.get("scopeId"),
            "scope_type": obj.get("scopeType"),
            "scope": obj.get("scope"),
            "entity_id": obj.get("entityId"),
            "entity_type": obj.get("entityType"),
            "entity": obj.get("entity"),
            "evaluation_state": obj.get("evaluationState"),
            "rule_priority": obj.get("rulePriority"),
            "rule_id": obj.get("ruleId"),
            "rule_version": obj.get("ruleVersion"),
            "exception_tier": obj.get("exceptionTier"),
            "evaluation_results": [V1ConditionResult.from_dict(_item) for _item in obj.get("evaluationResults")] if obj.get("evaluationResults") is not None else None,
            "exception_details": obj.get("exceptionDetails")
        })
        return _obj

