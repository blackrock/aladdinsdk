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
from pydantic import BaseModel, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.risk_rule.models.v1_risk_rule import V1RiskRule

class V1ListSubscribedRiskRulesByPortfolioResponse(BaseModel):
    """
    V1ListSubscribedRiskRulesByPortfolioResponse
    """
    rules: Optional[conlist(V1RiskRule)] = None
    __properties = ["rules"]

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
    def from_json(cls, json_str: str) -> V1ListSubscribedRiskRulesByPortfolioResponse:
        """Create an instance of V1ListSubscribedRiskRulesByPortfolioResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListSubscribedRiskRulesByPortfolioResponse:
        """Create an instance of V1ListSubscribedRiskRulesByPortfolioResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListSubscribedRiskRulesByPortfolioResponse.parse_obj(obj)

        _obj = V1ListSubscribedRiskRulesByPortfolioResponse.parse_obj({
            "rules": [V1RiskRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj

