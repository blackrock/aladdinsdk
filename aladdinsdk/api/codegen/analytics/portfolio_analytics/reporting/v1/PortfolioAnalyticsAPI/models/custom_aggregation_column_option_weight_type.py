# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CustomAggregationColumnOptionWeightType(str, Enum):
    """
    - WEIGHT_TYPE_UNSPECIFIED: Weight Unspecified  - WEIGHT_TYPE_PORTFOLIO: Weight Type Portfolio  - WEIGHT_TYPE_BENCHMARK: Weight Type Benchmark  - WEIGHT_TYPE_ACTIVE: Weight Type Active
    """

    """
    allowed enum values
    """
    WEIGHT_TYPE_UNSPECIFIED = 'WEIGHT_TYPE_UNSPECIFIED'
    WEIGHT_TYPE_PORTFOLIO = 'WEIGHT_TYPE_PORTFOLIO'
    WEIGHT_TYPE_BENCHMARK = 'WEIGHT_TYPE_BENCHMARK'
    WEIGHT_TYPE_ACTIVE = 'WEIGHT_TYPE_ACTIVE'

    @classmethod
    def from_json(cls, json_str: str) -> CustomAggregationColumnOptionWeightType:
        """Create an instance of CustomAggregationColumnOptionWeightType from a JSON string"""
        return CustomAggregationColumnOptionWeightType(json.loads(json_str))


