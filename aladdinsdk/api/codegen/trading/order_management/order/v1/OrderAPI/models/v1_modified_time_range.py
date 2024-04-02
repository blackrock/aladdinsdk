# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

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
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_time_range_parameter import V1TimeRangeParameter

class V1ModifiedTimeRange(BaseModel):
    """
    A time range used to filter orders by their modified time.  The start time range is a required field.  The end time range is an optional field, and will  default to the current server time if omitted.  The start time range must be before the end time range for a valid query range and  must not be more than 7 days from the end time range.  The timezone used will be the default aladdin timezone on the server.
    """
    start_time_range: Optional[V1TimeRangeParameter] = Field(None, alias="startTimeRange")
    end_time_range: Optional[V1TimeRangeParameter] = Field(None, alias="endTimeRange")
    __properties = ["startTimeRange", "endTimeRange"]

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
    def from_json(cls, json_str: str) -> V1ModifiedTimeRange:
        """Create an instance of V1ModifiedTimeRange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_time_range
        if self.start_time_range:
            _dict['startTimeRange'] = self.start_time_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_time_range
        if self.end_time_range:
            _dict['endTimeRange'] = self.end_time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ModifiedTimeRange:
        """Create an instance of V1ModifiedTimeRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ModifiedTimeRange.parse_obj(obj)

        _obj = V1ModifiedTimeRange.parse_obj({
            "start_time_range": V1TimeRangeParameter.from_dict(obj.get("startTimeRange")) if obj.get("startTimeRange") is not None else None,
            "end_time_range": V1TimeRangeParameter.from_dict(obj.get("endTimeRange")) if obj.get("endTimeRange") is not None else None
        })
        return _obj
