# coding: utf-8

"""
    Adc Dataset

    Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class V1SchemaId(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    database: StrictStr = ...
    var_schema: StrictStr = Field(..., alias="schema")
    __properties = ["database", "schema"]

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
    def from_json(cls, json_str: str) -> V1SchemaId:
        """Create an instance of V1SchemaId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SchemaId:
        """Create an instance of V1SchemaId from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return V1SchemaId.parse_obj(obj)

        _obj = V1SchemaId.parse_obj({
            "database": obj.get("database"),
            "var_schema": obj.get("schema")
        })
        return _obj

