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
from pydantic import BaseModel, Field, conlist
from aladdinsdk.api.codegen.platform.studio.adc.adc_virtual_warehouse.v1.AdcVirtualWarehouseAPI.models.v1_adc_virtual_warehouse_operation_response import V1AdcVirtualWarehouseOperationResponse

class V1SuspendAdcVirtualWarehouseResponse(BaseModel):
    """
    V1SuspendAdcVirtualWarehouseResponse
    """
    warehouse_suspend_statuses: Optional[conlist(V1AdcVirtualWarehouseOperationResponse)] = Field(None, alias="warehouseSuspendStatuses")
    __properties = ["warehouseSuspendStatuses"]

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
    def from_json(cls, json_str: str) -> V1SuspendAdcVirtualWarehouseResponse:
        """Create an instance of V1SuspendAdcVirtualWarehouseResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in warehouse_suspend_statuses (list)
        _items = []
        if self.warehouse_suspend_statuses:
            for _item in self.warehouse_suspend_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warehouseSuspendStatuses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1SuspendAdcVirtualWarehouseResponse:
        """Create an instance of V1SuspendAdcVirtualWarehouseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1SuspendAdcVirtualWarehouseResponse.parse_obj(obj)

        _obj = V1SuspendAdcVirtualWarehouseResponse.parse_obj({
            "warehouse_suspend_statuses": [V1AdcVirtualWarehouseOperationResponse.from_dict(_item) for _item in obj.get("warehouseSuspendStatuses")] if obj.get("warehouseSuspendStatuses") is not None else None
        })
        return _obj

