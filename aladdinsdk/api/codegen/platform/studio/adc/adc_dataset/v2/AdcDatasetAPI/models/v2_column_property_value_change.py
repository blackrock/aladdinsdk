# coding: utf-8

"""
    Adc Dataset

    Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

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
from aladdinsdk.api.codegen.platform.studio.adc.adc_dataset.v2.AdcDatasetAPI.models.v2_column_property import V2ColumnProperty

class V2ColumnPropertyValueChange(BaseModel):
    """
    V2ColumnPropertyValueChange
    """
    column_property: Optional[V2ColumnProperty] = Field(None, alias="columnProperty")
    current_value: Optional[StrictStr] = Field(None, alias="currentValue")
    previous_value: Optional[StrictStr] = Field(None, alias="previousValue")
    __properties = ["columnProperty", "currentValue", "previousValue"]

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
    def from_json(cls, json_str: str) -> V2ColumnPropertyValueChange:
        """Create an instance of V2ColumnPropertyValueChange from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ColumnPropertyValueChange:
        """Create an instance of V2ColumnPropertyValueChange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ColumnPropertyValueChange.parse_obj(obj)

        _obj = V2ColumnPropertyValueChange.parse_obj({
            "column_property": obj.get("columnProperty"),
            "current_value": obj.get("currentValue"),
            "previous_value": obj.get("previousValue")
        })
        return _obj
