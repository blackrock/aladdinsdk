# coding: utf-8

"""
    Principal and Interest Factor

    Principal and Interest Factors (PIFs) generally represent the amount of payment per 1000 of Original Face currency units value you currently hold in the given asset, and are used in conjunction with position data to generate cashflows. This API allows for filtering and retrieval of PIF records based on a number of criteria including assetId, dates, security groups, currency and more.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PrincipalInterestFactorState(str, Enum):
    """
    - STATE_UNSPECIFIED: Unspecified state  - STATE_PROJECTED: The calculated amount may change and is not final yet  - STATE_DONE: Calculations for this reset are complete  - STATE_ERROR: Accrual calculation failed  - STATE_FACTOR_WAIT: Calculation is incomplete due to missing Factor data  - STATE_MANUAL: Manually amended accrual values
    """

    """
    allowed enum values
    """
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'
    STATE_PROJECTED = 'STATE_PROJECTED'
    STATE_DONE = 'STATE_DONE'
    STATE_ERROR = 'STATE_ERROR'
    STATE_FACTOR_WAIT = 'STATE_FACTOR_WAIT'
    STATE_MANUAL = 'STATE_MANUAL'

    @classmethod
    def from_json(cls, json_str: str) -> PrincipalInterestFactorState:
        """Create an instance of PrincipalInterestFactorState from a JSON string"""
        return PrincipalInterestFactorState(json.loads(json_str))


