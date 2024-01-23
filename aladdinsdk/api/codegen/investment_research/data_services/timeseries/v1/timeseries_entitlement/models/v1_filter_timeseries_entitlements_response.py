# coding: utf-8

"""
    Timeseries Entitlement

    Timeseries entitlement offers the capability to assign, remove and lookup entitlements for each timeseries data.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.timeseries_entitlement.models.v1_timeseries_entitlement import V1TimeseriesEntitlement

class V1FilterTimeseriesEntitlementsResponse(BaseModel):
    """
    V1FilterTimeseriesEntitlementsResponse
    """
    timeseries_entitlements: conlist(V1TimeseriesEntitlement) = Field(..., alias="timeseriesEntitlements", description="The TimeseriesEntitlement entities that match the specified FilterTimeseriesEntitlementRequest.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    __properties = ["timeseriesEntitlements", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterTimeseriesEntitlementsResponse:
        """Create an instance of V1FilterTimeseriesEntitlementsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in timeseries_entitlements (list)
        _items = []
        if self.timeseries_entitlements:
            for _item in self.timeseries_entitlements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['timeseriesEntitlements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterTimeseriesEntitlementsResponse:
        """Create an instance of V1FilterTimeseriesEntitlementsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterTimeseriesEntitlementsResponse.parse_obj(obj)

        _obj = V1FilterTimeseriesEntitlementsResponse.parse_obj({
            "timeseries_entitlements": [V1TimeseriesEntitlement.from_dict(_item) for _item in obj.get("timeseriesEntitlements")] if obj.get("timeseriesEntitlements") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj

