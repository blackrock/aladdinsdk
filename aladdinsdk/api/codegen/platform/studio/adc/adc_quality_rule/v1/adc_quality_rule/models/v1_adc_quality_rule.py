# coding: utf-8

"""
    Adc Quality Rule

    Manages Data Qualiy Rules in Aladdin Data Cloud (ADC). Used by Dataset Owners and ADCQualityAnalysisServer.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.platform.studio.adc.adc_quality_rule.v1.adc_quality_rule.models.v1_rule import V1Rule
from aladdinsdk.api.codegen.platform.studio.adc.adc_quality_rule.v1.adc_quality_rule.models.v1_rule_group import V1RuleGroup

class V1AdcQualityRule(BaseModel):
    """
    Adc quality rule describes...
    """
    id: Optional[StrictStr] = None
    client_abbreviation: Optional[StrictStr] = Field(None, alias="clientAbbreviation")
    database: Optional[StrictStr] = None
    var_schema: Optional[StrictStr] = Field(None, alias="schema")
    dataset_name: Optional[StrictStr] = Field(None, alias="datasetName")
    description: Optional[StrictStr] = None
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    rule_group: Optional[V1RuleGroup] = Field(None, alias="ruleGroup")
    rule: Optional[V1Rule] = None
    cron_schedules: Optional[conlist(StrictStr)] = Field(None, alias="cronSchedules")
    stop_ingest: Optional[StrictBool] = Field(None, alias="stopIngest")
    min_acceptance_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="minAcceptanceRate")
    creator: Optional[StrictStr] = Field(None, description="Represents user that created this record.")
    create_time: Optional[datetime] = Field(None, alias="createTime")
    modifier: Optional[StrictStr] = Field(None, description="Represents user that last modified this record.")
    modify_time: Optional[datetime] = Field(None, alias="modifyTime")
    __properties = ["id", "clientAbbreviation", "database", "schema", "datasetName", "description", "isActive", "ruleGroup", "rule", "cronSchedules", "stopIngest", "minAcceptanceRate", "creator", "createTime", "modifier", "modifyTime"]

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
    def from_json(cls, json_str: str) -> V1AdcQualityRule:
        """Create an instance of V1AdcQualityRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rule
        if self.rule:
            _dict['rule'] = self.rule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AdcQualityRule:
        """Create an instance of V1AdcQualityRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AdcQualityRule.parse_obj(obj)

        _obj = V1AdcQualityRule.parse_obj({
            "id": obj.get("id"),
            "client_abbreviation": obj.get("clientAbbreviation"),
            "database": obj.get("database"),
            "var_schema": obj.get("schema"),
            "dataset_name": obj.get("datasetName"),
            "description": obj.get("description"),
            "is_active": obj.get("isActive"),
            "rule_group": obj.get("ruleGroup"),
            "rule": V1Rule.from_dict(obj.get("rule")) if obj.get("rule") is not None else None,
            "cron_schedules": obj.get("cronSchedules"),
            "stop_ingest": obj.get("stopIngest"),
            "min_acceptance_rate": obj.get("minAcceptanceRate"),
            "creator": obj.get("creator"),
            "create_time": obj.get("createTime"),
            "modifier": obj.get("modifier"),
            "modify_time": obj.get("modifyTime")
        })
        return _obj

