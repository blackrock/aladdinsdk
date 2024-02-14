# coding: utf-8

"""
    Broker

    API contains operations on Broker resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.BrokerAPI.models.v1_broker import V1Broker

class V1ValidateBrokerRequest(BaseModel):
    """
    The request message for BrokerAPI.ValidateBroker.
    """
    broker: Optional[V1Broker] = None
    __properties = ["broker"]

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
    def from_json(cls, json_str: str) -> V1ValidateBrokerRequest:
        """Create an instance of V1ValidateBrokerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of broker
        if self.broker:
            _dict['broker'] = self.broker.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ValidateBrokerRequest:
        """Create an instance of V1ValidateBrokerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ValidateBrokerRequest.parse_obj(obj)

        _obj = V1ValidateBrokerRequest.parse_obj({
            "broker": V1Broker.from_dict(obj.get("broker")) if obj.get("broker") is not None else None
        })
        return _obj

