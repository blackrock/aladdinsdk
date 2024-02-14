# coding: utf-8

"""
    Aladdin Corporate Action Entitlement

    API contains operations on Aladdin Corporate Action Entitlement resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.v1_cost_allocation_state import V1CostAllocationState
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.v1_election_processing_state import V1ElectionProcessingState

class V1ElectionProcessingInfo(BaseModel):
    """
    Processing information of election.This may not exist until processing is first attempted.
    """
    processing_id: StrictStr = Field(..., alias="processingId")
    election_processing_state: Optional[V1ElectionProcessingState] = Field(None, alias="electionProcessingState")
    processed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="processedAmount", description="Amount processed for this election.")
    processor: Optional[StrictStr] = Field(None, description="Name of the person who triggered the processing.")
    processed_time: Optional[datetime] = Field(None, alias="processedTime", description="Time when the election was processed.")
    modifier: Optional[StrictStr] = Field(None, description="Name of the person who last modified the election processing.")
    modified_time: Optional[datetime] = Field(None, alias="modifiedTime")
    touch_count: Optional[StrictInt] = Field(None, alias="touchCount", description="Version of election processing information.")
    cost_allocation_state: Optional[V1CostAllocationState] = Field(None, alias="costAllocationState")
    __properties = ["processingId", "electionProcessingState", "processedAmount", "processor", "processedTime", "modifier", "modifiedTime", "touchCount", "costAllocationState"]

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
    def from_json(cls, json_str: str) -> V1ElectionProcessingInfo:
        """Create an instance of V1ElectionProcessingInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ElectionProcessingInfo:
        """Create an instance of V1ElectionProcessingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ElectionProcessingInfo.parse_obj(obj)

        _obj = V1ElectionProcessingInfo.parse_obj({
            "processing_id": obj.get("processingId"),
            "election_processing_state": obj.get("electionProcessingState"),
            "processed_amount": obj.get("processedAmount"),
            "processor": obj.get("processor"),
            "processed_time": obj.get("processedTime"),
            "modifier": obj.get("modifier"),
            "modified_time": obj.get("modifiedTime"),
            "touch_count": obj.get("touchCount"),
            "cost_allocation_state": obj.get("costAllocationState")
        })
        return _obj

