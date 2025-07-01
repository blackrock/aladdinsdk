import json
import os
from unittest import TestCase, mock

from aenum import Enum
from aladdinsdk.common.notifications import studio_notifications


class TestStudioNotification(TestCase):
    def setUp(self):
        self.valid_action = 'STUDIO_NOTIFICATION_ACTION_SMTP'
        self.valid_event_type = 'STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE'
        self.valid_entity_type = 'STUDIO_ENTITY_TYPE_USER'
        self.valid_event_name = 'test_event'
        self.valid_entity_name = 'test_entity'
        self.valid_user = 'test_user@blackrock.com'

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    @mock.patch('aladdinsdk.common.notifications.studio_notifications.user_settings')
    def test_init_valid(self, mock_user_settings, mock_api):
        mock_user_settings.get_notifications_studio_action.return_value = self.valid_action
        mock_user_settings.get_notifications_studio_event_name.return_value = self.valid_event_name
        mock_user_settings.get_notifications_studio_event_type.return_value = self.valid_event_type
        mock_user_settings.get_notifications_studio_entity_name.return_value = self.valid_entity_name
        mock_user_settings.get_notifications_studio_entity_type.return_value = self.valid_entity_type
        mock_user_settings.get_username.return_value = self.valid_user
        notif = studio_notifications.StudioNotification()
        self.assertEqual(notif.notification_action, self.valid_action)
        self.assertEqual(notif.notification_event_name, self.valid_event_name)
        self.assertEqual(notif.notification_event_type, self.valid_event_type)
        self.assertEqual(notif.studio_entity_name, self.valid_entity_name)
        self.assertEqual(notif.studio_entity_type, self.valid_entity_type)
        self.assertEqual(notif.user, self.valid_user)

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.get_files_dat_token_value')
    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_create_subscription_valid(self, mock_api, mock_get_token):
        notif = studio_notifications.StudioNotification(
            notification_action=self.valid_action,
            notification_event_name=self.valid_event_name,
            notification_event_type=self.valid_event_type,
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        mock_get_token.return_value = '@blackrock.com'
        recipients = ['foo@blackrock.com']
        notif.studio_subscription_api.post = mock.Mock(return_value={'result': 'ok'})
        notif.create_subscription(recipients)
        notif.studio_subscription_api.post.assert_called()

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.get_files_dat_token_value')
    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_create_subscription_invalid_email(self, mock_api, mock_get_token):
        notif = studio_notifications.StudioNotification(
            notification_action=self.valid_action,
            notification_event_name=self.valid_event_name,
            notification_event_type=self.valid_event_type,
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        mock_get_token.return_value = '@blackrock.com'
        recipients = ['foo@notallowed.com']
        notif.studio_subscription_api.post = mock.Mock()
        notif.create_subscription(recipients)
        notif.studio_subscription_api.post.assert_not_called()

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_send_notification(self, mock_api):
        notif = studio_notifications.StudioNotification(
            notification_action=self.valid_action,
            notification_event_name=self.valid_event_name,
            notification_event_type=self.valid_event_type,
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        notif.studio_notification_api.post = mock.Mock(return_value={'result': 'sent'})
        notif.send_notification('subject', 'message', {'meta': 'data'})
        notif.studio_notification_api.post.assert_called()

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.StudioNotification')
    def test_send_studio_smtp_notification(self, mock_studio_notif):
        instance = mock_studio_notif.return_value
        recipients = ['foo@blackrock.com']
        subject = 'Test Subject'
        message = 'Test Message'
        metadata = {'foo': 'bar'}
        studio_notifications.send_studio_smtp_notification(recipients, subject, message, metadata)
        instance.create_subscription.assert_called_with(recipients)
        instance.send_notification.assert_called_with(subject, message, metadata)

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.get_files_dat_token_value')
    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_create_subscription_no_recipients(self, mock_api, mock_get_token):
        notif = studio_notifications.StudioNotification(
            notification_action=self.valid_action,
            notification_event_name=self.valid_event_name,
            notification_event_type=self.valid_event_type,
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        mock_get_token.return_value = '@blackrock.com'
        with self.assertRaises(ValueError):
            notif.create_subscription([])

    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_send_notification_with_none_metadata(self, mock_api):
        notif = studio_notifications.StudioNotification(
            notification_action=self.valid_action,
            notification_event_name=self.valid_event_name,
            notification_event_type=self.valid_event_type,
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        notif.studio_notification_api.post = mock.Mock(return_value={'result': 'sent'})
        notif.send_notification('subject', 'message')
        notif.studio_notification_api.post.assert_called()

    @mock.patch('logging.Logger.error')
    @mock.patch('aladdinsdk.common.notifications.studio_notifications.AladdinAPI')
    def test_send_notification_with_invalid_action(self, mock_api, mock_logger_error):
        notif = studio_notifications.StudioNotification(
            notification_action="INVALID_ACTION",
            notification_event_name=self.valid_event_name,
            notification_event_type="INVALID_EVENT_TYPE",
            studio_entity_name=self.valid_entity_name,
            studio_entity_type=self.valid_entity_type,
            user=self.valid_user
        )
        notif.studio_notification_api.post = mock.Mock(return_value={'result': 'sent'})
        notif.send_notification('subject', 'message')
        expected_calls = [
            mock.call("Invalid notification action: INVALID_ACTION."),
            mock.call("Invalid notification event type: INVALID_EVENT_TYPE.")
        ]
        mock_logger_error.assert_has_calls(expected_calls)
        notif.studio_notification_api.post.assert_called()
