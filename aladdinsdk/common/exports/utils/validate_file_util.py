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

import os
import logging
from pathlib import Path
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from aladdinsdk.config.user_settings import get_overwrite_data_flag

_logger = logging.getLogger(__name__)


def validate_file_and_path(file_location, overwrite_data=None):
    """
    Given a file location, determine if the path exists, user has write perms and if the file is empty

    Args:
        file_location (_type_, required): file location
        overwrite_data (_type_, optional): overwrite data flag

    Raises:
        AsdkExportDataException: _description_

    Returns:
        bool: True if file and path validation is successful
    """
    try:
        file_name = Path(file_location)
        folder_path = os.path.dirname(file_location)
        if os.path.exists(folder_path) and os.access(folder_path, os.W_OK):
            if os.path.isfile(file_location):
                if os.stat(file_name).st_size == 0:
                    return True
                else:
                    return _validate_overwrite_data_config(overwrite_data)
            else:
                with open(file_location, 'w'):
                    return True
        else:
            raise AsdkExportDataException('Unable to validate file path and permissions')
    except OSError as e:
        raise AsdkExportDataException(e)
    except AsdkExportDataException as e:
        _logger.error('Error validating file')
        raise e


def _validate_overwrite_data_config(overwrite_data=None):
    """
    Determine the overwrite data flag value
    Method arg value overrides the user setting config

    Args:
        overwrite_data (_type_, optional): overwrite data flag

    Raises:
        AsdkExportDataException: _description_

    Returns:
        bool: overwrite data flag
    """
    if overwrite_data is not None:
        return overwrite_data
    overwrite_data_flag = get_overwrite_data_flag()
    if isinstance(overwrite_data_flag, bool):
        return overwrite_data_flag
    elif overwrite_data_flag is None:
        _logger.error('Overwrite data config not set - and file has existing data')
        return False
    else:
        raise AsdkExportDataException('Overwrite data config type incorrect - Should be boolean')
