# coding: utf-8

"""
    Security Creation

    This service is used to create CDS, CDX, Equity Equity, Equity Option, Futures, FX NDF, FX SPOT, FX FWRD, FX CSWAP, FX Option, Swap, Swaption, CASH/TD, CASH/REPO, ARM/TBA and MBS/TBA securities.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsPaymentType(str, Enum):
    """
    - PAYMENT_TYPE_UNSPECIFIED: UNSPECIFIED  - PAYMENT_TYPE_DIVIDEND_COUPON_PAYMENT_DATE: DIVIDEND_COUPON_PAYMENT_DATE  - PAYMENT_TYPE_MATURITY_PAYMENT_DATE: MATURITY_PAYMENT_DATE  - PAYMENT_TYPE_PERFORMANCE_PAYMENT_DATE: PERFORMANCE_PAYMENT_DATE  - PAYMENT_TYPE_PERFORMANCE_AFTER_X_DIV_PAYMENT: PERFORMANCE_AFTER_X_DIV_PAYMENT  - PAYMENT_TYPE_PERFORMANCE_DIV_COUPON_PAYMENT_PLUS_DELAY: PERFORMANCE_DIV_COUPON_PAYMENT_PLUS_DELAY
    """

    """
    allowed enum values
    """
    PAYMENT_TYPE_UNSPECIFIED = 'PAYMENT_TYPE_UNSPECIFIED'
    PAYMENT_TYPE_DIVIDEND_COUPON_PAYMENT_DATE = 'PAYMENT_TYPE_DIVIDEND_COUPON_PAYMENT_DATE'
    PAYMENT_TYPE_MATURITY_PAYMENT_DATE = 'PAYMENT_TYPE_MATURITY_PAYMENT_DATE'
    PAYMENT_TYPE_PERFORMANCE_PAYMENT_DATE = 'PAYMENT_TYPE_PERFORMANCE_PAYMENT_DATE'
    PAYMENT_TYPE_PERFORMANCE_AFTER_X_DIV_PAYMENT = 'PAYMENT_TYPE_PERFORMANCE_AFTER_X_DIV_PAYMENT'
    PAYMENT_TYPE_PERFORMANCE_DIV_COUPON_PAYMENT_PLUS_DELAY = 'PAYMENT_TYPE_PERFORMANCE_DIV_COUPON_PAYMENT_PLUS_DELAY'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsPaymentType:
        """Create an instance of EnumsPaymentType from a JSON string"""
        return EnumsPaymentType(json.loads(json_str))

