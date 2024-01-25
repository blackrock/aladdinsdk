import os
from unittest import TestCase, mock
from test.resources.testutils import extmocks, utils


class TestBlkutilsWithDefaultWebServer(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.blkutils import blkutils
        self.test_subject = blkutils
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_account_from_files_dat(self, mock_requests_get):
        self.assertEqual(self.test_subject.get_adc_account_private_link(), "mock_snowflake_dswrite.privatelink")

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get_without_token)
    def test_get_adc_account_from_files_dat_failure(self, mock_requests_get):
        self.assertIsNone(self.test_subject.get_adc_account_private_link())

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get_with_token)
    def test_get_files_dat_token_value_success(self, mock_user_settings_default_web_server):
        self.assertEqual(self.test_subject.get_files_dat_token_value("TEST_TOKEN"), "TEST_TOKEN_VALUE")

    @mock.patch('requests.get', side_effect=Exception("something wrong"))
    @mock.patch('logging.Logger.warning')
    def test_get_files_dat_token_value_failure(self, mock_logger_warning, mock_user_settings_default_web_server):
        self.assertIsNone(self.test_subject.get_files_dat_token_value("TEST_TOKEN"), "TEST_TOKEN_VALUE")
        mock_logger_warning.assert_called_with("BlackRock default web server is not set or files.dat tokens unavailable.")
