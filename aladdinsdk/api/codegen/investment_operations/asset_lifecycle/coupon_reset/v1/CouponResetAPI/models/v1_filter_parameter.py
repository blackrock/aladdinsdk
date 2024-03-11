# coding: utf-8

"""
    Coupon Reset

    Coupon in Aladdin are generated internally by Aladdin's Bulk Rate Mechanism (BRM) module or sourced from external vendors. This API allows for retrieval of coupon reset records based on a number of criteria including assetId, dates and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.coupon_reset.v1.CouponResetAPI.models.v1_comparison import V1Comparison
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.coupon_reset.v1.CouponResetAPI.models.v1_coupon_reset_parameter_name import V1CouponResetParameterName
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.coupon_reset.v1.CouponResetAPI.models.v1_parameter_value import V1ParameterValue

class V1FilterParameter(BaseModel):
    """
    V1FilterParameter
    """
    parameter_name: Optional[V1CouponResetParameterName] = Field(None, alias="parameterName")
    parameter_value: Optional[V1ParameterValue] = Field(None, alias="parameterValue")
    self_operator: Optional[V1Comparison] = Field(None, alias="selfOperator")
    __properties = ["parameterName", "parameterValue", "selfOperator"]

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
    def from_json(cls, json_str: str) -> V1FilterParameter:
        """Create an instance of V1FilterParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parameter_value
        if self.parameter_value:
            _dict['parameterValue'] = self.parameter_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterParameter:
        """Create an instance of V1FilterParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterParameter.parse_obj(obj)

        _obj = V1FilterParameter.parse_obj({
            "parameter_name": obj.get("parameterName"),
            "parameter_value": V1ParameterValue.from_dict(obj.get("parameterValue")) if obj.get("parameterValue") is not None else None,
            "self_operator": obj.get("selfOperator")
        })
        return _obj

