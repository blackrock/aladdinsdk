from unittest import TestCase, mock
import os
from test.resources.testutils import utils

builtin_open = open  # save the unpatched version


def mock_open_for_p8_file(*args, **kwargs):
    if args[0] == "some/file/location.p8":
        from cryptography.hazmat.primitives import serialization, asymmetric
        from cryptography.hazmat.backends import default_backend
        private_key = asymmetric.rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,
                                        encryption_algorithm=serialization.BestAvailableEncryption(b"testpassphrase"))
        return mock.mock_open(read_data=pem)(*args, **kwargs)
    # unpatched version for every other path
    return builtin_open(*args, **kwargs)


@mock.patch("aladdinsdk.common.authentication.adc.AdcAuthUtil._fetch_adc_connection_access_token_from_tokenapi", return_value="MockedAccessToken")
class TestCommonAuthAdcDefaultConfig(TestCase):
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

    def test_adc_auth_util_init_default(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil()

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)

    def test_adc_auth_util_init_inflated_oauth_user_provided_token(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil(adc_conn_authenticator="oauth", adc_oauth_access_token="FOOBARACCESS")

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertEqual(test_adc_auth_util.user_provided_oauth_access_token, "FOOBARACCESS")
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)

    def test_adc_auth_util_init_inflated_oauth_token_api_basic_auth(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil(adc_conn_authenticator="oauth", auth_type="Basic Auth", username="ehunt", password="fallout")

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)
        self.assertEqual(test_adc_auth_util._inflated_api_init_kwargs['username'], "ehunt")
        self.assertEqual(test_adc_auth_util._inflated_api_init_kwargs['password'], "fallout")
        self.assertEqual(test_adc_auth_util._inflated_api_init_kwargs['auth_type'], "Basic Auth")

    def test_adc_auth_util_init_inflated_rsa_user_provided_private_key(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil(adc_conn_authenticator="oauth", adc_conn_rsa_private_key="FOOBARPRIVATEACCESS")

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key, "FOOBARPRIVATEACCESS")
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)

    def test_adc_auth_util_init_inflated_rsa_user_provided_private_key_filepath(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil(adc_conn_authenticator="oauth", adc_conn_rsa_private_key_filepath="testsecret/sample.p8")

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key_filepath, "testsecret/sample.p8")
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)

    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_oauth_token_api(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient

        test_adc_client = ADCClient()
        test_adc_client._generate_adc_connection = generate_conn_mock
        generated_sf_conn_params = test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)

        self.assertEqual(generated_sf_conn_params['token'], "MockedAccessToken")
        self.assertEqual(generated_sf_conn_params['authenticator'], "oauth")

    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_user_provided_token(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient

        test_adc_client = ADCClient(adc_oauth_access_token="UserProvidedAccessToken")
        generated_sf_conn_params = test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)

        self.assertEqual(generated_sf_conn_params['token'], "UserProvidedAccessToken")
        self.assertEqual(generated_sf_conn_params['authenticator'], "oauth")


