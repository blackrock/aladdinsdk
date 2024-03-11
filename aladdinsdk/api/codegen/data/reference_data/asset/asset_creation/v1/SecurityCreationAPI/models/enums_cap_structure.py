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





class EnumsCapStructure(str, Enum):
    """
    - CAP_STRUCTURE_UNSPECIFIED: UNSPECIFIED  - CAP_STRUCTURE_2_1_5: 2/1/5  - CAP_STRUCTURE_2_2_6: 2/2/6  - CAP_STRUCTURE_5_1_5: 5/1/5  - CAP_STRUCTURE_2_2_5: 2/2/5  - CAP_STRUCTURE_5_2_5: 5/2/5  - CAP_STRUCTURE_1_1_5: 1/1/5  - CAP_STRUCTURE_2_2_3: 2/2/3
    """

    """
    allowed enum values
    """
    CAP_STRUCTURE_UNSPECIFIED = 'CAP_STRUCTURE_UNSPECIFIED'
    CAP_STRUCTURE_2_1_5 = 'CAP_STRUCTURE_2_1_5'
    CAP_STRUCTURE_2_2_6 = 'CAP_STRUCTURE_2_2_6'
    CAP_STRUCTURE_5_1_5 = 'CAP_STRUCTURE_5_1_5'
    CAP_STRUCTURE_2_2_5 = 'CAP_STRUCTURE_2_2_5'
    CAP_STRUCTURE_5_2_5 = 'CAP_STRUCTURE_5_2_5'
    CAP_STRUCTURE_1_1_5 = 'CAP_STRUCTURE_1_1_5'
    CAP_STRUCTURE_2_2_3 = 'CAP_STRUCTURE_2_2_3'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsCapStructure:
        """Create an instance of EnumsCapStructure from a JSON string"""
        return EnumsCapStructure(json.loads(json_str))


