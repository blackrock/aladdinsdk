# coding: utf-8

"""
    Criterion

    Create, modify, delete, search and evaluate criteria.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.surveillance.criterion.v1.CriterionAPI.models.enums_criterion_type import EnumsCriterionType
from aladdinsdk.api.codegen.investment_research.surveillance.criterion.v1.CriterionAPI.models.enums_notification_frequency import EnumsNotificationFrequency

class V1RunCriteriaRequest(BaseModel):
    """
    V1RunCriteriaRequest
    """
    ids: Optional[conlist(StrictStr)] = None
    types: Optional[conlist(EnumsCriterionType)] = None
    list_ids: Optional[conlist(StrictStr)] = Field(None, alias="listIds")
    owners: Optional[conlist(StrictStr)] = None
    frequency: Optional[EnumsNotificationFrequency] = None
    last_execution_time: Optional[datetime] = Field(None, alias="lastExecutionTime")
    current_execution_time: Optional[datetime] = Field(None, alias="currentExecutionTime")
    __properties = ["ids", "types", "listIds", "owners", "frequency", "lastExecutionTime", "currentExecutionTime"]

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
    def from_json(cls, json_str: str) -> V1RunCriteriaRequest:
        """Create an instance of V1RunCriteriaRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RunCriteriaRequest:
        """Create an instance of V1RunCriteriaRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RunCriteriaRequest.parse_obj(obj)

        _obj = V1RunCriteriaRequest.parse_obj({
            "ids": obj.get("ids"),
            "types": obj.get("types"),
            "list_ids": obj.get("listIds"),
            "owners": obj.get("owners"),
            "frequency": obj.get("frequency"),
            "last_execution_time": obj.get("lastExecutionTime"),
            "current_execution_time": obj.get("currentExecutionTime")
        })
        return _obj
