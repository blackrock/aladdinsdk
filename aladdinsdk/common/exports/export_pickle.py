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