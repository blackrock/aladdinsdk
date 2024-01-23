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





class EnumsState(str, Enum):
    """
    Describes the capital flow status.   - STATE_UNSPECIFIED: Represents unspecified status.  - STATE_OPEN: Represents open status.  - STATE_CANCEL: Represents cancel status.  - STATE_AUTHORIZED: Represents authorized status.  - STATE_CONFIRMED: Represents confirmed status.  - STATE_CANCEL_REQUESTED: Represents cancel requested status.
    """

    """
    allowed enum values
    """
    STATE_UNSPECIFIED = 'STATE_UNSPECIFIED'
    STATE_OPEN = 'STATE_OPEN'
    STATE_CANCEL = 'STATE_CANCEL'
    STATE_AUTHORIZED = 'STATE_AUTHORIZED'
    STATE_CONFIRMED = 'STATE_CONFIRMED'
    STATE_CANCEL_REQUESTED = 'STATE_CANCEL_REQUESTED'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsState:
        """Create an instance of EnumsState from a JSON string"""
        return EnumsState(json.loads(json_str))


