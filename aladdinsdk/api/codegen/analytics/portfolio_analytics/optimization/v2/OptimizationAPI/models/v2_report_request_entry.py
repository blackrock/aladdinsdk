# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V2ReportRequestEntry(BaseModel):
    """
    V2ReportRequestEntry
    """
    report_type: Optional[StrictStr] = Field(None, alias="reportType")
    requested_columns: Optional[conlist(StrictStr)] = Field(None, alias="requestedColumns")
    __properties = ["reportType", "requestedColumns"]

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
    def from_json(cls, json_str: str) -> V2ReportRequestEntry:
        """Create an instance of V2ReportRequestEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ReportRequestEntry:
        """Create an instance of V2ReportRequestEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ReportRequestEntry.parse_obj(obj)

        _obj = V2ReportRequestEntry.parse_obj({
            "report_type": obj.get("reportType"),
            "requested_columns": obj.get("requestedColumns")
        })
        return _obj

