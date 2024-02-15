# coding: utf-8

"""
    Aladdin Corporate Action Entitlement

    API contains operations on Aladdin Corporate Action Entitlement resource.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.v1_election import V1Election
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.v1_entitlement_key import V1EntitlementKey

class V1ElectElectionRequestDetails(BaseModel):
    """
    The details for message ElectElectionsRequest.
    """
    entitlement_key: Optional[V1EntitlementKey] = Field(None, alias="entitlementKey")
    elections: conlist(V1Election) = Field(..., description="Elections to elect.")
    override_compliance: Optional[StrictBool] = Field(None, alias="overrideCompliance", description="Determines whether to ignore compliance violations while performing operation.")
    __properties = ["entitlementKey", "elections", "overrideCompliance"]

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
    def from_json(cls, json_str: str) -> V1ElectElectionRequestDetails:
        """Create an instance of V1ElectElectionRequestDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entitlement_key
        if self.entitlement_key:
            _dict['entitlementKey'] = self.entitlement_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in elections (list)
        _items = []
        if self.elections:
            for _item in self.elections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['elections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ElectElectionRequestDetails:
        """Create an instance of V1ElectElectionRequestDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ElectElectionRequestDetails.parse_obj(obj)

        _obj = V1ElectElectionRequestDetails.parse_obj({
            "entitlement_key": V1EntitlementKey.from_dict(obj.get("entitlementKey")) if obj.get("entitlementKey") is not None else None,
            "elections": [V1Election.from_dict(_item) for _item in obj.get("elections")] if obj.get("elections") is not None else None,
            "override_compliance": obj.get("overrideCompliance")
        })
        return _obj
