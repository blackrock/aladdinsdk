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





class V1LiquidityAggregationType(str, Enum):
    """
    - LIQUIDITY_AGGREGATION_TYPE_UNSPECIFIED: Unspecified  - LIQUIDITY_AGGREGATION_TYPE_NET: Aggregation Net  - LIQUIDITY_AGGREGATION_TYPE_GROSS: Aggregation Gross
    """

    """
    allowed enum values
    """
    LIQUIDITY_AGGREGATION_TYPE_UNSPECIFIED = 'LIQUIDITY_AGGREGATION_TYPE_UNSPECIFIED'
    LIQUIDITY_AGGREGATION_TYPE_NET = 'LIQUIDITY_AGGREGATION_TYPE_NET'
    LIQUIDITY_AGGREGATION_TYPE_GROSS = 'LIQUIDITY_AGGREGATION_TYPE_GROSS'

    @classmethod
    def from_json(cls, json_str: str) -> V1LiquidityAggregationType:
        """Create an instance of V1LiquidityAggregationType from a JSON string"""
        return V1LiquidityAggregationType(json.loads(json_str))

