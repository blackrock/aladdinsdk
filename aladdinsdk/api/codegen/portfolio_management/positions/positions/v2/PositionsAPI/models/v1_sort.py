# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v1_sort_order import V1SortOrder

class V1Sort(BaseModel):
    """
    V1Sort
    """
    sort_order: Optional[V1SortOrder] = Field(None, alias="sortOrder")
    attribute_id: StrictStr = Field(..., alias="attributeId")
    __properties = ["sortOrder", "attributeId"]

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
    def from_json(cls, json_str: str) -> V1Sort:
        """Create an instance of V1Sort from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Sort:
        """Create an instance of V1Sort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Sort.parse_obj(obj)

        _obj = V1Sort.parse_obj({
            "sort_order": obj.get("sortOrder"),
            "attribute_id": obj.get("attributeId")
        })
        return _obj
