# coding: utf-8

"""
    Data Access Service

    Allows for access to data stored in snowflake.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_research.data_services.access.v1.AccessAPI.models.v1_access import V1Access

class V1QueryViewRequest(BaseModel):
    """
    This service lists presigned urls from staging
    """
    query_request: Optional[V1Access] = Field(None, alias="queryRequest")
    __properties = ["queryRequest"]

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
    def from_json(cls, json_str: str) -> V1QueryViewRequest:
        """Create an instance of V1QueryViewRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of query_request
        if self.query_request:
            _dict['queryRequest'] = self.query_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1QueryViewRequest:
        """Create an instance of V1QueryViewRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1QueryViewRequest.parse_obj(obj)

        _obj = V1QueryViewRequest.parse_obj({
            "query_request": V1Access.from_dict(obj.get("queryRequest")) if obj.get("queryRequest") is not None else None
        })
        return _obj

