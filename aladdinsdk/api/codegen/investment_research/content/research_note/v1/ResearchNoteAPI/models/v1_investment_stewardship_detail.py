# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_engagement import V1InvestmentStewardshipEngagement
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_fixed_keyword import V1InvestmentStewardshipFixedKeyword
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_format import V1InvestmentStewardshipFormat
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_initiator import V1InvestmentStewardshipInitiator
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_score import V1InvestmentStewardshipScore
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_investment_stewardship_topic_details import V1InvestmentStewardshipTopicDetails

class V1InvestmentStewardshipDetail(BaseModel):
    """
    V1InvestmentStewardshipDetail
    """
    engagement_type: Optional[V1InvestmentStewardshipEngagement] = Field(None, alias="engagementType")
    initiator: Optional[V1InvestmentStewardshipInitiator] = None
    format: Optional[V1InvestmentStewardshipFormat] = None
    score: Optional[V1InvestmentStewardshipScore] = None
    engagement_date: Optional[date] = Field(None, alias="engagementDate", description="Engagement date.")
    external_attendees: Optional[conlist(StrictStr)] = Field(None, alias="externalAttendees", description="External attendees.")
    internal_attendees: Optional[conlist(StrictStr)] = Field(None, alias="internalAttendees", description="Internal attendees.")
    reporting: Optional[StrictBool] = Field(None, description="Reporting.")
    high_profile: Optional[StrictBool] = Field(None, alias="highProfile", description="High profile.")
    topics: Optional[conlist(V1InvestmentStewardshipTopicDetails)] = Field(None, description="Topics text.")
    fixed_keywords: Optional[conlist(V1InvestmentStewardshipFixedKeyword)] = Field(None, alias="fixedKeywords")
    client_note: Optional[StrictStr] = Field(None, alias="clientNote")
    __properties = ["engagementType", "initiator", "format", "score", "engagementDate", "externalAttendees", "internalAttendees", "reporting", "highProfile", "topics", "fixedKeywords", "clientNote"]

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
    def from_json(cls, json_str: str) -> V1InvestmentStewardshipDetail:
        """Create an instance of V1InvestmentStewardshipDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in topics (list)
        _items = []
        if self.topics:
            for _item in self.topics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['topics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1InvestmentStewardshipDetail:
        """Create an instance of V1InvestmentStewardshipDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1InvestmentStewardshipDetail.parse_obj(obj)

        _obj = V1InvestmentStewardshipDetail.parse_obj({
            "engagement_type": obj.get("engagementType"),
            "initiator": obj.get("initiator"),
            "format": obj.get("format"),
            "score": obj.get("score"),
            "engagement_date": obj.get("engagementDate"),
            "external_attendees": obj.get("externalAttendees"),
            "internal_attendees": obj.get("internalAttendees"),
            "reporting": obj.get("reporting"),
            "high_profile": obj.get("highProfile"),
            "topics": [V1InvestmentStewardshipTopicDetails.from_dict(_item) for _item in obj.get("topics")] if obj.get("topics") is not None else None,
            "fixed_keywords": obj.get("fixedKeywords"),
            "client_note": obj.get("clientNote")
        })
        return _obj

