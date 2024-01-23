# coding: utf-8

"""
    Broker Desk

    API contains operations on Broker Desk resource.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.broker_desk.models.rpc_status import RpcStatus

class V1BatchValidateBrokerDesksResponse(BaseModel):
    """
    The response message for BatchValidateBrokerDesks.
    """
    status: Optional[RpcStatus] = None
    broker_desk_validation: Optional[StrictStr] = Field(None, alias="brokerDeskValidation", description="Represents the validation associated with the broker desk records.")
    __properties = ["status", "brokerDeskValidation"]

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
    def from_json(cls, json_str: str) -> V1BatchValidateBrokerDesksResponse:
        """Create an instance of V1BatchValidateBrokerDesksResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchValidateBrokerDesksResponse:
        """Create an instance of V1BatchValidateBrokerDesksResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchValidateBrokerDesksResponse.parse_obj(obj)

        _obj = V1BatchValidateBrokerDesksResponse.parse_obj({
            "status": RpcStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "broker_desk_validation": obj.get("brokerDeskValidation")
        })
        return _obj

