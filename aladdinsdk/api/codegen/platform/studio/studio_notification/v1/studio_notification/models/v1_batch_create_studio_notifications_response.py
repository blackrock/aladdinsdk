# coding: utf-8

"""
    Studio Notification

    For creating and managing Aladdin Studio notifications.  # noqa: E501

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
from aladdinsdk.api.codegen.platform.studio.studio_notification.v1.studio_notification.models.v1_create_studio_notification_result import V1CreateStudioNotificationResult

class V1BatchCreateStudioNotificationsResponse(BaseModel):
    """
    V1BatchCreateStudioNotificationsResponse
    """
    results: Optional[conlist(V1CreateStudioNotificationResult)] = Field(None, description="The list of results of the operation in case of success.")
    __properties = ["results"]

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
    def from_json(cls, json_str: str) -> V1BatchCreateStudioNotificationsResponse:
        """Create an instance of V1BatchCreateStudioNotificationsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BatchCreateStudioNotificationsResponse:
        """Create an instance of V1BatchCreateStudioNotificationsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BatchCreateStudioNotificationsResponse.parse_obj(obj)

        _obj = V1BatchCreateStudioNotificationsResponse.parse_obj({
            "results": [V1CreateStudioNotificationResult.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj

