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
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.analytics.oversight.governance.v1.RiskRuleAPI.models.v1_risk_rule_subscription import V1RiskRuleSubscription

class V1RetrieveRiskRuleSubscriptionsResponse(BaseModel):
    """
    V1RetrieveRiskRuleSubscriptionsResponse
    """
    risk_rule_subscriptions: Optional[conlist(V1RiskRuleSubscription)] = Field(None, alias="riskRuleSubscriptions")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    __properties = ["riskRuleSubscriptions", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1RetrieveRiskRuleSubscriptionsResponse:
        """Create an instance of V1RetrieveRiskRuleSubscriptionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in risk_rule_subscriptions (list)
        _items = []
        if self.risk_rule_subscriptions:
            for _item in self.risk_rule_subscriptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['riskRuleSubscriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RetrieveRiskRuleSubscriptionsResponse:
        """Create an instance of V1RetrieveRiskRuleSubscriptionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RetrieveRiskRuleSubscriptionsResponse.parse_obj(obj)

        _obj = V1RetrieveRiskRuleSubscriptionsResponse.parse_obj({
            "risk_rule_subscriptions": [V1RiskRuleSubscription.from_dict(_item) for _item in obj.get("riskRuleSubscriptions")] if obj.get("riskRuleSubscriptions") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

