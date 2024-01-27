import datetime
from unittest import TestCase, mock
import os
from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkOAuthException
from test.resources.testutils import utils


class TestCommonAuthApi(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

    def test_add_api_key_header_to_configuration_passed_value(self):
        from aladdinsdk.common.authentication.api import add_api_key_header_to_configuration

        add_api_key_header_to_configuration(self.test_configuration, "test_api_key")

        self.assertEqual(self.test_configuration.api_key['APIKeyHeader'], "test_api_key")

    def test_add_api_key_header_to_configuration_config_value(self):
        from aladdinsdk.common.authentication.api import add_api_key_header_to_configuration

        add_api_key_header_to_configuration(self.test_configuration, "hippopotomonstrosesquippedaliophobia")

        self.assertEqual(self.test_configuration.api_key['APIKeyHeader'], "hippopotomonstrosesquippedaliophobia")

    def test_add_auth_details_to_configuration_passed_values(self):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration

        add_basic_auth_details_to_configuration(self.test_configuration, username="lhamilton", password="GOAT44")

        self.assertEqual(self.test_configuration.username, "lhamilton")
        self.assertEqual(self.test_configuration.password, "GOAT44")

    def test_add_auth_details_to_configuration_config_values(self):
        from aladdinsdk.common.authentication.basicauth import basicauthutil
        from aladdinsdk.common.authentication.api import ApiAuthUtil

        ApiAuthUtil(configuration=self.test_configuration)
        basicauthutil.add_basic_auth_details_to_configuration(self.test_configuration, username="jbond",
                                                              password=basicauthutil.fetch_password_from_user_settings())

        self.assertEqual(self.test_configuration.username, "jbond")
        self.assertEqual(self.test_configuration.password, "am_db9")

    def test_add_auth_details_to_configuration_mix_values(self):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration

        add_basic_auth_details_to_configuration(self.test_configuration, username="jbond", password="emp_no_007")

        self.assertEqual(self.test_configuration.username, "jbond")
        self.assertEqual(self.test_configuration.password, "emp_no_007")

    @mock.patch('aladdinsdk.common.authentication.api.basicauthutil.fetch_password_from_user_settings')
    @mock.patch('aladdinsdk.common.authentication.api.user_settings.get_user_password')
    def test_basic_auth_password_exception(self, mock_user_settings_get_user_password, mock_fetch_password_from_user_settings):
        mock_user_settings_get_user_password.return_value = None
        mock_fetch_password_from_user_settings.return_value = None
        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(configuration=self.test_configuration, username='test', auth_type='Basic Auth')
        with self.assertRaises(AsdkApiException) as context:
            api_auth_util.add_auth_details_to_header_and_config()
            self.assertTrue("Incomplete Basic Auth Details provided: Missing username and/or password. "
                            "Please check AladdinSDK documentation for configuration details." in context.exception)


class TestCommonAuthApiInLocalWithKeyring(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_local_test_keyring.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

    @mock.patch('aladdinsdk.common.authentication.basicauth.basicauthutil.keyringutil')
    def test_add_auth_details_to_configuration_keyring_password(self, mock_keyring_util):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration
        from aladdinsdk.common.authentication.basicauth.basicauthutil import fetch_password_from_user_settings

        mock_keyring_util.get_user_password.return_value = "GG"

        add_basic_auth_details_to_configuration(self.test_configuration, username="lhamilton", password=fetch_password_from_user_settings())

        self.assertEqual(self.test_configuration.username, "lhamilton")
        self.assertEqual(self.test_configuration.password, "GG")

    @mock.patch('aladdinsdk.common.authentication.basicauth.basicauthutil.keyringutil')
    def test_add_auth_details_to_configuration_keyring_prompt_user(self, mock_keyring_util):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration
        from aladdinsdk.common.authentication.basicauth.basicauthutil import fetch_password_from_user_settings

        mock_keyring_util.get_user_password.return_value = None
        mock_keyring_util.store_user_password.return_value = "WP"

        add_basic_auth_details_to_configuration(self.test_configuration, username="lhamilton", password=fetch_password_from_user_settings())

        mock_keyring_util.store_user_password.assert_called_with(prompt_user=True)
        self.assertEqual(self.test_configuration.username, "lhamilton")
        self.assertEqual(self.test_configuration.password, "WP")


class TestCommonAuthApiInLocalWithPasswordFilepathOnly(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_local_test_password_filepath.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

    def test_add_auth_details_to_configuration_password_filepath(self):
        from aladdinsdk.common.authentication.basicauth import basicauthutil
        pwd = basicauthutil.fetch_password_from_user_settings()
        self.assertEqual(pwd, "shh!thisisasecretdude,readitandforget!")


class TestCommonAuthApiInLocalWithPasswordAndEncKeyFilepath(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_local_test_password_with_enc_key_filepath.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

    def test_add_auth_details_to_configuration_password_filepath(self):
        from aladdinsdk.common.authentication.basicauth import basicauthutil
        pwd = basicauthutil.fetch_password_from_user_settings()
        self.assertEqual(pwd, "samplepassword")


class TestCommonAuthApiMissingConfigurationScenario(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_incomplete.yaml",
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()

        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_add_auth_details_to_configuration_passed_values(self):

        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration

        add_basic_auth_details_to_configuration(self.test_configuration, username="lhamilton", password="GOAT44")

        self.assertEqual(self.test_configuration.username, "lhamilton")
        self.assertEqual(self.test_configuration.password, "GOAT44")

    def test_add_auth_details_to_configuration_failure_missing_username(self):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration

        with self.assertRaises(Exception) as context:
            add_basic_auth_details_to_configuration(self.test_configuration, password="GOAT44")
            self.assertTrue('Insufficient API initialization information. Username not passed/configured for SDK.' in context.exception)

    def test_add_auth_details_to_configuration_failure_missing_password(self):
        from aladdinsdk.common.authentication.basicauth.basicauthutil import add_basic_auth_details_to_configuration

        with self.assertRaises(Exception) as context:
            add_basic_auth_details_to_configuration(self.test_configuration, username="lhamilton")
            self.assertTrue('Insufficient API initialization information for Basic Auth. Password not passed/configured for SDK.'
                            in context.exception)


class TestFetchOauthTokenComputeWorkload(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_filepath_values_set.yaml",
            "NB_USER": "user"
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()

        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=["ACCESS_TOKEN123", 3600])
    def test_oauth_token_successfully_created(self, oauth_token):

        from aladdinsdk.common.authentication.api import ApiAuthUtil

        api_auth_util = ApiAuthUtil(username='test')
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)

        self.assertEqual(result, ['ACCESS_TOKEN123', 3600])


class TestFetchOauthTokenComputeWorkloadInvalidPath(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_filepath_incorrect_values_set.yaml",
            "NB_USER": "user"
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()

        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_oauth_token_fetch_fail(self):

        from aladdinsdk.common.authentication.api import ApiAuthUtil

        api_auth_util = ApiAuthUtil(username='test')
        resp_access_token, resp_ttl = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertIsNone(resp_access_token)
        self.assertIsNone(resp_ttl)


class TestFetchOauthTokenLocal(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()

        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=["ACCESS_TOKEN123", 3600])
    def test_oauth_token_successfully_created(self, oauth_token):
        from aladdinsdk.common.authentication.api import ApiAuthUtil

        api_auth_util = ApiAuthUtil(username='test')
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)

        self.assertEqual(result, ['ACCESS_TOKEN123', 3600])


class TestFetchOauthTokenFromParams(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_params_passed.yaml",
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()

        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=["ACCESS_TOKEN123", 3600])
    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_oauth_request_headers_built_successfully_from_params(self, oauth_token, secrets):
        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, username='test', client_id='id',
                                    client_secret='secret', refresh_token='token')
        result = api_auth_util.add_auth_details_to_header_and_config()
        self.assertEqual(result.get("Authorization"), "Bearer ACCESS_TOKEN123")

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=["ACCESS_TOKEN456", 3600])
    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_oauth_access_token_refreshed_successfully(self, oauth_token, secrets):
        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, username='test', client_id='id',
                                    client_secret='secret', refresh_token='token')
        result = api_auth_util.add_auth_details_to_header_and_config()
        self.assertEqual(result.get("Authorization"), "Bearer ACCESS_TOKEN456")

    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_oauth_access_token_passed_in_by_user(self, secrets):
        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, api_access_token="ACCESS_TOKEN789")
        result = api_auth_util.add_auth_details_to_header_and_config()
        self.assertEqual(result.get("Authorization"), "Bearer ACCESS_TOKEN789")

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=(None, None))
    @mock.patch('aladdinsdk.common.authentication.api.okta_sidecar_client.get_access_token_ttl_from_okta_sidecar',
                return_value=(None, None))
    def test_oauth_request_headers_missing_access_token_error(self, mock_oauth_resp, mock_okta_sidecar_resp):

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, username='test', client_id='id',
                                    client_secret='secret', refresh_token='token')

        with self.assertRaises(AsdkOAuthException) as context:
            api_auth_util.add_auth_details_to_header_and_config()
            self.assertEqual("No valid access token for OAuth found!!!", context.exception.message)

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=(None, None))
    @mock.patch('aladdinsdk.common.authentication.api.okta_sidecar_client.get_access_token_ttl_from_okta_sidecar',
                return_value=("ACCESS_GRANTED", datetime.datetime(2021, 1, 1, 0, 0, 0, 0)))
    def test_oauth_request_headers_access_token_ttl_datetime(self, mock_oauth_resp, mock_okta_sidecar_resp):

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, username='test', client_id='id',
                                    client_secret='secret', refresh_token='token')

        api_auth_util.add_auth_details_to_header_and_config()
        self.assertEqual(api_auth_util.token_ttl, datetime.datetime(2021, 1, 1, 0, 0, 0, 0))

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=(None, None))
    @mock.patch('aladdinsdk.common.authentication.api.okta_sidecar_client.get_access_token_ttl_from_okta_sidecar',
                return_value=("ACCESS_GRANTED", None))
    def test_oauth_request_headers_access_token_ttl_only_none(self, mock_oauth_resp, mock_okta_sidecar_resp):

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil(auth_type="OAuth", configuration=self.test_configuration, username='test', client_id='id',
                                    client_secret='secret', refresh_token='token')

        api_auth_util.add_auth_details_to_header_and_config()
        self.assertIsNone(api_auth_util.token_ttl)
