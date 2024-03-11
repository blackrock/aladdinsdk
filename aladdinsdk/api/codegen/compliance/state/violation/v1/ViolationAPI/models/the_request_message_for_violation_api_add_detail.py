# coding: utf-8

"""
    Violation

    Retrieve and Create Compliance Violations  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class TheRequestMessageForViolationAPIAddDetail(BaseModel):
    """
    TheRequestMessageForViolationAPIAddDetail
    """
    cause_type: Optional[StrictStr] = Field(None, alias="causeType", description="The root cause of the violation.")
    modification_time: datetime = Field(..., alias="modificationTime", description="The modified time of the violation you are intending to update. This field will be used to validate that the violation being updated has not already been altered by someone else.")
    violation_detail: StrictStr = Field(..., alias="violationDetail")
    __properties = ["causeType", "modificationTime", "violationDetail"]

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
    def from_json(cls, json_str: str) -> TheRequestMessageForViolationAPIAddDetail:
        """Create an instance of TheRequestMessageForViolationAPIAddDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TheRequestMessageForViolationAPIAddDetail:
        """Create an instance of TheRequestMessageForViolationAPIAddDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TheRequestMessageForViolationAPIAddDetail.parse_obj(obj)

        _obj = TheRequestMessageForViolationAPIAddDetail.parse_obj({
            "cause_type": obj.get("causeType"),
            "modification_time": obj.get("modificationTime"),
            "violation_detail": obj.get("violationDetail")
        })
        return _obj

