import os
from unittest import TestCase, mock
from aladdinsdk.common.error.asdkerrors import AsdkEmailNotificationException

from test.resources.testutils import utils


class TestCommonNotificationsEmailWithHostAndPwdSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.notifications import email_notifications
        self.test_subject = email_notifications
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('email.mime.base.MIMEBase')
    @mock.patch('email.encoders')
    @mock.patch('email.mime.multipart.MIMEMultipart')
    @mock.patch('aladdinsdk.config.user_settings')
    def test_email_notification_valid(self, mimebase, encoders, mimemultipart, usersettings):
        # email notification without cc and attachments
        with mock.patch('smtplib.SMTP', autospec=True) as mocked_smtp:
            self.test_subject.send_email_notification('test subject', 'test content', ['test1@blk.com'])
            mocked_smtp.assert_called()
            context = mocked_smtp.return_value.__enter__.return_value
            context.starttls.assert_called()
            context.login.assert_called_with('jbond', 'test_pwd')
            context.sendmail.assert_called()

        # email notification with cc and attachments
        file_path = './test/resources/testdata//test_file.csv'
        open(file_path, 'w')
        with mock.patch('smtplib.SMTP', autospec=True) as mocked_smtp_2:
            self.test_subject.send_email_notification('test subject',
                                                      'test content',
                                                      ['test1@blk.com'],
                                                      cc=['test2@blk.com', 'test3@blk.com'],
                                                      attachments=[file_path])
            mocked_smtp_2.assert_called()
            context = mocked_smtp_2.return_value.__enter__.return_value
            context.starttls.assert_called()
            context.login.assert_called_with('jbond', 'test_pwd')
            context.sendmail.assert_called()
            os.remove(file_path)


class TestCommonNotificationsEmailWithHostAndPwdNotSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_incomplete.yaml",
            "defaultWebServer": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.notifications import email_notifications
        self.test_subject = email_notifications
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_email_exception_when_no_email_pwd_defined(self):
        with mock.patch('smtplib.SMTP', autospec=True):
            with self.assertRaises(AsdkEmailNotificationException) as context:
                self.test_subject.send_email_notification(subject='test subject',
                                                          message='test content',
                                                          recipients=['test1@blk.com'],
                                                          sender='test_sender@blk.com',
                                                          username='test_user',
                                                          host='blk.com',
                                                          cc=['test2@blk.com', 'test3@blk.com'])
            self.assertIsNotNone(context.exception.message)


class TestCommonNotificationsEmailWithoutHost(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_email_pwd_without_default_host.yaml",
            "defaultWebServer": "http://dummy.dws.com",
        })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.notifications import email_notifications
        self.test_subject = email_notifications
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('email.mime.base.MIMEBase')
    @mock.patch('email.encoders')
    @mock.patch('email.mime.multipart.MIMEMultipart')
    @mock.patch('aladdinsdk.config.user_settings')
    def test_email_notification_valid(self, mimebase, encoders, mimemultipart, usersettings):
        # email notification without cc and attachments
        with mock.patch('smtplib.SMTP', autospec=True) as mocked_smtp:
            self.test_subject.send_email_notification('test subject', 'test content', ['test1@blk.com'],
                                                      'jbond@blk.com', 'jbond', 'test_pwd',  'blk.com')
            mocked_smtp.assert_called()
            context = mocked_smtp.return_value.__enter__.return_value
            context.starttls.assert_called()
            context.login.assert_called_with('jbond', 'test_pwd')
            context.sendmail.assert_called()

        with mock.patch('smtplib.SMTP', autospec=True) as mocked_smtp:
            with self.assertRaises(AsdkEmailNotificationException) as context:
                self.test_subject.send_email_notification('test subject',
                                                          'test content',
                                                          ['test1@blk.com'],
                                                          attachments=['file_path.py'])
            self.assertIsNotNone(context.exception.message)
