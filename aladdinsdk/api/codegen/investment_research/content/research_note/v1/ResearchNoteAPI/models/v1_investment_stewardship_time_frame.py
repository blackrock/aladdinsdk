# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1InvestmentStewardshipTimeFrame(str, Enum):
    """
    - INVESTMENT_STEWARDSHIP_TIME_FRAME_UNSPECIFIED: Unspecified or N/A  - INVESTMENT_STEWARDSHIP_TIME_FRAME_IMMEDIATE: Immediate  - INVESTMENT_STEWARDSHIP_TIME_FRAME_SHORT_TERM: Short Term (<1 yr)  - INVESTMENT_STEWARDSHIP_TIME_FRAME_MEDIUM_TERM: Medium Term (1-2 yrs)  - INVESTMENT_STEWARDSHIP_TIME_FRAME_LONG_TERM: Long Term (2+ yrs)
    """

    """
    allowed enum values
    """
    INVESTMENT_STEWARDSHIP_TIME_FRAME_UNSPECIFIED = 'INVESTMENT_STEWARDSHIP_TIME_FRAME_UNSPECIFIED'
    INVESTMENT_STEWARDSHIP_TIME_FRAME_IMMEDIATE = 'INVESTMENT_STEWARDSHIP_TIME_FRAME_IMMEDIATE'
    INVESTMENT_STEWARDSHIP_TIME_FRAME_SHORT_TERM = 'INVESTMENT_STEWARDSHIP_TIME_FRAME_SHORT_TERM'
    INVESTMENT_STEWARDSHIP_TIME_FRAME_MEDIUM_TERM = 'INVESTMENT_STEWARDSHIP_TIME_FRAME_MEDIUM_TERM'
    INVESTMENT_STEWARDSHIP_TIME_FRAME_LONG_TERM = 'INVESTMENT_STEWARDSHIP_TIME_FRAME_LONG_TERM'

    @classmethod
    def from_json(cls, json_str: str) -> V1InvestmentStewardshipTimeFrame:
        """Create an instance of V1InvestmentStewardshipTimeFrame from a JSON string"""
        return V1InvestmentStewardshipTimeFrame(json.loads(json_str))


