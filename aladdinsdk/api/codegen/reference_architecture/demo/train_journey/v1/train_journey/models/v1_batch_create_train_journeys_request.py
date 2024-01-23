# coding: utf-8

"""
    Train Journey

    Demonstrate feature of Aladdin Graph services using train journeys, stations and trains.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey.models.v1_create_train_journey_request import V1CreateTrainJourneyRequest

class V1BatchCreateTrainJourneysRequest(BaseModel):
    """
    V1BatchCreateTrainJourneysRequest
    """
    requests: conlist(V1CreateTrainJourneyRequest) = Field(..., description="The request message specifying the train journeys to create. A maximum of 1000 train journeys can be created in a batch.")
    __properties = ["requests"]

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
    def from_json(cls, json_str: str) -> V1BatchCreateTrainJourneysRequest:
        """Create an instance of V1BatchCreateTrainJourneysRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchCreateTrainJourneysRequest:
        """Create an instance of V1BatchCreateTrainJourneysRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchCreateTrainJourneysRequest.parse_obj(obj)

        _obj = V1BatchCreateTrainJourneysRequest.parse_obj({
            "requests": [V1CreateTrainJourneyRequest.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None
        })
        return _obj

