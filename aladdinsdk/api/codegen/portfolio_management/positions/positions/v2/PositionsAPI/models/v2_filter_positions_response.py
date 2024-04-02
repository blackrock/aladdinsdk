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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.types_portfolio_as_of_stats import TypesPortfolioAsOfStats
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v1_data_table import V1DataTable
from aladdinsdk.api.codegen.portfolio_management.positions.positions.v2.PositionsAPI.models.v2_portfolio_position_warnings import V2PortfolioPositionWarnings

class V2FilterPositionsResponse(BaseModel):
    """
    V2FilterPositionsResponse
    """
    data_tables: conlist(V1DataTable) = Field(..., alias="dataTables")
    position_warnings: Optional[Dict[str, V2PortfolioPositionWarnings]] = Field(None, alias="positionWarnings")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken")
    portfolio_stats: Optional[Dict[str, TypesPortfolioAsOfStats]] = Field(None, alias="portfolioStats")
    __properties = ["dataTables", "positionWarnings", "nextPageToken", "portfolioStats"]

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
    def from_json(cls, json_str: str) -> V2FilterPositionsResponse:
        """Create an instance of V2FilterPositionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data_tables (list)
        _items = []
        if self.data_tables:
            for _item in self.data_tables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dataTables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in position_warnings (dict)
        _field_dict = {}
        if self.position_warnings:
            for _key in self.position_warnings:
                if self.position_warnings[_key]:
                    _field_dict[_key] = self.position_warnings[_key].to_dict()
            _dict['positionWarnings'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in portfolio_stats (dict)
        _field_dict = {}
        if self.portfolio_stats:
            for _key in self.portfolio_stats:
                if self.portfolio_stats[_key]:
                    _field_dict[_key] = self.portfolio_stats[_key].to_dict()
            _dict['portfolioStats'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2FilterPositionsResponse:
        """Create an instance of V2FilterPositionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2FilterPositionsResponse.parse_obj(obj)

        _obj = V2FilterPositionsResponse.parse_obj({
            "data_tables": [V1DataTable.from_dict(_item) for _item in obj.get("dataTables")] if obj.get("dataTables") is not None else None,
            "position_warnings": dict(
                (_k, V2PortfolioPositionWarnings.from_dict(_v))
                for _k, _v in obj.get("positionWarnings").items()
            )
            if obj.get("positionWarnings") is not None
            else None,
            "next_page_token": obj.get("nextPageToken"),
            "portfolio_stats": dict(
                (_k, TypesPortfolioAsOfStats.from_dict(_v))
                for _k, _v in obj.get("portfolioStats").items()
            )
            if obj.get("portfolioStats") is not None
            else None
        })
        return _obj
