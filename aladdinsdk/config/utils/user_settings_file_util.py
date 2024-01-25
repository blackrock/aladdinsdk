import os
from typing_extensions import deprecated
import yaml
from aladdinsdk.common.blkutils.blkutils import SDK_HELP_MESSAGE_SUFFIX
from aladdinsdk.config.asdkconf import AsdkConf
from aladdinsdk.config.user_settings import CONF_API_AUTH_TYPE_OAUTH, CONF_API_AUTH_TYPE_BASIC_AUTH, CONF_RUN_MODE_LOCAL
from aladdinsdk.config.user_settings import CONF_RUN_MODE_ALADDIN_COMPUTE, ALADDIN_COMPUTE_CLIENT_REFRESH_TOKEN_PATH
from aladdinsdk.config.user_settings import ALADDIN_COMPUTE_CLIENT_DETAILS_PATH, ALADDIN_COMPUTE_SECRETS_KEYENC_PATH

_ENV_VAR_NOTEBOOK_USER_NAME = "NB_USER"
_CONF_KEY_RUN_MODE = "RUN_MODE"
_CONF_KEY_API = "API"
_CONF_KEY_API_OAUTH = "OAUTH"
_CONF_KEY_API_OAUTH_CLIENT_DETAILS_FILEPATH = "CLIENT_DETAILS_FILEPATH"
_CONF_KEY_API_OAUTH_REFRESH_TOKEN_FILEPATH = "REFRESH_TOKEN_FILEPATH"
_CONF_KEY_AUTH_TYPE = "AUTH_TYPE"
_CONF_KEY_API_TOKEN = "TOKEN"
_CONF_KEY_USER_CREDENTIALS = "USER_CREDENTIALS"
_CONF_KEY_USERNAME = "USERNAME"
_CONF_KEY_PASSWORD_FILEPATH = "PASSWORD_FILEPATH"


@deprecated("Please use `print_user_config_file_template` instead.")
def create_user_config_file_template():
    print_user_config_file_template()


def print_user_config_file_template():
    """
    Construct and print a simple configuration file template to help users get started.
    This methods looks for NB_USER environment variable to deduce run mode, and presence of secret files at default locations to add as much detail
    as possible in the configuration.
    """
    _asdk_banner = """
      ___  _           _     _ _       ___________ _   __
     / _ \| |         | |   | (_)     /  ___|  _  \ | / /
    / /_\ \ | __ _  __| | __| |_ _ __ \ `--.| | | | |/ / 
    |  _  | |/ _` |/ _` |/ _` | | '_ \ `--. \ | | |    \ 
    | | | | | (_| | (_| | (_| | | | | /\__/ / |/ /| |\  \\
    \_| |_/_|\__,_|\__,_|\__,_|_|_| |_\____/|___/ \_| \_/    
    """  # noqa: W605, W291
    print(_asdk_banner)
    print(f"Creating SDK User Settings File. {SDK_HELP_MESSAGE_SUFFIX}")
    settings_data = {}

    _user_name = os.environ.get(_ENV_VAR_NOTEBOOK_USER_NAME, None)
    if _user_name is None:
        settings_data[_CONF_KEY_RUN_MODE] = CONF_RUN_MODE_LOCAL
        _user_name = _prompt_user_for_login_name()
    else:
        settings_data[_CONF_KEY_RUN_MODE] = CONF_RUN_MODE_ALADDIN_COMPUTE
    settings_data[_CONF_KEY_USER_CREDENTIALS] = {_CONF_KEY_USERNAME: _user_name}

    _set_auth_config_details(settings_data)

    _print_config_file(settings_data)


