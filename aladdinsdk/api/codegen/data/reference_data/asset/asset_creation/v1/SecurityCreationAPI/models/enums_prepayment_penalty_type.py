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





class EnumsPrepaymentPenaltyType(str, Enum):
    """
    - PREPAYMENT_PENALTY_TYPE_UNSPECIFIED: UNSPECIFIED  - PREPAYMENT_PENALTY_TYPE_NONE: NONE  - PREPAYMENT_PENALTY_TYPE_DECLINING_PREMIUM: DECLINING PREMIUM  - PREPAYMENT_PENALTY_TYPE_DEFEASANCE: DEFEASANCE  - PREPAYMENT_PENALTY_TYPE_PREPAYMENT_LOCKOUT: PREPAYMENT LOCKOUT  - PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE: YIELD MAINTENANCE  - PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE_CMT: YIELD MAINTENANCE CMT  - PREPAYMENT_PENALTY_TYPE_MULTIPLE_TYPES: MULTIPLE TYPES  - PREPAYMENT_PENALTY_TYPE_OTHER: OTHER
    """

    """
    allowed enum values
    """
    PREPAYMENT_PENALTY_TYPE_UNSPECIFIED = 'PREPAYMENT_PENALTY_TYPE_UNSPECIFIED'
    PREPAYMENT_PENALTY_TYPE_NONE = 'PREPAYMENT_PENALTY_TYPE_NONE'
    PREPAYMENT_PENALTY_TYPE_DECLINING_PREMIUM = 'PREPAYMENT_PENALTY_TYPE_DECLINING_PREMIUM'
    PREPAYMENT_PENALTY_TYPE_DEFEASANCE = 'PREPAYMENT_PENALTY_TYPE_DEFEASANCE'
    PREPAYMENT_PENALTY_TYPE_PREPAYMENT_LOCKOUT = 'PREPAYMENT_PENALTY_TYPE_PREPAYMENT_LOCKOUT'
    PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE = 'PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE'
    PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE_CMT = 'PREPAYMENT_PENALTY_TYPE_YIELD_MAINTENANCE_CMT'
    PREPAYMENT_PENALTY_TYPE_MULTIPLE_TYPES = 'PREPAYMENT_PENALTY_TYPE_MULTIPLE_TYPES'
    PREPAYMENT_PENALTY_TYPE_OTHER = 'PREPAYMENT_PENALTY_TYPE_OTHER'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsPrepaymentPenaltyType:
        """Create an instance of EnumsPrepaymentPenaltyType from a JSON string"""
        return EnumsPrepaymentPenaltyType(json.loads(json_str))


