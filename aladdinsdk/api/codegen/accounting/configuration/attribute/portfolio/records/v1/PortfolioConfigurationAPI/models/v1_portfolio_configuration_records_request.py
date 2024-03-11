# coding: utf-8

"""
    Portfolio Configuration Record For Accounting

    Configurations API for Aladdin Accounting allows you to access accounting configuration attributes for process types that portfolios are setup on. Data can be sourced in aggregate and filtered to improve oversight and scale of configuration monitoring. This API allows for retrieval of key data points for portfolio configurations by various parameters, including portfolio tickers, processCodes, and more.  # noqa: E501

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
from aladdinsdk.api.codegen.accounting.configuration.attribute.portfolio.records.v1.PortfolioConfigurationAPI.models.v1_configuration_long_running_filter_query import V1ConfigurationLongRunningFilterQuery

class V1PortfolioConfigurationRecordsRequest(BaseModel):
    """
    V1PortfolioConfigurationRecordsRequest
    """
    query: Optional[V1ConfigurationLongRunningFilterQuery] = None
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of tickers to be return. The service may return fewer than this value. The maximum value is 100. If unspecified, the default value is 100.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="Describes the token to be retrieved.")
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
    def from_json(cls, json_str: str) -> V1PortfolioConfigurationRecordsRequest:
        """Create an instance of V1PortfolioConfigurationRecordsRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1PortfolioConfigurationRecordsRequest:
        """Create an instance of V1PortfolioConfigurationRecordsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PortfolioConfigurationRecordsRequest.parse_obj(obj)

        _obj = V1PortfolioConfigurationRecordsRequest.parse_obj({
            "query": V1ConfigurationLongRunningFilterQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None,
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken")
        })
        return _obj

