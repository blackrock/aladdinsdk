# coding: utf-8

"""
    Counter Party Settlement Instruction

    API contains operations on Counter Party Settlement Instruction resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.counterparty_settlement_instruction.models.v1_counter_party_settlement_instruction_query import V1CounterPartySettlementInstructionQuery

class V1FilterCounterPartySettlementInstructionsRequest(BaseModel):
    """
    The request message for CounterPartySettlementInstructionAPI.FilterCounterPartySettlementInstructions.
    """
    counterparty_settlement_instruction_query: Optional[V1CounterPartySettlementInstructionQuery] = Field(None, alias="counterpartySettlementInstructionQuery")
    page_size: Optional[StrictInt] = Field(None, alias="pageSize", description="The maximum number of CounterPartySettlementInstructions to return. The service may return fewer than this value. If unspecified i.e 0, then complete list of CounterPartySettlementInstructions will be returned.")
    page_token: Optional[StrictStr] = Field(None, alias="pageToken", description="A page token, received from a previous 'FilterCounterPartySettlementInstructions' call. Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to 'FilterCounterPartySettlementInstructions' must match the call that provided the page token.")
    __properties = ["counterpartySettlementInstructionQuery", "pageSize", "pageToken"]

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
    def from_json(cls, json_str: str) -> V1FilterCounterPartySettlementInstructionsRequest:
        """Create an instance of V1FilterCounterPartySettlementInstructionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of counterparty_settlement_instruction_query
        if self.counterparty_settlement_instruction_query:
            _dict['counterpartySettlementInstructionQuery'] = self.counterparty_settlement_instruction_query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1FilterCounterPartySettlementInstructionsRequest:
        """Create an instance of V1FilterCounterPartySettlementInstructionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1FilterCounterPartySettlementInstructionsRequest.parse_obj(obj)

        _obj = V1FilterCounterPartySettlementInstructionsRequest.parse_obj({
            "counterparty_settlement_instruction_query": V1CounterPartySettlementInstructionQuery.from_dict(obj.get("counterpartySettlementInstructionQuery")) if obj.get("counterpartySettlementInstructionQuery") is not None else None,
            "page_size": obj.get("pageSize"),
            "page_token": obj.get("pageToken")
        })
        return _obj

