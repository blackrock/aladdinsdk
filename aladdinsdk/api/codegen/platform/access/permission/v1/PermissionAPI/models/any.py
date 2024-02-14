# coding: utf-8

"""
    Aladdin Permission

    API contains operations on Aladdin Permission resource. Permissions cannot be applied directly to a user, they must be applied to a User Group first, then the user is added to a User Group. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class Any(BaseModel):
    """
    `Any` contains an arbitrary serialized message along with a URL that describes the type of the serialized message
    """
    type: Optional[StrictStr] = Field(None, alias="@type", description="A URL/resource name that uniquely identifies the type of the serialized message.")
    __properties = ["@type"]

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
    def from_json(cls, json_str: str) -> Any:
        """Create an instance of Any from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Any:
        """Create an instance of Any from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Any.parse_obj(obj)

        _obj = Any.parse_obj({
            "type": obj.get("@type")
        })
        return _obj

