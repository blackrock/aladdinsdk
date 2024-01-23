# coding: utf-8

"""
    Research Note

    Create, modify, delete and retrieve research notes.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class V2NoteState(str, Enum):
    """
    - NOTE_STATE_UNSPECIFIED: The NoteStatus has not been specified  - NOTE_STATE_REGULAR: The note is a regular note  - NOTE_STATE_DRAFT: The note is a draft note  - NOTE_STATE_DELETED: The note is deleted  - NOTE_STATE_INVALID: The note is auto deleted and marked as invalid that deleted from Aladdin Research team either from index program or bulk load failure
    """

    """
    allowed enum values
    """
    NOTE_STATE_UNSPECIFIED = 'NOTE_STATE_UNSPECIFIED'
    NOTE_STATE_REGULAR = 'NOTE_STATE_REGULAR'
    NOTE_STATE_DRAFT = 'NOTE_STATE_DRAFT'
    NOTE_STATE_DELETED = 'NOTE_STATE_DELETED'
    NOTE_STATE_INVALID = 'NOTE_STATE_INVALID'

    @classmethod
    def from_json(cls, json_str: str) -> V2NoteState:
        """Create an instance of V2NoteState from a JSON string"""
        return V2NoteState(json.loads(json_str))


