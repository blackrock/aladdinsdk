# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.portfolio_analytics.optimization.v2.OptimizationAPI.models.any import Any

class RpcStatus(BaseModel):
    """
    The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details.  You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).
    """
    code: Optional[StrictInt] = Field(None, description="The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].")
    message: Optional[StrictStr] = Field(None, description="A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.")
    details: Optional[conlist(Any)] = Field(None, description="A list of messages that carry the error details.  There is a common set of message types for APIs to use.")
    __properties = ["code", "message", "details"]

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
    def from_json(cls, json_str: str) -> RpcStatus:
        """Create an instance of RpcStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RpcStatus:
        """Create an instance of RpcStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RpcStatus.parse_obj(obj)

        _obj = RpcStatus.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "details": [Any.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        return _obj

