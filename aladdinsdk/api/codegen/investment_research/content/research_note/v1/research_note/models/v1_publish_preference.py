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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class V1PublishPreference(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    default_note_category: Optional[StrictStr] = Field(None, alias="defaultNoteCategory")
    default_permission_groups: Optional[List[StrictStr]] = Field(None, alias="defaultPermissionGroups")
    can_publish_note: Optional[StrictBool] = Field(None, alias="canPublishNote")
    __properties = ["defaultNoteCategory", "defaultPermissionGroups", "canPublishNote"]

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
    def from_json(cls, json_str: str) -> V1PublishPreference:
        """Create an instance of V1PublishPreference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PublishPreference:
        """Create an instance of V1PublishPreference from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return V1PublishPreference.parse_obj(obj)

        _obj = V1PublishPreference.parse_obj({
            "default_note_category": obj.get("defaultNoteCategory"),
            "default_permission_groups": obj.get("defaultPermissionGroups"),
            "can_publish_note": obj.get("canPublishNote")
        })
        return _obj

