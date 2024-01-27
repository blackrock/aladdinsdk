# Sample Send Email Notifications

- Import the email notifications utility from aladdinsdk.common.notifications
- Arguments to be passed in: 
    Required:
        subject (String): email subject
        message (String): email content
        recipients (List<String>): list of users to send email
        sender (String): used in the sender field for the email
        username (String): used to login to email 
        password (String): used to login to email
        host (String): email host
    Optional (**kwargs):
        cc (List<String>): list of users to add as cc for email
        attachments (List<String>): files to attach to email

    ```py
    from aladdinsdk.common.notifications.email_notifications import send_email_notification

    # code snippet when email host, email username, email password, to and sender fields are set in the configuration file
    send_email_notification('Subject: Test Email for Notifications SDK', 'This is a sample email message', cc=['email_address'])

    # code snippet when all values are provided as function params at runtime
    send_email_notification('Subject: Test Email for Notifications SDK', 'This is a sample email message', ['list_of_recipients'], 'sender_email', 'email_username', 'email_password', 'email_host', cc=['email_address'])
    ```
