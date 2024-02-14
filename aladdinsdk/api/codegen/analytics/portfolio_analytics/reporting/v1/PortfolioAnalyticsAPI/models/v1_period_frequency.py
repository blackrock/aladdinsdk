# coding: utf-8

"""
    Portfolio Analytics

    Generate Portfolio Analytics.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V1PeriodFrequency(str, Enum):
    """
    - PERIOD_FREQUENCY_UNSPECIFIED: Timeseries period frequency Unspecified  - PERIOD_FREQUENCY_DAILY: Timeseries period frequency Daily  - PERIOD_FREQUENCY_WEEKLY: Timeseries period frequency Weekly  - PERIOD_FREQUENCY_MONTH_END: Timeseries period frequency Monthly End  - PERIOD_FREQUENCY_QUARTER_END: Timeseries period frequency Quarter End  - PERIOD_FREQUENCY_YEAR_END: Timeseries period frequency Year End
    """

    """
    allowed enum values
    """
    PERIOD_FREQUENCY_UNSPECIFIED = 'PERIOD_FREQUENCY_UNSPECIFIED'
    PERIOD_FREQUENCY_DAILY = 'PERIOD_FREQUENCY_DAILY'
    PERIOD_FREQUENCY_WEEKLY = 'PERIOD_FREQUENCY_WEEKLY'
    PERIOD_FREQUENCY_MONTH_END = 'PERIOD_FREQUENCY_MONTH_END'
    PERIOD_FREQUENCY_QUARTER_END = 'PERIOD_FREQUENCY_QUARTER_END'
    PERIOD_FREQUENCY_YEAR_END = 'PERIOD_FREQUENCY_YEAR_END'

    @classmethod
    def from_json(cls, json_str: str) -> V1PeriodFrequency:
        """Create an instance of V1PeriodFrequency from a JSON string"""
        return V1PeriodFrequency(json.loads(json_str))


