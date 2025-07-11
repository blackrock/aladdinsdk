# coding: utf-8

"""
    Train Journey

    Demonstrate feature of Aladdin Graph services using train journeys, stations and trains.  # noqa: E501

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
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey.models.any import Any
from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey.models.rpc_status import RpcStatus

class V1LongrunningOperation(BaseModel):
    """
    LongrunningOperation represents a long-running operation that is the result of a network API call.
    """
    id: Optional[StrictStr] = Field(None, description="The server-assigned id, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `id` should have the format of `operations/some/unique/id`.")
    meta: Optional[Any] = None
    done: Optional[StrictBool] = Field(None, description="If the value is `false`, it means the operation is still in progress. If true, the operation is completed, and either `error` or `response` is available.")
    error: Optional[RpcStatus] = None
    response: Optional[Any] = None
    __properties = ["id", "meta", "done", "error", "response"]

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
    def from_json(cls, json_str: str) -> V1LongrunningOperation:
        """Create an instance of V1LongrunningOperation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1LongrunningOperation:
        """Create an instance of V1LongrunningOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1LongrunningOperation.parse_obj(obj)

        _obj = V1LongrunningOperation.parse_obj({
            "id": obj.get("id"),
            "meta": Any.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
            "done": obj.get("done"),
            "error": RpcStatus.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "response": Any.from_dict(obj.get("response")) if obj.get("response") is not None else None
        })
        return _obj

