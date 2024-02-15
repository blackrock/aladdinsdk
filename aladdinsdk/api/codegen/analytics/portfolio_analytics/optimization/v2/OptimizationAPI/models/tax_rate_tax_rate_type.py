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





class TaxRateTaxRateType(str, Enum):
    """
    - TAX_RATE_TYPE_UNSPECIFIED: value if tax_rate_type is not specified. Will default to flat  - TAX_RATE_TYPE_LONGTERM: unspecified type  - TAX_RATE_TYPE_SHORTTERM: unspecified type  - TAX_RATE_TYPE_FLAT: unspecified type
    """

    """
    allowed enum values
    """
    TAX_RATE_TYPE_UNSPECIFIED = 'TAX_RATE_TYPE_UNSPECIFIED'
    TAX_RATE_TYPE_LONGTERM = 'TAX_RATE_TYPE_LONGTERM'
    TAX_RATE_TYPE_SHORTTERM = 'TAX_RATE_TYPE_SHORTTERM'
    TAX_RATE_TYPE_FLAT = 'TAX_RATE_TYPE_FLAT'

    @classmethod
    def from_json(cls, json_str: str) -> TaxRateTaxRateType:
        """Create an instance of TaxRateTaxRateType from a JSON string"""
        return TaxRateTaxRateType(json.loads(json_str))

