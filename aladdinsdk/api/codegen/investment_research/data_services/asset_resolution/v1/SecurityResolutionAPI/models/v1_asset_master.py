# coding: utf-8

"""
    Security Resolution Service

    Service for security resolution.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1AssetMaster(str, Enum):
    """
    - ASSET_MASTER_UNSPECIFIED: UNSPECIFIED  - ASSET_MASTER_BARRA: BARRA  - ASSET_MASTER_BLOOMBERG: BLOOMBERG  - ASSET_MASTER_FACTSET: FACTSET  - ASSET_MASTER_REFINITIVE: REFINITIVE  - ASSET_MASTER_SNP: SNP
    """

    """
    allowed enum values
    """
    ASSET_MASTER_UNSPECIFIED = 'ASSET_MASTER_UNSPECIFIED'
    ASSET_MASTER_BARRA = 'ASSET_MASTER_BARRA'
    ASSET_MASTER_BLOOMBERG = 'ASSET_MASTER_BLOOMBERG'
    ASSET_MASTER_FACTSET = 'ASSET_MASTER_FACTSET'
    ASSET_MASTER_REFINITIVE = 'ASSET_MASTER_REFINITIVE'
    ASSET_MASTER_SNP = 'ASSET_MASTER_SNP'

    @classmethod
    def from_json(cls, json_str: str) -> V1AssetMaster:
        """Create an instance of V1AssetMaster from a JSON string"""
        return V1AssetMaster(json.loads(json_str))


