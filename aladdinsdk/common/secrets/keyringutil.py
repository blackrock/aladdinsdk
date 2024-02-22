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

import importlib
import getpass
import logging
from aladdinsdk.common.blkutils.blkutils import DEFAULT_WEB_SERVER
from aladdinsdk.config import user_settings


_logger = logging.getLogger(__name__)

_keyring_available = False
_keyring = None

_asdk_user_password_service_prefix = "ASDK-PASSWORD-"

"""
keyring used to interact with OS credential manager (e.g. Keychain Access on MacOS)

Storing user password under service: 'ASDK-PASSWORD-defaultWebServer' and username: username
"""


def delete_user_password():
    service = _asdk_user_password_service_prefix + DEFAULT_WEB_SERVER
    username = user_settings.get_username()
    _delete_keyring_entry(service, username)


def store_user_password(password=None, prompt_user=False):
    service = _asdk_user_password_service_prefix + DEFAULT_WEB_SERVER
    username = user_settings.get_username()

    if (not password) or prompt_user:
        password = _prompt_passwd(service, username)

    if password is not None:
        is_pwd_set = _set_keyring_entry(service, username, password)
        if is_pwd_set:
            _logger.info(f"Password successfully stored for [username: {username} , service: {service}]")
    else:
        _logger.error(f"Failed to store password for [username: {username} , service: {service}]")

    return password


def get_user_password():
    service = _asdk_user_password_service_prefix + DEFAULT_WEB_SERVER
    username = user_settings.get_username()

    kr_password = _get_keyring_entry(service, username)

    if kr_password:
        _logger.info(f"Password found in OS Credential manager for [username: {user_settings.get_username()} , service: {service}]")
    else:
        _logger.info(f"No password found in OS Credential manager for [username: {user_settings.get_username()} , service: {service}]")

    return kr_password


# Helpers
def _delete_keyring_entry(service, username):
    if user_settings.get_run_mode() != user_settings.CONF_RUN_MODE_LOCAL:
        _logger.error("Secret management using keyring should only be used for local development.")
        return False

    if _is_keyring_available() and _keyring is not None:
        try:
            _keyring.delete_password(service, username)
        except _keyring.errors.PasswordDeleteError:
            _logger.warning(f"Attempted to delete keyring entry which does not exist: [service: {service}, username: {username}]")


def _set_keyring_entry(service, username, password):
    if user_settings.get_run_mode() != user_settings.CONF_RUN_MODE_LOCAL:
        _logger.error("Secret management using keyring should only be used for local development.")
        return False

    if _is_keyring_available() and _keyring is not None:
        try:
            _keyring.set_password(service, username, password)
            _logger.info(f"Password successfully stored for [username: {user_settings.get_username()} , service: {DEFAULT_WEB_SERVER}]")
            return True
        except _keyring.errors.PasswordSetError:
            _logger.warning(f"Unable to set keyring entry: [service: {service}, username: {username}]")
    else:
        _logger.error("Unable to set secret in keyring, 'keyring' unavailable.")
        return False


def _get_keyring_entry(service, username):
    if user_settings.get_run_mode() != user_settings.CONF_RUN_MODE_LOCAL:
        _logger.error("Secret management using keyring should only be used for local development.")
        return None

    # First check for keyring
    if _is_keyring_available() and _keyring is not None:
        return _keyring.get_password(service, username)
    else:
        _logger.error("Password not found in a credential manager, 'keyring' unavailable.")
        return None


def _prompt_passwd(service, username):
    """Prompt user to enter password

    :return: password string
    """
    passwd = None
    verify = ""

    retry_count = 3

    while (passwd != verify and retry_count > 0):
        if retry_count != 3:
            print(f"{retry_count} attempt(s) left")
        passwd = getpass.getpass(f"Enter password to be stored in OS credential manager for [username: {username} , service: {service}]: ")
        verify = getpass.getpass("Re-type password: ")
        retry_count -= 1

    if passwd == verify:
        return passwd
    else:
        return None


def _is_keyring_available():
    """Obtain reference to keyring module

    :return: keyring module reference
    """

    global _keyring_available, _keyring
    if _keyring_available:
        return _keyring_available
    else:
        try:
            _keyring = importlib.import_module("keyring")
            if _keyring.get_keyring() is not None:
                _logger.info("Local development mode. Using OS specific credential manager")
                _keyring_available = True
            else:
                _logger.error("Local development mode. OS specific credential manager cannot be used. Try importing keyring in venv.")
                _keyring_available = False
        except Exception:
            _logger.error("Local development mode. OS specific credential manager cannot be used. Try importing keyring in venv.")
            _keyring_available = False

    return _keyring_available
