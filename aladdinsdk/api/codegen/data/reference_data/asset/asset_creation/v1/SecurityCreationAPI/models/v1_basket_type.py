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
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.enums_basket_type_asset_type import EnumsBasketTypeAssetType
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.enums_basket_type_rating import EnumsBasketTypeRating
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.enums_basket_type_region import EnumsBasketTypeRegion
from aladdinsdk.api.codegen.data.reference_data.asset.asset_creation.v1.SecurityCreationAPI.models.enums_basket_type_sector import EnumsBasketTypeSector

class V1BasketType(BaseModel):
    """
    BasketType represents basket type of underlying security, it can be either of region, sector, finance, or asset type.
    """
    basket_type_rating: Optional[EnumsBasketTypeRating] = Field(None, alias="basketTypeRating")
    basket_type_region: Optional[EnumsBasketTypeRegion] = Field(None, alias="basketTypeRegion")
    basket_type_sector: Optional[EnumsBasketTypeSector] = Field(None, alias="basketTypeSector")
    basket_type_asset_type: Optional[EnumsBasketTypeAssetType] = Field(None, alias="basketTypeAssetType")
    __properties = ["basketTypeRating", "basketTypeRegion", "basketTypeSector", "basketTypeAssetType"]

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
    def from_json(cls, json_str: str) -> V1BasketType:
        """Create an instance of V1BasketType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1BasketType:
        """Create an instance of V1BasketType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1BasketType.parse_obj(obj)

        _obj = V1BasketType.parse_obj({
            "basket_type_rating": obj.get("basketTypeRating"),
            "basket_type_region": obj.get("basketTypeRegion"),
            "basket_type_sector": obj.get("basketTypeSector"),
            "basket_type_asset_type": obj.get("basketTypeAssetType")
        })
        return _obj

