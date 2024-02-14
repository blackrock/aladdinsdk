# coding: utf-8

"""
    Aladdin User

     API contains operations on Aladdin User resource.  # Description  An Aladdin User is a person or a system account that can login into  Aladdin client's website and may be granted access to Aladdin applications.  ## Example Use Cases   This API may be used to:   - create records of Aladdin Client's employees   - retrieve information about     = Aladdin Client's employees granted access to Aladdin     = BlackRock employees granted access to client's Aladdin products     = bot accounts granted access to Aladdin   - modify Aladdin Client's employees records in Aladdin system   - search User records by email or client's internal user id (if populated)  ## Implementation Status  This API is production ready. In the future it will be enhanced with additional search capabilities    [Developer Guide]: apps/aladdin-developer-portal/#/guides/developer-guide   # noqa: E501

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
from aladdinsdk.api.codegen.platform.identity.user.v1.UserAPI.models.v1_user import V1User

class V1ListUsersResponse(BaseModel):
    """
    V1ListUsersResponse
    """
    users: Optional[conlist(V1User)] = Field(None, description="users to be returned.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'page_token' to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["users", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1ListUsersResponse:
        """Create an instance of V1ListUsersResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListUsersResponse:
        """Create an instance of V1ListUsersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListUsersResponse.parse_obj(obj)

        _obj = V1ListUsersResponse.parse_obj({
            "users": [V1User.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

