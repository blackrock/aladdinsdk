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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.election_state import ElectionState
from aladdinsdk.api.codegen.investment_operations.asset_lifecycle.corporate_action.v1.CorporateActionEntitlementAPI.models.v1_election_processing_info import V1ElectionProcessingInfo

class V1Election(BaseModel):
    """
    Election describes the elections made for each of the corporate action entitlements as well as the information pertaining to instructing said election to the custodian. In case where an entitlement's election is split between multiple options there will be multiple elections for the same entitlement ID.
    """
    option_number: Optional[StrictInt] = Field(None, alias="optionNumber", description="Elected option number.")
    option_type: Optional[StrictStr] = Field(None, alias="optionType", description="Election option type.")
    entitled_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="entitledAmount", description="Entitlement amount at the time of election (useful for detecting stale elections).")
    elected_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="electedAmount", description="Elected amount.")
    applied_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="appliedAmount", description="Amount applied from the election (null means full elected amount is applied).")
    applied_amount_modifier: Optional[StrictStr] = Field(None, alias="appliedAmountModifier", description="User who modified applied amount.")
    election_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="electionPercentage", description="Percentage of future position changes to be applied with this option. Value between 0.0 (exclusive) and 1.0 (inclusive), e.g., 0.5 for 50 percent.")
    election_reason: Optional[StrictStr] = Field(None, alias="electionReason", description="Reason for making the election.")
    elector: Optional[StrictStr] = Field(None, description="Name of the person who made the election.")
    elected_time: Optional[datetime] = Field(None, alias="electedTime", description="Time when the election was made.")
    authorizer: Optional[StrictStr] = Field(None, description="Person that authorized election. When populated by internal Aladdin® systems this will be a username.")
    authorized_time: Optional[datetime] = Field(None, alias="authorizedTime", description="Time when the election was authorized.")
    instructed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="instructedAmount", description="Amount instructed to custodian / borrower (may differ from elected amount for operational reasons).")
    instructor: Optional[StrictStr] = Field(None, description="Person/method of making the instruction.")
    confirmer: Optional[StrictStr] = Field(None, description="Person/method of confirming the instruction.")
    election_state: Optional[ElectionState] = Field(None, alias="electionState")
    election_processing_infos: Optional[conlist(V1ElectionProcessingInfo)] = Field(None, alias="electionProcessingInfos", description="Processing information of election.This may not exist until processing is first attempted.")
    touch_count: Optional[StrictInt] = Field(None, alias="touchCount", description="Election version.")
    modifier: Optional[StrictStr] = Field(None, description="Name of the person who last modified elections.")
    modified_time: Optional[datetime] = Field(None, alias="modifiedTime")
    source_option_number: Optional[StrictInt] = Field(None, alias="sourceOptionNumber", description="Source option number that maps to the composite option number.")
    source_external_corp_act_id: Optional[StrictStr] = Field(None, alias="sourceExternalCorpActId", description="Source external corporate action Id that maps to the linked custodian event.")
    instruction_comment: Optional[StrictStr] = Field(None, alias="instructionComment", description="Special comments to be included with the election instruction.")
    bid_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="bidPrice", description="Bid Price for Dutch Auction Tenders.")
    __properties = ["optionNumber", "optionType", "entitledAmount", "electedAmount", "appliedAmount", "appliedAmountModifier", "electionPercentage", "electionReason", "elector", "electedTime", "authorizer", "authorizedTime", "instructedAmount", "instructor", "confirmer", "electionState", "electionProcessingInfos", "touchCount", "modifier", "modifiedTime", "sourceOptionNumber", "sourceExternalCorpActId", "instructionComment", "bidPrice"]

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
    def from_json(cls, json_str: str) -> V1Election:
        """Create an instance of V1Election from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in election_processing_infos (list)
        _items = []
        if self.election_processing_infos:
            for _item in self.election_processing_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['electionProcessingInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Election:
        """Create an instance of V1Election from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Election.parse_obj(obj)

        _obj = V1Election.parse_obj({
            "option_number": obj.get("optionNumber"),
            "option_type": obj.get("optionType"),
            "entitled_amount": obj.get("entitledAmount"),
            "elected_amount": obj.get("electedAmount"),
            "applied_amount": obj.get("appliedAmount"),
            "applied_amount_modifier": obj.get("appliedAmountModifier"),
            "election_percentage": obj.get("electionPercentage"),
            "election_reason": obj.get("electionReason"),
            "elector": obj.get("elector"),
            "elected_time": obj.get("electedTime"),
            "authorizer": obj.get("authorizer"),
            "authorized_time": obj.get("authorizedTime"),
            "instructed_amount": obj.get("instructedAmount"),
            "instructor": obj.get("instructor"),
            "confirmer": obj.get("confirmer"),
            "election_state": obj.get("electionState"),
            "election_processing_infos": [V1ElectionProcessingInfo.from_dict(_item) for _item in obj.get("electionProcessingInfos")] if obj.get("electionProcessingInfos") is not None else None,
            "touch_count": obj.get("touchCount"),
            "modifier": obj.get("modifier"),
            "modified_time": obj.get("modifiedTime"),
            "source_option_number": obj.get("sourceOptionNumber"),
            "source_external_corp_act_id": obj.get("sourceExternalCorpActId"),
            "instruction_comment": obj.get("instructionComment"),
            "bid_price": obj.get("bidPrice")
        })
        return _obj
