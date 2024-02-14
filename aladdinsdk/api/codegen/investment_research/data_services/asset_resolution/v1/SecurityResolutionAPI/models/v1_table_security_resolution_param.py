# coding: utf-8

"""
    Security Resolution Service

    Service for security resolution.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.SecurityResolutionAPI.models.v1_asset_master import V1AssetMaster
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.SecurityResolutionAPI.models.v1_resolution_type import V1ResolutionType

class V1TableSecurityResolutionParam(BaseModel):
    """
    TableSecurityResolutionParam represents parameters for resolving an entire identifier column present inside the src table.
    """
    src_table: StrictStr = Field(..., alias="srcTable")
    security_types: Dict[str, StrictStr] = Field(..., alias="securityTypes")
    asof_date_col: StrictStr = Field(..., alias="asofDateCol")
    exchange_code_col: Optional[StrictStr] = Field(None, alias="exchangeCodeCol")
    country_iso2_col: Optional[StrictStr] = Field(None, alias="countryIso2Col")
    currency_iso3_col: Optional[StrictStr] = Field(None, alias="currencyIso3Col")
    resolution_key_col: StrictStr = Field(..., alias="resolutionKeyCol")
    resolution_type: Optional[V1ResolutionType] = Field(None, alias="resolutionType")
    asset_master: Optional[V1AssetMaster] = Field(None, alias="assetMaster")
    __properties = ["srcTable", "securityTypes", "asofDateCol", "exchangeCodeCol", "countryIso2Col", "currencyIso3Col", "resolutionKeyCol", "resolutionType", "assetMaster"]

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
    def from_json(cls, json_str: str) -> V1TableSecurityResolutionParam:
        """Create an instance of V1TableSecurityResolutionParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TableSecurityResolutionParam:
        """Create an instance of V1TableSecurityResolutionParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TableSecurityResolutionParam.parse_obj(obj)

        _obj = V1TableSecurityResolutionParam.parse_obj({
            "src_table": obj.get("srcTable"),
            "security_types": obj.get("securityTypes"),
            "asof_date_col": obj.get("asofDateCol"),
            "exchange_code_col": obj.get("exchangeCodeCol"),
            "country_iso2_col": obj.get("countryIso2Col"),
            "currency_iso3_col": obj.get("currencyIso3Col"),
            "resolution_key_col": obj.get("resolutionKeyCol"),
            "resolution_type": obj.get("resolutionType"),
            "asset_master": obj.get("assetMaster")
        })
        return _obj

