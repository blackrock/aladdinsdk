# coding: utf-8

"""
    Aladdin Permission

    API contains operations on Aladdin Permission resource. Permissions cannot be applied directly to a user, they must be applied to a User Group first, then the user is added to a User Group. Note: This is not intended to be used for Authorization.  # noqa: E501

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
from aladdinsdk.api.codegen.platform.access.permission.v1.PermissionAPI.models.v1_permission_query import V1PermissionQuery

class V1FilterPermissionsRequest(BaseModel):
    """
    The request message for PermissionAPI.FilterPermissions.
    """
    permission_query: Optional[V1PermissionQuery] = Field(None, alias="permissionQuery")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterPermissions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'FilterPermissions' must match the call that provided the page token.")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of Permissions to return. The service may return fewer than this value. If unspecified, at most 1000 Permissions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.")
    __properties = ["permissionQuery", "pageToken", "pageSize"]

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
    def from_json(cls, json_str: str) -> V1FilterPermissionsRequest:
        """Create an instance of V1FilterPermissionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of permission_query
        if self.permission_query:
            _dict['permissionQuery'] = self.permission_query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterPermissionsRequest:
        """Create an instance of V1FilterPermissionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterPermissionsRequest.parse_obj(obj)

        _obj = V1FilterPermissionsRequest.parse_obj({
            "permission_query": V1PermissionQuery.from_dict(obj.get("permissionQuery")) if obj.get("permissionQuery") is not None else None,
            "page_token": obj.get("pageToken"),
            "page_size": obj.get("pageSize")
        })
        return _obj
