# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from aladdinsdk.api.codegen.analytics.portfolio_analytics.reporting.v1.portfolio_analytics.models.v1_esma_partial_liquidation_bucket_option import V1EsmaPartialLiquidationBucketOption

class V1EsmaPartialLiquidationModel(BaseModel):
    """
    V1EsmaPartialLiquidationModel
    """
    liquidation_bucket_option: Optional[V1EsmaPartialLiquidationBucketOption] = Field(None, alias="liquidationBucketOption")
    percent_nav_liquidated: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="percentNavLiquidated")
    __properties = ["liquidationBucketOption", "percentNavLiquidated"]

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
    def from_json(cls, json_str: str) -> V1EsmaPartialLiquidationModel:
        """Create an instance of V1EsmaPartialLiquidationModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of liquidation_bucket_option
        if self.liquidation_bucket_option:
            _dict['liquidationBucketOption'] = self.liquidation_bucket_option.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1EsmaPartialLiquidationModel:
        """Create an instance of V1EsmaPartialLiquidationModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1EsmaPartialLiquidationModel.parse_obj(obj)

        _obj = V1EsmaPartialLiquidationModel.parse_obj({
            "liquidation_bucket_option": V1EsmaPartialLiquidationBucketOption.from_dict(obj.get("liquidationBucketOption")) if obj.get("liquidationBucketOption") is not None else None,
            "percent_nav_liquidated": obj.get("percentNavLiquidated")
        })
        return _obj

