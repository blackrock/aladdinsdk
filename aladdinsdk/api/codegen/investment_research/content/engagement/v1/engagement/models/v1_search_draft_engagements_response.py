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
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.investment_research.content.engagement.v1.engagement.models.v1_engagement import V1Engagement

class V1SearchDraftEngagementsResponse(BaseModel):
    """
    V1SearchDraftEngagementsResponse
    """
    engagements: Optional[conlist(V1Engagement)] = Field(None, description="Engagement to be returned.")
    __properties = ["engagements"]

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
    def from_json(cls, json_str: str) -> V1SearchDraftEngagementsResponse:
        """Create an instance of V1SearchDraftEngagementsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in engagements (list)
        _items = []
        if self.engagements:
            for _item in self.engagements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['engagements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SearchDraftEngagementsResponse:
        """Create an instance of V1SearchDraftEngagementsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SearchDraftEngagementsResponse.parse_obj(obj)

        _obj = V1SearchDraftEngagementsResponse.parse_obj({
            "engagements": [V1Engagement.from_dict(_item) for _item in obj.get("engagements")] if obj.get("engagements") is not None else None
        })
        return _obj

