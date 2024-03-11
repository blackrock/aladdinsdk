# coding: utf-8

"""
    Compliance Rule

    Compliance Rules are used to automatically monitor whether a fund adheres to a regulation, client mandate, or internal guideline.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1TokenSeverity(str, Enum):
    """
    Enumeration of TokenSeverity.   - TOKEN_SEVERITY_UNSPECIFIED: Unspecified.  - TOKEN_SEVERITY_WARNING: Warning.  - TOKEN_SEVERITY_RESTRICTION: Restriction.
    """

    """
    allowed enum values
    """
    TOKEN_SEVERITY_UNSPECIFIED = 'TOKEN_SEVERITY_UNSPECIFIED'
    TOKEN_SEVERITY_WARNING = 'TOKEN_SEVERITY_WARNING'
    TOKEN_SEVERITY_RESTRICTION = 'TOKEN_SEVERITY_RESTRICTION'

    @classmethod
    def from_json(cls, json_str: str) -> V1TokenSeverity:
        """Create an instance of V1TokenSeverity from a JSON string"""
        return V1TokenSeverity(json.loads(json_str))


