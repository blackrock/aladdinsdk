# coding: utf-8

"""
    Compliance Rule Assignment

    Rule assignment assigns compliance rules for portfolio.  # noqa: E501

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
from aladdinsdk.api.codegen.compliance.state.compliance_rule_assignment.v1.compliance_rule_assignment.models.enums_compliance_test_detail_operator import EnumsComplianceTestDetailOperator

class V1TestDetail(BaseModel):
    """
    V1TestDetail
    """
    test_token: Optional[StrictStr] = Field(None, alias="testToken")
    test_operator: Optional[EnumsComplianceTestDetailOperator] = Field(None, alias="testOperator")
    test_value1: Optional[StrictStr] = Field(None, alias="testValue1")
    test_value2: Optional[StrictStr] = Field(None, alias="testValue2")
    warning_value1: Optional[StrictStr] = Field(None, alias="warningValue1")
    warning_value2: Optional[StrictStr] = Field(None, alias="warningValue2")
    __properties = ["testToken", "testOperator", "testValue1", "testValue2", "warningValue1", "warningValue2"]

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
    def from_json(cls, json_str: str) -> V1TestDetail:
        """Create an instance of V1TestDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TestDetail:
        """Create an instance of V1TestDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TestDetail.parse_obj(obj)

        _obj = V1TestDetail.parse_obj({
            "test_token": obj.get("testToken"),
            "test_operator": obj.get("testOperator"),
            "test_value1": obj.get("testValue1"),
            "test_value2": obj.get("testValue2"),
            "warning_value1": obj.get("warningValue1"),
            "warning_value2": obj.get("warningValue2")
        })
        return _obj

