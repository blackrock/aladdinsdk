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



from pydantic import BaseModel, Field, StrictStr, constr

class ResearchNoteAPICreateResearchNote400Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: constr(strict=True, max_length=40) = Field(..., description="A short mnemonic reference code for the error.")
    message: StrictStr = Field(..., description="A human readable description of the error.")
    __properties = ["code", "message"]

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
    def from_json(cls, json_str: str) -> ResearchNoteAPICreateResearchNote400Response:
        """Create an instance of ResearchNoteAPICreateResearchNote400Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResearchNoteAPICreateResearchNote400Response:
        """Create an instance of ResearchNoteAPICreateResearchNote400Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ResearchNoteAPICreateResearchNote400Response.parse_obj(obj)

        _obj = ResearchNoteAPICreateResearchNote400Response.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message")
        })
        return _obj

