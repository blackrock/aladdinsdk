# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

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
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v1.PositionsAPI.models.v1_data_value import V1DataValue

class V1Range(BaseModel):
    """
    V1Range
    """
    start_value: Optional[V1DataValue] = Field(None, alias="startValue")
    end_value: Optional[V1DataValue] = Field(None, alias="endValue")
    __properties = ["startValue", "endValue"]

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
    def from_json(cls, json_str: str) -> V1Range:
        """Create an instance of V1Range from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_value
        if self.start_value:
            _dict['startValue'] = self.start_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_value
        if self.end_value:
            _dict['endValue'] = self.end_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Range:
        """Create an instance of V1Range from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Range.parse_obj(obj)

        _obj = V1Range.parse_obj({
            "start_value": V1DataValue.from_dict(obj.get("startValue")) if obj.get("startValue") is not None else None,
            "end_value": V1DataValue.from_dict(obj.get("endValue")) if obj.get("endValue") is not None else None
        })
        return _obj
