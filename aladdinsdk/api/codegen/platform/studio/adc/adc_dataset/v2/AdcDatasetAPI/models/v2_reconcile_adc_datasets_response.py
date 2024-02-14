# coding: utf-8

"""
    Adc Dataset

    Manages Datasets in Aladdin Data Cloud (ADC). Used by Studio's ADC Admin Center.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class V2ReconcileAdcDatasetsResponse(BaseModel):
    """
    The response message for AdcDatasetAPI.ReconcileAdcDatasets.
    """
    recon_executed_adc_datasets: Optional[conlist(StrictStr)] = Field(None, alias="reconExecutedAdcDatasets")
    recon_unexecuted_adc_datasets: Optional[conlist(StrictStr)] = Field(None, alias="reconUnexecutedAdcDatasets")
    recon_exception: Optional[StrictStr] = Field(None, alias="reconException")
    __properties = ["reconExecutedAdcDatasets", "reconUnexecutedAdcDatasets", "reconException"]

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
    def from_json(cls, json_str: str) -> V2ReconcileAdcDatasetsResponse:
        """Create an instance of V2ReconcileAdcDatasetsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ReconcileAdcDatasetsResponse:
        """Create an instance of V2ReconcileAdcDatasetsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ReconcileAdcDatasetsResponse.parse_obj(obj)

        _obj = V2ReconcileAdcDatasetsResponse.parse_obj({
            "recon_executed_adc_datasets": obj.get("reconExecutedAdcDatasets"),
            "recon_unexecuted_adc_datasets": obj.get("reconUnexecutedAdcDatasets"),
            "recon_exception": obj.get("reconException")
        })
        return _obj

