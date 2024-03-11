# coding: utf-8

"""
    Aladdin Investment Target

    This service provides advance capabilities to create and manage all types of Aladdin Investment Targets and their associated subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1SubscriptionType(str, Enum):
    """
    - SUBSCRIPTION_TYPE_UNSPECIFIED: No definition present (not a valid input value)  - SUBSCRIPTION_TYPE_INFORMATIONAL: Informational  - SUBSCRIPTION_TYPE_OPERATIONAL: Operational
    """

    """
    allowed enum values
    """
    SUBSCRIPTION_TYPE_UNSPECIFIED = 'SUBSCRIPTION_TYPE_UNSPECIFIED'
    SUBSCRIPTION_TYPE_INFORMATIONAL = 'SUBSCRIPTION_TYPE_INFORMATIONAL'
    SUBSCRIPTION_TYPE_OPERATIONAL = 'SUBSCRIPTION_TYPE_OPERATIONAL'

    @classmethod
    def from_json(cls, json_str: str) -> V1SubscriptionType:
        """Create an instance of V1SubscriptionType from a JSON string"""
        return V1SubscriptionType(json.loads(json_str))


