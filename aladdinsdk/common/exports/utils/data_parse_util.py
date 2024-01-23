import json
import pandas as pd
from aladdinsdk.common.datatransformation import json_to_pandas

def is_data_type_primitive(type):
    """ 
    Given an input, determine if it is a primitive data type
        
    Args:
        type (_type_, required)
        
    Returns:
        bool: True if data type is primitive
    """      
    return isinstance(type, bool) or isinstance(type, str) or isinstance(type, int) or isinstance(type, float) or isinstance(type, tuple)

def input_data_to_dataframe(input_data, json_flattening):
    """ 
    Given input data and json flattening structure, determine data type and restructure data to dataframe
    If data cannot be converted to a dataframe, it is returned as is
        
    Args:
        input_data (_type_, required)
        json_flattening (_type_, optional)
        
    Returns:
        DataFrame or dict
    """       
    if hasattr(input_data, 'to_dict') and not isinstance(input_data, pd.DataFrame):
        input_data = input_data.to_dict()
    
    if is_data_type_primitive(input_data) or isinstance(input_data, dict) or isinstance(input_data, list):
        input_data = json_to_pandas.convert(json.dumps(input_data), json_flattening)
    
    return input_data
