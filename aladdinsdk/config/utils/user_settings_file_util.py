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

from enum import Enum
import os
import yaml
from pick import pick
from cryptography.fernet import Fernet
from aladdinsdk.common.secrets import fsutil
from aladdinsdk.common.blkutils.blkutils import SDK_HELP_MESSAGE_SUFFIX
from aladdinsdk.config.asdkconf import AsdkConf
from aladdinsdk.config.user_settings import CONF_API_AUTH_TYPE_OAUTH, CONF_API_AUTH_TYPE_BASIC_AUTH, CONF_RUN_MODE_LOCAL
from aladdinsdk.config.user_settings import CONF_RUN_MODE_ALADDIN_COMPUTE
from aladdinsdk.config.user_settings import CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON, CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON
from aladdinsdk.config.user_settings import CONF_ADC_CONN_AUTHENTICATOR_OAUTH, CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT
from aladdinsdk.config.user_settings import CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN, CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS

_ENV_VAR_NOTEBOOK_USER_NAME = "NB_USER"  # For Aladdin Compute run modes

_CONF_KEY_RUN_MODE = "RUN_MODE"
_CONF_KEY_API = "API"
_CONF_KEY_OAUTH = "OAUTH"
_CONF_KEY_ACCESS_TOKEN = "ACCESS_TOKEN"
_CONF_KEY_ACCESS_TOKEN_FILEPATH = "ACCESS_TOKEN_FILEPATH"
_CONF_KEY_CLIENT_ID = "CLIENT_ID"
_CONF_KEY_CLIENT_SECRET = "CLIENT_SECRET"
_CONF_KEY_REFRESH_TOKEN = "REFRESH_TOKEN"
_CONF_KEY_CLIENT_DETAILS_FILEPATH = "CLIENT_DETAILS_FILEPATH"
_CONF_KEY_REFRESH_TOKEN_FILEPATH = "REFRESH_TOKEN_FILEPATH"
_CONF_KEY_AUTH_TYPE = "AUTH_TYPE"
_CONF_KEY_AUTH_FLOW_TYPE = "AUTH_FLOW_TYPE"
_CONF_KEY_API_TOKEN = "TOKEN"
_CONF_KEY_USER_CREDENTIALS = "USER_CREDENTIALS"
_CONF_KEY_USERNAME = "USERNAME"
_CONF_KEY_PASSWORD = "PASSWORD"
_CONF_KEY_ENCRYPTED_PASSWORD_FILEPATH = "ENCRYPTED_PASSWORD_FILEPATH"
_CONF_KEY_ENCRYPTION_FILEPATH = "ENCRYPTION_FILEPATH"
_CONF_KEY_ADC = "ADC"
_CONF_KEY_CONNECTION_TYPE = "CONNECTION_TYPE"
_CONF_KEY_CONN = "CONN"
_CONF_KEY_AUTHENTICATOR = "AUTHENTICATOR"
_CONF_KEY_RSA = "RSA"
_CONF_KEY_PRIVATE_KEY = "PRIVATE_KEY"
_CONF_KEY_PRIVATE_KEY_FILEPATH = "PRIVATE_KEY_FILEPATH"
_CONF_KEY_PRIVATE_KEY_PASSPHRASE = "PRIVATE_KEY_PASSPHRASE"
_CONF_KEY_ACCOUNT = "ACCOUNT"
_CONF_KEY_ROLE = "ROLE"
_CONF_KEY_WAREHOUSE = "WAREHOUSE"
_CONF_KEY_DATABASE = "DATABASE"
_CONF_KEY_SCHEMA = "SCHEMA"


class _OAuthSecretsMechanism(Enum):
    ProvideAccessToken = "Provide Access Token"
    ProvideAccessTokenFilepath = "Provide filepath to file containing Access Token in plain text"
    ProvideDetailsToFetchAccessToken = "Provide details to add in config file to have SDK fetch access token"
    ProvideDetailsFilepathToFetchAccessToken = "Provide filepath to files containing details SDK can use to fetch access token"


class _PasswordMechanism(Enum):
    EncryptedFile = "Encrypt and store in files"
    PlainText = "Plain text in Config file"


class _RsaKeyMechanism(Enum):
    PrivateKey = "Provide private key value"
    PassphraseAndPrivateKeyFile = "Provide private key filepath and passphrase"


def print_user_config_file_template():
    """
    Construct and print a simple configuration file template to help users get started.
    """
    create_user_config_file_template(print_only=True)


