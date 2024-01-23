# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Tablev1NullValue(str, Enum):
    """
    - NULL_VALUE: (-- api-linter: core::0126::unspecified=disabled aip.dev/not-precedent: We need to do this because not necessary --) Set if value described is null
    """

    """
    allowed enum values
    """
    NULL_VALUE = 'NULL_VALUE'

    @classmethod
    def from_json(cls, json_str: str) -> Tablev1NullValue:
        """Create an instance of Tablev1NullValue from a JSON string"""
        return Tablev1NullValue(json.loads(json_str))


