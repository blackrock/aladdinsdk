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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v1.positions.models.v1_boolean_operator import V1BooleanOperator

class V1DataFilterTree(BaseModel):
    """
    V1DataFilterTree
    """
    boolean_operator: Optional[V1BooleanOperator] = Field(None, alias="booleanOperator")
    data_filters: Optional[conlist(V1DataFilter)] = Field(None, alias="dataFilters")
    __properties = ["booleanOperator", "dataFilters"]

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
    def from_json(cls, json_str: str) -> V1DataFilterTree:
        """Create an instance of V1DataFilterTree from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data_filters (list)
        _items = []
        if self.data_filters:
            for _item in self.data_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DataFilterTree:
        """Create an instance of V1DataFilterTree from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DataFilterTree.parse_obj(obj)

        _obj = V1DataFilterTree.parse_obj({
            "boolean_operator": obj.get("booleanOperator"),
            "data_filters": [V1DataFilter.from_dict(_item) for _item in obj.get("dataFilters")] if obj.get("dataFilters") is not None else None
        })
        return _obj

