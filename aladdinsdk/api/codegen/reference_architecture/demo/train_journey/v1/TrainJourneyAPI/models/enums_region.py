# coding: utf-8

"""
    Train Journey

    Demonstrate feature of Aladdin Graph services using train journeys, stations and trains.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumsRegion(str, Enum):
    """
    Region is the Government Office Region (GOR) to which the station belongs.   - REGION_UNSPECIFIED: Default value  - REGION_EAST: REGION_EAST  - REGION_EAST_MIDLANDS: REGION_EAST_MIDLANDS  - REGION_LONDON: REGION_LONDON  - REGION_NORTH_EAST: REGION_NORTH_EAST  - REGION_NORTH_WEST: REGION_NORTH_WEST  - REGION_SCOTLAND: REGION_SCOTLAND  - REGION_SOUTH_EAST: REGION_SOUTH_EAST  - REGION_SOUTH_WEST: REGION_SOUTH_WEST  - REGION_WALES: REGION_WALES  - REGION_WEST_MIDLANDS: REGION_WEST_MIDLANDS  - REGION_YORKSHIRE: REGION_YORKSHIRE
    """

    """
    allowed enum values
    """
    REGION_UNSPECIFIED = 'REGION_UNSPECIFIED'
    REGION_EAST = 'REGION_EAST'
    REGION_EAST_MIDLANDS = 'REGION_EAST_MIDLANDS'
    REGION_LONDON = 'REGION_LONDON'
    REGION_NORTH_EAST = 'REGION_NORTH_EAST'
    REGION_NORTH_WEST = 'REGION_NORTH_WEST'
    REGION_SCOTLAND = 'REGION_SCOTLAND'
    REGION_SOUTH_EAST = 'REGION_SOUTH_EAST'
    REGION_SOUTH_WEST = 'REGION_SOUTH_WEST'
    REGION_WALES = 'REGION_WALES'
    REGION_WEST_MIDLANDS = 'REGION_WEST_MIDLANDS'
    REGION_YORKSHIRE = 'REGION_YORKSHIRE'

    @classmethod
    def from_json(cls, json_str: str) -> EnumsRegion:
        """Create an instance of EnumsRegion from a JSON string"""
        return EnumsRegion(json.loads(json_str))


