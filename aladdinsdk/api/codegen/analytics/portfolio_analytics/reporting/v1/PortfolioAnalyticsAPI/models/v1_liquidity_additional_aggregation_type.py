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





class V1LiquidityAdditionalAggregationType(str, Enum):
    """
    - LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_UNSPECIFIED: Unspecified  - LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_LONG_ONLY: Aggregation Long Only  - LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_NET_SLASH_GROSS: Aggregation Net / Gross
    """

    """
    allowed enum values
    """
    LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_UNSPECIFIED = 'LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_UNSPECIFIED'
    LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_LONG_ONLY = 'LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_LONG_ONLY'
    LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_NET_SLASH_GROSS = 'LIQUIDITY_ADDITIONAL_AGGREGATION_TYPE_NET_SLASH_GROSS'

    @classmethod
    def from_json(cls, json_str: str) -> V1LiquidityAdditionalAggregationType:
        """Create an instance of V1LiquidityAdditionalAggregationType from a JSON string"""
        return V1LiquidityAdditionalAggregationType(json.loads(json_str))

