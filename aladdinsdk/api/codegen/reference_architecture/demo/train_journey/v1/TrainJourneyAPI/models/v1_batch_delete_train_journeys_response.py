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
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.TrainJourneyAPI.models.v1_delete_train_journey_result import V1DeleteTrainJourneyResult

class V1BatchDeleteTrainJourneysResponse(BaseModel):
    """
    The Response for BatchDeleteTrainJourneys method.
    """
    results: Optional[conlist(V1DeleteTrainJourneyResult)] = Field(None, description="Train Journeys deleted.")
    __properties = ["results"]

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
    def from_json(cls, json_str: str) -> V1BatchDeleteTrainJourneysResponse:
        """Create an instance of V1BatchDeleteTrainJourneysResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchDeleteTrainJourneysResponse:
        """Create an instance of V1BatchDeleteTrainJourneysResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchDeleteTrainJourneysResponse.parse_obj(obj)

        _obj = V1BatchDeleteTrainJourneysResponse.parse_obj({
            "results": [V1DeleteTrainJourneyResult.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj
