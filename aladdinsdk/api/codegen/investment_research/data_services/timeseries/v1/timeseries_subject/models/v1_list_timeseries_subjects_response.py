# coding: utf-8

"""
    Timeseries Subject

    As a part of the Timeseries metadata, Timeseries Subject offers the capability to handle timeseries entity (ex. BLK, APPL) metadata information.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.timeseries_subject.models.v1_timeseries_subject import V1TimeseriesSubject

class V1ListTimeseriesSubjectsResponse(BaseModel):
    """
    V1ListTimeseriesSubjectsResponse
    """
    subjects: conlist(V1TimeseriesSubject) = Field(...)
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    __properties = ["subjects", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1ListTimeseriesSubjectsResponse:
        """Create an instance of V1ListTimeseriesSubjectsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in subjects (list)
        _items = []
        if self.subjects:
            for _item in self.subjects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListTimeseriesSubjectsResponse:
        """Create an instance of V1ListTimeseriesSubjectsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListTimeseriesSubjectsResponse.parse_obj(obj)

        _obj = V1ListTimeseriesSubjectsResponse.parse_obj({
            "subjects": [V1TimeseriesSubject.from_dict(_item) for _item in obj.get("subjects")] if obj.get("subjects") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

