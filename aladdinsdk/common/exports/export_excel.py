import json
import pandas as pd
from aladdinsdk.common.datatransformation import json_to_pandas
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from aladdinsdk.common.exports.utils import data_parse_util

def export_data(input_data, file_location, json_flattening="[*]"):
    """ 
    Given input data, file location and json flattening option, export the data to the excel file
        
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
            input_data.to_excel(file_location)

        else:
            raise AsdkExportDataException("Unsupported input data type for export")
    except (AsdkExportDataException, TypeError, AttributeError, OSError) as e:
        raise AsdkExportDataException(e)