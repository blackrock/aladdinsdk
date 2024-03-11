# coding: utf-8

"""
    Price

    This service offers the ability to retrieve security prices via specifying a price hierarchy or price purpose. This can be used to retrieve a single price for a specific date, time series of prices for a date range, or month-end prices for a date range.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.data.market_data.price.v2.PricingAPI.models.v2_time_series_month_end_price_purpose import V2TimeSeriesMonthEndPricePurpose

class V2FilterTimeSeriesMonthEndPricesPurposeRequest(BaseModel):
    """
    V2FilterTimeSeriesMonthEndPricesPurposeRequest
    """
    time_series_monthend_asset_price_requests_purpose: Optional[V2TimeSeriesMonthEndPricePurpose] = Field(None, alias="timeSeriesMonthendAssetPriceRequestsPurpose")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterAssetPricesPurposes' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'FilterAssetPricesPurposes' must match the call that provided the page token.")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="This is the maximum number of Prices(per page) to return. The service may return fewer than this value. If unspecified, at most 100 Prices will be returned. The maximum value is 100; values above 100 will be coerced to 100.")
    __properties = ["timeSeriesMonthendAssetPriceRequestsPurpose", "pageToken", "pageSize"]

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
    def from_json(cls, json_str: str) -> V2FilterTimeSeriesMonthEndPricesPurposeRequest:
        """Create an instance of V2FilterTimeSeriesMonthEndPricesPurposeRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of time_series_monthend_asset_price_requests_purpose
        if self.time_series_monthend_asset_price_requests_purpose:
            _dict['timeSeriesMonthendAssetPriceRequestsPurpose'] = self.time_series_monthend_asset_price_requests_purpose.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2FilterTimeSeriesMonthEndPricesPurposeRequest:
        """Create an instance of V2FilterTimeSeriesMonthEndPricesPurposeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2FilterTimeSeriesMonthEndPricesPurposeRequest.parse_obj(obj)

        _obj = V2FilterTimeSeriesMonthEndPricesPurposeRequest.parse_obj({
            "time_series_monthend_asset_price_requests_purpose": V2TimeSeriesMonthEndPricePurpose.from_dict(obj.get("timeSeriesMonthendAssetPriceRequestsPurpose")) if obj.get("timeSeriesMonthendAssetPriceRequestsPurpose") is not None else None,
            "page_token": obj.get("pageToken"),
            "page_size": obj.get("pageSize")
        })
        return _obj

