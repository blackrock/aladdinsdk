# coding: utf-8

"""
    Timeseries

    Timeseries offers a unified interface for researchers to retrieve, update and delete timeseries data that are stored in Snowflake.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.timeseries.models.v1_timeseries_query import V1TimeseriesQuery

class V1RetrieveTimeseriesRequest(BaseModel):
    """
    (-- api-linter: core::0158::request-page-token-field=disabled  aip.dev/not-precedent: We need to do this because only one timeseries object  will be returned so page token field is not required--) (-- api-linter: core::0158::request-page-size-field=disabled  aip.dev/not-precedent: We need to do this because only one timeseries object  will be returned and page size field is not required--)
    """
    query: Optional[V1TimeseriesQuery] = None
    __properties = ["query"]

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
    def from_json(cls, json_str: str) -> V1RetrieveTimeseriesRequest:
        """Create an instance of V1RetrieveTimeseriesRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1RetrieveTimeseriesRequest:
        """Create an instance of V1RetrieveTimeseriesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RetrieveTimeseriesRequest.parse_obj(obj)

        _obj = V1RetrieveTimeseriesRequest.parse_obj({
            "query": V1TimeseriesQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj

