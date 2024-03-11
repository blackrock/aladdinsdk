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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from aladdinsdk.api.codegen.platform.studio.adc.adc_dataset.v1.AdcDatasetAPI.models.v1_dataset_type import V1DatasetType
from aladdinsdk.api.codegen.platform.studio.adc.adc_dataset.v1.AdcDatasetAPI.models.v1_state import V1State

class V1AdcDatasetQuery(BaseModel):
    """
    The query required to perform a AdcDatasetAPI.FilterAdcDatasets query.
    """
    dataset_name: Optional[StrictStr] = Field(None, alias="datasetName")
    client_abbreviation: Optional[StrictStr] = Field(None, alias="clientAbbreviation")
    database: Optional[StrictStr] = None
    var_schema: Optional[StrictStr] = Field(None, alias="schema")
    version: Optional[StrictStr] = None
    states: Optional[conlist(V1State)] = None
    dataset_type: Optional[V1DatasetType] = Field(None, alias="datasetType")
    include_column_metadata: Optional[StrictBool] = Field(None, alias="includeColumnMetadata")
    __properties = ["datasetName", "clientAbbreviation", "database", "schema", "version", "states", "datasetType", "includeColumnMetadata"]

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
    def from_json(cls, json_str: str) -> V1AdcDatasetQuery:
        """Create an instance of V1AdcDatasetQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AdcDatasetQuery:
        """Create an instance of V1AdcDatasetQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AdcDatasetQuery.parse_obj(obj)

        _obj = V1AdcDatasetQuery.parse_obj({
            "dataset_name": obj.get("datasetName"),
            "client_abbreviation": obj.get("clientAbbreviation"),
            "database": obj.get("database"),
            "var_schema": obj.get("schema"),
            "version": obj.get("version"),
            "states": obj.get("states"),
            "dataset_type": obj.get("datasetType"),
            "include_column_metadata": obj.get("includeColumnMetadata")
        })
        return _obj

