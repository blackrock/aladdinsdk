# coding: utf-8

"""
    Risk Governance - Exceptions

    Retrieve, update, or create Exceptions as surfaced in Risk Radar.  # noqa: E501

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

class V1RiskNavigationLinks(BaseModel):
    """
    Class to carry the links to be used when navigating across the data matched by a given criteria.
    """
    var_self: Optional[StrictStr] = Field(None, alias="self")
    first: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    next: Optional[StrictStr] = None
    last: Optional[StrictStr] = None
    __properties = ["self", "first", "previous", "next", "last"]

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
    def from_json(cls, json_str: str) -> V1RiskNavigationLinks:
        """Create an instance of V1RiskNavigationLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RiskNavigationLinks:
        """Create an instance of V1RiskNavigationLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RiskNavigationLinks.parse_obj(obj)

        _obj = V1RiskNavigationLinks.parse_obj({
            "var_self": obj.get("self"),
            "first": obj.get("first"),
            "previous": obj.get("previous"),
            "next": obj.get("next"),
            "last": obj.get("last")
        })
        return _obj
