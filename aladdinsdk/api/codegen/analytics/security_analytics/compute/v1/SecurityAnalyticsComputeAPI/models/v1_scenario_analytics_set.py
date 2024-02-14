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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.types_projected_speed import TypesProjectedSpeed
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_greek_analytic_set import V1GreekAnalyticSet
from aladdinsdk.api.codegen.analytics.security_analytics.compute.v1.SecurityAnalyticsComputeAPI.models.v1_horizon_analytics_set import V1HorizonAnalyticsSet

class V1ScenarioAnalyticsSet(BaseModel):
    """
    V1ScenarioAnalyticsSet
    """
    market_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="marketPrice")
    market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="marketValue")
    notional_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="notionalMarketValue")
    accrued_interest: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="accruedInterest")
    accrued_interest_dollar_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="accruedInterestDollarValue")
    yield_to_maturity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="yieldToMaturity")
    wal_to_maturity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walToMaturity")
    modified_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="modifiedDuration")
    modified_duration_dv01: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="modifiedDurationDv01")
    modified_convexity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="modifiedConvexity")
    spread_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="spreadDuration")
    spread_duration_dollar_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="spreadDurationDollarValue")
    spread_duration_dv01: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="spreadDurationDv01")
    spread_convexity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="spreadConvexity")
    oas: Optional[Union[StrictFloat, StrictInt]] = None
    oad: Optional[Union[StrictFloat, StrictInt]] = None
    oad_dollar_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="oadDollarValue")
    oad_dv01: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="oadDv01")
    oac: Optional[Union[StrictFloat, StrictInt]] = None
    model_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="modelDuration")
    model_convexity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="modelConvexity")
    greek_analytic_set: Optional[V1GreekAnalyticSet] = Field(None, alias="greekAnalyticSet")
    greek_dollar_value_set: Optional[V1GreekAnalyticSet] = Field(None, alias="greekDollarValueSet")
    volatility: Optional[Union[StrictFloat, StrictInt]] = None
    ois_libor_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="oisLiborDuration")
    at_the_money_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="atTheMoneyRate")
    at_the_money_volatility: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="atTheMoneyVolatility")
    inflation_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="inflationDuration")
    inflation_duration_dv01: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="inflationDurationDv01")
    inflation_convexity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="inflationConvexity")
    breakeven_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="breakevenRate")
    street_yield: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="streetYield")
    prepay_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="prepayDuration")
    mortgage_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="mortgageDuration")
    mortgage_rate_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="mortgageRateDuration")
    mortgage_treasury_basis_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="mortgageTreasuryBasisDuration")
    pss_duration: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="pssDuration")
    wal_equiv_cpr: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walEquivCpr")
    wal_equiv_psa: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walEquivPsa")
    wal_of_principal: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walOfPrincipal")
    wal_of_interest: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walOfInterest")
    wal_of_losses: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walOfLosses")
    prepayment_speeds_set: Optional[TypesProjectedSpeed] = Field(None, alias="prepaymentSpeedsSet")
    default_speeds_set: Optional[TypesProjectedSpeed] = Field(None, alias="defaultSpeedsSet")
    delinquency_speeds_set: Optional[TypesProjectedSpeed] = Field(None, alias="delinquencySpeedsSet")
    loss_severity_speeds_set: Optional[TypesProjectedSpeed] = Field(None, alias="lossSeveritySpeedsSet")
    a_spread: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="aSpread")
    j_spread: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="jSpread")
    static_spread: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="staticSpread")
    option_cost: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="optionCost")
    dxs: Optional[Union[StrictFloat, StrictInt]] = None
    option_adjusted_yield: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="optionAdjustedYield")
    oac_dollar_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="oacDollarValue")
    oac_cv01: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="oacCv01")
    wal_to_worst: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="walToWorst")
    yield_to_worst: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="yieldToWorst")
    horizon_analytics_set: Optional[V1HorizonAnalyticsSet] = Field(None, alias="horizonAnalyticsSet")
    yield_to_worst_date: Optional[date] = Field(None, alias="yieldToWorstDate")
    yield_to_call: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="yieldToCall")
    yield_to_call_date: Optional[date] = Field(None, alias="yieldToCallDate")
    __properties = ["marketPrice", "marketValue", "notionalMarketValue", "accruedInterest", "accruedInterestDollarValue", "yieldToMaturity", "walToMaturity", "modifiedDuration", "modifiedDurationDv01", "modifiedConvexity", "spreadDuration", "spreadDurationDollarValue", "spreadDurationDv01", "spreadConvexity", "oas", "oad", "oadDollarValue", "oadDv01", "oac", "modelDuration", "modelConvexity", "greekAnalyticSet", "greekDollarValueSet", "volatility", "oisLiborDuration", "atTheMoneyRate", "atTheMoneyVolatility", "inflationDuration", "inflationDurationDv01", "inflationConvexity", "breakevenRate", "streetYield", "prepayDuration", "mortgageDuration", "mortgageRateDuration", "mortgageTreasuryBasisDuration", "pssDuration", "walEquivCpr", "walEquivPsa", "walOfPrincipal", "walOfInterest", "walOfLosses", "prepaymentSpeedsSet", "defaultSpeedsSet", "delinquencySpeedsSet", "lossSeveritySpeedsSet", "aSpread", "jSpread", "staticSpread", "optionCost", "dxs", "optionAdjustedYield", "oacDollarValue", "oacCv01", "walToWorst", "yieldToWorst", "horizonAnalyticsSet", "yieldToWorstDate", "yieldToCall", "yieldToCallDate"]

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
    def from_json(cls, json_str: str) -> V1ScenarioAnalyticsSet:
        """Create an instance of V1ScenarioAnalyticsSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of greek_analytic_set
        if self.greek_analytic_set:
            _dict['greekAnalyticSet'] = self.greek_analytic_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of greek_dollar_value_set
        if self.greek_dollar_value_set:
            _dict['greekDollarValueSet'] = self.greek_dollar_value_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prepayment_speeds_set
        if self.prepayment_speeds_set:
            _dict['prepaymentSpeedsSet'] = self.prepayment_speeds_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_speeds_set
        if self.default_speeds_set:
            _dict['defaultSpeedsSet'] = self.default_speeds_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delinquency_speeds_set
        if self.delinquency_speeds_set:
            _dict['delinquencySpeedsSet'] = self.delinquency_speeds_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loss_severity_speeds_set
        if self.loss_severity_speeds_set:
            _dict['lossSeveritySpeedsSet'] = self.loss_severity_speeds_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of horizon_analytics_set
        if self.horizon_analytics_set:
            _dict['horizonAnalyticsSet'] = self.horizon_analytics_set.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ScenarioAnalyticsSet:
        """Create an instance of V1ScenarioAnalyticsSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ScenarioAnalyticsSet.parse_obj(obj)

        _obj = V1ScenarioAnalyticsSet.parse_obj({
            "market_price": obj.get("marketPrice"),
            "market_value": obj.get("marketValue"),
            "notional_market_value": obj.get("notionalMarketValue"),
            "accrued_interest": obj.get("accruedInterest"),
            "accrued_interest_dollar_value": obj.get("accruedInterestDollarValue"),
            "yield_to_maturity": obj.get("yieldToMaturity"),
            "wal_to_maturity": obj.get("walToMaturity"),
            "modified_duration": obj.get("modifiedDuration"),
            "modified_duration_dv01": obj.get("modifiedDurationDv01"),
            "modified_convexity": obj.get("modifiedConvexity"),
            "spread_duration": obj.get("spreadDuration"),
            "spread_duration_dollar_value": obj.get("spreadDurationDollarValue"),
            "spread_duration_dv01": obj.get("spreadDurationDv01"),
            "spread_convexity": obj.get("spreadConvexity"),
            "oas": obj.get("oas"),
            "oad": obj.get("oad"),
            "oad_dollar_value": obj.get("oadDollarValue"),
            "oad_dv01": obj.get("oadDv01"),
            "oac": obj.get("oac"),
            "model_duration": obj.get("modelDuration"),
            "model_convexity": obj.get("modelConvexity"),
            "greek_analytic_set": V1GreekAnalyticSet.from_dict(obj.get("greekAnalyticSet")) if obj.get("greekAnalyticSet") is not None else None,
            "greek_dollar_value_set": V1GreekAnalyticSet.from_dict(obj.get("greekDollarValueSet")) if obj.get("greekDollarValueSet") is not None else None,
            "volatility": obj.get("volatility"),
            "ois_libor_duration": obj.get("oisLiborDuration"),
            "at_the_money_rate": obj.get("atTheMoneyRate"),
            "at_the_money_volatility": obj.get("atTheMoneyVolatility"),
            "inflation_duration": obj.get("inflationDuration"),
            "inflation_duration_dv01": obj.get("inflationDurationDv01"),
            "inflation_convexity": obj.get("inflationConvexity"),
            "breakeven_rate": obj.get("breakevenRate"),
            "street_yield": obj.get("streetYield"),
            "prepay_duration": obj.get("prepayDuration"),
            "mortgage_duration": obj.get("mortgageDuration"),
            "mortgage_rate_duration": obj.get("mortgageRateDuration"),
            "mortgage_treasury_basis_duration": obj.get("mortgageTreasuryBasisDuration"),
            "pss_duration": obj.get("pssDuration"),
            "wal_equiv_cpr": obj.get("walEquivCpr"),
            "wal_equiv_psa": obj.get("walEquivPsa"),
            "wal_of_principal": obj.get("walOfPrincipal"),
            "wal_of_interest": obj.get("walOfInterest"),
            "wal_of_losses": obj.get("walOfLosses"),
            "prepayment_speeds_set": TypesProjectedSpeed.from_dict(obj.get("prepaymentSpeedsSet")) if obj.get("prepaymentSpeedsSet") is not None else None,
            "default_speeds_set": TypesProjectedSpeed.from_dict(obj.get("defaultSpeedsSet")) if obj.get("defaultSpeedsSet") is not None else None,
            "delinquency_speeds_set": TypesProjectedSpeed.from_dict(obj.get("delinquencySpeedsSet")) if obj.get("delinquencySpeedsSet") is not None else None,
            "loss_severity_speeds_set": TypesProjectedSpeed.from_dict(obj.get("lossSeveritySpeedsSet")) if obj.get("lossSeveritySpeedsSet") is not None else None,
            "a_spread": obj.get("aSpread"),
            "j_spread": obj.get("jSpread"),
            "static_spread": obj.get("staticSpread"),
            "option_cost": obj.get("optionCost"),
            "dxs": obj.get("dxs"),
            "option_adjusted_yield": obj.get("optionAdjustedYield"),
            "oac_dollar_value": obj.get("oacDollarValue"),
            "oac_cv01": obj.get("oacCv01"),
            "wal_to_worst": obj.get("walToWorst"),
            "yield_to_worst": obj.get("yieldToWorst"),
            "horizon_analytics_set": V1HorizonAnalyticsSet.from_dict(obj.get("horizonAnalyticsSet")) if obj.get("horizonAnalyticsSet") is not None else None,
            "yield_to_worst_date": obj.get("yieldToWorstDate"),
            "yield_to_call": obj.get("yieldToCall"),
            "yield_to_call_date": obj.get("yieldToCallDate")
        })
        return _obj

