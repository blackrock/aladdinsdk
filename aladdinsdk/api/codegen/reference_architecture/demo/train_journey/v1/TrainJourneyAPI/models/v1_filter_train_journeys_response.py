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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.TrainJourneyAPI.models.v1_train_journey import V1TrainJourney

class V1FilterTrainJourneysResponse(BaseModel):
    """
    Response for FilterTrainJourneys method.
    """
    train_journeys: Optional[conlist(V1TrainJourney)] = Field(None, alias="trainJourneys", description="The train journey entities that match the specified [FilterTrainJourneysRequest].")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token to retrieve the next page of results.")
    __properties = ["trainJourneys", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterTrainJourneysResponse:
        """Create an instance of V1FilterTrainJourneysResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in train_journeys (list)
        _items = []
        if self.train_journeys:
            for _item in self.train_journeys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trainJourneys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterTrainJourneysResponse:
        """Create an instance of V1FilterTrainJourneysResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterTrainJourneysResponse.parse_obj(obj)

        _obj = V1FilterTrainJourneysResponse.parse_obj({
            "train_journeys": [V1TrainJourney.from_dict(_item) for _item in obj.get("trainJourneys")] if obj.get("trainJourneys") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj
