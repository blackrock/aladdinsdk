# coding: utf-8

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionAPI.models.v1_corporate_action import V1CorporateAction

class V1FilterCorporateActionsResponse(BaseModel):
    """
    The response message for CorporateActionAPI.FilterCorporateActions.
    """
    corporate_actions: Optional[conlist(V1CorporateAction)] = Field(None, alias="corporateActions", description="The entities that match the specified CorporateActionsRequest.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'pageToken' to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["corporateActions", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterCorporateActionsResponse:
        """Create an instance of V1FilterCorporateActionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in corporate_actions (list)
        _items = []
        if self.corporate_actions:
            for _item in self.corporate_actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['corporateActions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterCorporateActionsResponse:
        """Create an instance of V1FilterCorporateActionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterCorporateActionsResponse.parse_obj(obj)

        _obj = V1FilterCorporateActionsResponse.parse_obj({
            "corporate_actions": [V1CorporateAction.from_dict(_item) for _item in obj.get("corporateActions")] if obj.get("corporateActions") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

