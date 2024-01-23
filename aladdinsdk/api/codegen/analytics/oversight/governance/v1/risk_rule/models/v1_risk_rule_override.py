# coding: utf-8

"""
    Risk Governance - Rules

    Retrieve, update, and create Rules and Rule Subscriptions as surfaced in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_rule.models.v1_condition_definition_override import V1ConditionDefinitionOverride
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_rule.models.v1_risk_rule_state import V1RiskRuleState

class V1RiskRuleOverride(BaseModel):
    """
    Captures one or more overridden condition attributes and limit definitions for a given RiskRule.
    """
    id: Optional[StrictStr] = None
    rule_id: StrictStr = Field(..., alias="ruleId")
    name: StrictStr = Field(...)
    condition_overrides: Optional[conlist(V1ConditionDefinitionOverride)] = Field(None, alias="conditionOverrides")
    override_state: Optional[V1RiskRuleState] = Field(None, alias="overrideState")
    final_sign_off_author: Optional[StrictStr] = Field(None, alias="finalSignOffAuthor")
    final_sign_off_time: Optional[datetime] = Field(None, alias="finalSignOffTime")
    modifier: Optional[StrictStr] = None
    modify_time: Optional[datetime] = Field(None, alias="modifyTime")
    version: Optional[StrictStr] = None
    effective_date: date = Field(..., alias="effectiveDate")
    version_time: Optional[datetime] = Field(None, alias="versionTime")
    __properties = ["id", "ruleId", "name", "conditionOverrides", "overrideState", "finalSignOffAuthor", "finalSignOffTime", "modifier", "modifyTime", "version", "effectiveDate", "versionTime"]

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
    def from_json(cls, json_str: str) -> V1RiskRuleOverride:
        """Create an instance of V1RiskRuleOverride from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "version_time",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in condition_overrides (list)
        _items = []
        if self.condition_overrides:
            for _item in self.condition_overrides:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditionOverrides'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RiskRuleOverride:
        """Create an instance of V1RiskRuleOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RiskRuleOverride.parse_obj(obj)

        _obj = V1RiskRuleOverride.parse_obj({
            "id": obj.get("id"),
            "rule_id": obj.get("ruleId"),
            "name": obj.get("name"),
            "condition_overrides": [V1ConditionDefinitionOverride.from_dict(_item) for _item in obj.get("conditionOverrides")] if obj.get("conditionOverrides") is not None else None,
            "override_state": obj.get("overrideState"),
            "final_sign_off_author": obj.get("finalSignOffAuthor"),
            "final_sign_off_time": obj.get("finalSignOffTime"),
            "modifier": obj.get("modifier"),
            "modify_time": obj.get("modifyTime"),
            "version": obj.get("version"),
            "effective_date": obj.get("effectiveDate"),
            "version_time": obj.get("versionTime")
        })
        return _obj

