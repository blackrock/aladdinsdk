# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_model_input_type import V1ModelInputType

class V1ModelInput(BaseModel):
    """
    V1ModelInput
    """
    input_type: Optional[V1ModelInputType] = Field(None, alias="inputType")
    flat_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="flatValue")
    vector_value: Optional[StrictStr] = Field(None, alias="vectorValue")
    __properties = ["inputType", "flatValue", "vectorValue"]

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
    def from_json(cls, json_str: str) -> V1ModelInput:
        """Create an instance of V1ModelInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ModelInput:
        """Create an instance of V1ModelInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ModelInput.parse_obj(obj)

        _obj = V1ModelInput.parse_obj({
            "input_type": obj.get("inputType"),
            "flat_value": obj.get("flatValue"),
            "vector_value": obj.get("vectorValue")
        })
        return _obj

