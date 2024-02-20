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

import json
from jsonpath_ng import jsonpath, parse
import collections
import logging
import pandas as pd

from aladdinsdk.common.error.asdkerrors import AsdkTransformationException


# Conversion
def convert(json_string: str, json_path: str):
    """
    Utility to convert given json data into a pandas dataframe.

    Args:
        json_string (string): data to be converted as a json string
        json_path (string): path to flatten on during conversion

    Raises:
        AsdkTransformationException: If invalid input json provided for conversion

    Returns:
        pandas.dataframe: Json data flattened at given path
    """
    data_to_transform = None
    df_result = pd.DataFrame()

    try:
        data_to_transform = json.loads(json_string)
    except Exception as e:
        logging.error(e)
        raise AsdkTransformationException("Invalid json")

    jsonpath_expression = parse(json_path)

    token_list = jsonpath_expression.find(data_to_transform)

    for current_token in token_list:
        row = collections.defaultdict()

        full_path = _get_full_path(current_token)
        if type(current_token.value) is list:
            _convert_list_to_row(current_token, full_path, row)
        elif type(current_token.value) is not dict:
            # This is just a value in an array
            row[full_path + "[*]"] = current_token.value

        is_leaf = True
        while current_token:
            if type(current_token.value) is dict:
                full_path = _get_full_path(current_token)
                _convert_dict_to_row(current_token, full_path, is_leaf, row)
            is_leaf = False
            current_token = current_token.context
        df_row = pd.DataFrame([row])
        df_result = pd.concat([df_result, df_row], ignore_index=True)
    return df_result


def _get_full_path(current_token):
    token_parent_key_list = []
    while current_token.context:
        if type(current_token.path) is jsonpath.Fields:
            token_parent_key_list.append(str(current_token.path))
        current_token = current_token.context
    token_parent_key_list.reverse()
    token_parent_key = ".".join(token_parent_key_list)
    return token_parent_key if len(token_parent_key_list) == 0 else token_parent_key + "."


def _convert_list_to_row(current_token, full_path, row):
    i = 0
    for token_value in current_token.value:
        array_base_name = current_token.path
        row[f"{full_path}{array_base_name}_{i}"] = token_value
        i += 1


def _convert_dict_to_row(current_token, full_path, is_leaf, row):
    for token_key, token_value in current_token.value.items():
        if (type(token_value) is not dict and type(token_value) is not list) or is_leaf:
            row[full_path + token_key] = token_value


# Conversion options
def conversion_options(json_string: str):
    """
    Given a json string return a list of json paths on which the data can be flattened to tabular format for dataframe conversion.
    One of these options can be used as a parameter for the convert function.

    Args:
        json_string (string): Json string data

    Raises:
        AsdkTransformationException: If invalid input json provided for conversion

    Returns:
        List of strings: A list of options for flattening the json data
    """
    json_object = None
    options_list = []

    try:
        json_object = json.loads(json_string)
    except Exception as e:
        logging.error(e)
        raise AsdkTransformationException("Invalid json")

    _read_keys(json_object, "", options_list)
    extension = _extend_path_combination(options_list)
    options_list.insert(0, "[*]")
    for el in extension:
        _append_if_unique(options_list, el)
    return options_list


def _make_a_path_prefix(parent_key_path, do_append, options_list, suffix):
    if do_append:
        options_list.append(f"{parent_key_path}{suffix}")
        return f"{parent_key_path}."
    return parent_key_path


def _read_keys(j_object, parent_key_path, options_list):
    logging.debug(f"parent [{parent_key_path}]")
    do_append = True
    if not parent_key_path:
        do_append = False
    if hasattr(j_object, "keys") and j_object.keys():
        path_prefix = _make_a_path_prefix(parent_key_path, do_append, options_list, "")
        for k in j_object.keys():
            sub_node = j_object[k]
            _read_keys(sub_node, path_prefix + k, options_list)
    elif isinstance(j_object, collections.abc.Sequence) and (not isinstance(j_object, str)):
        path_prefix = _make_a_path_prefix(parent_key_path, do_append, options_list, ".[*]")
        for i in range(len(j_object)):
            _read_keys(j_object[i], f"{path_prefix}[{i}]", options_list)
    else:
        return


def _append_if_unique(options_list, el):
    if el not in options_list:
        options_list.append(el)


def _extend_path_combination(options_list):
    additional_arr = []
    for el in options_list:
        lst = el.split(".")
        i = 0
        pure = []
        while i < len(lst):
            if lst[i].startswith("["):
                pure.append(i)
            i = i+1
        for i in pure:
            if i > 0:
                _append_if_unique(additional_arr, ".".join(lst[:i]))
            else:
                _append_if_unique(additional_arr, lst[i])
            lst[i] = "[*]"
        _append_if_unique(additional_arr, ".".join(lst))
    return additional_arr
