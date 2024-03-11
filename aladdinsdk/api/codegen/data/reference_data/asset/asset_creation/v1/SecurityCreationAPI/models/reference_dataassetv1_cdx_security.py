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
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.v1_cdx_info import V1CdxInfo

class ReferenceDataassetv1CdxSecurity(BaseModel):
    """
    ReferenceDataassetv1CdxSecurity
    """
    cdx_info: Optional[V1CdxInfo] = Field(None, alias="cdxInfo")
    exchange: StrictStr = Field(..., description="represents BILATERAL, ICE etc Check out the decodes CDS_EXCHANGE for corresponding cde value to be used.")
    counterparty: Optional[StrictStr] = None
    __properties = ["cdxInfo", "exchange", "counterparty"]

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
    def from_json(cls, json_str: str) -> ReferenceDataassetv1CdxSecurity:
        """Create an instance of ReferenceDataassetv1CdxSecurity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cdx_info
        if self.cdx_info:
            _dict['cdxInfo'] = self.cdx_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferenceDataassetv1CdxSecurity:
        """Create an instance of ReferenceDataassetv1CdxSecurity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferenceDataassetv1CdxSecurity.parse_obj(obj)

        _obj = ReferenceDataassetv1CdxSecurity.parse_obj({
            "cdx_info": V1CdxInfo.from_dict(obj.get("cdxInfo")) if obj.get("cdxInfo") is not None else None,
            "exchange": obj.get("exchange"),
            "counterparty": obj.get("counterparty")
        })
        return _obj

