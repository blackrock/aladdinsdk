# coding: utf-8

"""
    Aladdin Corporate Action

    A corporate action is an event triggered by a public company that changes an equity or fixed income security issued by the company. There are two main categories - Mandatory and Voluntary.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1PayoutType(str, Enum):
    """
    Enumeration of payout types.   - PAYOUT_TYPE_UNSPECIFIED: Reserved value. Default value if not specified.  - PAYOUT_TYPE_CASH: Cash.  - PAYOUT_TYPE_PRINCIPAL_CASH: Principal Cash.  - PAYOUT_TYPE_DIVIDEND: Dividend.  - PAYOUT_TYPE_INTEREST: Interest.  - PAYOUT_TYPE_SECURITY: Security.  - PAYOUT_TYPE_LONG_TERM_CAPITAL_GAIN: Long Term Capital Gain.  - PAYOUT_TYPE_SHORT_TERM_CAPITAL_GAIN: Short Term Capital Gain.  - PAYOUT_TYPE_FRANKED: Franked.  - PAYOUT_TYPE_UNFRANKED: Unfranked.  - PAYOUT_TYPE_INCOME_DISTRIBUTION: Income Distribution.  - PAYOUT_TYPE_FUND_EQUALIZATION: Fund Equalization.  - PAYOUT_TYPE_MANAGEMENT_FEES: Management Fees.  - PAYOUT_TYPE_OTHER_EXPENSES: Other Expenses.  - PAYOUT_TYPE_TAX_DEFERRED: Tax Deferred.  - PAYOUT_TYPE_TAX_EXEMPTED: Tax Exempted.  - PAYOUT_TYPE_PROPERTY_INCOME_DISTRIBUTION: Property Income Distribution.  - PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_CONCESSIONAL: Capital Gain Property - Concessional.  - PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_DISCOUNTED: Capital Gain Property - Discounted.  - PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_NON_TAX: Capital Gain Property - Non Tax.  - PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_OTHER: Capital Gain Property - Other.  - PAYOUT_TYPE_FOREIGN_INCOME: Foreign Income.  - PAYOUT_TYPE_ROYALTIES: Royalties.  - PAYOUT_TYPE_TAX_CREDIT: Tax Credit.  - PAYOUT_TYPE_PREMIUM: Premium.  - PAYOUT_TYPE_PRINCIPAL_PAYMENT: Principal Payment.  - PAYOUT_TYPE_DRIP_CASH_FOR_SECURITY: Drip Cash for Security.
    """

    """
    allowed enum values
    """
    PAYOUT_TYPE_UNSPECIFIED = 'PAYOUT_TYPE_UNSPECIFIED'
    PAYOUT_TYPE_CASH = 'PAYOUT_TYPE_CASH'
    PAYOUT_TYPE_PRINCIPAL_CASH = 'PAYOUT_TYPE_PRINCIPAL_CASH'
    PAYOUT_TYPE_DIVIDEND = 'PAYOUT_TYPE_DIVIDEND'
    PAYOUT_TYPE_INTEREST = 'PAYOUT_TYPE_INTEREST'
    PAYOUT_TYPE_SECURITY = 'PAYOUT_TYPE_SECURITY'
    PAYOUT_TYPE_LONG_TERM_CAPITAL_GAIN = 'PAYOUT_TYPE_LONG_TERM_CAPITAL_GAIN'
    PAYOUT_TYPE_SHORT_TERM_CAPITAL_GAIN = 'PAYOUT_TYPE_SHORT_TERM_CAPITAL_GAIN'
    PAYOUT_TYPE_FRANKED = 'PAYOUT_TYPE_FRANKED'
    PAYOUT_TYPE_UNFRANKED = 'PAYOUT_TYPE_UNFRANKED'
    PAYOUT_TYPE_INCOME_DISTRIBUTION = 'PAYOUT_TYPE_INCOME_DISTRIBUTION'
    PAYOUT_TYPE_FUND_EQUALIZATION = 'PAYOUT_TYPE_FUND_EQUALIZATION'
    PAYOUT_TYPE_MANAGEMENT_FEES = 'PAYOUT_TYPE_MANAGEMENT_FEES'
    PAYOUT_TYPE_OTHER_EXPENSES = 'PAYOUT_TYPE_OTHER_EXPENSES'
    PAYOUT_TYPE_TAX_DEFERRED = 'PAYOUT_TYPE_TAX_DEFERRED'
    PAYOUT_TYPE_TAX_EXEMPTED = 'PAYOUT_TYPE_TAX_EXEMPTED'
    PAYOUT_TYPE_PROPERTY_INCOME_DISTRIBUTION = 'PAYOUT_TYPE_PROPERTY_INCOME_DISTRIBUTION'
    PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_CONCESSIONAL = 'PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_CONCESSIONAL'
    PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_DISCOUNTED = 'PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_DISCOUNTED'
    PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_NON_TAX = 'PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_NON_TAX'
    PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_OTHER = 'PAYOUT_TYPE_CAPITAL_GAIN_PROPERTY_OTHER'
    PAYOUT_TYPE_FOREIGN_INCOME = 'PAYOUT_TYPE_FOREIGN_INCOME'
    PAYOUT_TYPE_ROYALTIES = 'PAYOUT_TYPE_ROYALTIES'
    PAYOUT_TYPE_TAX_CREDIT = 'PAYOUT_TYPE_TAX_CREDIT'
    PAYOUT_TYPE_PREMIUM = 'PAYOUT_TYPE_PREMIUM'
    PAYOUT_TYPE_PRINCIPAL_PAYMENT = 'PAYOUT_TYPE_PRINCIPAL_PAYMENT'
    PAYOUT_TYPE_DRIP_CASH_FOR_SECURITY = 'PAYOUT_TYPE_DRIP_CASH_FOR_SECURITY'

    @classmethod
    def from_json(cls, json_str: str) -> V1PayoutType:
        """Create an instance of V1PayoutType from a JSON string"""
        return V1PayoutType(json.loads(json_str))

