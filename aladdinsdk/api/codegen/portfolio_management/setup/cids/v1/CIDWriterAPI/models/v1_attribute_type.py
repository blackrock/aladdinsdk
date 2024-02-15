# coding: utf-8

"""
    Custom Investment Dataset Writer

    API for writing Dataset Definitions and Entities.  _CIDS does not transform the input data in any kind. The writer of the data owns it and is responsible for this data. CIDS provides a way to ingest the custom investment data into Aladdin for usage across Portfolio Management tools._  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1AttributeType(str, Enum):
    """
    Describes AttributeType for a Schema. Default support for Basic Known DataTypes.   - ATTRIBUTE_TYPE_UNSPECIFIED: Unspecified AttributeType. This is an Error Scenario  - ATTRIBUTE_TYPE_STRING: Mentioned for Character Attribute Value field  - ATTRIBUTE_TYPE_INTEGER: Mentioned for Integer Attribute Value field  - ATTRIBUTE_TYPE_DOUBLE: Mentioned for Decimal Attribute Value field  - ATTRIBUTE_TYPE_LONG: Mentioned for Big Integer Attribute Value field  - ATTRIBUTE_TYPE_BOOLEAN: Mentioned for Boolean Attribute Value field  - ATTRIBUTE_TYPE_DATETIME: Mentioned for Datetime Attribute Value field  - ATTRIBUTE_TYPE_ENUM: Mentioned for Enum Attribute Value field
    """

    """
    allowed enum values
    """
    ATTRIBUTE_TYPE_UNSPECIFIED = 'ATTRIBUTE_TYPE_UNSPECIFIED'
    ATTRIBUTE_TYPE_STRING = 'ATTRIBUTE_TYPE_STRING'
    ATTRIBUTE_TYPE_INTEGER = 'ATTRIBUTE_TYPE_INTEGER'
    ATTRIBUTE_TYPE_DOUBLE = 'ATTRIBUTE_TYPE_DOUBLE'
    ATTRIBUTE_TYPE_LONG = 'ATTRIBUTE_TYPE_LONG'
    ATTRIBUTE_TYPE_BOOLEAN = 'ATTRIBUTE_TYPE_BOOLEAN'
    ATTRIBUTE_TYPE_DATETIME = 'ATTRIBUTE_TYPE_DATETIME'
    ATTRIBUTE_TYPE_ENUM = 'ATTRIBUTE_TYPE_ENUM'

    @classmethod
    def from_json(cls, json_str: str) -> V1AttributeType:
        """Create an instance of V1AttributeType from a JSON string"""
        return V1AttributeType(json.loads(json_str))

