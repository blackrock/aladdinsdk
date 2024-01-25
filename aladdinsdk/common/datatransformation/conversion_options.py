from typing_extensions import deprecated
from aladdinsdk.common.datatransformation import json_to_pandas


@deprecated("Use json_to_pandas.conversion_options instead")
def json_to_pandas_dataframe_options(json_string):
    return json_to_pandas.conversion_options(json_string)
