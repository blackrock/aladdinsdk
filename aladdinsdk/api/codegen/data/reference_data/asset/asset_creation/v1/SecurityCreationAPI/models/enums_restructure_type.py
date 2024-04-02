# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsRestructureType(str, Enum):
    """
    - RESTRUCTURE_TYPE_UNSPECIFIED: UNSPECIFIED  - RESTRUCTURE_TYPE_2014_MOD_MOD: 2014_MOD_MOD  - RESTRUCTURE_TYPE_2014_MODIFIED: 2014_MODIFIED  - RESTRUCTURE_TYPE_2014_NONE: 2014_NONE  - RESTRUCTURE_TYPE_2014_OLD: 2014_OLD  - RESTRUCTURE_TYPE_MODIFIED: MODIFIED  - RESTRUCTURE_TYPE_OLD: OLD  - RESTRUCTURE_TYPE_NONE: NONE  - RESTRUCTURE_TYPE_MOD_MOD: MOD_MOD
    """

    """
    allowed enum values
    """
    RESTRUCTURE_TYPE_UNSPECIFIED = 'RESTRUCTURE_TYPE_UNSPECIFIED'
    RESTRUCTURE_TYPE_2014_MOD_MOD = 'RESTRUCTURE_TYPE_2014_MOD_MOD'
    RESTRUCTURE_TYPE_2014_MODIFIED = 'RESTRUCTURE_TYPE_2014_MODIFIED'
    RESTRUCTURE_TYPE_2014_NONE = 'RESTRUCTURE_TYPE_2014_NONE'
    RESTRUCTURE_TYPE_2014_OLD = 'RESTRUCTURE_TYPE_2014_OLD'
    RESTRUCTURE_TYPE_MODIFIED = 'RESTRUCTURE_TYPE_MODIFIED'
    RESTRUCTURE_TYPE_OLD = 'RESTRUCTURE_TYPE_OLD'
    RESTRUCTURE_TYPE_NONE = 'RESTRUCTURE_TYPE_NONE'
    RESTRUCTURE_TYPE_MOD_MOD = 'RESTRUCTURE_TYPE_MOD_MOD'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsRestructureType:
        """Create an instance of EnumsRestructureType from a JSON string"""
        return EnumsRestructureType(json.loads(json_str))

