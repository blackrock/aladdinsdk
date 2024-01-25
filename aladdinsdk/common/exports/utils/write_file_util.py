import pickle
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException


def write_json(file_location, json_string):
    """
    Given a file location and a json string, write the data to the file

    Args:
        file_location (_type_, required)
        json_string (_type_, required)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        with open(file_location, 'w') as file:
            file.write(json_string)
    except OSError as e:
        raise AsdkExportDataException(e)


def write_pickle(file_location, input):
    """
    Given a file location and pickle input, write the data to the file

    Args:
        file_location (_type_, required)
        input (_type_, required)

    Raises:
        AsdkExportDataException: _description_
    """
    try:
        with open(file_location, 'wb') as file:
            pickle.dump(input, file, protocol=pickle.HIGHEST_PROTOCOL)
    except OSError as e:
        raise AsdkExportDataException(e)
