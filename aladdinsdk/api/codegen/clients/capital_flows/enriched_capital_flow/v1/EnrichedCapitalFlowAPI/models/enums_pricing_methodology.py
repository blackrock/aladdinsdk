# coding: utf-8

"""
    Capital Flows 1.0.0

    Capital flows are the cash and asset subscriptions coming into a fund and the cash and asset redemptions going out of a fund (e.g., client contributions, withdrawals, and initial funding for a portfolio). This API permits users to validate, create, update, and receive capital flows transactions and their details. User needs standard API permissison ALADDIN_API_USER to use the Capital Flows API and standard newcash permissions to perform different actions. Please refer to the Capital Flows User Guide on the client landing page for more information on newcash permission structure.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsPricingMethodology(str, Enum):
    """
    Describes the pricing methodology of capital flow record.   - PRICING_METHODOLOGY_UNSPECIFIED: Represents unspecified pricing methodology  - PRICING_METHODOLOGY_CANCELLED: Represents cancelled pricing methodology.  - PRICING_METHODOLOGY_ESTIMATE: Represents estimate pricing methodology. Estimate pricing methodology is always unpriced.  - PRICING_METHODOLOGY_UNPRICED: Represents unpriced pricing methodology .  - PRICING_METHODOLOGY_PRICED: Represents priced pricing methodology.
    """

    """
    allowed enum values
    """
    PRICING_METHODOLOGY_UNSPECIFIED = 'PRICING_METHODOLOGY_UNSPECIFIED'
    PRICING_METHODOLOGY_CANCELLED = 'PRICING_METHODOLOGY_CANCELLED'
    PRICING_METHODOLOGY_ESTIMATE = 'PRICING_METHODOLOGY_ESTIMATE'
    PRICING_METHODOLOGY_UNPRICED = 'PRICING_METHODOLOGY_UNPRICED'
    PRICING_METHODOLOGY_PRICED = 'PRICING_METHODOLOGY_PRICED'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsPricingMethodology:
        """Create an instance of EnumsPricingMethodology from a JSON string"""
        return EnumsPricingMethodology(json.loads(json_str))


