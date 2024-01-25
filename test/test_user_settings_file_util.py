import os
from unittest import TestCase, mock

from aladdinsdk.config.asdkconf import ENV_VAR_ASDK_USER_CONFIG_FILE
from aladdinsdk.config.utils.user_settings_file_util import _ENV_VAR_NOTEBOOK_USER_NAME
from test.resources.testutils import utils


class TestDefaultUserSettingsFileUtilWhenEnvNBUserIsNotSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_TEST__ENV": "TEST_VAL",
            "defaultWebServer": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        from aladdinsdk.config.utils import user_settings_file_util
        self.test_subject = user_settings_file_util
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_login_name', return_value='vrathore')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_auth_type', return_value='Basic Auth')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_api_key', return_value='test')
    @mock.patch('builtins.open')
    def test_setting_nb_user_environment_variable_not_set(self, op_file, input, auth_input, username_input):
        result = self.test_subject.print_user_config_file_template()
        self.assertEqual(os.environ.get(_ENV_VAR_NOTEBOOK_USER_NAME, None), None)
        self.assertIsNone(result)

    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_login_name', return_value='vrathore')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_auth_type', return_value='Basic Auth')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_api_key', return_value='test')
    @mock.patch('builtins.open')
    def test_print_user_config_file_template_nb_user_environment_variable_not_set(self, op_file, input, auth_input, username_input):
        result = self.test_subject.print_user_config_file_template()
        self.assertEqual(os.environ.get(_ENV_VAR_NOTEBOOK_USER_NAME, None), None)
        self.assertIsNone(result)


class TestDefaultUserSettingsFileUtilWhenEnvNBUserIsSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_TEST__ENV": "TEST_VAL",
            "defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        from aladdinsdk.config.utils import user_settings_file_util
        self.test_subject = user_settings_file_util
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('os.environ')
    @mock.patch('builtins.open')
    @mock.patch('os.path.abspath')
    @mock.patch('yaml.dump')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_api_key', return_value='test')
    @mock.patch('aladdinsdk.config.utils.user_settings_file_util._prompt_user_for_auth_type', return_value='Basic Auth')
    def test_setting_nb_user_environment_variable_set_success(self, arg1, arg2, arg3, arg4, input, auth_type):
        result = self.test_subject.print_user_config_file_template()
        self.assertNotEqual(os.environ.get(_ENV_VAR_NOTEBOOK_USER_NAME, None), None)
        self.assertNotEqual(os.environ.get(ENV_VAR_ASDK_USER_CONFIG_FILE, None), None)
        self.assertIsNone(result)

    @mock.patch('builtins.input', return_value='test')
    def test_get_input(self, input):
        result = self.test_subject._prompt_user_for_api_key()
        self.assertEqual(result, 'test')

    @mock.patch('builtins.input', return_value='test')
    def test_get_input_auth_type(self, input):
        result = self.test_subject._prompt_user_for_auth_type()
        self.assertEqual(result, 'test')

    @mock.patch('builtins.input', return_value='test')
    def test_get_input_login_name(self, input):
        result = self.test_subject._prompt_user_for_login_name()
        self.assertEqual(result, 'test')


class TestDefaultUserSettingsFileUtil(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('builtins.print')
    def test_get_input(self, mock_print):
        from aladdinsdk.config.utils import user_settings_file_util
        user_settings_file_util.print_current_user_config()
        mock_print.assert_called()
