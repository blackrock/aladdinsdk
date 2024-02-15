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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.investment_research.content.research_note.v1.ResearchNoteAPI.models.v1_research_note import V1ResearchNote

class V1SearchResearchNotesResponse(BaseModel):
    """
    V1SearchResearchNotesResponse
    """
    research_notes: Optional[conlist(V1ResearchNote)] = Field(None, alias="researchNotes", description="researchs to be returned.")
    __properties = ["researchNotes"]

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
    def from_json(cls, json_str: str) -> V1SearchResearchNotesResponse:
        """Create an instance of V1SearchResearchNotesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in research_notes (list)
        _items = []
        if self.research_notes:
            for _item in self.research_notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['researchNotes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SearchResearchNotesResponse:
        """Create an instance of V1SearchResearchNotesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SearchResearchNotesResponse.parse_obj(obj)

        _obj = V1SearchResearchNotesResponse.parse_obj({
            "research_notes": [V1ResearchNote.from_dict(_item) for _item in obj.get("researchNotes")] if obj.get("researchNotes") is not None else None
        })
        return _obj
