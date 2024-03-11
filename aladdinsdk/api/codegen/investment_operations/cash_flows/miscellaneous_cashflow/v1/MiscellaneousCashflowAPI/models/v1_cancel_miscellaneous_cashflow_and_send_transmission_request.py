# coding: utf-8

"""
    Miscellaneous Cash

    Allows users to create, update and cancel miscellaneous cash. For full details including permissions required and sample calls, please check out the Release Notes available in the Release Note section on Studio or on your client site homepage.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool
from aladdinsdk.api.codegen.investment_operations.cash_flows.miscellaneous_cashflow.v1.MiscellaneousCashflowAPI.models.v1_miscellaneous_cashflow import V1MiscellaneousCashflow

class V1CancelMiscellaneousCashflowAndSendTransmissionRequest(BaseModel):
    """
    V1CancelMiscellaneousCashflowAndSendTransmissionRequest
    """
    miscellaneous_cashflow: Optional[V1MiscellaneousCashflow] = Field(None, alias="miscellaneousCashflow")
    validate_only: Optional[StrictBool] = Field(None, alias="validateOnly")
    update_extern_id1: Optional[StrictBool] = Field(None, alias="updateExternId1")
    __properties = ["miscellaneousCashflow", "validateOnly", "updateExternId1"]

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
    def from_json(cls, json_str: str) -> V1CancelMiscellaneousCashflowAndSendTransmissionRequest:
        """Create an instance of V1CancelMiscellaneousCashflowAndSendTransmissionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of miscellaneous_cashflow
        if self.miscellaneous_cashflow:
            _dict['miscellaneousCashflow'] = self.miscellaneous_cashflow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CancelMiscellaneousCashflowAndSendTransmissionRequest:
        """Create an instance of V1CancelMiscellaneousCashflowAndSendTransmissionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CancelMiscellaneousCashflowAndSendTransmissionRequest.parse_obj(obj)

        _obj = V1CancelMiscellaneousCashflowAndSendTransmissionRequest.parse_obj({
            "miscellaneous_cashflow": V1MiscellaneousCashflow.from_dict(obj.get("miscellaneousCashflow")) if obj.get("miscellaneousCashflow") is not None else None,
            "validate_only": obj.get("validateOnly"),
            "update_extern_id1": obj.get("updateExternId1")
        })
        return _obj

