# coding: utf-8

"""
    Aladdin Investment Target

    This service provides advance capabilities to create and manage all types of Aladdin Investment Targets and their associated subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1TargetThresholdType(str, Enum):
    """
    - TARGET_THRESHOLD_TYPE_UNSPECIFIED: No definition present (not a valid input value)  - TARGET_THRESHOLD_TYPE_ABSOLUTE: Absolute  - TARGET_THRESHOLD_TYPE_RELATIVE: Relative
    """

    """
    allowed enum values
    """
    TARGET_THRESHOLD_TYPE_UNSPECIFIED = 'TARGET_THRESHOLD_TYPE_UNSPECIFIED'
    TARGET_THRESHOLD_TYPE_ABSOLUTE = 'TARGET_THRESHOLD_TYPE_ABSOLUTE'
    TARGET_THRESHOLD_TYPE_RELATIVE = 'TARGET_THRESHOLD_TYPE_RELATIVE'

    @classmethod
    def from_json(cls, json_str: str) -> V1TargetThresholdType:
        """Create an instance of V1TargetThresholdType from a JSON string"""
        return V1TargetThresholdType(json.loads(json_str))


