# coding: utf-8

"""
    Data Access Service

    Allows for access to data stored in snowflake.  # noqa: E501

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

class V1ViewResponse(BaseModel):
    """
    This service lists presigned urls from staging
    """
    presigned_urls: Optional[conlist(StrictStr)] = Field(None, alias="presignedUrls")
    query_status: Optional[StrictStr] = Field(None, alias="queryStatus")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A page token provide this to retrieve the subsequent page. When paginating, all other parameters provided to 'ListIntegrations' must match the call that provided the page token.")
    __properties = ["presignedUrls", "queryStatus", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1ViewResponse:
        """Create an instance of V1ViewResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ViewResponse:
        """Create an instance of V1ViewResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ViewResponse.parse_obj(obj)

        _obj = V1ViewResponse.parse_obj({
            "presigned_urls": obj.get("presignedUrls"),
            "query_status": obj.get("queryStatus"),
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

