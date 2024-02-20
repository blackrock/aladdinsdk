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

import logging
from aladdinsdk.common.error.asdkerrors import AsdkApiException
from aladdinsdk.common.secrets import fsutil, keyringutil
from aladdinsdk.config import user_settings

_logger = logging.getLogger(__name__)


# BASIC AUTH HELPERS
def add_basic_auth_details_to_configuration(configuration, username=None, password=None):
    """
    Given an API instance configuration, add basic auth details to configuration

    Priority order:
    - Key set in API Client instantiation
    - Key set as environment variable config
    - Key set in user settings file

    Args:
        configuration (_type_): _description_

    Raises:
        AsdkApiException: _description_
    """
    if password and username is not None:
        _logger.debug("Adding basic auth details to config.")
        configuration.username = username
        configuration.password = password
    else:
        raise AsdkApiException("Incomplete Basic Auth Details provided: Missing username and/or password. "
                               "Please check AladdinSDK documentation for configuration details.")


def fetch_password_from_user_settings(password_filepath=None, encrypted_password_filepath=None, encryption_key_filepath=None):
    """
    Given password filepath (encrypted or with optional encryption key), fetch the user password

    Args:
        password_filepath (_type_): Password Filepath
        encrypted_password_filepath (_type_): Encrypted Password Filepath
        encryption_key_filepath (_type_): Encryption Key Filepath

    Raises:
        AsdkApiException: _description_
    """
    password = user_settings.get_user_password()

    if password is not None:
        _logger.debug('Providing user credential (password) from configuration file')
        return password

    if user_settings.get_run_mode() == user_settings.CONF_RUN_MODE_LOCAL:
        password = __fetch_password_in_local_mode(password_filepath, encrypted_password_filepath, encryption_key_filepath)
    elif user_settings.get_run_mode() == user_settings.CONF_RUN_MODE_ALADDIN_COMPUTE:
        password = __fetch_password_in_aladdin_compute_mode(password_filepath, encrypted_password_filepath, encryption_key_filepath)

    if password is None:
        raise AsdkApiException("Insufficient API initialization information for Basic Auth. Password not passed/configured for SDK.")

    return password


def __fetch_password_in_local_mode(password_filepath=None, encrypted_password_filepath=None, encryption_key_filepath=None):
    password = None

    password_filepath = user_settings.get_password_filepath() if password_filepath is None else password_filepath
    encrypted_password_filepath = user_settings.get_encrypted_password_filepath() if encrypted_password_filepath is None \
        else encrypted_password_filepath
    encryption_key_filepath = user_settings.get_encryption_filepath() if encryption_key_filepath is None else encryption_key_filepath

    if password_filepath is not None or encrypted_password_filepath is not None:
        password = __fetch_password_using_filepath(password_filepath=password_filepath, encrypted_password_filepath=encrypted_password_filepath,
                                                   encryption_key_filepath=encryption_key_filepath)
    else:
        _logger.debug('Providing user credential (password) from OS Credential manager using keyring')
        # check in local credential manager or prompt user
        password = keyringutil.get_user_password()
        if password is None:
            password = keyringutil.store_user_password(prompt_user=True)
    return password


def __fetch_password_in_aladdin_compute_mode(password_filepath=None, encrypted_password_filepath=None, encryption_key_filepath=None):
    password = None

    password_filepath = user_settings.get_password_filepath() if password_filepath is None else password_filepath
    encrypted_password_filepath = user_settings.get_encrypted_password_filepath() if encrypted_password_filepath is None \
        else encrypted_password_filepath
    encryption_key_filepath = user_settings.get_encryption_filepath() if encryption_key_filepath is None else encryption_key_filepath

    if password_filepath is not None and password_filepath == user_settings.ALADDIN_COMPUTE_SECRETS_KEYENC_PATH:
        # in compute mode, user password is injected from Vault as a base64 encoded file
        password = fsutil.read_base64_enc_file(password_filepath)
    elif password_filepath is not None or encrypted_password_filepath is not None:
        password = __fetch_password_using_filepath(password_filepath=password_filepath, encrypted_password_filepath=encrypted_password_filepath,
                                                   encryption_key_filepath=encryption_key_filepath)
    return password


def __fetch_password_using_filepath(password_filepath=None, encrypted_password_filepath=None, encryption_key_filepath=None):
    # read password from file
    password = None

    if encrypted_password_filepath is not None:
        password = fsutil.decrypt_file_content(filepath_to_encrypted_secret=encrypted_password_filepath,
                                               filepath_to_encryption_key=encryption_key_filepath)
    elif password_filepath is not None:
        password = fsutil.read_secret_from_file(password_filepath)

    if password is not None:
        _logger.debug('Providing user credential (password) using filepath provided in configuration file')

    return password