def create_user_config_file_template(print_only=False):
    """
    Construct and print/create a simple configuration file template to help users get started.
    This methods looks for NB_USER environment variable to deduce run mode, but gives users options to select from and
    build out a configuration to include base attributes that will enable users to make API/ADC calls
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
    settings_data = {}

    confirmation_resp = _read_input_or_default_str(f"Create AladdinSDK user settings file template to get started.\n{SDK_HELP_MESSAGE_SUFFIX}\n"
                                                   "This may clear console output.\n"
                                                   "Proceed? (y/n)",
                                                   default_value="y")
    if confirmation_resp.lower() == "n":
        return

    try:
        cls()
        _set_run_mode_and_username(settings_data)

        cls()
        _set_api_auth_config_details(settings_data)

        cls()
        _set_adc_auth_config_details(settings_data)

        cls()
        _print_config_file(settings_data, print_only)
    except Exception as e:
        print(f"Failed to create configuration file template. Error: {e}")


def _set_run_mode_and_username(settings_data):
    _default_index_for_run_mode_options = 0
    _env_notebook_username = os.environ.get(_ENV_VAR_NOTEBOOK_USER_NAME)
    if _env_notebook_username is not None:
        _default_index_for_run_mode_options = 1
        _username = _read_input_or_default_str(f"Enter {_CONF_KEY_USER_CREDENTIALS}.{_CONF_KEY_USERNAME} config value.",
                                               default_value=_env_notebook_username)
    else:
        _username = _read_input_or_none(f"Enter {_CONF_KEY_USER_CREDENTIALS}.{_CONF_KEY_USERNAME} config value.")

    _run_mode = _read_input_from_options(f"Enter {_CONF_KEY_RUN_MODE} config value.",
                                         options=[CONF_RUN_MODE_LOCAL, CONF_RUN_MODE_ALADDIN_COMPUTE],
                                         default_index=_default_index_for_run_mode_options)
    settings_data[_CONF_KEY_RUN_MODE] = _run_mode

    if _username is not None:
        settings_data[_CONF_KEY_USER_CREDENTIALS] = {_CONF_KEY_USERNAME: _username}


# API attributes

def _set_api_auth_config_details(settings_data):
    api_auth_type = _read_input_from_options(f"To be able to make API calls, enter {_CONF_KEY_API}.{_CONF_KEY_AUTH_TYPE} config value.",
                                             options=[None, CONF_API_AUTH_TYPE_BASIC_AUTH, CONF_API_AUTH_TYPE_OAUTH])
    if api_auth_type is None:
        return

    settings_data[_CONF_KEY_API] = {}
    settings_data[_CONF_KEY_API][_CONF_KEY_AUTH_TYPE] = api_auth_type

    if api_auth_type == CONF_API_AUTH_TYPE_BASIC_AUTH:
        _set_basic_auth_config_details(settings_data)

    if api_auth_type == CONF_API_AUTH_TYPE_OAUTH:
        _set_oauth_auth_config_details(settings_data)


def _set_basic_auth_config_details(settings_data):
    resp = _read_input_from_options("Basic Auth requires username and password and API key.\n"
                                    "Password does not need to be provided if working in 'local' mode and 'keyring' is pre-installed.\n"
                                    "Password can be provided as plain text (not recommended), or by pointing to files containing the "
                                    "encrypted password and encryption key.\n"
                                    "Select preferred mechanism",
                                    options=[_PasswordMechanism.EncryptedFile.value, _PasswordMechanism.PlainText.value])

    if resp == _PasswordMechanism.PlainText.value:
        _user_password = _read_input_or_none(f"Enter {_CONF_KEY_USER_CREDENTIALS}.{_CONF_KEY_PASSWORD} config value. "
                                             "(NOTE: Sensitive field).")
        if _user_password is not None:
            if _CONF_KEY_USER_CREDENTIALS not in settings_data:
                settings_data[_CONF_KEY_USER_CREDENTIALS] = {}
            settings_data[_CONF_KEY_USER_CREDENTIALS][_CONF_KEY_PASSWORD] = _user_password

    if resp == _PasswordMechanism.EncryptedFile.value:
        _set_basic_auth_config_details_encrypt_password(settings_data)

    cls()
    api_token = _read_input_or_none(f"Enter API key from Studio to be added to {_CONF_KEY_API}.{_CONF_KEY_API_TOKEN} config value.")
    if api_token is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_API_TOKEN] = str(api_token)


def _set_basic_auth_config_details_encrypt_password(settings_data):
    _user_password = _read_input_or_none("Enter password to encrypt.")
    if _user_password is None:
        return

    current_working_dir = os.getcwd()
    _user_password_encryption_key = _read_input_or_default_str("Enter encryption key to use.",
                                                               default_value=Fernet.generate_key())
    if type(_user_password_encryption_key) is not bytes:
        _user_password_encryption_key = _user_password_encryption_key.encode()

    _user_password_encrypted_filepath = _read_input_or_default_str("Enter filepath for storing encrypted password",
                                                                   default_value=os.path.join(os.sep, current_working_dir, "encrypted_password"))
    _user_password_encryption_key_filepath = _read_input_or_default_str("Enter filepath for storing encryption key",
                                                                        default_value=os.path.join(os.sep, current_working_dir, "encryption_key"))

    if _CONF_KEY_USER_CREDENTIALS not in settings_data:
        settings_data[_CONF_KEY_USER_CREDENTIALS] = {}

    with open(_user_password_encryption_key_filepath, 'wb') as f:
        f.write(_user_password_encryption_key)

    fsutil.store_encrypted_content_in_file(_user_password, _user_password_encrypted_filepath,
                                           filepath_to_encryption_key=_user_password_encryption_key_filepath)
    settings_data[_CONF_KEY_USER_CREDENTIALS][_CONF_KEY_ENCRYPTED_PASSWORD_FILEPATH] = _user_password_encrypted_filepath
    settings_data[_CONF_KEY_USER_CREDENTIALS][_CONF_KEY_ENCRYPTION_FILEPATH] = _user_password_encryption_key_filepath


def _set_oauth_auth_config_details(settings_data):
    selected_oauth_secret_mechanism = _read_input_from_options("OAuth requires a valid OAuth access token to make API calls.\n"
                                                               "If not available, AladdinSDK will attempt to fetch one for you provided following "
                                                               "details are configured:\n"
                                                               f"\t - Auth flow type ({CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN} or "
                                                               f"{CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS}).\n"
                                                               "\t - Client ID, Client Secret\n"
                                                               f"\t - Refresh Token (for {CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN} auth flow type)\n"
                                                               "\n"
                                                               "First, select one of",
                                                               options=[x.value for x in _OAuthSecretsMechanism])

    if selected_oauth_secret_mechanism in [_OAuthSecretsMechanism.ProvideAccessToken.value,
                                           _OAuthSecretsMechanism.ProvideAccessTokenFilepath.value]:
        _set_oauth_auth_config_details_access_token(settings_data, selected_oauth_secret_mechanism)

    if selected_oauth_secret_mechanism in [_OAuthSecretsMechanism.ProvideDetailsToFetchAccessToken.value,
                                           _OAuthSecretsMechanism.ProvideDetailsFilepathToFetchAccessToken.value]:
        _set_oauth_auth_config_details_oauth_details(settings_data, selected_oauth_secret_mechanism)


def _set_oauth_auth_config_details_access_token(settings_data, selected_oauth_secret_mechanism):
    if _CONF_KEY_OAUTH not in settings_data[_CONF_KEY_API]:
        settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH] = {}

    if selected_oauth_secret_mechanism == _OAuthSecretsMechanism.ProvideAccessToken.value:
        access_token = _read_input_or_none("Enter valid API OAuth Access Token.")
        if access_token is not None:
            settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_ACCESS_TOKEN] = access_token

    if selected_oauth_secret_mechanism == _OAuthSecretsMechanism.ProvideAccessTokenFilepath.value:
        access_token_filepath = _read_input_or_none("Enter path to file containing valid API OAuth Access Token.")
        if access_token_filepath is not None:
            settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_ACCESS_TOKEN_FILEPATH] = access_token_filepath


def _set_oauth_auth_config_details_oauth_details(settings_data, selected_oauth_secret_mechanism):
    auth_flow_type = _read_input_from_options("Select OAuth flow type",
                                              options=[CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN, CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS])
    if auth_flow_type is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_AUTH_FLOW_TYPE] = auth_flow_type

    if _CONF_KEY_OAUTH not in settings_data[_CONF_KEY_API]:
        settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH] = {}

    if selected_oauth_secret_mechanism == _OAuthSecretsMechanism.ProvideDetailsToFetchAccessToken.value:
        _set_oauth_auth_config_details_oauth_details_in_config_file(settings_data, auth_flow_type)

    if selected_oauth_secret_mechanism == _OAuthSecretsMechanism.ProvideDetailsFilepathToFetchAccessToken.value:
        _set_oauth_auth_config_details_oauth_details_filepath(settings_data, auth_flow_type)


def _set_oauth_auth_config_details_oauth_details_in_config_file(settings_data, auth_flow_type):
    client_id = _read_input_or_none(f"Enter {_CONF_KEY_API}.{_CONF_KEY_OAUTH}.{_CONF_KEY_CLIENT_ID} config value.")
    if client_id is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_CLIENT_ID] = client_id

    client_secret = _read_input_or_none(f"Enter {_CONF_KEY_API}.{_CONF_KEY_OAUTH}.{_CONF_KEY_CLIENT_SECRET} config value.")
    if client_secret is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_CLIENT_SECRET] = client_secret

    if auth_flow_type == CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN:
        refresh_token = _read_input_or_none(f"Enter {_CONF_KEY_API}.{_CONF_KEY_OAUTH}.{_CONF_KEY_REFRESH_TOKEN} config value.")
        if refresh_token is not None:
            settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_REFRESH_TOKEN] = refresh_token


def _set_oauth_auth_config_details_oauth_details_filepath(settings_data, auth_flow_type):
    client_details_filepath = _read_input_or_none(f"Enter {_CONF_KEY_API}.{_CONF_KEY_OAUTH}.{_CONF_KEY_CLIENT_DETAILS_FILEPATH} "
                                                  "config value.\n\nNote: This should be a yaml file containing the following keys:\n"
                                                  "\t - id (value is client_id)\n"
                                                  "\t - secret (value is client_secret)\n")
    if client_details_filepath is not None:
        settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_CLIENT_DETAILS_FILEPATH] = client_details_filepath

    if auth_flow_type == CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN:
        refresh_token_filepath = _read_input_or_none(f"Enter {_CONF_KEY_API}.{_CONF_KEY_OAUTH}.{_CONF_KEY_REFRESH_TOKEN_FILEPATH} "
                                                     "config value.\n\nNote: This should be a yaml file containing the following key:\n"
                                                     "\t - token (value is user's refresh_token)\n")
        if refresh_token_filepath is not None:
            settings_data[_CONF_KEY_API][_CONF_KEY_OAUTH][_CONF_KEY_REFRESH_TOKEN_FILEPATH] = refresh_token_filepath


# ADC attributes

def _set_adc_auth_config_details(settings_data):
    adc_auth_type = _read_input_from_options(f"To be able to make ADC queries, enter {_CONF_KEY_ADC}.{_CONF_KEY_CONNECTION_TYPE} config value.",
                                             options=[None,
                                                      CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON,
                                                      CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON])
    if adc_auth_type is None:
        return

    settings_data[_CONF_KEY_ADC] = {}
    settings_data[_CONF_KEY_ADC][_CONF_KEY_CONNECTION_TYPE] = adc_auth_type

    adc_conn_authenticator = _read_input_from_options(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_AUTHENTICATOR} config value.",
                                                      options=[CONF_ADC_CONN_AUTHENTICATOR_OAUTH, CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT])

    if _CONF_KEY_CONN not in settings_data[_CONF_KEY_ADC]:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN] = {}

    settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_AUTHENTICATOR] = adc_conn_authenticator

    if adc_conn_authenticator == CONF_ADC_CONN_AUTHENTICATOR_OAUTH:
        _set_adc_auth_config_details_for_oauth(settings_data)

    if adc_conn_authenticator == CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT:
        _set_adc_auth_config_details_for_snowflake_jwt(settings_data)

    cls()
    print("Additional optional ADC connection attributes.")
    adc_conn_account = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_ACCOUNT}")
    if adc_conn_account is not None:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_ACCOUNT] = adc_conn_account
    adc_conn_role = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_ROLE}")
    if adc_conn_role is not None:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_ROLE] = adc_conn_role
    adc_conn_warehouse = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_WAREHOUSE}")
    if adc_conn_warehouse is not None:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_WAREHOUSE] = adc_conn_warehouse
    adc_conn_database = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_DATABASE}")
    if adc_conn_database is not None:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_DATABASE] = adc_conn_database
    adc_conn_schema = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_SCHEMA}")
    if adc_conn_schema is not None:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_SCHEMA] = adc_conn_schema


def _set_adc_auth_config_details_for_oauth(settings_data):

    adc_oauth_access_token = _read_input_or_none(f"Enter {_CONF_KEY_ADC}.{_CONF_KEY_CONN}.{_CONF_KEY_OAUTH}.{_CONF_KEY_ACCESS_TOKEN}.\n"
                                                 "If not provided, and appropriate API auth configuration provided, "
                                                 "SDK will attempt to get token from TokenAPI\n")
    if adc_oauth_access_token is not None:
        if _CONF_KEY_OAUTH not in settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN]:
            settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_OAUTH] = {}
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_OAUTH][_CONF_KEY_ACCESS_TOKEN] = adc_oauth_access_token


def _set_adc_auth_config_details_for_snowflake_jwt(settings_data):
    if _CONF_KEY_RSA not in settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN]:
        settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_RSA] = {}

    rsa_key_option = _read_input_from_options("For snowflake_jwt / RSA Key authenticator, select one of the following.",
                                              options=[x.value for x in _RsaKeyMechanism])
    if rsa_key_option == _RsaKeyMechanism.PrivateKey.value:
        rsa_private_key = _read_input_or_none("Enter private key.")
        if rsa_private_key is not None:
            settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_RSA][_CONF_KEY_PRIVATE_KEY] = rsa_private_key

    if rsa_key_option == _RsaKeyMechanism.PassphraseAndPrivateKeyFile.value:
        rsa_private_key_filepath = _read_input_or_none("Enter private key filepath.")
        if rsa_private_key_filepath is not None:
            settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_RSA][_CONF_KEY_PRIVATE_KEY_FILEPATH] = rsa_private_key_filepath

        rsa_private_key_passphrase = _read_input_or_none("Enter private key passphrase.")
        if rsa_private_key_passphrase is not None:
            settings_data[_CONF_KEY_ADC][_CONF_KEY_CONN][_CONF_KEY_RSA][_CONF_KEY_PRIVATE_KEY_PASSPHRASE] = rsa_private_key_passphrase


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


def _print_config_file(settings_data, print_only=False):
    print("\n")
    print(yaml.dump(settings_data, sort_keys=False))

    print("\nFinished printing an AladdinSDK user configuration file template.")
    print("Create a configuration file and copy the template into it. As needed, make changes to add/edit configurations.")
    print("Restart kernel to ensure new configuration changes are picked.")
    print("Set the environment variable 'ASDK_USER_CONFIG_FILE' to point to the configuration file path.")
    print("To confirm configurations are picked correctly, use aladdinsdk.config.print_current_user_config()\n")

    if print_only:
        return

    output_config_file_path = _read_input_or_none("To write content to a file, provide yaml file path.")
    if output_config_file_path is not None:
        with open(output_config_file_path, 'w') as outfile:
            yaml.dump(settings_data, outfile, sort_keys=False)
            print(f"Config file created. Set 'ASDK_USER_CONFIG_FILE' environment variable to {os.path.abspath(output_config_file_path)}")


# Helper methods

def _read_input_or_default_str(input_prompt: str, default_value: str):
    if default_value is not None:
        input_prompt = f"{input_prompt} Press ⮐  to default to '{default_value}'."
    value_read = get_input(input_prompt)
    if value_read == "":
        value_read = default_value
    return value_read


def _read_input_from_options(input_prompt: str, options: list, default_index: int = 0):
    try:
        value_read, _ = pick(options, f"{input_prompt}: ", indicator='=>', default_index=default_index)
        return value_read
    except Exception:
        # potentially running in a notebook environment where curses based 'pick' library is not supported
        print("\n(Note: Open terminal and run 'aladdinsdk-cli' command for a better experience)")
        ind = 1
        options_with_index = {}
        for op in options:
            options_with_index[ind] = op
            ind += 1
        try:
            value_read_index = int(_read_input_or_none(f"{input_prompt}\n\nSelect index number for option:\n{options_with_index}\n "))
            return options_with_index[value_read_index]
        except Exception as e:
            print(f"\nInvalid option selected. Available options {[x for x in options_with_index.keys()]}. Exiting.")
            raise e


def _read_input_or_none(input_prompt: str):
    input_prompt = f"{input_prompt} Press ⮐  to skip"
    value_read = get_input(input_prompt)
    if value_read == "":
        value_read = None
    return value_read


def get_input(input_prompt):
    return input(f"{input_prompt}: ")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
