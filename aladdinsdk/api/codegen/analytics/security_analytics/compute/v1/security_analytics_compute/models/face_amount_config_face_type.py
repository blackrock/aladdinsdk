# coding: utf-8

"""
    Security Analytics Compute

    Compute security level analytics, cash flows and scenario analytics with custom valuation settings.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class FaceAmountConfigFaceType(str, Enum):
    """
    - FACE_TYPE_UNSPECIFIED: Default value  - FACE_TYPE_ORIGINAL: Represents an input of Original Face  - FACE_TYPE_CURRENT: Represents an input of Current Face
    """

    """
    allowed enum values
    """
    FACE_TYPE_UNSPECIFIED = 'FACE_TYPE_UNSPECIFIED'
    FACE_TYPE_ORIGINAL = 'FACE_TYPE_ORIGINAL'
    FACE_TYPE_CURRENT = 'FACE_TYPE_CURRENT'

    @classmethod
    def from_json(cls, json_str: str) -> FaceAmountConfigFaceType:
        """Create an instance of FaceAmountConfigFaceType from a JSON string"""
        return FaceAmountConfigFaceType(json.loads(json_str))


