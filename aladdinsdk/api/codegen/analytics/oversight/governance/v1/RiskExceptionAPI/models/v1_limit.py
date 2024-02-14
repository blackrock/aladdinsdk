# coding: utf-8

"""
    Risk Governance - Exceptions

    Retrieve, update, or create Exceptions as surfaced in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskExceptionAPI.models.v1_limit_type import V1LimitType

class V1Limit(BaseModel):
    """
    V1Limit
    """
    limit_type: Optional[V1LimitType] = Field(None, alias="limitType")
    target: Optional[Union[StrictFloat, StrictInt]] = None
    thresholds: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(None, description="Specifies the individual thresholds captured for this limit and their numerical values.  The permitted keys are 'upperBreach', 'upperWarning', 'lowerWarning', 'lowerBreach'.  A limit has at least one entry specified.")
    __properties = ["limitType", "target", "thresholds"]

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
    def from_json(cls, json_str: str) -> V1Limit:
        """Create an instance of V1Limit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Limit:
        """Create an instance of V1Limit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Limit.parse_obj(obj)

        _obj = V1Limit.parse_obj({
            "limit_type": obj.get("limitType"),
            "target": obj.get("target"),
            "thresholds": obj.get("thresholds")
        })
        return _obj

