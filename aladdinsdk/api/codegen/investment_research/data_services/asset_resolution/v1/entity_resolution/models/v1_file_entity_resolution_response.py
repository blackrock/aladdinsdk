# coding: utf-8

"""
    Entity Resolution Service

    Service for entity resolution.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_resolution_error import V1ResolutionError

class V1FileEntityResolutionResponse(BaseModel):
    """
    V1FileEntityResolutionResponse
    """
    message: Optional[StrictStr] = None
    exception: Optional[StrictStr] = None
    resolution_error: Optional[V1ResolutionError] = Field(None, alias="resolutionError")
    __properties = ["message", "exception", "resolutionError"]

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
    def from_json(cls, json_str: str) -> V1FileEntityResolutionResponse:
        """Create an instance of V1FileEntityResolutionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of resolution_error
        if self.resolution_error:
            _dict['resolutionError'] = self.resolution_error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FileEntityResolutionResponse:
        """Create an instance of V1FileEntityResolutionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FileEntityResolutionResponse.parse_obj(obj)

        _obj = V1FileEntityResolutionResponse.parse_obj({
            "message": obj.get("message"),
            "exception": obj.get("exception"),
            "resolution_error": V1ResolutionError.from_dict(obj.get("resolutionError")) if obj.get("resolutionError") is not None else None
        })
        return _obj

