# coding: utf-8

"""
    ESG Data

    The ESG Data API offers a centralized source of ESG data and meta data across multiple vendors. The API retrieves ESG data by asset and issuer from multiple vendors, providing the data in one digestible schema. Retrieve ESG data for selected assets and issuers by providing entity id, provider id, date(s) and measure name. Meta data on ESG data measures can be retrieved by selecting a provider, provider category and unique measure names. Time Series API in alpha version, changes may be made at any time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1DataType(str, Enum):
    """
    enum for measure datatypes.   - DATA_TYPE_UNSPECIFIED: Unspecified data type  - DATA_TYPE_STRING: String based data  - DATA_TYPE_NUMERIC: Numeric based data  - DATA_TYPE_DATE: Date/time data  - DATA_TYPE_INTEGER: Integer based data
    """

    """
    allowed enum values
    """
    DATA_TYPE_UNSPECIFIED = 'DATA_TYPE_UNSPECIFIED'
    DATA_TYPE_STRING = 'DATA_TYPE_STRING'
    DATA_TYPE_NUMERIC = 'DATA_TYPE_NUMERIC'
    DATA_TYPE_DATE = 'DATA_TYPE_DATE'
    DATA_TYPE_INTEGER = 'DATA_TYPE_INTEGER'

    @classmethod
    def from_json(cls, json_str: str) -> V1DataType:
        """Create an instance of V1DataType from a JSON string"""
        return V1DataType(json.loads(json_str))

