# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.research_note.models.any import Any

class RpcStatus(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: Optional[StrictInt] = None
    message: Optional[StrictStr] = None
    details: Optional[List[Any]] = None
    __properties = ["code", "message", "details"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RpcStatus:
        """Create an instance of RpcStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RpcStatus:
        """Create an instance of RpcStatus from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RpcStatus.parse_obj(obj)

        _obj = RpcStatus.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "details": [Any.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        return _obj

