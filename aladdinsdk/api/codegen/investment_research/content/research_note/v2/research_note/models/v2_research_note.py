# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.content.research_note.v2.research_note.models.types_data_value import TypesDataValue
from aladdinsdk.api.codegen.investment_research.content.research_note.v2.research_note.models.types_entity_id import TypesEntityId
from aladdinsdk.api.codegen.investment_research.content.research_note.v2.research_note.models.v2_expiring_permission_group import V2ExpiringPermissionGroup
from aladdinsdk.api.codegen.investment_research.content.research_note.v2.research_note.models.v2_note_state import V2NoteState

class V2ResearchNote(BaseModel):
    """
    Research Note object is used in Research Note API server for persisting Research data.
    """
    id: Optional[StrictStr] = Field(None, description="ID describes the computer or human assigned resource identifier. The research note id.")
    author: Optional[StrictStr] = Field(None, description="The author of the research note.")
    creator: Optional[StrictStr] = Field(None, description="The creator of the research note.")
    subject: Optional[StrictStr] = None
    note_category: Optional[StrictStr] = Field(None, alias="noteCategory", description="The note category.")
    keywords: Optional[conlist(StrictStr)] = Field(None, description="The keywords.")
    publish_time: Optional[datetime] = Field(None, alias="publishTime", description="The publish time.")
    note: Optional[StrictStr] = Field(None, description="The note textual content.")
    note_state: Optional[V2NoteState] = Field(None, alias="noteState")
    selected_permission_groups: Optional[conlist(StrictStr)] = Field(None, alias="selectedPermissionGroups")
    entities: Optional[conlist(TypesEntityId)] = None
    broker_id: Optional[StrictStr] = Field(None, alias="brokerId")
    expiring_permission_groups: Optional[conlist(V2ExpiringPermissionGroup)] = Field(None, alias="expiringPermissionGroups")
    note_html: Optional[StrictStr] = Field(None, alias="noteHtml")
    template_name: Optional[StrictStr] = Field(None, alias="templateName")
    template_version: Optional[StrictInt] = Field(None, alias="templateVersion")
    custom_fields: Optional[Dict[str, TypesDataValue]] = Field(None, alias="customFields")
    update_time: Optional[datetime] = Field(None, alias="updateTime", description="The update time.")
    __properties = ["id", "author", "creator", "subject", "noteCategory", "keywords", "publishTime", "note", "noteState", "selectedPermissionGroups", "entities", "brokerId", "expiringPermissionGroups", "noteHtml", "templateName", "templateVersion", "customFields", "updateTime"]

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
    def from_json(cls, json_str: str) -> V2ResearchNote:
        """Create an instance of V2ResearchNote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expiring_permission_groups (list)
        _items = []
        if self.expiring_permission_groups:
            for _item in self.expiring_permission_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expiringPermissionGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in custom_fields (dict)
        _field_dict = {}
        if self.custom_fields:
            for _key in self.custom_fields:
                if self.custom_fields[_key]:
                    _field_dict[_key] = self.custom_fields[_key].to_dict()
            _dict['customFields'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ResearchNote:
        """Create an instance of V2ResearchNote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ResearchNote.parse_obj(obj)

        _obj = V2ResearchNote.parse_obj({
            "id": obj.get("id"),
            "author": obj.get("author"),
            "creator": obj.get("creator"),
            "subject": obj.get("subject"),
            "note_category": obj.get("noteCategory"),
            "keywords": obj.get("keywords"),
            "publish_time": obj.get("publishTime"),
            "note": obj.get("note"),
            "note_state": obj.get("noteState"),
            "selected_permission_groups": obj.get("selectedPermissionGroups"),
            "entities": [TypesEntityId.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "broker_id": obj.get("brokerId"),
            "expiring_permission_groups": [V2ExpiringPermissionGroup.from_dict(_item) for _item in obj.get("expiringPermissionGroups")] if obj.get("expiringPermissionGroups") is not None else None,
            "note_html": obj.get("noteHtml"),
            "template_name": obj.get("templateName"),
            "template_version": obj.get("templateVersion"),
            "custom_fields": dict(
                (_k, TypesDataValue.from_dict(_v))
                for _k, _v in obj.get("customFields").items()
            )
            if obj.get("customFields") is not None
            else None,
            "update_time": obj.get("updateTime")
        })
        return _obj

