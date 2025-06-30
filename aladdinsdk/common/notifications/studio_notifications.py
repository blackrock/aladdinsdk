"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from aladdinsdk.api import AladdinAPI
from aladdinsdk.api.codegen.platform.studio.studio_notification.v1.studio_subscription.models.v1_studio_entity_type import V1StudioEntityType
from aladdinsdk.api.codegen.platform.studio.studio_notification.v1.studio_subscription.models.v1_studio_notification_action import V1StudioNotificationAction
from aladdinsdk.api.codegen.platform.studio.studio_notification.v1.studio_subscription.models.v1_studio_notification_event_type import V1StudioNotificationEventType
from aladdinsdk.common.blkutils.blkutils import get_files_dat_token_value
from aladdinsdk.config import user_settings
import datetime
import logging
import uuid

_logger = logging.getLogger(__name__)


class StudioNotification():
    def __init__(self,
                 notification_action: str = None,
                 notification_event_name: str = None,
                 notification_event_type: str = None,
                 studio_entity_name: str = None,
                 studio_entity_type: str = None,
                 user: str = None,
                 **kwargs):
        """
        notification_action: (string) Action to perform for the notification. Must be in V1StudioNotificationAction values,
        notification_event_name: (string) Name of the notification event.,
        notification_event_type: (string) Type of the notification event. Must be in V1StudioNotificationEventType values,
        studio_entity_name: (string) Name of the studio entity. If not provided, a unique string using UUID and datetime will be generated,
        studio_entity_type: (string) Type of the studio entity. Must be in V1StudioEntityType values,
        auth_flow_type (string, optional): Auth Flow type for oauth token generation. Defaults to user_settings.get_auth_flow_type().
        api_key (string, optional): API Key. Defaults to value set as "ASDK_API__TOKEN" environment variable, or "api.token" in settings yaml,
            None if not configured.
        auth_type (string, optional): API Authentication Type. Must be in [BASIC_AUTH, OAUTH]
        username (string, optional): Username. Defaults to value set as "ASDK_USER_CREDENTIALS__USERNAME" environment variable,
            or "user_credentials.username" in settings yaml, None if not configured.
        password (string, optional): Password. Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD" environment variable,
            or "user_credentials.password" in settings yaml, None if not configured.
        client_id (string, optional): Client Id for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_ID" environment variable,
            or "oauth.client_id" in settings yaml, None if not configured.
        client_secret (string, optional): Client Secret for Oauth. Defaults to value set as "ASDK_OAUTH__CLIENT_SECRET" environment variable,
            or "oauth.client_secret" in settings yaml, None if not configured.
        refresh_token (string, optional): Refresh token to use for oauth token uri. Defaults to value set as "ASDK_OAUTH__REFRESH_TOKEN"
            environment variable, or "oauth.refresh_token" in settings yaml, None if not configured.
        api_access_token (string, optional): API Authentication token for Oauth. Defaults to None. If no access token provided,
            AladdinSDK will look to client id, secret and refresh token values for fetching access token
        auth_server_proxy (string, optional): API Auth Server Proxy for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_PROXY"
            environment variable, or "oauth.auth_server_proxy" in settings yaml, None if not configured.
        auth_server_url (string, optional): API Auth Server URL for Oauth. Defaults to value set as "ASDK_OAUTH__AUTH_SERVER_URL"
            environment variable, or "oauth.auth_server_url" in settings yaml, None if not configured.
        password_filepath (string, optional): Password filepath (Basic Auth). Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH"
            environment variable, or "user_credentials.password_filepath" in settings yaml, None if not configured.
        encrypted_password_filepath (string, optional): Encrypted Password filepath (Basic Auth). Defaults to value set as
            "ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH" environment variable, or "user_credentials.encrypted_password_filepath" in
            settings yaml, None if not configured.
        encryption_filepath (string, optional): Encryption filepath. Defaults to value set as "ASDK_USER_CREDENTIALS__ENCRYPTED_FILEPATH"
            environment variable, or "user_credentials.encryption_filepath" in settings yaml, None if not configured.
        """
        notification_action = notification_action or user_settings.get_notifications_studio_action()
        notification_event_name = notification_event_name or user_settings.get_notifications_studio_event_name()
        notification_event_type = notification_event_type or user_settings.get_notifications_studio_event_type()
        studio_entity_name = studio_entity_name or user_settings.get_notifications_studio_entity_name()
        studio_entity_type = studio_entity_type or user_settings.get_notifications_studio_entity_type()
        user = user or user_settings.get_username()

        self.studio_subscription_api = AladdinAPI('StudioSubscriptionAPI', **kwargs)
        self.studio_notification_api = AladdinAPI('StudioNotificationAPI', **kwargs)

        if notification_action not in V1StudioNotificationAction.__members__.values():
            _logger.error(f"Invalid notification action: {notification_action}.")
            notification_action = V1StudioNotificationAction.STUDIO_NOTIFICATION_ACTION_UNSPECIFIED
        self.notification_action = notification_action

        if notification_event_name is None or notification_event_name == "":
            raise ValueError("Notification event name must be provided/configured.")
        self.notification_event_name = notification_event_name

        if notification_event_type not in V1StudioNotificationEventType.__members__.values():
            _logger.error(f"Invalid notification event type: {notification_event_type}.")
            notification_event_type = V1StudioNotificationEventType.STUDIO_NOTIFICATION_EVENT_TYPE_UNSPECIFIED
        self.notification_event_type = notification_event_type

        if studio_entity_name is None:
            studio_entity_name = str(uuid.uuid4()) + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.studio_entity_name = studio_entity_name

        if studio_entity_type not in V1StudioEntityType.__members__.values():
            _logger.error(f"Invalid studio entity type: {studio_entity_type}. Must be one of {list(V1StudioEntityType.__members__.values())}.")
            studio_entity_type = V1StudioEntityType.STUDIO_ENTITY_TYPE_UNSPECIFIED
        self.studio_entity_type = studio_entity_type

        if user is None or user == "":
            _logger.error("User must be provided or set in user settings for Studio Notifications.")
            raise ValueError("User must be provided or set in user settings for Studio Notifications.")
        self.user = user
        _logger.debug(f"StudioNotification initialized with action: {self.notification_action}, event name: {self.notification_event_name}, " +
                      f"event type: {self.notification_event_type}, entity name: {self.studio_entity_name}, entity type: {self.studio_entity_type}, user: {self.user}")

    def create_subscription(self, recipients: list):
        """
        Create a subscription for the specified recipients to receive notifications.

        Args:
            recipients (list): List of email addresses to receive notifications.

        Raises:
            ValueError: If no recipients are provided.
        """
        if len(recipients) == 0:
            _logger.debug("No recipients provided for the notification.")
            raise ValueError("At least one recipient is required to send a notification.")

        valid_email_domains = get_files_dat_token_value('RESEARCH_EMAIL_WHITELIST', default='').split(',')
        for recipient in recipients:
            if self.notification_action == V1StudioNotificationAction.STUDIO_NOTIFICATION_ACTION_SMTP and not any(recipient.endswith(domain.strip()) for domain in valid_email_domains):
                _logger.warning(f"Skipping recipient {recipient}. Sending notification is not permitted.")
                continue
            try:
                subscription_payload = {
                    "creationDateTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    "email": recipient,
                    "studioNotificationAction": self.notification_action,
                    "studioNotificationEvent": {
                        "eventName": self.notification_event_name,
                        "studioNotificationEventType": self.notification_event_type
                    },
                    "studioNotificationScope": {
                        "studioEntityName": self.studio_entity_name,
                        "studioEntityType": self.studio_entity_type
                    },
                    "user": self.user
                }
                create_subscription_response = self.studio_subscription_api.post('/studioSubscriptions',
                                                                                 request_body=subscription_payload)
                logging.debug(f"Studio subscription created successfully: {create_subscription_response}")
            except Exception as e:
                logging.error(f"Failed to create studio subscription for {subscription_payload['email']}: {e}")
                continue

    def send_notification(self,
                          subject: str,
                          message: str,
                          metadata: dict = None):
        """
        Send a notification with the specified subject and message.

        Args:
            subject (str): Notification subject.
            message (str): Notification message.
            metadata (dict, optional): Additional metadata to include in the notification.
        """
        notification_payload = {
            "creationDateTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "notificationMessage": message,
            "notificationMetadata": metadata,
            "notificationSubject": subject,
            "sender": self.user,
            "studioNotificationEvent": {
                "eventName": self.notification_event_name,
                "studioNotificationEventType": self.notification_event_type
            },
            "studioNotificationScope": {
                "studioEntityName": self.studio_entity_name,
                "studioEntityType": self.studio_entity_type
            }
        }

        create_notification_response = self.studio_notification_api.post('/studioNotifications',
                                                                         request_body=notification_payload)
        logging.debug(f"Studio notification sent successfully: {create_notification_response}")


def send_studio_smtp_notification(recipients: list,
                                  subject: str,
                                  message: str,
                                  metadata: dict = None,
                                  **kwargs):
    """
    Send a Studio SMTP notification to the specified recipients.
    This function creates a subscription for the recipients and sends a notification with the given subject and message.

    Args:
        recipients (list): List of email addresses to receive the notification.
        subject (str): Notification subject.
        message (str): Notification message.
        metadata (dict, optional): Additional metadata to include in the notification.
    """
    notification_action = V1StudioNotificationAction.STUDIO_NOTIFICATION_ACTION_SMTP
    notification_event_name = "aladdin_sdk_notification"
    notification_event_type = V1StudioNotificationEventType.STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE
    studio_entity_name = str(uuid.uuid4()) + "_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    studio_entity_type = V1StudioEntityType.STUDIO_ENTITY_TYPE_USER

    notification = StudioNotification(notification_action, notification_event_name, notification_event_type,
                                      studio_entity_name, studio_entity_type, **kwargs)
    notification.create_subscription(recipients)
    notification.send_notification(subject, message, metadata)
