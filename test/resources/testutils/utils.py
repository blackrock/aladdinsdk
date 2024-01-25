from importlib import reload
import io


def reload_modules():
    """
    For test cases where configuration changes need to be tested, reloading modules ensures
    new configuration is picked when dynamic reload is not set in code.
    """
    import aladdinsdk
    from aladdinsdk.common.authentication import api  # noqa: F811, F401
    from aladdinsdk.common.authentication.basicauth import basicauthutil  # noqa: F811, F401
    from aladdinsdk.config import asdkconf, user_settings, internal_settings  # noqa: F811, F401
    from aladdinsdk.common.blkutils import blkutils  # noqa: F811, F401
    from aladdinsdk.common.datatransformation import conversion, conversion_options  # noqa: F811, F401

    from aladdinsdk.config import asdkconf, user_settings  # noqa: F811, F401
    from aladdinsdk.common.secrets import fsutil, keyringutil  # noqa: F811, F401
    from aladdinsdk.common.error import handler  # noqa: F811, F401
    from aladdinsdk.common.notifications import email_notifications  # noqa: F811, F401
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
