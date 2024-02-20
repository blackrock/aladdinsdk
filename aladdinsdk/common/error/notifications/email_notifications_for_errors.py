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

import traceback
from aladdinsdk.common.error.asdkerrors import AsdkEmailNotificationException, AsdkSetupException
from aladdinsdk.common.notifications.email_notifications import send_email_notification
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload


@dynamic_asdk_config_reload
def email_notification_for_exception(original_exception):
    """
    Given email notifications are enabled, send an email for the original exception
    Email notification settings are picked up from the aladdinsdk config file

    Args:
        original_exception (_type_, required): Client Id for Oauth Application

    Returns:
        bool: True if email successfully sent
    """
    if type(original_exception).__name__ in user_settings.get_error_handling_email_notifications_exception_types():
        _send_email_notification_for_exception(original_exception,
                                               user_settings.get_error_handling_email_notifications_to(),
                                               user_settings.get_notifications_email_sender(),
                                               user_settings.get_notifications_email_username(),
                                               user_settings.get_notifications_email_password(),
                                               user_settings.get_notifications_email_host())


def _send_email_notification_for_exception(original_exception, recipients, sender, username, password, host):
    try:
        email_subject = "{0} occurred when running the SDK".format(type(original_exception).__name__)
        send_email_notification(email_subject,
                                _format_error_message(original_exception),
                                recipients,
                                sender,
                                username,
                                password,
                                host)
    except (AsdkSetupException, AsdkEmailNotificationException) as e:
        raise AsdkEmailNotificationException("Unable to send email notification for exception", e)


def _format_error_message(original_exception):
    return "Error message: [{0}]. Stacktrace: [{1}]".format(str(original_exception), str(traceback.format_exc()))
