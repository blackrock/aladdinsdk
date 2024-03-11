# coding: utf-8

"""
    Risk Governance - Rules

    Retrieve, update, and create Rules and Rule Subscriptions as surfaced in Risk Radar.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskRuleAPI.models.v1_look_through_proxy_type import V1LookThroughProxyType
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskRuleAPI.models.v1_look_through_security_type import V1LookThroughSecurityType

class Oversightgovernancev1LookThroughConfig(BaseModel):
    """
    Oversightgovernancev1LookThroughConfig
    """
    look_through_portfolio: StrictBool = Field(..., alias="lookThroughPortfolio")
    look_through_benchmark: StrictBool = Field(..., alias="lookThroughBenchmark")
    look_through_security_types: conlist(V1LookThroughSecurityType) = Field(..., alias="lookThroughSecurityTypes")
    look_through_proxy_types: Optional[conlist(V1LookThroughProxyType)] = Field(None, alias="lookThroughProxyTypes")
    look_through_inheritance: Optional[StrictBool] = Field(None, alias="lookThroughInheritance")
    __properties = ["lookThroughPortfolio", "lookThroughBenchmark", "lookThroughSecurityTypes", "lookThroughProxyTypes", "lookThroughInheritance"]

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
    def from_json(cls, json_str: str) -> Oversightgovernancev1LookThroughConfig:
        """Create an instance of Oversightgovernancev1LookThroughConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Oversightgovernancev1LookThroughConfig:
        """Create an instance of Oversightgovernancev1LookThroughConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Oversightgovernancev1LookThroughConfig.parse_obj(obj)

        _obj = Oversightgovernancev1LookThroughConfig.parse_obj({
            "look_through_portfolio": obj.get("lookThroughPortfolio"),
            "look_through_benchmark": obj.get("lookThroughBenchmark"),
            "look_through_security_types": obj.get("lookThroughSecurityTypes"),
            "look_through_proxy_types": obj.get("lookThroughProxyTypes"),
            "look_through_inheritance": obj.get("lookThroughInheritance")
        })
        return _obj