def _set_auth_config_details(settings_data):
    _basicauth_secret_exists = os.path.exists(ALADDIN_COMPUTE_SECRETS_KEYENC_PATH)
    _oauth_secret_exists = os.path.exists(ALADDIN_COMPUTE_CLIENT_REFRESH_TOKEN_PATH)

    settings_data[_CONF_KEY_API] = {}

    # Auth Params
    if _oauth_secret_exists:
        _auth_type = CONF_API_AUTH_TYPE_OAUTH
        settings_data[_CONF_KEY_API][_CONF_KEY_API_OAUTH] = {}
        settings_data[_CONF_KEY_API][_CONF_KEY_API_OAUTH][_CONF_KEY_API_OAUTH_CLIENT_DETAILS_FILEPATH] = ALADDIN_COMPUTE_CLIENT_DETAILS_PATH
        settings_data[_CONF_KEY_API][_CONF_KEY_API_OAUTH][_CONF_KEY_API_OAUTH_REFRESH_TOKEN_FILEPATH] = ALADDIN_COMPUTE_CLIENT_REFRESH_TOKEN_PATH
        print("Setting default aladdin-compute configurations for OAuth.")
    elif _basicauth_secret_exists:
        _auth_type = CONF_API_AUTH_TYPE_BASIC_AUTH
        settings_data[_CONF_KEY_USER_CREDENTIALS][_CONF_KEY_PASSWORD_FILEPATH] = ALADDIN_COMPUTE_SECRETS_KEYENC_PATH
        print("Setting default aladdin-compute configurations for Basic Auth.")
    else:
        valid_auth_type = False
        attempt_num = 0
        while not valid_auth_type:
            attempt_num = attempt_num + 1
            if attempt_num > 5:
                print("Incorrect Auth Type field set. Unable to create config file.")
                return False
            _auth_type = _prompt_user_for_auth_type()
            valid_auth_type = _auth_type in [CONF_API_AUTH_TYPE_BASIC_AUTH, CONF_API_AUTH_TYPE_OAUTH]
        print(f"{SDK_HELP_MESSAGE_SUFFIX} on additional configuration fields to be set per selected auth type.")
        if _auth_type == CONF_API_AUTH_TYPE_BASIC_AUTH:
            print(f"\tNote: {CONF_API_AUTH_TYPE_BASIC_AUTH} requires username and password combination")
        if _auth_type == CONF_API_AUTH_TYPE_OAUTH:
            print(f"\tNote: {CONF_API_AUTH_TYPE_OAUTH} requires client ID, client secret and refresh token combination")
    settings_data[_CONF_KEY_API][_CONF_KEY_AUTH_TYPE] = _auth_type

    # API Key
    api_token = _prompt_user_for_api_key()
    if api_token is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_API_TOKEN] = str(api_token)


def _print_config_file(settings_data):
    print("\n")
    print(yaml.dump(settings_data, sort_keys=False))

    print("\nFinished printing an AladdinSDK user configuration file template.")
    print("Create a configuration file and copy the template into it. As needed, make changes to add/edit configurations.")
    print("Restart kernel to ensure new configuration changes are picked.")
    print("Set the environment variable 'ASDK_USER_CONFIG_FILE' to point to the configuration file path.")
    print("To confirm configurations are picked correctly, use aladdinsdk.config.print_current_user_config()")


def _prompt_user_for_login_name():
    return input("Please enter login username: ")


def _prompt_user_for_api_key():
    return input("As part of the configuration for making API calls, and API Key is required. "
                 "Please enter a valid key registered from your profile within Studio: ")


def _prompt_user_for_auth_type():
    return input("Enter API authentication type to be used ['Basic Auth'/'OAuth']: ")


# Show settings
def print_current_user_config():
    conf_copy = AsdkConf.as_dict()
    # Hide internal settings
    conf_copy.pop('CODEGEN_API_SETTINGS')
    conf_copy.pop('LOAD_DOTENV')
    # Hide user password
    if 'USER_CREDENTIALS' in conf_copy.keys() \
       and 'PASSWORD' in conf_copy['USER_CREDENTIALS'].keys() \
       and conf_copy['USER_CREDENTIALS']['PASSWORD'] is not None:
        conf_copy['USER_CREDENTIALS']['PASSWORD'] = "".join(['*' for _ in range(len(conf_copy['USER_CREDENTIALS']['PASSWORD']))])
    _print_user_conf_helper(conf_copy)


def _print_user_conf_helper(conf_copy, indent=0):
    for key, value in conf_copy.items():
        if isinstance(value, dict):
            print(' ' * indent + str(key) + ":")
            _print_user_conf_helper(value, indent+1)
        else:
            print(' ' * indent + str(key) + ": " + str(value))
