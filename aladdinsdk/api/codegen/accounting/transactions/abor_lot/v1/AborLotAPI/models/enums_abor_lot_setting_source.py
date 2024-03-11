# coding: utf-8

"""
    Abor Lot

    This service can be used to get AborLot data.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsAborLotSettingSource(str, Enum):
    """
    - ABOR_LOT_SETTING_SOURCE_UNSPECIFIED: source unsepcified  - ABOR_LOT_SETTING_SOURCE_PORTFOLIO_DEFAULT: source is portfolio default  - ABOR_LOT_SETTING_SOURCE_ABOR_LOT_METADATA: source is abor lot metadata
    """

    """
    allowed enum values
    """
    ABOR_LOT_SETTING_SOURCE_UNSPECIFIED = 'ABOR_LOT_SETTING_SOURCE_UNSPECIFIED'
    ABOR_LOT_SETTING_SOURCE_PORTFOLIO_DEFAULT = 'ABOR_LOT_SETTING_SOURCE_PORTFOLIO_DEFAULT'
    ABOR_LOT_SETTING_SOURCE_ABOR_LOT_METADATA = 'ABOR_LOT_SETTING_SOURCE_ABOR_LOT_METADATA'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsAborLotSettingSource:
        """Create an instance of EnumsAborLotSettingSource from a JSON string"""
        return EnumsAborLotSettingSource(json.loads(json_str))


