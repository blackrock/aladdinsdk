# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

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
from aladdinsdk.api.codegen.trading.order_management.order.v1.order.models.v1_order import V1Order
from aladdinsdk.api.codegen.trading.order_management.order.v1.order.models.v1_post_order_config import V1PostOrderConfig

class V1BatchPostOrdersRequest(BaseModel):
    """
    V1BatchPostOrdersRequest
    """
    post_order_config: Optional[V1PostOrderConfig] = Field(None, alias="postOrderConfig")
    orders: conlist(V1Order) = Field(...)
    __properties = ["postOrderConfig", "orders"]

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
    def from_json(cls, json_str: str) -> V1BatchPostOrdersRequest:
        """Create an instance of V1BatchPostOrdersRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of post_order_config
        if self.post_order_config:
            _dict['postOrderConfig'] = self.post_order_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item in self.orders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchPostOrdersRequest:
        """Create an instance of V1BatchPostOrdersRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchPostOrdersRequest.parse_obj(obj)

        _obj = V1BatchPostOrdersRequest.parse_obj({
            "post_order_config": V1PostOrderConfig.from_dict(obj.get("postOrderConfig")) if obj.get("postOrderConfig") is not None else None,
            "orders": [V1Order.from_dict(_item) for _item in obj.get("orders")] if obj.get("orders") is not None else None
        })
        return _obj

