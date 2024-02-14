# coding: utf-8

"""
    Aladdin User Group

    API contains operations on Aladdin User Group resource. Note: This is not intended to be used for Authorization.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.platform.access.user_group.v1.UserGroupAPI.models.v1_membership_type import V1MembershipType

class V1UserGroupQuery(BaseModel):
    """
    Represents query to filter User Groups for users and permissions.
    """
    user_id: Optional[StrictStr] = Field(None, alias="userId", description="User ID to retrieve all the User Groups the user is in.")
    permission_id: Optional[StrictStr] = Field(None, alias="permissionId", description="Permission ID to retrieve all the User Groups the permission is applied to.")
    membership_type: Optional[V1MembershipType] = Field(None, alias="membershipType")
    __properties = ["userId", "permissionId", "membershipType"]

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
    def from_json(cls, json_str: str) -> V1UserGroupQuery:
        """Create an instance of V1UserGroupQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1UserGroupQuery:
        """Create an instance of V1UserGroupQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1UserGroupQuery.parse_obj(obj)

        _obj = V1UserGroupQuery.parse_obj({
            "user_id": obj.get("userId"),
            "permission_id": obj.get("permissionId"),
            "membership_type": obj.get("membershipType")
        })
        return _obj

