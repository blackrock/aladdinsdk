import os
from unittest.mock import patch
import yaml
from unittest import TestCase, mock
from aladdinsdk.config.asdkconf import _CODEGEN_ALLOW_LIST_INTERNAL_CONFIG_FILE
from test.resources.testutils import utils


class TestAsdkConf(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_TEST__ENV": "TEST_VAL",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        # del sys.modules['aladdinsdk.config.asdkconf'] # re-import to lose context created by other suites
        utils.reload_modules()
        from aladdinsdk.config.asdkconf import AsdkConf
        self.test_subject = AsdkConf
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_setting_config_via_environment_variable(self):
        self.assertEqual(self.test_subject.get("TEST__ENV"), "TEST_VAL")
        self.assertEqual(self.test_subject.get("test.env"), "TEST_VAL")

    def test_asdkconf_reads_user_provided_settings_file(self):
        self.assertEqual(self.test_subject.get("RUN_MODE"), "test")


class TestAsdkConfInComputeWorkloadWithConfigEnvVar(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_TEST__ENV": "TEST_VAL",
            "NB_USER": "TEST_USER",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        # del sys.modules['aladdinsdk.config.asdkconf'] # re-import to lose context created by other suites
        utils.reload_modules()
        from aladdinsdk.config.asdkconf import AsdkConf
        self.test_subject = AsdkConf
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_setting_config_via_environment_variable(self):
        self.assertEqual(self.test_subject.get("TEST__ENV"), "TEST_VAL")
        self.assertEqual(self.test_subject.get("test.env"), "TEST_VAL")
        self.assertEqual(self.test_subject.get("RUN_MODE"), "test")


class TestAsdkConfInComputeWorkloadWithConfigEnvVarAndDefault(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_TEST__ENV": "TEST_VAL",
            "NB_USER": "TEST_USER",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        # del sys.modules['aladdinsdk.config.asdkconf'] # re-import to lose context created by other suites
        utils.reload_modules()
        from aladdinsdk.config.asdkconf import AsdkConf
        self.test_subject = AsdkConf
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @patch('os.path.exists', return_value=True)
    @patch('os.environ')
    @patch('os.path.abspath', return_value=True)
    @patch('aladdinsdk.config.asdkconf._get_preloaded_config_files_to_read_list',
           return_value=[_CODEGEN_ALLOW_LIST_INTERNAL_CONFIG_FILE, "test/resources/testdata/sample_default_user_settings_compute.yaml"])
    def test_run_mode_in_compute_with_default_config(self, mock_path, mock_environ, mock_abspath, mock_file_list):
        self.assertEqual(self.test_subject.get("TEST__ENV"), "TEST_VAL")
        self.assertEqual(self.test_subject.get("test.env"), "TEST_VAL")
        self.assertEqual(self.test_subject.get("RUN_MODE"), "test")


class TestUserSettings(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_TEST__ENV": "TEST_VAL",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        import aladdinsdk.config.user_settings as user_settings
        self.test_subject = user_settings
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_get_run_mode(self):
        self.assertEqual(self.test_subject.get_run_mode(), "test")

    def test_get_api_auth_type(self):
        self.assertEqual(self.test_subject.get_api_auth_type(), "Basic Auth")

    def test_get_api_token(self):
        self.assertEqual(self.test_subject.get_api_token(), "hippopotomonstrosesquippedaliophobia")

    def test_get_adc_conn_account(self):
        self.assertEqual(self.test_subject.get_adc_conn_account(), "mi6-uke2sf.privatelink")

    def test_get_adc_conn_role(self):
        self.assertEqual(self.test_subject.get_adc_conn_role(), "SPY")

    def test_get_adc_conn_warehouse(self):
        self.assertEqual(self.test_subject.get_adc_conn_warehouse(), "SPECTRE")

    def test_get_adc_conn_database(self):
        self.assertEqual(self.test_subject.get_adc_conn_database(), "MI_6_EMPS")

    def test_get_adc_conn_schema(self):
        self.assertEqual(self.test_subject.get_adc_conn_schema(), "AGENTS")

    def test_get_username(self):
        self.assertEqual(self.test_subject.get_username(), "jbond")

    def test_get_user_password(self):
        self.assertEqual(self.test_subject.get_user_password(), "am_db9")

    def test_get_encryption_filepath(self):
        self.assertEqual(self.test_subject.get_encryption_filepath(), "test/resources/testdata/sample_encryption_key.txt")

    def test_get_password_filepath(self):
        self.assertEqual(self.test_subject.get_password_filepath(), "test/resources/testdata/sample_encrypted_password.txt")

    @mock.patch('builtins.print')
    def test_get_input(self, mock_print):
        from aladdinsdk.config.utils import user_settings_file_util
        user_settings_file_util.print_current_user_config()
        mock_print.assert_called()


class TestInternalSettings(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_TEST__ENV": "TEST_VAL",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        import aladdinsdk.config.internal_settings as internal_settings
        self.test_subject = internal_settings
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_get_api_allow_list(self):
        with open("aladdinsdk/api/codegen/codegen_allow_list.yaml", "r") as stream:
            config_file_contents = yaml.safe_load(stream)
            allow_list = config_file_contents['CODEGEN_API_SETTINGS']['ALLOW_LIST']
            self.assertEqual(len(self.test_subject.get_api_allow_list()), len(allow_list))
