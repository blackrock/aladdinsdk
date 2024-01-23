# coding: utf-8

"""
    Timeseries Bulk Retrieval

    Timeseries Bulk Retrieval offers the capability to retrieve, and filter more than one timeseries at once.  # noqa: E501

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
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.timeseries_bulk_retrieval.models.v1_subject_metadata_query import V1SubjectMetadataQuery
from aladdinsdk.api.codegen.investment_research.data_services.timeseries.v1.timeseries_bulk_retrieval.models.v1_timeseries_measure_query import V1TimeseriesMeasureQuery

class V1TimeseriesMetadataQuery(BaseModel):
    """
    The message required to perform a search query.
    """
    timeseries_ids: Optional[conlist(StrictStr)] = Field(None, alias="timeseriesIds", description="This criterion specifies the id of the timeseries.  (-- api-linter: core::0124::required-reference=disabled     aip.dev/not-precedent: This is the Timseseries Metadata id --) (-- api-linter: aladdin::9016::query-message-criterion=disabled  aip.dev/not-precedent: We need to do this because number of ids  changes each time... --)")
    subject: Optional[V1SubjectMetadataQuery] = None
    measure: Optional[V1TimeseriesMeasureQuery] = None
    vendor: Optional[StrictStr] = None
    frequency: Optional[StrictStr] = Field(None, description="(-- api-linter: aladdin::0901::dictionary-message-field=disabled  aip.dev/not-precedent: We need to do this because we use our own domain defined frequencies --)")
    source: Optional[StrictStr] = None
    timeseries_type: Optional[StrictStr] = Field(None, alias="timeseriesType")
    exclude_empty: Optional[StrictBool] = Field(None, alias="excludeEmpty")
    __properties = ["timeseriesIds", "subject", "measure", "vendor", "frequency", "source", "timeseriesType", "excludeEmpty"]

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
    def from_json(cls, json_str: str) -> V1TimeseriesMetadataQuery:
        """Create an instance of V1TimeseriesMetadataQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        # override the default output from pydantic by calling `to_dict()` of measure
        if self.measure:
            _dict['measure'] = self.measure.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1TimeseriesMetadataQuery:
        """Create an instance of V1TimeseriesMetadataQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1TimeseriesMetadataQuery.parse_obj(obj)

        _obj = V1TimeseriesMetadataQuery.parse_obj({
            "timeseries_ids": obj.get("timeseriesIds"),
            "subject": V1SubjectMetadataQuery.from_dict(obj.get("subject")) if obj.get("subject") is not None else None,
            "measure": V1TimeseriesMeasureQuery.from_dict(obj.get("measure")) if obj.get("measure") is not None else None,
            "vendor": obj.get("vendor"),
            "frequency": obj.get("frequency"),
            "source": obj.get("source"),
            "timeseries_type": obj.get("timeseriesType"),
            "exclude_empty": obj.get("excludeEmpty")
        })
        return _obj

