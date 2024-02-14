# coding: utf-8

"""
    Portfolio Group

    Operations on Aladdin Portfolio Group resource.  # noqa: E501

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
from aladdinsdk.api.codegen.portfolio.configuration.portfolio_group.v1.PortfolioGroupAPI.models.v1_portfolio_group_node_query import V1PortfolioGroupNodeQuery

class DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar(BaseModel):
    """
    DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar
    """
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of members to return. The service may return fewer than this value. If unspecified, at most 50 members will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous `FilterPortfolioGroupNodes` call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to `FilterPortfolioGroupNodes` must match the call that provided the page token.")
    query: Optional[V1PortfolioGroupNodeQuery] = None
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
    def from_json(cls, json_str: str) -> DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar:
        """Create an instance of DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar:
        """Create an instance of DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar.parse_obj(obj)

        _obj = DescribesTheFilterPortfolioGroupNodesRequestApiLinterAladdin9016RequestMessageNameDisabledAipDevNotPrecedentRequestIsIncorrectlyFlaggedBySonar.parse_obj({
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken"),
            "query": V1PortfolioGroupNodeQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj

