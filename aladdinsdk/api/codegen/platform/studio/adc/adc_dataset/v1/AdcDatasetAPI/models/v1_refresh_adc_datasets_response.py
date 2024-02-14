# coding: utf-8

"""
    Adc Dataset

    Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from aladdinsdk.api.codegen.platform.studio.adc.adc_dataset.v1.AdcDatasetAPI.models.v1_refresh_adc_datasets_success_response import V1RefreshAdcDatasetsSuccessResponse

class V1RefreshAdcDatasetsResponse(BaseModel):
    """
    V1RefreshAdcDatasetsResponse
    """
    success: Optional[V1RefreshAdcDatasetsSuccessResponse] = None
    __properties = ["success"]

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
    def from_json(cls, json_str: str) -> V1RefreshAdcDatasetsResponse:
        """Create an instance of V1RefreshAdcDatasetsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of success
        if self.success:
            _dict['success'] = self.success.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1RefreshAdcDatasetsResponse:
        """Create an instance of V1RefreshAdcDatasetsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1RefreshAdcDatasetsResponse.parse_obj(obj)

        _obj = V1RefreshAdcDatasetsResponse.parse_obj({
            "success": V1RefreshAdcDatasetsSuccessResponse.from_dict(obj.get("success")) if obj.get("success") is not None else None
        })
        return _obj

