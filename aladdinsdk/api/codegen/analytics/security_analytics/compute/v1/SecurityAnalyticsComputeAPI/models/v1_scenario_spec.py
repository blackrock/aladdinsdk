# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_interest_rate_shock import V1InterestRateShock
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_shock_input import V1ShockInput

class V1ScenarioSpec(BaseModel):
    """
    V1ScenarioSpec
    """
    interest_rate_shock: Optional[V1InterestRateShock] = Field(None, alias="interestRateShock")
    fx_spot_shock: Optional[V1ShockInput] = Field(None, alias="fxSpotShock")
    underlying_level_shock: Optional[V1ShockInput] = Field(None, alias="underlyingLevelShock")
    option_volatility_shock: Optional[V1ShockInput] = Field(None, alias="optionVolatilityShock")
    horizon_date: Optional[date] = Field(None, alias="horizonDate")
    oas_shock: Optional[V1ShockInput] = Field(None, alias="oasShock")
    cds_shock: Optional[V1ShockInput] = Field(None, alias="cdsShock")
    inflation_shock: Optional[V1ShockInput] = Field(None, alias="inflationShock")
    __properties = ["interestRateShock", "fxSpotShock", "underlyingLevelShock", "optionVolatilityShock", "horizonDate", "oasShock", "cdsShock", "inflationShock"]

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
    def from_json(cls, json_str: str) -> V1ScenarioSpec:
        """Create an instance of V1ScenarioSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of interest_rate_shock
        if self.interest_rate_shock:
            _dict['interestRateShock'] = self.interest_rate_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fx_spot_shock
        if self.fx_spot_shock:
            _dict['fxSpotShock'] = self.fx_spot_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of underlying_level_shock
        if self.underlying_level_shock:
            _dict['underlyingLevelShock'] = self.underlying_level_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of option_volatility_shock
        if self.option_volatility_shock:
            _dict['optionVolatilityShock'] = self.option_volatility_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oas_shock
        if self.oas_shock:
            _dict['oasShock'] = self.oas_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cds_shock
        if self.cds_shock:
            _dict['cdsShock'] = self.cds_shock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inflation_shock
        if self.inflation_shock:
            _dict['inflationShock'] = self.inflation_shock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ScenarioSpec:
        """Create an instance of V1ScenarioSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ScenarioSpec.parse_obj(obj)

        _obj = V1ScenarioSpec.parse_obj({
            "interest_rate_shock": V1InterestRateShock.from_dict(obj.get("interestRateShock")) if obj.get("interestRateShock") is not None else None,
            "fx_spot_shock": V1ShockInput.from_dict(obj.get("fxSpotShock")) if obj.get("fxSpotShock") is not None else None,
            "underlying_level_shock": V1ShockInput.from_dict(obj.get("underlyingLevelShock")) if obj.get("underlyingLevelShock") is not None else None,
            "option_volatility_shock": V1ShockInput.from_dict(obj.get("optionVolatilityShock")) if obj.get("optionVolatilityShock") is not None else None,
            "horizon_date": obj.get("horizonDate"),
            "oas_shock": V1ShockInput.from_dict(obj.get("oasShock")) if obj.get("oasShock") is not None else None,
            "cds_shock": V1ShockInput.from_dict(obj.get("cdsShock")) if obj.get("cdsShock") is not None else None,
            "inflation_shock": V1ShockInput.from_dict(obj.get("inflationShock")) if obj.get("inflationShock") is not None else None
        })
        return _obj
