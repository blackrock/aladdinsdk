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

import pandas as pd
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from aladdinsdk.common.exports.utils import data_parse_util


def export_data(input_data, file_location, json_flattening="[*]"):
    """
    Given input data, file location and json flattening option, export the data to the csv file

    Args:
        input_data (_type_, required)
        file_location (_type_, required)
        json_flattening (_type_, optional)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        input_data = data_parse_util.input_data_to_dataframe(input_data, json_flattening)

        if isinstance(input_data, pd.DataFrame):
            input_data.to_csv()
            input_data.to_csv(file_location, header=True, index=True)

        else:
            raise AsdkExportDataException("Unsupported input data type for export")
    except (AsdkExportDataException, TypeError, AttributeError, OSError) as e:
        raise AsdkExportDataException(e)
