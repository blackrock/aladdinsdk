# coding: utf-8

"""
    Portfolio Optimization 2.0

    Optimize portfolio positions to maximize expected returns and minimize risk and transaction costs.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V2TransactionType(str, Enum):
    """
    - TRANSACTION_TYPE_UNSPECIFIED: value if transaction_type is not specified. All types of transactions are allowed  - TRANSACTION_TYPE_BUY_ONLY: only buys are allowed  - TRANSACTION_TYPE_SELL_ONLY: only sells are allowed  - TRANSACTION_TYPE_BUY_AND_SELL_ONLY: only buys and sells are allowed  - TRANSACTION_TYPE_BUY_AND_SHORT_ONLY: only buys and shorts are allowed  - TRANSACTION_TYPE_SELL_AND_COVER_ONLY: only sells and covers are allowed
    """

    """
    allowed enum values
    """
    TRANSACTION_TYPE_UNSPECIFIED = 'TRANSACTION_TYPE_UNSPECIFIED'
    TRANSACTION_TYPE_BUY_ONLY = 'TRANSACTION_TYPE_BUY_ONLY'
    TRANSACTION_TYPE_SELL_ONLY = 'TRANSACTION_TYPE_SELL_ONLY'
    TRANSACTION_TYPE_BUY_AND_SELL_ONLY = 'TRANSACTION_TYPE_BUY_AND_SELL_ONLY'
    TRANSACTION_TYPE_BUY_AND_SHORT_ONLY = 'TRANSACTION_TYPE_BUY_AND_SHORT_ONLY'
    TRANSACTION_TYPE_SELL_AND_COVER_ONLY = 'TRANSACTION_TYPE_SELL_AND_COVER_ONLY'

    @classmethod
    def from_json(cls, json_str: str) -> V2TransactionType:
        """Create an instance of V2TransactionType from a JSON string"""
        return V2TransactionType(json.loads(json_str))


