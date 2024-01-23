# coding: utf-8

"""
    Broker Confirm Routing

    API contains operations on Broker Confirm Routing resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.broker_confirm_routing.models.enums_filter_type import EnumsFilterType
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.broker_confirm_routing.models.v1_broker_confirm_routing_extended_query import V1BrokerConfirmRoutingExtendedQuery

class V1BrokerConfirmRoutingQuery(BaseModel):
    """
    The query required to perform a filter query.
    """
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId", description="Aladdin Broker Identifier (Numeric) (Not supported currently).")
    broker_ticker: Optional[StrictStr] = Field(None, alias="brokerTicker", description="Broker ticker.")
    load_defunct: Optional[StrictBool] = Field(None, alias="loadDefunct", description="Load Defunct Flag - If true , will load all (including defuncts) , else will only load non defunct data.")
    broker_confirm_routing_extended_query: Optional[V1BrokerConfirmRoutingExtendedQuery] = Field(None, alias="brokerConfirmRoutingExtendedQuery")
    filter_type: Optional[EnumsFilterType] = Field(None, alias="filterType")
    __properties = ["brokerId", "brokerTicker", "loadDefunct", "brokerConfirmRoutingExtendedQuery", "filterType"]

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
    def from_json(cls, json_str: str) -> V1BrokerConfirmRoutingQuery:
        """Create an instance of V1BrokerConfirmRoutingQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of broker_confirm_routing_extended_query
        if self.broker_confirm_routing_extended_query:
            _dict['brokerConfirmRoutingExtendedQuery'] = self.broker_confirm_routing_extended_query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BrokerConfirmRoutingQuery:
        """Create an instance of V1BrokerConfirmRoutingQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BrokerConfirmRoutingQuery.parse_obj(obj)

        _obj = V1BrokerConfirmRoutingQuery.parse_obj({
            "broker_id": obj.get("brokerId"),
            "broker_ticker": obj.get("brokerTicker"),
            "load_defunct": obj.get("loadDefunct"),
            "broker_confirm_routing_extended_query": V1BrokerConfirmRoutingExtendedQuery.from_dict(obj.get("brokerConfirmRoutingExtendedQuery")) if obj.get("brokerConfirmRoutingExtendedQuery") is not None else None,
            "filter_type": obj.get("filterType")
        })
        return _obj

