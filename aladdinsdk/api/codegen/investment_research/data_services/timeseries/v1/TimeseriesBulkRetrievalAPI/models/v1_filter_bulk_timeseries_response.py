# coding: utf-8

"""
    Timeseries Bulk Retrieval

    Timeseries Bulk Retrieval offers the capability to retrieve, and filter more than one timeseries at once.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class V1FilterBulkTimeseriesResponse(BaseModel):
    """
    V1FilterBulkTimeseriesResponse
    """
    urls: Optional[conlist(StrictStr)] = None
    __properties = ["urls"]

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
    def from_json(cls, json_str: str) -> V1FilterBulkTimeseriesResponse:
        """Create an instance of V1FilterBulkTimeseriesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterBulkTimeseriesResponse:
        """Create an instance of V1FilterBulkTimeseriesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterBulkTimeseriesResponse.parse_obj(obj)

        _obj = V1FilterBulkTimeseriesResponse.parse_obj({
            "urls": obj.get("urls")
        })
        return _obj

