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
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_file_entity_resolution_param import V1FileEntityResolutionParam
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_interactive_entity_resolution_param import V1InteractiveEntityResolutionParam
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_snowflake_session import V1SnowflakeSession
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_table_entity_resolution_param import V1TableEntityResolutionParam

class V1ResolveEntityRequest(BaseModel):
    """
    V1ResolveEntityRequest
    """
    interactive_resolution_parameter: Optional[V1InteractiveEntityResolutionParam] = Field(None, alias="interactiveResolutionParameter")
    file_resolution_parameter: Optional[V1FileEntityResolutionParam] = Field(None, alias="fileResolutionParameter")
    table_resolution_parameter: Optional[V1TableEntityResolutionParam] = Field(None, alias="tableResolutionParameter")
    snowflake_session_parameter: Optional[V1SnowflakeSession] = Field(None, alias="snowflakeSessionParameter")
    __properties = ["interactiveResolutionParameter", "fileResolutionParameter", "tableResolutionParameter", "snowflakeSessionParameter"]

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
    def from_json(cls, json_str: str) -> V1ResolveEntityRequest:
        """Create an instance of V1ResolveEntityRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of interactive_resolution_parameter
        if self.interactive_resolution_parameter:
            _dict['interactiveResolutionParameter'] = self.interactive_resolution_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_resolution_parameter
        if self.file_resolution_parameter:
            _dict['fileResolutionParameter'] = self.file_resolution_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of table_resolution_parameter
        if self.table_resolution_parameter:
            _dict['tableResolutionParameter'] = self.table_resolution_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snowflake_session_parameter
        if self.snowflake_session_parameter:
            _dict['snowflakeSessionParameter'] = self.snowflake_session_parameter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ResolveEntityRequest:
        """Create an instance of V1ResolveEntityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ResolveEntityRequest.parse_obj(obj)

        _obj = V1ResolveEntityRequest.parse_obj({
            "interactive_resolution_parameter": V1InteractiveEntityResolutionParam.from_dict(obj.get("interactiveResolutionParameter")) if obj.get("interactiveResolutionParameter") is not None else None,
            "file_resolution_parameter": V1FileEntityResolutionParam.from_dict(obj.get("fileResolutionParameter")) if obj.get("fileResolutionParameter") is not None else None,
            "table_resolution_parameter": V1TableEntityResolutionParam.from_dict(obj.get("tableResolutionParameter")) if obj.get("tableResolutionParameter") is not None else None,
            "snowflake_session_parameter": V1SnowflakeSession.from_dict(obj.get("snowflakeSessionParameter")) if obj.get("snowflakeSessionParameter") is not None else None
        })
        return _obj

