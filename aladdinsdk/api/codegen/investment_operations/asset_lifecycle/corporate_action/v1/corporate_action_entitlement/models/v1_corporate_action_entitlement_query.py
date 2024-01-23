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
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.corporate_action_entitlement.models.v1_entitlement_type import V1EntitlementType

class V1CorporateActionEntitlementQuery(BaseModel):
    """
    The query required to perform a CorporateActionEntitlementAPI.FilterCorporateActionEntitlements query.
    """
    ids: Optional[conlist(StrictStr)] = Field(None, description="Aladdin corporate action entitlement Ids. Numeric values stored as strings. Entitlment Id provided alone does not work for this Filter RPC. It only works when provided in conjunction with portfolio ids and entitlement types.")
    corporate_action_ids: conlist(StrictStr) = Field(..., alias="corporateActionIds", description="Aladdin parent corporate action Ids. Numeric values stored as strings. This is mandatory input for this RPC call.")
    portfolio_ids: Optional[conlist(StrictStr)] = Field(None, alias="portfolioIds", description="Portfolio Id for the entitlement. Numeric value stored as a string. This input parameter works in conjunction with entitlement ids and entitlement type.")
    entitlement_types: Optional[conlist(V1EntitlementType)] = Field(None, alias="entitlementTypes", description="Represents corporate action entitlement types. This input parameter works in conjunction with entitlement Ids and portfolio Ids.")
    __properties = ["ids", "corporateActionIds", "portfolioIds", "entitlementTypes"]

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
    def from_json(cls, json_str: str) -> V1CorporateActionEntitlementQuery:
        """Create an instance of V1CorporateActionEntitlementQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1CorporateActionEntitlementQuery:
        """Create an instance of V1CorporateActionEntitlementQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1CorporateActionEntitlementQuery.parse_obj(obj)

        _obj = V1CorporateActionEntitlementQuery.parse_obj({
            "ids": obj.get("ids"),
            "corporate_action_ids": obj.get("corporateActionIds"),
            "portfolio_ids": obj.get("portfolioIds"),
            "entitlement_types": obj.get("entitlementTypes")
        })
        return _obj

