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

import logging
import os
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import ENV_VAR_ASDK_USER_CONFIG_FILE

# Import these attributes into other files as needed to
# identify the project version at runtime.
try:
    from .version import git_revision as __git_revision__
    from .version import version as __version__
except ImportError:
    __git_revision__ = 'Unknown'
    __version__ = 'Unknown'


def set_stream_logger(name='aladdinsdk', level=logging.DEBUG, format_string=None):
    """
    Add a stream handler for the given name and level to the logging module.
    By default, this logs all aladdinsdk messages to ``stdout``.
        >>> import aladdinsdk
        >>> aladdinsdk.set_stream_logger('aladdinsdk', logging.INFO)
    For debugging purposes a good choice is to set the stream logger to ``''``
    which is equivalent to saying "log everything".
    .. WARNING::
       Be aware that when logging trace will appear in your logs.
       If your payload contain sensitive data this should not
       be used in production.
    :type name: string
    :param name: Log name
    :type level: int
    :param level: Logging level, e.g. ``logging.INFO``
    :type format_string: str
    :param format_string: Log message format
    """
    if format_string is None:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(message)s"

    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


# Set up logging to ``/dev/null`` like a library is supposed to.
# https://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
class NullHandler(logging.Handler):
    def emit(self, record):
        pass


logging.getLogger('aladdinsdk').addHandler(NullHandler())

# Add set stream loggers and logging level is read from user_config
user_settings_log_level = user_settings.get_log_level()
set_stream_logger(level=user_settings_log_level)
logger = logging.getLogger(__name__)
logger.debug(f"Log Level set using user settings ::{user_settings_log_level}")


def zen():
    import this  # noqa: F401


# If user hasn't set a config file
if os.environ.get(ENV_VAR_ASDK_USER_CONFIG_FILE, None) is None:
    logger.debug(f"{ENV_VAR_ASDK_USER_CONFIG_FILE} environment variable not set.")
    logger.debug("Hint: Use aladdinsdk.config.create_user_config_file_template() to get started.")
