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

from aladdinsdk.api import AladdinAPI
from aladdinsdk.config import user_settings
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload
from aladdinsdk.common.error.asdkerrors import AsdkAdcException
from aladdinsdk.common.authentication.api import inflate_api_kwargs
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


class AdcAuthUtil():
    """
    Authentication utility to assist with ADC connections.
    Using user settings and/or user provided init params during ADCClient initialization, determines the
    right set of ADC snowflake connection parameters

    Raises:
        AsdkAdcException: If incompatible or incorrect connection parameters provided
    """

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def __init__(self, **kwargs):
        self.adc_init_kwargs = inflate_adc_kwargs(kwargs.copy())
        self._inflated_api_init_kwargs = inflate_api_kwargs(kwargs.copy())

        self.adc_conn_authenticator = self.adc_init_kwargs['adc_conn_authenticator'].lower()

        self.user_provided_oauth_access_token = self.adc_init_kwargs['adc_oauth_access_token'] \
            if 'adc_oauth_access_token' in self.adc_init_kwargs else None
        self.adc_conn_rsa_private_key_passphrase = self.adc_init_kwargs['adc_conn_rsa_private_key_passphrase'] \
            if 'adc_conn_rsa_private_key_passphrase' in self.adc_init_kwargs else None
        self.adc_conn_rsa_private_key_filepath = self.adc_init_kwargs['adc_conn_rsa_private_key_filepath'] \
            if 'adc_conn_rsa_private_key_filepath' in self.adc_init_kwargs else None
        self.adc_conn_rsa_private_key = self.adc_init_kwargs['adc_conn_rsa_private_key'] \
            if 'adc_conn_rsa_private_key' in self.adc_init_kwargs else None

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def generate_sf_connection_params(self, adc_client):
        """
        Provides a dictionary containing Snowflake connection parameters. These can be used with a python
        snowflake connector or snowflake snowpark connector.
        Currenty supports 'oauth' and 'snowflake_jwt' authentication. Defaults to oauth authenticator.

        Args:
            adc_client (_type_): ADCClient connection object this utility is part of.

        Returns:
            dict: Snowflake connection parameters
        """
        sf_connection_params = {
            'account': adc_client._account,
            'user': self._inflated_api_init_kwargs['username'],
            'role': adc_client._role,
            'warehouse': adc_client._warehouse,
            'database': adc_client._database,
            'schema': adc_client._schema,
            'session_parameters': adc_client._session_parameters
        }

        if self.adc_conn_authenticator == user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH:
            self._add_oauth_connection_params(sf_connection_params)
        elif self.adc_conn_authenticator == user_settings.CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT:
            self._add_snowflake_jwt_connection_params(sf_connection_params)

        return sf_connection_params

    def _add_oauth_connection_params(self, sf_connection_params):
        """
        Helper method for adding oauth authenticator parameters

        Args:
            sf_connection_params (_type_): _description_
        """
        sf_connection_params['authenticator'] = user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH
        if self.user_provided_oauth_access_token is not None:
            sf_connection_params['token'] = self.user_provided_oauth_access_token
        else:
            sf_connection_params['token'] = self._fetch_adc_connection_access_token_from_tokenapi()

    def _fetch_adc_connection_access_token_from_tokenapi(self):
        """
        Fetches ADC connection access token from AccessTokenService

        Args:
            adc_connection_kwargs (_type_): Connection parameters set during ADC client initialization, inflated to include API call parameters

        Raises:
            AsdkAdcException: _description_

        Returns:
            string: OAuth access token for ADC connection
        """
        token_api_instance = AladdinAPI('TokenAPI', **self._inflated_api_init_kwargs)
        generate_token_response = token_api_instance.call_api('token_api_generate_token', application_name='studio')
        if not hasattr(generate_token_response, 'access_token'):
            raise AsdkAdcException("Unable to generate ADC connection due to missing refresh_token in TokenAPI response")
        access_token_from_api = (generate_token_response.access_token).strip()
        return access_token_from_api

    def _add_snowflake_jwt_connection_params(self, sf_connection_params):
        """
        Helper method for adding snowflake_jwt authenticator parameters

        Args:
            sf_connection_params (_type_): _description_
        """
        sf_connection_params['authenticator'] = user_settings.CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT
        sf_connection_params['private_key'] = self._read_rsa_private_key()

    def _read_rsa_private_key(self):
        """
        For snowflake_jwt authenticator, determine the private key.
        If user provided, use the value as is. Else if private key filepath + passphrase provided, read content and
        generate private key.

        Raises:
            AsdkAdcException: If incorrect set of parameters provided, OR
                              If error occurs while reading private key file or reading key using filepath + passphrase combo

        Returns:
            _type_: _description_
        """
        private_key_data = None
        if self.adc_conn_rsa_private_key is not None and self.adc_conn_rsa_private_key_passphrase is not None:
            if isinstance(self.adc_conn_rsa_private_key, str):
                private_key_data = self.adc_conn_rsa_private_key.encode()
            else:
                private_key_data = self.adc_conn_rsa_private_key
        elif self.adc_conn_rsa_private_key_filepath is not None and self.adc_conn_rsa_private_key_passphrase is not None:
            # Else read private key from provided file
            try:
                with open(self.adc_conn_rsa_private_key_filepath, "rb") as key:
                    private_key_data = key.read()
            except Exception as e:
                raise AsdkAdcException(f"Unable to read private key file. Error: {e}")
        else:
            raise AsdkAdcException("Attempting to connect using RSA key pair, but private key details not configured. "
                                   "Provide passphrase with either private key or private key filepath.")

        try:
            # Private key data with passphrase provided
            p_key = serialization.load_pem_private_key(
                private_key_data,
                password=self.adc_conn_rsa_private_key_passphrase.encode() if self.adc_conn_rsa_private_key_passphrase != "" else None,
                backend=default_backend()
            )

            private_key = p_key.private_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption())

            return private_key
        except Exception as e:
            raise AsdkAdcException(f"Unable to read configured private key. Error: {e}")


def inflate_adc_kwargs(kwargs):
    """
    Given ADC initialization kwargs, fill in any missing values from user settings
    The resulting kwargs will be used to initialize the ADC client object

    Args:
        kwargs (_type_): _description_

    Returns:
        _type_: _description_
    """
    if 'adc_conn_authenticator' not in kwargs and user_settings.get_adc_conn_authenticator() is not None:
        kwargs['adc_conn_authenticator'] = user_settings.get_adc_conn_authenticator()

    if 'adc_conn_rsa_private_key_passphrase' not in kwargs and user_settings.get_adc_conn_rsa_private_key_passphrase() is not None:
        kwargs['adc_conn_rsa_private_key_passphrase'] = user_settings.get_adc_conn_rsa_private_key_passphrase()
    if 'adc_conn_rsa_private_key_filepath' not in kwargs and user_settings.get_adc_conn_rsa_private_key_filepath() is not None:
        kwargs['adc_conn_rsa_private_key_filepath'] = user_settings.get_adc_conn_rsa_private_key_filepath()
    if 'adc_conn_rsa_private_key' not in kwargs and user_settings.get_adc_conn_rsa_private_key() is not None:
        kwargs['adc_conn_rsa_private_key'] = user_settings.get_adc_conn_rsa_private_key()

    if 'adc_oauth_access_token' not in kwargs and user_settings.get_adc_conn_oauth_access_token() is not None:
        kwargs['adc_oauth_access_token'] = user_settings.get_adc_conn_oauth_access_token()

    return kwargs
