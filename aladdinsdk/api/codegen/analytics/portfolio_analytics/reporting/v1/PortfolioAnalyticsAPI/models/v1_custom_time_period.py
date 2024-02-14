# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class V1CustomTimePeriod(BaseModel):
    """
    Time period with a custom start and end date.
    """
    start_date: Optional[date] = Field(None, alias="startDate", description="The start date of the time period.")
    end_date: Optional[date] = Field(None, alias="endDate", description="The end date of the time period.")
    __properties = ["startDate", "endDate"]

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
    def from_json(cls, json_str: str) -> V1CustomTimePeriod:
        """Create an instance of V1CustomTimePeriod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomTimePeriod:
        """Create an instance of V1CustomTimePeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomTimePeriod.parse_obj(obj)

        _obj = V1CustomTimePeriod.parse_obj({
            "start_date": obj.get("startDate"),
            "end_date": obj.get("endDate")
        })
        return _obj

