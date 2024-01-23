import json
from pandas import DataFrame
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from aladdinsdk.common.exports.utils.data_parse_util import is_data_type_primitive
from aladdinsdk.common.exports.utils.write_file_util import write_json

def export_data(input_data, file_location):
    """ 
    Given input data, file location and json flattening option, export the data to the json file
        
    Args:
        input_data (_type_, required)
        file_location (_type_, required)
        
    Raises:
        AsdkExportDataException: _description_ 
    """      
    try: 
        if isinstance(input_data, DataFrame):
            input_data.to_json(file_location, orient = 'split', compression = 'infer', index = 'true', indent = 4)
        
        else:
            if is_data_type_primitive(input_data) or isinstance(input_data, dict) or isinstance(input_data, list):
                json_string = json.dumps(input_data, indent = 4)
            elif hasattr(input_data, 'to_dict'):
                json_string = json.dumps(input_data.__dict__, indent = 4)
            write_json(file_location, json_string)

    except (TypeError, AttributeError) as e:
        raise AsdkExportDataException(e)