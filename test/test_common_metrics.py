from unittest import TestCase, mock
import os

from test.resources.testutils import utils


class TestCommonMetricsSuffixUpdate(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('logging.Logger.debug')
    def test_successful_update(self, mock_logger_debug):
        test_suffix = "test/suffix"
        from aladdinsdk.common.metrics import update_domain_sdk_metrics_suffix
        update_domain_sdk_metrics_suffix(test_suffix)
        from aladdinsdk.api.client import _DEFAULT_SDK_USER_AGENT_SUFFIX
        from aladdinsdk.adc.client import _DEFAULT_SDK_QUERY_TAG_SUFFIX
        self.assertEqual(_DEFAULT_SDK_USER_AGENT_SUFFIX, test_suffix)
        self.assertEqual(_DEFAULT_SDK_QUERY_TAG_SUFFIX, test_suffix)

    @mock.patch('logging.Logger.debug')
    def test_successful_update_alphanumeric(self, mock_logger_debug):
        test_suffix = "test123suffix"
        from aladdinsdk.common.metrics import update_domain_sdk_metrics_suffix
        update_domain_sdk_metrics_suffix(test_suffix)
        mock_logger_debug.assert_called_with("Updating SDK query tag to QueryViaSDK-AladdinSDK-test123suffix")
        from aladdinsdk.api.client import _DEFAULT_SDK_USER_AGENT_SUFFIX
        from aladdinsdk.adc.client import _DEFAULT_SDK_QUERY_TAG_SUFFIX
        self.assertEqual(_DEFAULT_SDK_USER_AGENT_SUFFIX, test_suffix)
        self.assertEqual(_DEFAULT_SDK_QUERY_TAG_SUFFIX, test_suffix)

    @mock.patch('logging.Logger.error')
    def test_failure_to_set_due_to_invalid_special_char(self, mock_logger_error):
        test_suffix = "invalid_suffix"
        from aladdinsdk.common.metrics import update_domain_sdk_metrics_suffix
        update_domain_sdk_metrics_suffix(test_suffix)
        mock_logger_error.assert_called_with(f"Invalid domain SDK suffix provided: '{test_suffix}'. "
                                             "Error: User Agent suffix should be alphanumeric string of max length 15.")

    @mock.patch('logging.Logger.error')
    def test_failure_to_set_query_tag_due_to_invalid_special_char(self, mock_logger_error):
        test_suffix = "invalid_suffix"
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException

        with self.assertRaises(AsdkAdcException):
            from aladdinsdk.adc.client import update_domain_sdk_query_tag_suffix
            update_domain_sdk_query_tag_suffix(test_suffix)
