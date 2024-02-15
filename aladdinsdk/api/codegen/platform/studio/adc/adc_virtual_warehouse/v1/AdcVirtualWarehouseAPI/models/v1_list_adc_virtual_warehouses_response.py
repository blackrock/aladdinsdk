# coding: utf-8

"""
    Adc Virtual Warehouse

    Manages Virtual Warehouses for Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

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
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse import V1AdcVirtualWarehouse

class V1ListAdcVirtualWarehousesResponse(BaseModel):
    """
    The response message for AdcVirtualWarehouseAPI.ListAdcVirtualWarehouses.
    """
    adc_virtual_warehouses: Optional[conlist(V1AdcVirtualWarehouse)] = Field(None, alias="adcVirtualWarehouses", description="ADC Virtual Warehouses to be returned.")
    next_page_token: Optional[StrictStr] = Field(None, alias="nextPageToken", description="A token, which can be sent as 'page_token' to retrieve the next page. If this field is omitted, there are no subsequent pages.")
    __properties = ["adcVirtualWarehouses", "nextPageToken"]

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
    def from_json(cls, json_str: str) -> V1ListAdcVirtualWarehousesResponse:
        """Create an instance of V1ListAdcVirtualWarehousesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in adc_virtual_warehouses (list)
        _items = []
        if self.adc_virtual_warehouses:
            for _item in self.adc_virtual_warehouses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['adcVirtualWarehouses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ListAdcVirtualWarehousesResponse:
        """Create an instance of V1ListAdcVirtualWarehousesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ListAdcVirtualWarehousesResponse.parse_obj(obj)

        _obj = V1ListAdcVirtualWarehousesResponse.parse_obj({
            "adc_virtual_warehouses": [V1AdcVirtualWarehouse.from_dict(_item) for _item in obj.get("adcVirtualWarehouses")] if obj.get("adcVirtualWarehouses") is not None else None,
            "next_page_token": obj.get("nextPageToken")
        })
        return _obj
