# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v1_date_settings import V1DateSettings
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_benchmark_type import V2BenchmarkType
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_desired_currency_type import V2DesiredCurrencyType
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_fund_nav_type import V2FundNavType
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_new_cash_type import V2NewCashType
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_positions_view_request import V2PositionsViewRequest

class V2PositionsQuery(BaseModel):
    """
    The query required to perform a Positions API call.
    """
    portfolio_tickers: conlist(StrictStr) = Field(..., alias="portfolioTickers")
    pm_case_id: Optional[StrictStr] = Field(None, alias="pmCaseId")
    date_settings: Optional[V1DateSettings] = Field(None, alias="dateSettings")
    fund_nav_type: Optional[V2FundNavType] = Field(None, alias="fundNavType")
    bench_type: Optional[V2BenchmarkType] = Field(None, alias="benchType")
    new_cash_type: Optional[V2NewCashType] = Field(None, alias="newCashType")
    display_currency: Optional[StrictStr] = Field(None, alias="displayCurrency")
    desired_currency_type: Optional[V2DesiredCurrencyType] = Field(None, alias="desiredCurrencyType")
    positions_view_requests: Optional[conlist(V2PositionsViewRequest)] = Field(None, alias="positionsViewRequests", description="multi view request to get data for a given entity or combination of entities.")
    user_scoped_session: Optional[StrictBool] = Field(None, alias="userScopedSession")
    __properties = ["portfolioTickers", "pmCaseId", "dateSettings", "fundNavType", "benchType", "newCashType", "displayCurrency", "desiredCurrencyType", "positionsViewRequests", "userScopedSession"]

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
    def from_json(cls, json_str: str) -> V2PositionsQuery:
        """Create an instance of V2PositionsQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of date_settings
        if self.date_settings:
            _dict['dateSettings'] = self.date_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in positions_view_requests (list)
        _items = []
        if self.positions_view_requests:
            for _item in self.positions_view_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['positionsViewRequests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2PositionsQuery:
        """Create an instance of V2PositionsQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2PositionsQuery.parse_obj(obj)

        _obj = V2PositionsQuery.parse_obj({
            "portfolio_tickers": obj.get("portfolioTickers"),
            "pm_case_id": obj.get("pmCaseId"),
            "date_settings": V1DateSettings.from_dict(obj.get("dateSettings")) if obj.get("dateSettings") is not None else None,
            "fund_nav_type": obj.get("fundNavType"),
            "bench_type": obj.get("benchType"),
            "new_cash_type": obj.get("newCashType"),
            "display_currency": obj.get("displayCurrency"),
            "desired_currency_type": obj.get("desiredCurrencyType"),
            "positions_view_requests": [V2PositionsViewRequest.from_dict(_item) for _item in obj.get("positionsViewRequests")] if obj.get("positionsViewRequests") is not None else None,
            "user_scoped_session": obj.get("userScopedSession")
        })
        return _obj

