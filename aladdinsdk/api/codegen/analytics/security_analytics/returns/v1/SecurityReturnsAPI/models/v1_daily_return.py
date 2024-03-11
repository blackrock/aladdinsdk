# coding: utf-8

"""
    Security Returns

    Retrieve daily time-series of security level returns  # noqa: E501

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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class V1DailyReturn(BaseModel):
    """
    V1DailyReturn
    """
    asset_id: Optional[StrictStr] = Field(None, alias="assetId")
    price_hierarchy: Optional[StrictStr] = Field(None, alias="priceHierarchy")
    return_date: Optional[date] = Field(None, alias="returnDate")
    currency_code: Optional[StrictStr] = Field(None, alias="currencyCode")
    notional_weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="notionalWeight")
    total_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalReturn")
    principal_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="principalReturn")
    income_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="incomeReturn")
    price_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="priceReturn")
    paydown_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="paydownReturn")
    currency_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="currencyReturn")
    begin_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="beginMarketValue")
    begin_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="beginPrice")
    end_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="endPrice")
    end_market_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="endMarketValue")
    income_payment: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="incomePayment")
    principal_payment: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="principalPayment")
    begin_accrued_interest: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="beginAccruedInterest")
    end_accrued_interest: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="endAccruedInterest")
    begin_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="beginFactor")
    end_factor: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="endFactor")
    withholding_tax_return: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="withholdingTaxReturn")
    __properties = ["assetId", "priceHierarchy", "returnDate", "currencyCode", "notionalWeight", "totalReturn", "principalReturn", "incomeReturn", "priceReturn", "paydownReturn", "currencyReturn", "beginMarketValue", "beginPrice", "endPrice", "endMarketValue", "incomePayment", "principalPayment", "beginAccruedInterest", "endAccruedInterest", "beginFactor", "endFactor", "withholdingTaxReturn"]

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
    def from_json(cls, json_str: str) -> V1DailyReturn:
        """Create an instance of V1DailyReturn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1DailyReturn:
        """Create an instance of V1DailyReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1DailyReturn.parse_obj(obj)

        _obj = V1DailyReturn.parse_obj({
            "asset_id": obj.get("assetId"),
            "price_hierarchy": obj.get("priceHierarchy"),
            "return_date": obj.get("returnDate"),
            "currency_code": obj.get("currencyCode"),
            "notional_weight": obj.get("notionalWeight"),
            "total_return": obj.get("totalReturn"),
            "principal_return": obj.get("principalReturn"),
            "income_return": obj.get("incomeReturn"),
            "price_return": obj.get("priceReturn"),
            "paydown_return": obj.get("paydownReturn"),
            "currency_return": obj.get("currencyReturn"),
            "begin_market_value": obj.get("beginMarketValue"),
            "begin_price": obj.get("beginPrice"),
            "end_price": obj.get("endPrice"),
            "end_market_value": obj.get("endMarketValue"),
            "income_payment": obj.get("incomePayment"),
            "principal_payment": obj.get("principalPayment"),
            "begin_accrued_interest": obj.get("beginAccruedInterest"),
            "end_accrued_interest": obj.get("endAccruedInterest"),
            "begin_factor": obj.get("beginFactor"),
            "end_factor": obj.get("endFactor"),
            "withholding_tax_return": obj.get("withholdingTaxReturn")
        })
        return _obj

