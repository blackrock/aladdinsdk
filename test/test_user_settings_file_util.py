import os
from unittest import TestCase, mock
from test.resources.testutils import utils


class TestUserSettingsUtilRunModeMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_local_run_mode_no_user(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [(user_settings_file_util.CONF_RUN_MODE_LOCAL, 0)]
        mock_get_input.side_effect = ["ehunt"]
        user_settings_file_util._set_run_mode_and_username(settings_data)
        self.assertEqual(settings_data["RUN_MODE"], user_settings_file_util.CONF_RUN_MODE_LOCAL)
        self.assertEqual(settings_data['USER_CREDENTIALS']['USERNAME'], "ehunt")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.os.environ.get')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_compute_run_mode_with_user(self, mock_get_input, mock_pick, mock_os_env_get):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_os_env_get.return_value = "jbond"
        mock_pick.side_effect = [(user_settings_file_util.CONF_RUN_MODE_LOCAL, 0)]
        mock_get_input.side_effect = [""]
        user_settings_file_util._set_run_mode_and_username(settings_data)
        self.assertEqual(settings_data["RUN_MODE"], user_settings_file_util.CONF_RUN_MODE_LOCAL)
        self.assertEqual(settings_data['USER_CREDENTIALS']['USERNAME'], "jbond")


class TestUserSettingsUtilApiAuthMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    def test_no_api_conf(self, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [(None, 0)]
        user_settings_file_util._set_api_auth_config_details(settings_data)
        self.assertEqual(settings_data, settings_data)

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_basicauth_user_password(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [
            (user_settings_file_util.CONF_API_AUTH_TYPE_BASIC_AUTH, 0),
            (user_settings_file_util._PasswordMechanism.PlainText.value, 0)
        ]
        mock_get_input.side_effect = ["MockPass", "MockApiKey"]
        user_settings_file_util._set_api_auth_config_details(settings_data)
        self.assertEqual(settings_data['USER_CREDENTIALS']['PASSWORD'], 'MockPass')
        self.assertEqual(settings_data['API']['AUTH_TYPE'], 'Basic Auth')
        self.assertEqual(settings_data['API']['TOKEN'], 'MockApiKey')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_oauth_access_token(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [
            (user_settings_file_util.CONF_API_AUTH_TYPE_OAUTH, 0),
            (user_settings_file_util._OAuthSecretsMechanism.ProvideAccessToken.value, 0)
        ]
        mock_get_input.side_effect = ["MockAccessToken"]
        user_settings_file_util._set_api_auth_config_details(settings_data)
        self.assertEqual(settings_data['API']['OAUTH']['ACCESS_TOKEN'], 'MockAccessToken')


class TestUserSettingsUtilApiBasicAuthMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_user_password_to_conf(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [(user_settings_file_util._PasswordMechanism.PlainText.value, 0)]
        mock_get_input.side_effect = ["MockPass", "MockApiKey"]
        user_settings_file_util._set_basic_auth_config_details(settings_data)
        self.assertEqual(settings_data['USER_CREDENTIALS']['PASSWORD'], 'MockPass')
        self.assertEqual(settings_data['API']['TOKEN'], 'MockApiKey')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    @mock.patch('builtins.open')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.fsutil.store_encrypted_content_in_file')
    def test_add_encrypted_password_filepath(self, mock_fs_util, mock_open, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [(user_settings_file_util._PasswordMechanism.EncryptedFile.value, 0)]
        mock_get_input.side_effect = ["MockPass", "", "MockPassFilePath", "MockEncKeyFilepath", "MockApiKey"]
        user_settings_file_util._set_basic_auth_config_details(settings_data)
        mock_open.assert_called_with("MockEncKeyFilepath", "wb")
        mock_fs_util.assert_called_with("MockPass", "MockPassFilePath", filepath_to_encryption_key="MockEncKeyFilepath")
        self.assertEqual(settings_data['USER_CREDENTIALS']['ENCRYPTED_PASSWORD_FILEPATH'], 'MockPassFilePath')
        self.assertEqual(settings_data['USER_CREDENTIALS']['ENCRYPTION_FILEPATH'], 'MockEncKeyFilepath')
        self.assertEqual(settings_data['API']['TOKEN'], 'MockApiKey')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    @mock.patch('builtins.open')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.fsutil.store_encrypted_content_in_file')
    def test_add_encrypted_password_filepath_user_provided_key(self, mock_fs_util, mock_open, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [(user_settings_file_util._PasswordMechanism.EncryptedFile.value, 0)]
        mock_get_input.side_effect = ["MockPass", "MockEncryptionKey", "MockPassFilePath", "MockEncKeyFilepath", "MockApiKey"]
        user_settings_file_util._set_basic_auth_config_details(settings_data)
        mock_open.assert_called_with("MockEncKeyFilepath", "wb")
        mock_fs_util.assert_called_with("MockPass", "MockPassFilePath", filepath_to_encryption_key="MockEncKeyFilepath")
        self.assertEqual(settings_data['USER_CREDENTIALS']['ENCRYPTED_PASSWORD_FILEPATH'], 'MockPassFilePath')
        self.assertEqual(settings_data['USER_CREDENTIALS']['ENCRYPTION_FILEPATH'], 'MockEncKeyFilepath')
        self.assertEqual(settings_data['API']['TOKEN'], 'MockApiKey')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    @mock.patch('builtins.open')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.fsutil.store_encrypted_content_in_file')
    def test_add_encrypted_password_filepath_skipped(self, mock_fs_util, mock_open, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [(user_settings_file_util._PasswordMechanism.EncryptedFile.value, 0)]
        mock_get_input.side_effect = ["", "MockApiKey"]
        user_settings_file_util._set_basic_auth_config_details(settings_data)
        self.assertEqual(settings_data['API']['TOKEN'], 'MockApiKey')


class TestUserSettingsUtilApiOAuthMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_pick_mechanism_access_token(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [(user_settings_file_util._OAuthSecretsMechanism.ProvideAccessToken.value, 0)]
        mock_get_input.side_effect = ["MockAccessToken"]
        user_settings_file_util._set_oauth_auth_config_details(settings_data)
        self.assertEqual(settings_data['API']['OAUTH']['ACCESS_TOKEN'], 'MockAccessToken')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_pick_mechanism_client_details(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {}
        }
        mock_pick.side_effect = [
            (user_settings_file_util._OAuthSecretsMechanism.RefreshTokenFlow.value, 0)
        ]
        mock_get_input.side_effect = ["MockClientId", "MockClientSecret", "MockRefreshToken"]
        user_settings_file_util._set_oauth_auth_config_details(settings_data)
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_ID'], 'MockClientId')
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_SECRET'], 'MockClientSecret')
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN'], 'MockRefreshToken')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_access_token(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockAccessToken"]
        user_settings_file_util._set_oauth_auth_config_details_access_token(settings_data,
                                                                            user_settings_file_util._OAuthSecretsMechanism.ProvideAccessToken.value)
        self.assertEqual(settings_data['API']['OAUTH']['ACCESS_TOKEN'], 'MockAccessToken')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_access_token_filepath(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockAccessTokenFilepath"]
        user_settings_file_util._set_oauth_auth_config_details_access_token(settings_data,
                                                                            user_settings_file_util
                                                                            ._OAuthSecretsMechanism.ProvideAccessTokenFilepath.value)
        self.assertEqual(settings_data['API']['OAUTH']['ACCESS_TOKEN_FILEPATH'], 'MockAccessTokenFilepath')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_pick.side_effect = [("refresh_token", 0)]
        mock_get_input.side_effect = ["MockClientId", "MockClientSecret", "MockRefreshToken"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details(settings_data,
                                                                             user_settings_file_util._OAuthSecretsMechanism.RefreshTokenFlow.value)
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_ID'], 'MockClientId')
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_SECRET'], 'MockClientSecret')
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN'], 'MockRefreshToken')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_filepaths(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_pick.side_effect = [("refresh_token", 0)]
        mock_get_input.side_effect = ["MockClientDetailsFilepath", "MockRefreshTokenFilepath"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details(settings_data,
                                                                             user_settings_file_util._OAuthSecretsMechanism.RefreshTokenFlowFilepath.value)
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_DETAILS_FILEPATH'], 'MockClientDetailsFilepath')
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN_FILEPATH'], 'MockRefreshTokenFilepath')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_to_settings_client_credentials(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockClientId", "MockClientSecret"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details_in_config_file(settings_data, "client_credentials")
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_ID'], 'MockClientId')
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_SECRET'], 'MockClientSecret')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_to_settings_refresh_token(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockClientId", "MockClientSecret", "MockRefreshToken"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details_in_config_file(settings_data, "refresh_token")
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_ID'], 'MockClientId')
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_SECRET'], 'MockClientSecret')
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN'], 'MockRefreshToken')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_client_creds(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockClientDetailsFilepath"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details_filepath(settings_data, "client_credentials")
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_DETAILS_FILEPATH'], 'MockClientDetailsFilepath')

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_api_oauth_config_details_refresh_token(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        mock_get_input.side_effect = ["MockClientDetailsFilepath", "MockRefreshTokenFilepath"]
        user_settings_file_util._set_oauth_auth_config_details_oauth_details_filepath(settings_data, "refresh_token")
        self.assertEqual(settings_data['API']['OAUTH']['CLIENT_DETAILS_FILEPATH'], 'MockClientDetailsFilepath')
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN_FILEPATH'], 'MockRefreshTokenFilepath')


class TestUserSettingsUtilAdcMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_oauth_config_none(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [(None, 0)]
        user_settings_file_util._set_adc_auth_config_details(settings_data)
        self.assertEqual(settings_data, settings_data)

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_oauth_config(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [("snowflake-connector-python", 1), ("oauth", 0)]
        mock_get_input.side_effect = ["MockAccessToken", "", "", "", "", ""]
        user_settings_file_util._set_adc_auth_config_details(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['OAUTH']['ACCESS_TOKEN'], "MockAccessToken")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_oauth_config_rsa(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [("snowflake-connector-python", 1), ("snowflake_jwt", 0), ("Provide private key value", 0)]
        mock_get_input.side_effect = ["MockPrivateKey", "", "", "", "", ""]
        user_settings_file_util._set_adc_auth_config_details(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['RSA']['PRIVATE_KEY'], "MockPrivateKey")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_oauth_config_optional_conn_attributes(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {}
        mock_pick.side_effect = [("snowflake-connector-python", 1), ("oauth", 0), ("Provide private key value", 0)]
        mock_get_input.side_effect = ["MockAccessToken", "MockAccount", "MockRole", "MockWarehouse", "MockDatabase", "MockSchema"]
        user_settings_file_util._set_adc_auth_config_details(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['OAUTH']['ACCESS_TOKEN'], "MockAccessToken")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_oauth_token_set(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'ADC': {
                'CONN': {}
            }
        }
        mock_pick.side_effect = [("Provide private key value", 0)]
        mock_get_input.side_effect = ["MockAccessToken"]
        user_settings_file_util._set_adc_auth_config_details_for_oauth(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['OAUTH']['ACCESS_TOKEN'], "MockAccessToken")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_rsa_private_key(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'ADC': {
                'CONN': {}
            }
        }
        mock_pick.side_effect = [("Provide private key value", 0)]
        mock_get_input.side_effect = ["MockPrivateKey"]
        user_settings_file_util._set_adc_auth_config_details_for_snowflake_jwt(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['RSA']['PRIVATE_KEY'], "MockPrivateKey")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input')
    def test_add_adc_rsa_private_keyfilepath_passphrase(self, mock_get_input, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        settings_data = {
            'ADC': {
                'CONN': {}
            }
        }
        mock_pick.side_effect = [("Provide private key filepath and passphrase", 1)]
        mock_get_input.side_effect = ["Mock/Private/Key/FilePath.p8", "MockPassPhrase"]
        user_settings_file_util._set_adc_auth_config_details_for_snowflake_jwt(settings_data)
        self.assertEqual(settings_data['ADC']['CONN']['RSA']['PRIVATE_KEY_FILEPATH'], "Mock/Private/Key/FilePath.p8")
        self.assertEqual(settings_data['ADC']['CONN']['RSA']['PRIVATE_KEY_PASSPHRASE'], "MockPassPhrase")


class TestUserSettingsUtilHelperMethods(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {"defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value='sample response')
    def test_get_read_input_or_none(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_or_none("Sample input prompt.")
        self.assertEqual(resp, "sample response")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value="")
    def test_get_read_input_or_none_no_resp(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_or_none("Sample input prompt.")
        self.assertIsNone(resp)

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value='sample response')
    def test_get_read_input_or_default_str(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_or_default_str("Sample input prompt.", default_value="default resp")
        self.assertEqual(resp, "sample response")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value='')
    def test_get_read_input_or_default_str_default(self, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_or_default_str("Sample input prompt.", default_value="default resp")
        self.assertEqual(resp, "default resp")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick', return_value=("OPTION_2", 2))
    def test_get_read_input_from_options(self, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_from_options("Sample input prompt.", options=["OPTION_0", "OPTION_1", "OPTION_2"])
        self.assertEqual(resp, "OPTION_2")

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.pick', return_value=[("OPTION_1", 1), ("OPTION_2", 2)])
    def test_get_read_input_from_options_multi_select(self, mock_pick):
        from aladdinsdk.config.utils import user_settings_file_util
        resp = user_settings_file_util._read_input_from_options("Sample input prompt.",
                                                                options=["OPTION_0", "OPTION_1", "OPTION_2"],
                                                                multiselect=True)
        self.assertEqual(resp, ["OPTION_1", "OPTION_2"])


    def test_list_currently_available_scopes(self):
        from aladdinsdk.config.utils import user_settings_file_util
        scopes = user_settings_file_util._list_currently_available_scopes()
        self.assertIn('offline_access', scopes)

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._set_client_id_client_secret', return_value=('M_CLIENT_ID', 'M_CLIENT_SECRET'))
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._read_input_or_default_str', side_effect=[3001, 'm_auth_url', 'm_token_url'])
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._read_input_from_options', return_value=['offline_access', 'm_scope_1'])
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_refresh_token_from_oauth_server', return_value='m_refresh_token')
    def test_set_oauth_auth_config_details_oauth_details_generate_refresh_token(self, mock_refresh_token, mock_scope, mock_inputs, mock_client_details_set):
        from aladdinsdk.config.utils.user_settings_file_util import _set_oauth_auth_config_details_oauth_details_generate_refresh_token
        settings_data = {
            'API': {
                'OAUTH': {}
            }
        }
        _set_oauth_auth_config_details_oauth_details_generate_refresh_token(settings_data)
        self.assertEqual(settings_data['API']['OAUTH']['REFRESH_TOKEN'], "m_refresh_token")


    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value='')
    @mock.patch('builtins.print')
    def test_print_config_file(self, mock_print, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util

        dummy_settings_data = {
            'RUN_MODE': 'local',
            'USER_CREDENTIALS': {
                'USERNAME': 'atendo',
            },
            'API': {
                'AUTH_TYPE': 'OAuth',
                'AUTH_FLOW_TYPE': 'client_credentials',
                'OAUTH': {
                    'CLIENT_ID': 'cli_id',
                    'CLIENT_SECRET': 'shhhhh'
                }
            }
        }

        user_settings_file_util._print_config_file(dummy_settings_data)
        mock_print.assert_called()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util.get_input', return_value='xyz.yaml')
    @mock.patch('builtins.print')
    @mock.patch('builtins.open')
    def test_print_config_file_output_to_file(self, mock_open, mock_print, mock_get_input):
        from aladdinsdk.config.utils import user_settings_file_util

        dummy_settings_data = {
            'RUN_MODE': 'local',
            'USER_CREDENTIALS': {
                'USERNAME': 'atendo',
            },
            'API': {
                'AUTH_TYPE': 'OAuth',
                'AUTH_FLOW_TYPE': 'client_credentials',
                'OAUTH': {
                    'CLIENT_ID': 'cli_id',
                    'CLIENT_SECRET': 'shhhhh'
                }
            }
        }

        user_settings_file_util._print_config_file(dummy_settings_data)
        mock_print.assert_called()
        mock_open.assert_called()
