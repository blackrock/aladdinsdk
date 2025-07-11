# coding: utf-8

"""
    Studio Notification

    For creating and managing Aladdin Studio notifications.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProtobufNullValue(str, Enum):
    """
    `NullValue` is a singleton enumeration to represent the null value for the `Value` type union.   The JSON representation for `NullValue` is JSON `null`.   - NULL_VALUE: Null value.
    """

    """
    allowed enum values
    """
    NULL_VALUE = 'NULL_VALUE'

    @classmethod
    def from_json(cls, json_str: str) -> ProtobufNullValue:
        """Create an instance of ProtobufNullValue from a JSON string"""
        return ProtobufNullValue(json.loads(json_str))


