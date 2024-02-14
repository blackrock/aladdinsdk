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
from pydantic import BaseModel, Field
from aladdinsdk.api.codegen.investment_operations.reference_data.broker.v1.CounterPartySettlementInstructionAPI.models.v1_counter_party_settlement_instruction import V1CounterPartySettlementInstruction

class V1ValidateCounterPartySettlementInstructionRequest(BaseModel):
    """
    The request message for CounterPartySettlementInstructionAPI.ValidateCounterPartySettlementInstruction.
    """
    counter_party_settlement_instruction: Optional[V1CounterPartySettlementInstruction] = Field(None, alias="counterPartySettlementInstruction")
    __properties = ["counterPartySettlementInstruction"]

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
    def from_json(cls, json_str: str) -> V1ValidateCounterPartySettlementInstructionRequest:
        """Create an instance of V1ValidateCounterPartySettlementInstructionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of counter_party_settlement_instruction
        if self.counter_party_settlement_instruction:
            _dict['counterPartySettlementInstruction'] = self.counter_party_settlement_instruction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1ValidateCounterPartySettlementInstructionRequest:
        """Create an instance of V1ValidateCounterPartySettlementInstructionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1ValidateCounterPartySettlementInstructionRequest.parse_obj(obj)

        _obj = V1ValidateCounterPartySettlementInstructionRequest.parse_obj({
            "counter_party_settlement_instruction": V1CounterPartySettlementInstruction.from_dict(obj.get("counterPartySettlementInstruction")) if obj.get("counterPartySettlementInstruction") is not None else None
        })
        return _obj

