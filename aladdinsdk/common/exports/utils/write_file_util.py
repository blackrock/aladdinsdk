"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import pickle
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException


def write_json(file_location, json_string):
    """
    Given a file location and a json string, write the data to the file

    Args:
        file_location (_type_, required)
        json_string (_type_, required)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        with open(file_location, 'w') as file:
            file.write(json_string)
    except OSError as e:
        raise AsdkExportDataException(e)


def write_pickle(file_location, input):
    """
    Given a file location and pickle input, write the data to the file

    Args:
        file_location (_type_, required)
        input (_type_, required)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        with open(file_location, 'wb') as file:
            pickle.dump(input, file, protocol=pickle.HIGHEST_PROTOCOL)
    except OSError as e:
        raise AsdkExportDataException(e)
