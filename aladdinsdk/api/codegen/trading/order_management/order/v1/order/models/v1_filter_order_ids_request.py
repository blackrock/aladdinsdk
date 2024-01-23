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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.trading.order_management.order.v1.order.models.v1_order_id_query import V1OrderIdQuery

class V1FilterOrderIdsRequest(BaseModel):
    """
    V1FilterOrderIdsRequest
    """
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of results desired to be returned by the API in a single page of data. If this value exceeds the maximum supported for the operation or there are fewer data results than this value, a smaller number of results will be returned. The maximum value is 20000. If unspecified or out of range, the default value of 20000 is used.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterOrderIds' call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to 'FilterOrderIds' must match the call that provided the page token.")
    query: Optional[V1OrderIdQuery] = None
    __properties = ["pageSize", "pageToken", "query"]

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
    def from_json(cls, json_str: str) -> V1FilterOrderIdsRequest:
        """Create an instance of V1FilterOrderIdsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterOrderIdsRequest:
        """Create an instance of V1FilterOrderIdsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterOrderIdsRequest.parse_obj(obj)

        _obj = V1FilterOrderIdsRequest.parse_obj({
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken"),
            "query": V1OrderIdQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj

