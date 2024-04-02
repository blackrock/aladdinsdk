# coding: utf-8

"""
    Positions

    API to retrieve and monitor managed positions for Start of Day Positions. Managed positions are positions enriched with additional context such as restrictions and substitutions.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1BooleanOperator(str, Enum):
    """
    - BOOLEAN_OPERATOR_UNSPECIFIED: Operator not specified  - BOOLEAN_OPERATOR_NOT: Operator not  - BOOLEAN_OPERATOR_AND: Operator and  - BOOLEAN_OPERATOR_OR: Operator or
    """

    """
    allowed enum values
    """
    BOOLEAN_OPERATOR_UNSPECIFIED = 'BOOLEAN_OPERATOR_UNSPECIFIED'
    BOOLEAN_OPERATOR_NOT = 'BOOLEAN_OPERATOR_NOT'
    BOOLEAN_OPERATOR_AND = 'BOOLEAN_OPERATOR_AND'
    BOOLEAN_OPERATOR_OR = 'BOOLEAN_OPERATOR_OR'

    @classmethod
    def from_json(cls, json_str: str) -> V1BooleanOperator:
        """Create an instance of V1BooleanOperator from a JSON string"""
        return V1BooleanOperator(json.loads(json_str))

