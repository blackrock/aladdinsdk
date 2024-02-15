# coding: utf-8

"""
    Order

    Filter, post or cancel orders. An order is a directive from a portfolio manager to the trading desk to execute a particular investment decision.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsFinancingType(str, Enum):
    """
    - FINANCING_TYPE_UNSPECIFIED: Unspecified  - FINANCING_TYPE_PHYSICAL: Physical  - FINANCING_TYPE_SYNTHETIC: Synthetic
    """

    """
    allowed enum values
    """
    FINANCING_TYPE_UNSPECIFIED = 'FINANCING_TYPE_UNSPECIFIED'
    FINANCING_TYPE_PHYSICAL = 'FINANCING_TYPE_PHYSICAL'
    FINANCING_TYPE_SYNTHETIC = 'FINANCING_TYPE_SYNTHETIC'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsFinancingType:
        """Create an instance of EnumsFinancingType from a JSON string"""
        return EnumsFinancingType(json.loads(json_str))

