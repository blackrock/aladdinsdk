# coding: utf-8

"""
    Criterion

    Create, modify, delete, search and evaluate criteria.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.investment_research.surveillance.criterion.v1.criterion.models.types_string_array import TypesStringArray

class TypesDataValue(BaseModel):
    """
    TypesDataValue
    """
    boolean_value: Optional[StrictBool] = Field(None, alias="booleanValue")
    integer_value: Optional[StrictInt] = Field(None, alias="integerValue")
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="doubleValue")
    string_value: Optional[StrictStr] = Field(None, alias="stringValue")
    long_value: Optional[StrictStr] = Field(None, alias="longValue")
    string_array_value: Optional[TypesStringArray] = Field(None, alias="stringArrayValue")
    field_date: Optional[date] = Field(None, alias="fieldDate")
    __properties = ["booleanValue", "integerValue", "doubleValue", "stringValue", "longValue", "stringArrayValue", "fieldDate"]

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
    def from_json(cls, json_str: str) -> TypesDataValue:
        """Create an instance of TypesDataValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of string_array_value
        if self.string_array_value:
            _dict['stringArrayValue'] = self.string_array_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypesDataValue:
        """Create an instance of TypesDataValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypesDataValue.parse_obj(obj)

        _obj = TypesDataValue.parse_obj({
            "boolean_value": obj.get("booleanValue"),
            "integer_value": obj.get("integerValue"),
            "double_value": obj.get("doubleValue"),
            "string_value": obj.get("stringValue"),
            "long_value": obj.get("longValue"),
            "string_array_value": TypesStringArray.from_dict(obj.get("stringArrayValue")) if obj.get("stringArrayValue") is not None else None,
            "field_date": obj.get("fieldDate")
        })
        return _obj

