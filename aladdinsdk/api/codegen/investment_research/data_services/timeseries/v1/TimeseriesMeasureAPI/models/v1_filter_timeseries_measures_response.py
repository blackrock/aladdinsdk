# coding: utf-8

"""
    Timeseries Measure

    As a part of the timeseries metadata, timeseries Measure offers the capability to handle timeseries measure (ex. price, volume) metadata information.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.TimeseriesMeasureAPI.models.v1_timeseries_measure import V1TimeseriesMeasure

class V1FilterTimeseriesMeasuresResponse(BaseModel):
    """
    (-- api-linter: aladdin::9016::response-message=disabled  aip.dev/not-precedent: We need to be consistent with the returned entity collection name --)
    """
    measures: conlist(V1TimeseriesMeasure) = Field(...)
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    __properties = ["measures", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterTimeseriesMeasuresResponse:
        """Create an instance of V1FilterTimeseriesMeasuresResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in measures (list)
        _items = []
        if self.measures:
            for _item in self.measures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['measures'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterTimeseriesMeasuresResponse:
        """Create an instance of V1FilterTimeseriesMeasuresResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterTimeseriesMeasuresResponse.parse_obj(obj)

        _obj = V1FilterTimeseriesMeasuresResponse.parse_obj({
            "measures": [V1TimeseriesMeasure.from_dict(_item) for _item in obj.get("measures")] if obj.get("measures") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

