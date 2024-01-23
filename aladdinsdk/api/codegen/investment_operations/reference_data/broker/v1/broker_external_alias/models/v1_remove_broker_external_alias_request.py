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


from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.broker_external_alias.models.v1_broker_external_alias import V1BrokerExternalAlias

class V1RemoveBrokerExternalAliasRequest(BaseModel):
    """
    The request message for BrokerExternalAliasAPI.BatchRemoveBrokerExternalAlias.
    """
    broker_external_alias: Optional[V1BrokerExternalAlias] = Field(None, alias="brokerExternalAlias")
    __properties = ["brokerExternalAlias"]

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
    def from_json(cls, json_str: str) -> V1RemoveBrokerExternalAliasRequest:
        """Create an instance of V1RemoveBrokerExternalAliasRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of broker_external_alias
        if self.broker_external_alias:
            _dict['brokerExternalAlias'] = self.broker_external_alias.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RemoveBrokerExternalAliasRequest:
        """Create an instance of V1RemoveBrokerExternalAliasRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RemoveBrokerExternalAliasRequest.parse_obj(obj)

        _obj = V1RemoveBrokerExternalAliasRequest.parse_obj({
            "broker_external_alias": V1BrokerExternalAlias.from_dict(obj.get("brokerExternalAlias")) if obj.get("brokerExternalAlias") is not None else None
        })
        return _obj

