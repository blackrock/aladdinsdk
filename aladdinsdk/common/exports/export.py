import logging
from enum import Enum
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.common.exports.utils.validate_file_util import validate_file_and_path
from aladdinsdk.common.exports import export_csv, export_excel, export_json, export_pickle

_logger = logging.getLogger(__name__)


class ExportTypes(Enum):
    csv = 1
    excel = 2
    json = 3
    pickle = 4


def get_supported_export_types():
    return ExportTypes._member_names_


@asdk_exception_handler
def export_data(input_data, file_location, export_type, overwrite_data=None):
    """
    Export input data into a file. Export type provided must be from currently supported export type list

    Args:
        input_data (Dataframe/dict/list): User input data to be exported to file
        file_location (string): Path to the file to export the input data to
        export_type (string): File type to export data to
        overwrite_data (bool): If file contains data then overwrite

    Returns:
        isSuccess (bool): Returns true if export to file is successful, else returns false
    """
    if not validate_file_and_path(file_location, overwrite_data):
        _logger.error('File and path validation failed')
        return False

    if export_type == ExportTypes.csv.name:
        export_csv.export_data(input_data, file_location)
    elif export_type == ExportTypes.excel.name:
        export_excel.export_data(input_data, file_location)
    elif export_type == ExportTypes.json.name:
        export_json.export_data(input_data, file_location)
    elif export_type == ExportTypes.pickle.name:
        export_pickle.export_data(input_data, file_location)
    else:
        _logger.error(f'Invalid export type provided. Specify one of {get_supported_export_types()}')
        return False

    _logger.info('Export data complete')
    return True
