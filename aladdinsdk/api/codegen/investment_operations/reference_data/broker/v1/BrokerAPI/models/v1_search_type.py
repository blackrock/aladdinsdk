# coding: utf-8

"""
    Broker

    API contains operations on Broker resource.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1SearchType(str, Enum):
    """
    Represents type of search being performed.   - SEARCH_TYPE_UNSPECIFIED: The API will default to the BROKER type  - SEARCH_TYPE_BROKER: This is the default value Fields searched - brokerTicker,brokerName.  - SEARCH_TYPE_ISSUER: Fields searched - issuer.  - SEARCH_TYPE_LEI: Fields searched - legal entity identifier.
    """

    """
    allowed enum values
    """
    SEARCH_TYPE_UNSPECIFIED = 'SEARCH_TYPE_UNSPECIFIED'
    SEARCH_TYPE_BROKER = 'SEARCH_TYPE_BROKER'
    SEARCH_TYPE_ISSUER = 'SEARCH_TYPE_ISSUER'
    SEARCH_TYPE_LEI = 'SEARCH_TYPE_LEI'

    @classmethod
    def from_json(cls, json_str: str) -> V1SearchType:
        """Create an instance of V1SearchType from a JSON string"""
        return V1SearchType(json.loads(json_str))


