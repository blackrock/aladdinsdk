# coding: utf-8

"""
    Adc Access

    Manages User Access via Functional Roles and Access Roles in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

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
from aladdinsdk.api.codegen.platform.studio.adc.adc_access.v1.adc_access.models.v1_functional_role_query import V1FunctionalRoleQuery

class V1FilterFunctionalRolesRequest(BaseModel):
    """
    V1FilterFunctionalRolesRequest
    """
    query: V1FunctionalRoleQuery = Field(...)
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterFunctionalRoles' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'FilterFunctionalRoles' must match the call that provided the page token.")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of FunctionalRoles to return. The service may return fewer than this value. If unspecified, at most X FunctionalRoles will be returned. The maximum value is Y; values above Y will be coerced to Y.")
    __properties = ["query", "pageToken", "pageSize"]

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
    def from_json(cls, json_str: str) -> V1FilterFunctionalRolesRequest:
        """Create an instance of V1FilterFunctionalRolesRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterFunctionalRolesRequest:
        """Create an instance of V1FilterFunctionalRolesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterFunctionalRolesRequest.parse_obj(obj)

        _obj = V1FilterFunctionalRolesRequest.parse_obj({
            "query": V1FunctionalRoleQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None,
            "page_token": obj.get("pageToken"),
            "page_size": obj.get("pageSize")
        })
        return _obj

