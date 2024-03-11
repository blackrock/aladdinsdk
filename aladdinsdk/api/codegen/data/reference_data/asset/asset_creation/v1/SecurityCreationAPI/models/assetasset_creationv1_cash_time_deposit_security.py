# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

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
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_create_security_response import V1CreateSecurityResponse

class AssetassetCreationv1CashTimeDepositSecurity(BaseModel):
    """
    AssetassetCreationv1CashTimeDepositSecurity
    """
    cash_time_deposit_security_response: Optional[V1CreateSecurityResponse] = Field(None, alias="cashTimeDepositSecurityResponse")
    __properties = ["cashTimeDepositSecurityResponse"]

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
    def from_json(cls, json_str: str) -> AssetassetCreationv1CashTimeDepositSecurity:
        """Create an instance of AssetassetCreationv1CashTimeDepositSecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cash_time_deposit_security_response
        if self.cash_time_deposit_security_response:
            _dict['cashTimeDepositSecurityResponse'] = self.cash_time_deposit_security_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetassetCreationv1CashTimeDepositSecurity:
        """Create an instance of AssetassetCreationv1CashTimeDepositSecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AssetassetCreationv1CashTimeDepositSecurity.parse_obj(obj)

        _obj = AssetassetCreationv1CashTimeDepositSecurity.parse_obj({
            "cash_time_deposit_security_response": V1CreateSecurityResponse.from_dict(obj.get("cashTimeDepositSecurityResponse")) if obj.get("cashTimeDepositSecurityResponse") is not None else None
        })
        return _obj

