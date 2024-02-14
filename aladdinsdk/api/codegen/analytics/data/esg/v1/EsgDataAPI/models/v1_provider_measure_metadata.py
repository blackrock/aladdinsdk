# coding: utf-8

"""
    ESG Data

    The ESG Data API offers a centralized source of ESG data and meta data across multiple vendors. The API retrieves ESG data by asset and issuer from multiple vendors, providing the data in one digestible schema. Retrieve ESG data for selected assets and issuers by providing entity id, provider id, date(s) and measure name. Meta data on ESG data measures can be retrieved by selecting a provider, provider category and unique measure names. Time Series API in alpha version, changes may be made at any time.  # noqa: E501

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
from aladdinsdk.api.codegen.analytics.data.esg.v1.EsgDataAPI.models.v1_data_type import V1DataType
from aladdinsdk.api.codegen.analytics.data.esg.v1.EsgDataAPI.models.v1_provider_measure_metadata_ext import V1ProviderMeasureMetadataExt

class V1ProviderMeasureMetadata(BaseModel):
    """
    Measure dataset response to request client.
    """
    measure_code: Optional[StrictStr] = Field(None, alias="measureCode", description="Blackrock specific measure code.")
    measure_description: Optional[StrictStr] = Field(None, alias="measureDescription", description="Description of the measure.")
    external_source_code: Optional[StrictStr] = Field(None, alias="externalSourceCode", description="Vendor identifier for the measure.")
    data_type: Optional[V1DataType] = Field(None, alias="dataType")
    measure_ext: Optional[conlist(V1ProviderMeasureMetadataExt)] = Field(None, alias="measureExt")
    __properties = ["measureCode", "measureDescription", "externalSourceCode", "dataType", "measureExt"]

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
    def from_json(cls, json_str: str) -> V1ProviderMeasureMetadata:
        """Create an instance of V1ProviderMeasureMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in measure_ext (list)
        _items = []
        if self.measure_ext:
            for _item in self.measure_ext:
                if _item:
                    _items.append(_item.to_dict())
            _dict['measureExt'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ProviderMeasureMetadata:
        """Create an instance of V1ProviderMeasureMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ProviderMeasureMetadata.parse_obj(obj)

        _obj = V1ProviderMeasureMetadata.parse_obj({
            "measure_code": obj.get("measureCode"),
            "measure_description": obj.get("measureDescription"),
            "external_source_code": obj.get("externalSourceCode"),
            "data_type": obj.get("dataType"),
            "measure_ext": [V1ProviderMeasureMetadataExt.from_dict(_item) for _item in obj.get("measureExt")] if obj.get("measureExt") is not None else None
        })
        return _obj

