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

import hashlib
import os
from dynaconf import Dynaconf
from pathlib import Path
import logging
from functools import wraps

_logger = logging.getLogger(__name__)

# Environment variable names
ENV_VAR_ASDK_USER_CONFIG_FILE = "ASDK_USER_CONFIG_FILE"
ENV_VAR_DEFAULT_WEB_SERVER = "defaultWebServer"
ENV_VAR_NB_USER = "NB_USER"
ENV_VAR_DEFAULT_ASDK_CONFIG_FILE = "DEFAULT_ASDK_CONFIG_FILE"
DEFAULT_ASDK_CONFIG_FILE = os.environ.get(ENV_VAR_DEFAULT_ASDK_CONFIG_FILE,
                                          os.path.abspath(os.path.join(os.sep, "tmp", "asdk", "asdk_default_config.yaml")))

# Read SDK codebase settings
_CODEGEN_ALLOW_LIST_INTERNAL_CONFIG_FILE = Path(__file__).parent / "../api/codegen/codegen_allow_list.yaml"


# Decorators
def dynamic_asdk_config_reload(func):
    """
    Decorator for reloading AladdinSDK configurations dynamically by detecting changes in provided config file.
    Adding this decorator to any function will ensure any changes done to the configuration file mid-program execution,
    are loaded before executing the decorated function.
    Note: In the event configuration changes are still not loaded due to file system io latency, re-run your program

    Args:
        func (_type_): Function to be decorated
    """
    @wraps(func)
    def _handler_function(*args, **kwargs):
        global AsdkConf, config_file_md5
        _user_config_file_path = os.environ.get(ENV_VAR_ASDK_USER_CONFIG_FILE, None)

        if _user_config_file_path is not None:
            current_config_file_md5 = _get_file_md5_hash(_user_config_file_path)
            if current_config_file_md5 != config_file_md5:
                AsdkConf = Dynaconf(envvar_prefix="ASDK", load_dotenv=True,
                                    preload=_get_preloaded_config_files_to_read_list(),
                                    settings_files=_get_user_config_file(),
                                    merge_enabled=True)
                config_file_md5 = current_config_file_md5
        return func(*args, **kwargs)  # execute decorated config read helper method
    return _handler_function


# Helpers
def _get_file_md5_hash(filepath):
    file_md5_hash = None
    with open(filepath, "rb") as f:
        file_md5_hash = hashlib.sha512(f.read()).hexdigest()
    f.close()
    return file_md5_hash


def _get_user_config_file():
    user_provided_config_filepath = os.environ.get(ENV_VAR_ASDK_USER_CONFIG_FILE, None)
    if user_provided_config_filepath is not None:
        return [user_provided_config_filepath]
    else:
        return []


def _get_preloaded_config_files_to_read_list():
    preloaded_config_files = [_CODEGEN_ALLOW_LIST_INTERNAL_CONFIG_FILE]
    if DEFAULT_ASDK_CONFIG_FILE is not None and os.path.exists(DEFAULT_ASDK_CONFIG_FILE):
        preloaded_config_files.append(DEFAULT_ASDK_CONFIG_FILE)
    return preloaded_config_files


# Read user provided config file if present
config_file_md5 = None

_user_config_file_path = os.environ.get(ENV_VAR_ASDK_USER_CONFIG_FILE, None)
if _user_config_file_path is not None:
    config_file_md5 = _get_file_md5_hash(_user_config_file_path)
else:
    _logger.debug("AladdinSDK running without a user configuration file. Some of the SDK functionality may be unavailable in this case. "
                  f"Set {ENV_VAR_ASDK_USER_CONFIG_FILE} environment variable, pointing to the user configuration yaml file.")

# Initialize config settings instance
AsdkConf = Dynaconf(envvar_prefix="ASDK", load_dotenv=True,
                    preload=_get_preloaded_config_files_to_read_list(),
                    settings_files=_get_user_config_file(),
                    merge_enabled=True)

# Set default web server if not already passed in via configuration
if AsdkConf.get(ENV_VAR_DEFAULT_WEB_SERVER) is None:
    AsdkConf[ENV_VAR_DEFAULT_WEB_SERVER] = os.environ.get(ENV_VAR_DEFAULT_WEB_SERVER)
