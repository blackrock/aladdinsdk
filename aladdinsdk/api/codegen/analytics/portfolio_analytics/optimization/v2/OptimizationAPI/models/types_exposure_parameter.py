# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class TypesExposureParameter(BaseModel):
    """
    TypesExposureParameter
    """
    exposure_hierarchy: Optional[StrictStr] = Field(None, alias="exposureHierarchy")
    risk_hierarchy: Optional[StrictStr] = Field(None, alias="riskHierarchy")
    price_hierarchy: Optional[StrictStr] = Field(None, alias="priceHierarchy")
    exposure_tolerance: Optional[StrictInt] = Field(None, alias="exposureTolerance")
    exposure_purpose: Optional[StrictStr] = Field(None, alias="exposurePurpose")
    exposure_date: Optional[date] = Field(None, alias="exposureDate")
    __properties = ["exposureHierarchy", "riskHierarchy", "priceHierarchy", "exposureTolerance", "exposurePurpose", "exposureDate"]

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
    def from_json(cls, json_str: str) -> TypesExposureParameter:
        """Create an instance of TypesExposureParameter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TypesExposureParameter:
        """Create an instance of TypesExposureParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TypesExposureParameter.parse_obj(obj)

        _obj = TypesExposureParameter.parse_obj({
            "exposure_hierarchy": obj.get("exposureHierarchy"),
            "risk_hierarchy": obj.get("riskHierarchy"),
            "price_hierarchy": obj.get("priceHierarchy"),
            "exposure_tolerance": obj.get("exposureTolerance"),
            "exposure_purpose": obj.get("exposurePurpose"),
            "exposure_date": obj.get("exposureDate")
        })
        return _obj