@mock.patch("aladdinsdk.common.authentication.adc.AdcAuthUtil._fetch_adc_connection_access_token_from_tokenapi", return_value="MockedAccessToken")
class TestCommonAuthAdcRsaConfig(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_adc_rsa_conn.yaml",
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

    def test_adc_auth_util_init_inflated_rsa_user_provided_private_key_filepath_passphrase(self, mock_token_api_call):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil(adc_conn_authenticator="oauth", adc_conn_rsa_private_key_filepath="testsecret/sample.p8",
                                         adc_conn_rsa_private_key_passphrase="friction")

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key_filepath, "testsecret/sample.p8")
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key_passphrase, "friction")

    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_user_provided_rsa_private_key(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient
        from cryptography.hazmat.primitives import serialization, asymmetric
        from cryptography.hazmat.backends import default_backend
        private_key = asymmetric.rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8,
                                        encryption_algorithm=serialization.NoEncryption())

        test_adc_client = ADCClient(adc_conn_authenticator="snowflake_jwt", adc_conn_rsa_private_key=pem,
                                    adc_conn_rsa_private_key_passphrase="")
        generated_sf_conn_params = test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)

        self.assertIsNotNone(generated_sf_conn_params['private_key'])
        self.assertEqual(generated_sf_conn_params['authenticator'], "snowflake_jwt")

    @mock.patch("builtins.open", mock_open_for_p8_file)
    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_rsa_private_key_from_file(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient

        test_adc_client = ADCClient(adc_conn_authenticator="snowflake_jwt", adc_conn_rsa_private_key_filepath="some/file/location.p8",
                                    adc_conn_rsa_private_key_passphrase="testpassphrase")
        generated_sf_conn_params = test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)

        self.assertIn('private_key', generated_sf_conn_params.keys())

    @mock.patch("builtins.open", mock_open_for_p8_file)
    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_rsa_private_key_missing_passphrase(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException

        with self.assertRaises(AsdkAdcException) as context:
            test_adc_client = ADCClient(adc_conn_authenticator="snowflake_jwt", adc_conn_rsa_private_key_filepath="some/file/location.p8",
                                        adc_conn_rsa_private_key_passphrase=None)
            test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)
            self.assertTrue("Attempting to connect using RSA key pair, but private key details not configured. "
                            "Either private key or private key filepath with passphrase needed." in context.exception)

    @mock.patch("builtins.open", mock_open_for_p8_file)
    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_rsa_private_key_incorrect_passphrase(self, generate_conn_mock, mock_token_api_call):
        from aladdinsdk.adc.client import ADCClient
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException

        with self.assertRaises(AsdkAdcException) as context:
            test_adc_client = ADCClient(adc_conn_authenticator="snowflake_jwt", adc_conn_rsa_private_key_filepath="some/file/location.p8",
                                        adc_conn_rsa_private_key_passphrase="invalidpass")
            test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)
            self.assertEqual("Unable to read configured private key. Error: Password was given but private key is not encrypted.", context.exception)


class TestCommonAuthAdcRsaConfigWithKeys(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_adc_rsa_conn_with_key.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    def test_adc_auth_util_init_rsa_key_with_passphrase(self):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil()

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_SNOWFLAKE_JWT)
        self.assertIsNone(test_adc_auth_util.user_provided_oauth_access_token)
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key_passphrase, "testpassphrase")
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertEqual(test_adc_auth_util.adc_conn_rsa_private_key, "dummyprivatekeyval")

    @mock.patch("builtins.open", mock_open_for_p8_file)
    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_generate_sf_connection_params_rsa_private_key(self, generate_conn_mock):
        from aladdinsdk.adc.client import ADCClient
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric import rsa

        mock_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        mock_passphrase = b"my_passphrase"

        mock_private_key_pem = mock_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(mock_passphrase)
        )

        test_adc_client = ADCClient(adc_conn_authenticator="snowflake_jwt", adc_conn_rsa_private_key=mock_private_key_pem.decode(),
                                    adc_conn_rsa_private_key_passphrase="my_passphrase")
        generated_sf_conn_params = test_adc_client._adc_auth_util.generate_sf_connection_params(test_adc_client)

        self.assertIn('private_key', generated_sf_conn_params.keys())


class TestCommonAuthAdcOauthConfigWithToken(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_adc_oauth_conn.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    def test_adc_auth_util_init_rsa_key_with_passphrase(self):
        from aladdinsdk.common.authentication.adc import AdcAuthUtil
        from aladdinsdk.config import user_settings

        test_adc_auth_util = AdcAuthUtil()

        self.assertEqual(test_adc_auth_util.adc_conn_authenticator, user_settings.CONF_ADC_CONN_AUTHENTICATOR_OAUTH)
        self.assertEqual(test_adc_auth_util.user_provided_oauth_access_token, "dummyaccesstoken")
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_passphrase)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key_filepath)
        self.assertIsNone(test_adc_auth_util.adc_conn_rsa_private_key)
