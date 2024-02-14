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
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_order import V1Order
from aladdinsdk.api.codegen.trading.order_management.order.v1.OrderAPI.models.v1_violation import V1Violation

class V1PostOrderResponse(BaseModel):
    """
    Response message to posting an order.
    """
    compliance_violations: Optional[conlist(V1Violation)] = Field(None, alias="complianceViolations", description="Compliance violations triggered by posting this order.")
    order: Optional[V1Order] = None
    __properties = ["complianceViolations", "order"]

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
    def from_json(cls, json_str: str) -> V1PostOrderResponse:
        """Create an instance of V1PostOrderResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in compliance_violations (list)
        _items = []
        if self.compliance_violations:
            for _item in self.compliance_violations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['complianceViolations'] = _items
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PostOrderResponse:
        """Create an instance of V1PostOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PostOrderResponse.parse_obj(obj)

        _obj = V1PostOrderResponse.parse_obj({
            "compliance_violations": [V1Violation.from_dict(_item) for _item in obj.get("complianceViolations")] if obj.get("complianceViolations") is not None else None,
            "order": V1Order.from_dict(obj.get("order")) if obj.get("order") is not None else None
        })
        return _obj

