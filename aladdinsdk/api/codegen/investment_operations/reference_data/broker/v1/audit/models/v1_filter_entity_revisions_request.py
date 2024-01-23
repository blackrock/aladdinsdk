# coding: utf-8

"""
    Broker Entities - Audit

    Operations to retrieve audit data for broker entities.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.audit.models.v1_audit_entity_query import V1AuditEntityQuery

class V1FilterEntityRevisionsRequest(BaseModel):
    """
    V1FilterEntityRevisionsRequest
    """
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of audit records to return. The service may return fewer than this value. If unspecified, at most 500 audit records will be returned. The maximum value is 500; values above 500 will be coerced to 500.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterAuditRecords' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'FilterAuditRecords' must match the call that provided the page token.")
    query: Optional[V1AuditEntityQuery] = None
    __properties = ["pageSize", "pageToken", "query"]

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
    def from_json(cls, json_str: str) -> V1FilterEntityRevisionsRequest:
        """Create an instance of V1FilterEntityRevisionsRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> V1FilterEntityRevisionsRequest:
        """Create an instance of V1FilterEntityRevisionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterEntityRevisionsRequest.parse_obj(obj)

        _obj = V1FilterEntityRevisionsRequest.parse_obj({
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken"),
            "query": V1AuditEntityQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj

