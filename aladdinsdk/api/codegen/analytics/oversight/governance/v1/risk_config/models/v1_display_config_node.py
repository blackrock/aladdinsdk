# coding: utf-8

"""
    Risk Governance - Configuration

    Retrieve, update, and create configurations which drive Risk Governance behaviours and Risk Radar UI choices.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictInt
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_config.models.types_analytic_data_value import TypesAnalyticDataValue

class V1DisplayConfigNode(BaseModel):
    """
    V1DisplayConfigNode
    """
    display_value: Optional[TypesAnalyticDataValue] = Field(None, alias="displayValue")
    display_order: Optional[StrictInt] = Field(None, alias="displayOrder")
    risk_config_nodes: Optional[Dict[str, V1DisplayConfigNode]] = Field(None, alias="riskConfigNodes")
    __properties = ["displayValue", "displayOrder", "riskConfigNodes"]

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
    def from_json(cls, json_str: str) -> V1DisplayConfigNode:
        """Create an instance of V1DisplayConfigNode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of display_value
        if self.display_value:
            _dict['displayValue'] = self.display_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in risk_config_nodes (dict)
        _field_dict = {}
        if self.risk_config_nodes:
            for _key in self.risk_config_nodes:
                if self.risk_config_nodes[_key]:
                    _field_dict[_key] = self.risk_config_nodes[_key].to_dict()
            _dict['riskConfigNodes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DisplayConfigNode:
        """Create an instance of V1DisplayConfigNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DisplayConfigNode.parse_obj(obj)

        _obj = V1DisplayConfigNode.parse_obj({
            "display_value": TypesAnalyticDataValue.from_dict(obj.get("displayValue")) if obj.get("displayValue") is not None else None,
            "display_order": obj.get("displayOrder"),
            "risk_config_nodes": dict(
                (_k, V1DisplayConfigNode.from_dict(_v))
                for _k, _v in obj.get("riskConfigNodes").items()
            )
            if obj.get("riskConfigNodes") is not None
            else None
        })
        return _obj

