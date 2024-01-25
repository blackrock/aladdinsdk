from typing_extensions import deprecated
from aladdinsdk.common.datatransformation import json_to_pandas


@deprecated("Use json_to_pandas.convert instead")
def json_to_pandas_dataframe(json_string, json_path):
    return json_to_pandas.convert(json_string, json_path)
