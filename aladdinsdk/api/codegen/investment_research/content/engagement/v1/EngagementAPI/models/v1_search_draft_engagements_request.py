# coding: utf-8

"""
    Engagement

    Create, modify, delete, retrieve, search and historical engagement search.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.content.engagement.v1.EngagementAPI.models.types_entity_id import TypesEntityId

class V1SearchDraftEngagementsRequest(BaseModel):
    """
    V1SearchDraftEngagementsRequest
    """
    entity_ids: Optional[conlist(TypesEntityId)] = Field(None, alias="entityIds")
    filter_criteria: Optional[conlist(StrictStr)] = Field(None, alias="filterCriteria")
    order_by: Optional[StrictStr] = Field(None, alias="orderBy")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of engagement to return. The service may return fewer than this value. If unspecified, at most 10 note will be returned.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'SearchEngagement' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'SearchEngagement' must match the call that provided the page token.")
    __properties = ["entityIds", "filterCriteria", "orderBy", "pageSize", "pageToken"]

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
    def from_json(cls, json_str: str) -> V1SearchDraftEngagementsRequest:
        """Create an instance of V1SearchDraftEngagementsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entity_ids (list)
        _items = []
        if self.entity_ids:
            for _item in self.entity_ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entityIds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SearchDraftEngagementsRequest:
        """Create an instance of V1SearchDraftEngagementsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SearchDraftEngagementsRequest.parse_obj(obj)

        _obj = V1SearchDraftEngagementsRequest.parse_obj({
            "entity_ids": [TypesEntityId.from_dict(_item) for _item in obj.get("entityIds")] if obj.get("entityIds") is not None else None,
            "filter_criteria": obj.get("filterCriteria"),
            "order_by": obj.get("orderBy"),
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken")
        })
        return _obj

