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





class V1ExpiringPermissionTimeUnit(str, Enum):
    """
    - EXPIRING_PERMISSION_TIME_UNIT_UNSPECIFIED: Unspecified  - EXPIRING_PERMISSION_TIME_UNIT_DAYS: Days  - EXPIRING_PERMISSION_TIME_UNIT_WEEKS: Weeks  - EXPIRING_PERMISSION_TIME_UNIT_MONTHS: Months  - EXPIRING_PERMISSION_TIME_UNIT_FOREVER: Forever
    """

    """
    allowed enum values
    """
    EXPIRING_PERMISSION_TIME_UNIT_UNSPECIFIED = 'EXPIRING_PERMISSION_TIME_UNIT_UNSPECIFIED'
    EXPIRING_PERMISSION_TIME_UNIT_DAYS = 'EXPIRING_PERMISSION_TIME_UNIT_DAYS'
    EXPIRING_PERMISSION_TIME_UNIT_WEEKS = 'EXPIRING_PERMISSION_TIME_UNIT_WEEKS'
    EXPIRING_PERMISSION_TIME_UNIT_MONTHS = 'EXPIRING_PERMISSION_TIME_UNIT_MONTHS'
    EXPIRING_PERMISSION_TIME_UNIT_FOREVER = 'EXPIRING_PERMISSION_TIME_UNIT_FOREVER'

    @classmethod
    def from_json(cls, json_str: str) -> V1ExpiringPermissionTimeUnit:
        """Create an instance of V1ExpiringPermissionTimeUnit from a JSON string"""
        return V1ExpiringPermissionTimeUnit(json.loads(json_str))


