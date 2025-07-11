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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey.models.enums_operator import EnumsOperator
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey.models.enums_train_type import EnumsTrainType

class TrainTrainSummarySlice(BaseModel):
    """
    A train summary slice that represents a summary set of properties of a train.
    """
    train_id: Optional[StrictStr] = Field(None, alias="trainId")
    name: Optional[StrictStr] = None
    train_type: Optional[EnumsTrainType] = Field(None, alias="trainType")
    operator: Optional[EnumsOperator] = None
    __properties = ["trainId", "name", "trainType", "operator"]

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
    def from_json(cls, json_str: str) -> TrainTrainSummarySlice:
        """Create an instance of TrainTrainSummarySlice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrainTrainSummarySlice:
        """Create an instance of TrainTrainSummarySlice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrainTrainSummarySlice.parse_obj(obj)

        _obj = TrainTrainSummarySlice.parse_obj({
            "train_id": obj.get("trainId"),
            "name": obj.get("name"),
            "train_type": obj.get("trainType"),
            "operator": obj.get("operator")
        })
        return _obj

