# coding: utf-8

"""
    Broker External Alias

    API contains operations on Broker External Alias resource.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.BrokerExternalAliasAPI.models.enums_action_type import EnumsActionType
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.BrokerExternalAliasAPI.models.v1_validate_broker_external_alias_request import V1ValidateBrokerExternalAliasRequest

class V1BatchValidateBrokerExternalAliasesRequest(BaseModel):
    """
    The request message for BrokerDeskAPI.BatchValidateBrokerExternalAliases.
    """
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId")
    broker_ticker: Optional[StrictStr] = Field(None, alias="brokerTicker")
    requests: conlist(V1ValidateBrokerExternalAliasRequest) = Field(..., description="A maximum of 100 broker external aliases can be validated in a batch.")
    action_type: Optional[EnumsActionType] = Field(None, alias="actionType")
    __properties = ["brokerId", "brokerTicker", "requests", "actionType"]

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
    def from_json(cls, json_str: str) -> V1BatchValidateBrokerExternalAliasesRequest:
        """Create an instance of V1BatchValidateBrokerExternalAliasesRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1BatchValidateBrokerExternalAliasesRequest:
        """Create an instance of V1BatchValidateBrokerExternalAliasesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchValidateBrokerExternalAliasesRequest.parse_obj(obj)

        _obj = V1BatchValidateBrokerExternalAliasesRequest.parse_obj({
            "broker_id": obj.get("brokerId"),
            "broker_ticker": obj.get("brokerTicker"),
            "requests": [V1ValidateBrokerExternalAliasRequest.from_dict(_item) for _item in obj.get("requests")] if obj.get("requests") is not None else None,
            "action_type": obj.get("actionType")
        })
        return _obj

