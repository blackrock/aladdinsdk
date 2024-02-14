# coding: utf-8

"""
    Counter Party Settlement Instruction

    API contains operations on Counter Party Settlement Instruction resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1SettlementInstructionState(str, Enum):
    """
    Enumeration of possible states of Counter Party Settlement Instructions.   - SETTLEMENT_INSTRUCTION_STATE_UNSPECIFIED: Reserved value.  - SETTLEMENT_INSTRUCTION_STATE_APPROVED: Approved cde=0.  - SETTLEMENT_INSTRUCTION_STATE_DELETED: Deleted cde=1.  - SETTLEMENT_INSTRUCTION_STATE_UNAPPROVED: Unapproved cde=3.  - SETTLEMENT_INSTRUCTION_STATE_REJECTED: Rejected cde=4.
    """

    """
    allowed enum values
    """
    SETTLEMENT_INSTRUCTION_STATE_UNSPECIFIED = 'SETTLEMENT_INSTRUCTION_STATE_UNSPECIFIED'
    SETTLEMENT_INSTRUCTION_STATE_APPROVED = 'SETTLEMENT_INSTRUCTION_STATE_APPROVED'
    SETTLEMENT_INSTRUCTION_STATE_DELETED = 'SETTLEMENT_INSTRUCTION_STATE_DELETED'
    SETTLEMENT_INSTRUCTION_STATE_UNAPPROVED = 'SETTLEMENT_INSTRUCTION_STATE_UNAPPROVED'
    SETTLEMENT_INSTRUCTION_STATE_REJECTED = 'SETTLEMENT_INSTRUCTION_STATE_REJECTED'

    @classmethod
    def from_json(cls, json_str: str) -> V1SettlementInstructionState:
        """Create an instance of V1SettlementInstructionState from a JSON string"""
        return V1SettlementInstructionState(json.loads(json_str))


