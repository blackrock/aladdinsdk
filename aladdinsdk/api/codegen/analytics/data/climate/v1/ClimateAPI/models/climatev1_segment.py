# coding: utf-8

"""
    Climate

    The Aladdin Climate Data API exposes physical, transition, and temperature alignment analytics as of a given date. Users can retrieve data for selected entity types by specifying the desired datapoints for each climate risk type and scenario. The Aladdin Climate Meta Data API outlines the datapoints available across physical, transition, and temperature alignment analytics.  # noqa: E501

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

class Climatev1Segment(BaseModel):
    """
    Climatev1Segment
    """
    name: Optional[StrictStr] = None
    attributes: Optional[conlist(StrictStr)] = Field(None, description="(-- api-linter: core::0124::required-reference=disabled     aip.dev/not-precedent: We need to do this because this is an existing field and does not require resource association--) (-- api-linter: aladdin::0901::dictionary-message-field=disabled     aip.dev/not-precedent: This field in independent and conflict is cross-domain, hence we need to override the type--) Attributes are the different levels of segmentation in which the entity is involved in for the specific metric value that is returned.")
    __properties = ["name", "attributes"]

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
    def from_json(cls, json_str: str) -> Climatev1Segment:
        """Create an instance of Climatev1Segment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Climatev1Segment:
        """Create an instance of Climatev1Segment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Climatev1Segment.parse_obj(obj)

        _obj = Climatev1Segment.parse_obj({
            "name": obj.get("name"),
            "attributes": obj.get("attributes")
        })
        return _obj
