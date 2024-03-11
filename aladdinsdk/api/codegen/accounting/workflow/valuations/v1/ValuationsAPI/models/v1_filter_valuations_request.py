# coding: utf-8

"""
    Valuations

    In an accounting workflow, valuations are generated for various processes at the portfolio/portfolio group level. This service can be used to retrieve and filter for accounting valuations data.  # noqa: E501

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
from aladdinsdk.api.codegen.accounting.workflow.valuations.v1.ValuationsAPI.models.v1_valuation_query import V1ValuationQuery

class V1FilterValuationsRequest(BaseModel):
    """
    V1FilterValuationsRequest
    """
    query: Optional[V1ValuationQuery] = None
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of Valuation to return. The service may return fewer than this value. If unspecified, at most 100 Valuation will be returned. The maximum value is 100; values above 100 will be coerced to 100.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'ListValuations' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'ListValuations' must match the call that provided the page token.")
    __properties = ["query", "pageSize", "pageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterValuationsRequest:
        """Create an instance of V1FilterValuationsRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1FilterValuationsRequest:
        """Create an instance of V1FilterValuationsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterValuationsRequest.parse_obj(obj)

        _obj = V1FilterValuationsRequest.parse_obj({
            "query": V1ValuationQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None,
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken")
        })
        return _obj

