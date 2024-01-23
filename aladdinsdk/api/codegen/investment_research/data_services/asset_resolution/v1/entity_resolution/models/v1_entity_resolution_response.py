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
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_file_entity_resolution_response import V1FileEntityResolutionResponse
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_interactive_entity_resolution_response import V1InteractiveEntityResolutionResponse
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_table_entity_resolution_response import V1TableEntityResolutionResponse

class V1EntityResolutionResponse(BaseModel):
    """
    V1EntityResolutionResponse
    """
    interactive_resolution_response: Optional[V1InteractiveEntityResolutionResponse] = Field(None, alias="interactiveResolutionResponse")
    file_resolution_response: Optional[V1FileEntityResolutionResponse] = Field(None, alias="fileResolutionResponse")
    table_resolution_response: Optional[V1TableEntityResolutionResponse] = Field(None, alias="tableResolutionResponse")
    __properties = ["interactiveResolutionResponse", "fileResolutionResponse", "tableResolutionResponse"]

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
    def from_json(cls, json_str: str) -> V1EntityResolutionResponse:
        """Create an instance of V1EntityResolutionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of interactive_resolution_response
        if self.interactive_resolution_response:
            _dict['interactiveResolutionResponse'] = self.interactive_resolution_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_resolution_response
        if self.file_resolution_response:
            _dict['fileResolutionResponse'] = self.file_resolution_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of table_resolution_response
        if self.table_resolution_response:
            _dict['tableResolutionResponse'] = self.table_resolution_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EntityResolutionResponse:
        """Create an instance of V1EntityResolutionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EntityResolutionResponse.parse_obj(obj)

        _obj = V1EntityResolutionResponse.parse_obj({
            "interactive_resolution_response": V1InteractiveEntityResolutionResponse.from_dict(obj.get("interactiveResolutionResponse")) if obj.get("interactiveResolutionResponse") is not None else None,
            "file_resolution_response": V1FileEntityResolutionResponse.from_dict(obj.get("fileResolutionResponse")) if obj.get("fileResolutionResponse") is not None else None,
            "table_resolution_response": V1TableEntityResolutionResponse.from_dict(obj.get("tableResolutionResponse")) if obj.get("tableResolutionResponse") is not None else None
        })
        return _obj

