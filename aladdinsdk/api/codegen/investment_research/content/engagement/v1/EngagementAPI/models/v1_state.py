# coding: utf-8

"""
    Engagement

    Create, modify, delete, retrieve, search and historical engagement search.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1State(str, Enum):
    """
    - STATE_UNSPECIFIED: The engagement has not been specified  - STATE_DRAFT: The engagement is a draft  - STATE_PUBLISH: The engagement is a publish  - STATE_INVALID: The engagement is auto deleted and marked as invalid that deleted from Aladdin Research team either from index program or bulk load failure
    """

    """
    allowed enum values
    """
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'
    STATE_DRAFT = 'STATE_DRAFT'
    STATE_PUBLISH = 'STATE_PUBLISH'
    STATE_INVALID = 'STATE_INVALID'

    @classmethod
    def from_json(cls, json_str: str) -> V1State:
        """Create an instance of V1State from a JSON string"""
        return V1State(json.loads(json_str))


