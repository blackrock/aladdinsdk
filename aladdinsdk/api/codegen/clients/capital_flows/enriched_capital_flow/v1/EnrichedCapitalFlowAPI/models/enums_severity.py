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





class EnumsSeverity(str, Enum):
    """
    Severity describes whether it is a warning or restriction.   - SEVERITY_UNSPECIFIED: Default value.  - SEVERITY_WARNING: Warning.  - SEVERITY_RESTRICTION: Restriction.
    """

    """
    allowed enum values
    """
    SEVERITY_UNSPECIFIED = 'SEVERITY_UNSPECIFIED'
    SEVERITY_WARNING = 'SEVERITY_WARNING'
    SEVERITY_RESTRICTION = 'SEVERITY_RESTRICTION'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsSeverity:
        """Create an instance of EnumsSeverity from a JSON string"""
        return EnumsSeverity(json.loads(json_str))


