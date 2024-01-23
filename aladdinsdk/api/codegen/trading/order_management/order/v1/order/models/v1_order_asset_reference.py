# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from aladdinsdk.api.codegen.trading.order_management.order.v1.order.models.v1_client_id_reference import V1ClientIdReference

class V1OrderAssetReference(BaseModel):
    """
    V1OrderAssetReference
    """
    snp_cusip: Optional[StrictStr] = Field(None, alias="snpCusip")
    cins: Optional[StrictStr] = None
    isin: Optional[StrictStr] = None
    sedol: Optional[StrictStr] = None
    ric: Optional[StrictStr] = None
    local_id: Optional[StrictStr] = Field(None, alias="localId")
    client_id_reference: Optional[V1ClientIdReference] = Field(None, alias="clientIdReference")
    ccy_pair: Optional[StrictStr] = Field(None, alias="ccyPair")
    __properties = ["snpCusip", "cins", "isin", "sedol", "ric", "localId", "clientIdReference", "ccyPair"]

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
    def from_json(cls, json_str: str) -> V1OrderAssetReference:
        """Create an instance of V1OrderAssetReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of client_id_reference
        if self.client_id_reference:
            _dict['clientIdReference'] = self.client_id_reference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1OrderAssetReference:
        """Create an instance of V1OrderAssetReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1OrderAssetReference.parse_obj(obj)

        _obj = V1OrderAssetReference.parse_obj({
            "snp_cusip": obj.get("snpCusip"),
            "cins": obj.get("cins"),
            "isin": obj.get("isin"),
            "sedol": obj.get("sedol"),
            "ric": obj.get("ric"),
            "local_id": obj.get("localId"),
            "client_id_reference": V1ClientIdReference.from_dict(obj.get("clientIdReference")) if obj.get("clientIdReference") is not None else None,
            "ccy_pair": obj.get("ccyPair")
        })
        return _obj

