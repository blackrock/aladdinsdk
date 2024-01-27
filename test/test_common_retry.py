from unittest import TestCase, mock
import os
from test.resources.testutils import utils


class TestRetry(TestCase):
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

    def test_API_retry_without_exception(self):
        from aladdinsdk.common.retry import api_retry

        @api_retry.api_retry
        def dummy_without_exception():
            return True

        result = dummy_without_exception()

        self.assertEqual(result, True)

    def test_API_retry_with_exception(self):
        from aladdinsdk.common.retry import api_retry

        @api_retry.api_retry
        def dummy_with_exception():
            raise Exception("fail in retry")

        try:
            result = dummy_with_exception()
        except Exception as e:
            result = e.args[0]

        self.assertEqual(result, "fail in retry")

    def test_ADC_retry_without_exception(self):
        from aladdinsdk.common.retry import adc_retry

        @adc_retry.adc_retry
        def dummy_without_exception():
            return True

        result = dummy_without_exception()

        self.assertEqual(result, True)

    def test_ADC_retry_with_exception(self):
        from aladdinsdk.common.retry import adc_retry

        @adc_retry.adc_retry
        def dummy_with_exception():
            raise Exception("fail in retry")

        try:
            result = dummy_with_exception()
        except Exception as e:
            result = e.args[0]

        self.assertEqual(result, "fail in retry")
