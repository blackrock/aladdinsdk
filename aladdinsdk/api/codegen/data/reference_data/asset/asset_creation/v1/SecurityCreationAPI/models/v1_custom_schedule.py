# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class V1CustomSchedule(BaseModel):
    """
    V1CustomSchedule
    """
    determination_start_date: Optional[date] = Field(None, alias="determinationStartDate")
    determination_end_date: Optional[date] = Field(None, alias="determinationEndDate")
    accrual_start_date: Optional[date] = Field(None, alias="accrualStartDate")
    accrual_end_date: Optional[date] = Field(None, alias="accrualEndDate")
    pay_date: Optional[date] = Field(None, alias="payDate", description="payment date.")
    __properties = ["determinationStartDate", "determinationEndDate", "accrualStartDate", "accrualEndDate", "payDate"]

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
    def from_json(cls, json_str: str) -> V1CustomSchedule:
        """Create an instance of V1CustomSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CustomSchedule:
        """Create an instance of V1CustomSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CustomSchedule.parse_obj(obj)

        _obj = V1CustomSchedule.parse_obj({
            "determination_start_date": obj.get("determinationStartDate"),
            "determination_end_date": obj.get("determinationEndDate"),
            "accrual_start_date": obj.get("accrualStartDate"),
            "accrual_end_date": obj.get("accrualEndDate"),
            "pay_date": obj.get("payDate")
        })
        return _obj

