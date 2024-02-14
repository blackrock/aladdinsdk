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





class V1Purpose(str, Enum):
    """
    Describes the Dataset level in the Dataset Hierarchy. Dataset Hierarchy definition is represented through a list of strings separated by a '.' (CATEGORY.CLASS.GROUP.DATASET).   - PURPOSE_UNSPECIFIED: Unspecified PURPOSE. When provided API will throw an error.  - PURPOSE_CATEGORY: Category indicates top level Dataset which contains set of Classes.  - PURPOSE_CLASS: Class contains set of Groups.  - PURPOSE_GROUP: Group contains set of leaf level Datasets.  - PURPOSE_DATASET: Dataset indicates a true leaf level Dataset and is the only purpose that in which Entities can be created.
    """

    """
    allowed enum values
    """
    PURPOSE_UNSPECIFIED = 'PURPOSE_UNSPECIFIED'
    PURPOSE_CATEGORY = 'PURPOSE_CATEGORY'
    PURPOSE_CLASS = 'PURPOSE_CLASS'
    PURPOSE_GROUP = 'PURPOSE_GROUP'
    PURPOSE_DATASET = 'PURPOSE_DATASET'

    @classmethod
    def from_json(cls, json_str: str) -> V1Purpose:
        """Create an instance of V1Purpose from a JSON string"""
        return V1Purpose(json.loads(json_str))


