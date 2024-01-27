from unittest import TestCase, mock
import os
from aladdinsdk.common.error.asdkerrors import AsdkEmailNotificationException, AsdkApiException
from test.resources.testutils import utils


class TestCommonErrorNotificationsThroughEmail(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_error_email_notifications_set.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.error.notifications import email_notifications_for_errors
        self.test_subject = email_notifications_for_errors
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('aladdinsdk.common.error.notifications.email_notifications_for_errors.send_email_notification', return_value=True)
    def test_email_notification_for_exception_success(self, email_notif):
        test_exception = AsdkApiException("TEST")
        self.test_subject.email_notification_for_exception(test_exception)

    def test_email_notification_for_exception_fail(self):
        with mock.patch('aladdinsdk.common.error.notifications.email_notifications_for_errors.send_email_notification',
                        side_effect=AsdkEmailNotificationException):
            with self.assertRaises(Exception) as context:
                test_exception = AsdkApiException("TEST")
                self.test_subject.email_notification_for_exception(test_exception)
                self.assertTrue('Unable to send email notification for exception' in context.exception)
