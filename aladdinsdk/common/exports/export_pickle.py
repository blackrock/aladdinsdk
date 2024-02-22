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

from pandas import DataFrame
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from aladdinsdk.common.exports.utils.write_file_util import write_pickle


def export_data(input_data, file_location):
    """
    Given input data, file location and json flattening option, export the data to the pickle file

    Args:
        input_data (_type_, required)
        file_location (_type_, required)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        if isinstance(input_data, DataFrame):
            input_data.to_pickle(file_location)
        else:
            write_pickle(file_location, input_data)
    except (TypeError, AttributeError) as e:
        raise AsdkExportDataException(e)
