# coding: utf-8

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1VoluntaryMandatoryCode(str, Enum):
    """
    Enumeration of corporate action category codes.   - VOLUNTARY_MANDATORY_CODE_UNSPECIFIED: Reserved value. Default value if not specified.  - VOLUNTARY_MANDATORY_CODE_VOLUNTARY: Voluntary action.  - VOLUNTARY_MANDATORY_CODE_MANDATORY: Mandatory action.
    """

    """
    allowed enum values
    """
    VOLUNTARY_MANDATORY_CODE_UNSPECIFIED = 'VOLUNTARY_MANDATORY_CODE_UNSPECIFIED'
    VOLUNTARY_MANDATORY_CODE_VOLUNTARY = 'VOLUNTARY_MANDATORY_CODE_VOLUNTARY'
    VOLUNTARY_MANDATORY_CODE_MANDATORY = 'VOLUNTARY_MANDATORY_CODE_MANDATORY'

    @classmethod
    def from_json(cls, json_str: str) -> V1VoluntaryMandatoryCode:
        """Create an instance of V1VoluntaryMandatoryCode from a JSON string"""
        return V1VoluntaryMandatoryCode(json.loads(json_str))


