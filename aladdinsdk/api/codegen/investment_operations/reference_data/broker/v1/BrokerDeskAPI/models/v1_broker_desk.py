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

class V1BrokerDesk(BaseModel):
    """
    Each broker in Aladdin will have at least one desk assigned. The desk selected for a trade designates the group and specific contact at the broker firm with whom the transaction was done.
    """
    id: Optional[StrictStr] = Field(None, description="Resources must have a 'id' field. Name describes the computer or human assigned resource identifier. Desk id.")
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId", description="Represents Aladdin Broker Identifier (Numeric), commonly referred to as broker code.")
    broker_entity: Optional[StrictStr] = Field(None, alias="brokerEntity", description="Broker entity based on the decode BROKER_ENTITY.")
    desk_type: Optional[StrictStr] = Field(None, alias="deskType", description="Broker desk types.")
    assistant_id: Optional[StrictStr] = Field(None, alias="assistantId", description="Assistant id.")
    salesman_id: Optional[StrictStr] = Field(None, alias="salesmanId", description="Salesman id.")
    desk_rule: Optional[StrictStr] = Field(None, alias="deskRule", description="Represents rule like BQL to default a Desk to a Trade.")
    desk_code: Optional[StrictStr] = Field(None, alias="deskCode", description="Desk Code.")
    __properties = ["id", "brokerId", "brokerEntity", "deskType", "assistantId", "salesmanId", "deskRule", "deskCode"]

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
    def from_json(cls, json_str: str) -> V1BrokerDesk:
        """Create an instance of V1BrokerDesk from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BrokerDesk:
        """Create an instance of V1BrokerDesk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BrokerDesk.parse_obj(obj)

        _obj = V1BrokerDesk.parse_obj({
            "id": obj.get("id"),
            "broker_id": obj.get("brokerId"),
            "broker_entity": obj.get("brokerEntity"),
            "desk_type": obj.get("deskType"),
            "assistant_id": obj.get("assistantId"),
            "salesman_id": obj.get("salesmanId"),
            "desk_rule": obj.get("deskRule"),
            "desk_code": obj.get("deskCode")
        })
        return _obj

