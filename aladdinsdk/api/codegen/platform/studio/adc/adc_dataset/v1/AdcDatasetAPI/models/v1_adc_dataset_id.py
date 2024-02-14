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



from pydantic import BaseModel, Field, StrictStr

class V1AdcDatasetId(BaseModel):
    """
    V1AdcDatasetId
    """
    database: StrictStr = Field(...)
    var_schema: StrictStr = Field(..., alias="schema")
    dataset_name: StrictStr = Field(..., alias="datasetName")
    client_abbreviation: StrictStr = Field(..., alias="clientAbbreviation")
    version: StrictStr = Field(...)
    __properties = ["database", "schema", "datasetName", "clientAbbreviation", "version"]

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
    def from_json(cls, json_str: str) -> V1AdcDatasetId:
        """Create an instance of V1AdcDatasetId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1AdcDatasetId:
        """Create an instance of V1AdcDatasetId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1AdcDatasetId.parse_obj(obj)

        _obj = V1AdcDatasetId.parse_obj({
            "database": obj.get("database"),
            "var_schema": obj.get("schema"),
            "dataset_name": obj.get("datasetName"),
            "client_abbreviation": obj.get("clientAbbreviation"),
            "version": obj.get("version")
        })
        return _obj

