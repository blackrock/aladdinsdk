from importlib import reload
import io

def reload_modules():
    import aladdinsdk
    from aladdinsdk.common.authentication import api
    from aladdinsdk.common.authentication.basicauth import basicauthutil
    from aladdinsdk.config import asdkconf, user_settings, internal_settings
    from aladdinsdk.common.blkutils import blkutils
    from aladdinsdk.common.datatransformation import conversion, conversion_options
    
    from aladdinsdk.config import asdkconf, user_settings
    from aladdinsdk.common.secrets import fsutil, keyringutil
    from aladdinsdk.common.error import handler
    from aladdinsdk.common.notifications import email_notifications
    reload(aladdinsdk)
    reload(aladdinsdk.common.authentication.api)
    reload(aladdinsdk.common.authentication.basicauth.basicauthutil)
    reload(aladdinsdk.common.blkutils.blkutils)
    reload(aladdinsdk.common.datatransformation.conversion)
    reload(aladdinsdk.common.datatransformation.conversion_options)
    reload(aladdinsdk.config.asdkconf)
    reload(aladdinsdk.config.user_settings)
    reload(aladdinsdk.config.internal_settings)
    reload(aladdinsdk.common.secrets.fsutil)
    reload(aladdinsdk.common.secrets.keyringutil)
    reload(aladdinsdk.common.error.handler)
    reload(aladdinsdk.common.notifications.email_notifications)

class UnitTestRESTResponse(io.IOBase):

    def __init__(self, resp, status, reason, raw_data):
        self.urllib3_response = resp
        self.status = status
        self.reason = reason
        self.raw_data = raw_data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)