# coding: utf-8

"""
    Entity Resolution Service

    Service for entity resolution.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.investment_research.data_services.asset_resolution.v1.entity_resolution.models.v1_asset_master import V1AssetMaster

class V1FileEntityResolutionParam(BaseModel):
    """
    FileEntityResolutionParam represents parameters for resolving the entity column present inside the file.
    """
    file_name: StrictStr = Field(..., alias="fileName")
    file_loc: StrictStr = Field(..., alias="fileLoc")
    file_type: StrictStr = Field(..., alias="fileType")
    file_headers: Optional[conlist(StrictStr)] = Field(None, alias="fileHeaders")
    file_delimiter: Optional[StrictStr] = Field(None, alias="fileDelimiter")
    field_enclosed_character: Optional[StrictStr] = Field(None, alias="fieldEnclosedCharacter")
    my_date_format: Optional[StrictStr] = Field(None, alias="myDateFormat")
    my_time_format: Optional[StrictStr] = Field(None, alias="myTimeFormat")
    my_timestamp_format: Optional[StrictStr] = Field(None, alias="myTimestampFormat")
    null_if: Optional[StrictStr] = Field(None, alias="nullIf")
    skip_header_count: Optional[StrictInt] = Field(None, alias="skipHeaderCount")
    encoding_value: Optional[StrictStr] = Field(None, alias="encodingValue")
    uid: StrictStr = Field(...)
    entity_col: Optional[StrictStr] = Field(None, alias="entityCol")
    asof_date_col: Optional[StrictStr] = Field(None, alias="asofDateCol")
    uri_col: Optional[StrictStr] = Field(None, alias="uriCol")
    year_founded_col: Optional[StrictStr] = Field(None, alias="yearFoundedCol")
    phone_number_col: Optional[StrictStr] = Field(None, alias="phoneNumberCol")
    address_col: Optional[StrictStr] = Field(None, alias="addressCol")
    city_name_col: Optional[StrictStr] = Field(None, alias="cityNameCol")
    zipcode_col: Optional[StrictStr] = Field(None, alias="zipcodeCol")
    state_name_col: Optional[StrictStr] = Field(None, alias="stateNameCol")
    country_name_col: Optional[StrictStr] = Field(None, alias="countryNameCol")
    top_records_count: Optional[StrictInt] = Field(None, alias="topRecordsCount")
    asset_master: Optional[V1AssetMaster] = Field(None, alias="assetMaster")
    model_name: Optional[StrictStr] = Field(None, alias="modelName")
    model_version: Optional[StrictStr] = Field(None, alias="modelVersion")
    dataset_vendor: Optional[StrictStr] = Field(None, alias="datasetVendor")
    __properties = ["fileName", "fileLoc", "fileType", "fileHeaders", "fileDelimiter", "fieldEnclosedCharacter", "myDateFormat", "myTimeFormat", "myTimestampFormat", "nullIf", "skipHeaderCount", "encodingValue", "uid", "entityCol", "asofDateCol", "uriCol", "yearFoundedCol", "phoneNumberCol", "addressCol", "cityNameCol", "zipcodeCol", "stateNameCol", "countryNameCol", "topRecordsCount", "assetMaster", "modelName", "modelVersion", "datasetVendor"]

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
    def from_json(cls, json_str: str) -> V1FileEntityResolutionParam:
        """Create an instance of V1FileEntityResolutionParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FileEntityResolutionParam:
        """Create an instance of V1FileEntityResolutionParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FileEntityResolutionParam.parse_obj(obj)

        _obj = V1FileEntityResolutionParam.parse_obj({
            "file_name": obj.get("fileName"),
            "file_loc": obj.get("fileLoc"),
            "file_type": obj.get("fileType"),
            "file_headers": obj.get("fileHeaders"),
            "file_delimiter": obj.get("fileDelimiter"),
            "field_enclosed_character": obj.get("fieldEnclosedCharacter"),
            "my_date_format": obj.get("myDateFormat"),
            "my_time_format": obj.get("myTimeFormat"),
            "my_timestamp_format": obj.get("myTimestampFormat"),
            "null_if": obj.get("nullIf"),
            "skip_header_count": obj.get("skipHeaderCount"),
            "encoding_value": obj.get("encodingValue"),
            "uid": obj.get("uid"),
            "entity_col": obj.get("entityCol"),
            "asof_date_col": obj.get("asofDateCol"),
            "uri_col": obj.get("uriCol"),
            "year_founded_col": obj.get("yearFoundedCol"),
            "phone_number_col": obj.get("phoneNumberCol"),
            "address_col": obj.get("addressCol"),
            "city_name_col": obj.get("cityNameCol"),
            "zipcode_col": obj.get("zipcodeCol"),
            "state_name_col": obj.get("stateNameCol"),
            "country_name_col": obj.get("countryNameCol"),
            "top_records_count": obj.get("topRecordsCount"),
            "asset_master": obj.get("assetMaster"),
            "model_name": obj.get("modelName"),
            "model_version": obj.get("modelVersion"),
            "dataset_vendor": obj.get("datasetVendor")
        })
        return _obj

