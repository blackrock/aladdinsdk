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

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import smtplib
import ssl
from aladdinsdk.common.error.asdkerrors import AsdkEmailNotificationException
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload

_logger = logging.getLogger(__name__)


@dynamic_asdk_config_reload
def send_email_notification(subject: str,
                            message: str,
                            recipients: list = user_settings.get_notifications_email_to(),
                            sender: str = user_settings.get_notifications_email_sender(),
                            username: str = user_settings.get_notifications_email_username(),
                            password: str = user_settings.get_notifications_email_password(),
                            host: str = user_settings.get_notifications_email_host(),
                            **kwargs):
    """
    Send an email notification using SMTP

    Args:
        Required:
        subject (String): email subject
        message (String): email content
        recipients (List<String>): list of users to send email
        sender (String): used in the sender field for the email
        username (String): used to login to email
        password (String): used to login to email
        host (String): email host
        Optional:
        cc (List<String>): list of users to add as cc for email
        attachments (List<String>): files to attach to email

    Raises:
        AsdkEmailNotificationException: _description_

    Returns:
        bool: True if email was successfully sent
    """
    try:
        email_msg = _create_email_msg(username, password, sender, recipients, subject, message, **kwargs)
        email_host = _get_email_host(host)
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        _logger.info(f"Preparing to send email notification by [username: {user_settings.get_username()}]")
        _send_email(context, email_host, email_msg, username, password)
        return True
    except (smtplib.SMTPResponseException, TypeError, OSError, AsdkEmailNotificationException) as e:
        raise AsdkEmailNotificationException(e)


def _send_email(context, email_host, email_msg, username, password):
    """
    Initializes smtp with host to send email notification

    Args:
        context (SSLContext): ssl.PROTOCOL_TLSv1_2
        email_host (String): host for sending email
        email_msg (MIMEMultipart): email message to be sent
        username (String): used as sender of email
        password (String): used to initialize blk smtp email client
    """
    with smtplib.SMTP(email_host) as smtp:
        smtp.starttls(context=context)
        smtp.login(username, password)
        if email_msg['Cc'] is None:
            smtp.sendmail(email_msg['From'], email_msg['To'].split(','), email_msg.as_string())
        else:
            smtp.sendmail(email_msg['From'], email_msg['To'].split(',') + email_msg['Cc'].split(','), email_msg.as_string())
        _logger.info(f"Email notification successfully sent by [username: {user_settings.get_username()}]")


def _get_email_host(host):
    """
    Get server to use for email.
    User can pass in host in function call or define it in the configuration

    Args:
        host (String): email host

    Returns:
        String: email host
    """
    if host is not None:
        return host
    email_host = user_settings.get_notifications_email_host()
    _logger.info(f"[Email host: {email_host}]")
    if email_host is None:
        raise AsdkEmailNotificationException("Missing argument: No smtp host defined for sending email notifications")
    return email_host


def _create_email_msg(username, password, sender, recipients, subject=None, message=None, **kwargs):
    """
    Construct email message

    Args:
        username (String): to login to email
        password (String): to login to email
        sender (String): to use as sender of the email
        recipients (List<String>): list of users to send email
        cc (List<String>): list of users to add as cc for email
        subject (String): email subject
        message (String): email content
        attachments (List<String>): files to attach to email

    Raises:
        AsdkEmailNotificationException: For missing arguments

    Returns:
        MIMEMultipart: email message
    """
    if sender is None or recipients is None:
        raise AsdkEmailNotificationException("Missing argument: No sender/recipients defined for sending email notification")
    if username is None or password is None:
        raise AsdkEmailNotificationException("Missing argument: No username/password defined for logging into email for sending notification")
    email_msg = MIMEMultipart('alternative')
    email_msg['From'] = sender
    email_msg['To'] = ",".join(recipients)
    if 'cc' in kwargs and kwargs['cc'] is not None:
        email_msg['cc'] = ",".join(kwargs['cc'])
    if subject is not None:
        email_msg['Subject'] = subject
    if message is not None:
        content = MIMEText(message, 'html')
        email_msg.attach(content)
    if 'attachments' in kwargs and kwargs['attachments'] is not None:
        _attach_files_to_email(email_msg, kwargs['attachments'])
    _logger.info("Completed email message construction")
    return email_msg


def _attach_files_to_email(email_msg, attachments):
    """
    Add attachments to the email message

    Args:
        email_msg: MIMEMultipart
        attachments (List<String>): files to attach to email

    Raises:
        AsdkEmailNotificationException: For inability to read or encode file content
    """
    try:
        for file in attachments:
            attachment = open(file, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % file)
            email_msg.attach(part)
        _logger.info("Completed adding attachments to email")

    except (OSError, UnicodeEncodeError) as e:
        raise AsdkEmailNotificationException(e)
