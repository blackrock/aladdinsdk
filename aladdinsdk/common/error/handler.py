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
from functools import wraps
from aladdinsdk.common.error.notifications.email_notifications_for_errors import email_notification_for_exception

from aladdinsdk.config import user_settings

from aladdinsdk.common.error.asdkerrors import AsdkSetupException
from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, exception_type_matches
from aladdinsdk.common.error.handlers.internal import AsdkInternalExceptionHandler
from aladdinsdk.common.error.handlers.api import APIExceptionHandler
from aladdinsdk.common.error.handlers.adc import ADCExceptionHandler

_logger = logging.getLogger(__name__)

_asdk_exception_handlers = [AsdkInternalExceptionHandler, APIExceptionHandler, ADCExceptionHandler]

# User settings for error handling
sdk_should_handle_errors = user_settings.get_error_handler_active()


def _exception_in_supported_list(supported_exceptions_list, original_exception):
    return any(exception_type_matches(se, original_exception) for se in supported_exceptions_list)


def _map_exception_to_handler(original_exception):
    for registered_exception in _asdk_exception_handlers:
        if _exception_in_supported_list(registered_exception.supported_exception_modules, original_exception):
            return registered_exception(original_exception)
    return None


def register_handler_class(handler_class):
    """
    Utility for domain specific SDK developers to provide additional handler classes.
    Handler classes must be an implementation of AbstractAsdkExceptionHandler, else AsdkSetupException is raised.

    Args:
        handler_class (_type_): _description_

    Raises:
        AsdkSetupException: _description_
    """
    if not issubclass(handler_class, AbstractAsdkExceptionHandler):
        raise AsdkSetupException("Unable to register provided exception handler. Must be an implementation of AbstractAsdkExceptionHandler.")

    if handler_class not in _asdk_exception_handlers:
        _asdk_exception_handlers.append(handler_class)


def asdk_exception_handler(func):
    """
    Common decorator for exceptions handled by AladdinSDK/

    For exceptions that can be handled, if the user settings configuration denotes that SDK should handle the exception,
    specific error handler class's methods would be called. If exception handler not found, exception is raised as is.

    If user settings configuration denotes that SDK should not handled the exception, any exception raised is bubbled up
    as is.

    Args:
        func (_type_): Any method in AladdinSDK which raises an exception that needs to be handled by the common AladdinSDK handler
    """
    @wraps(func)
    def _handler_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)  # Call decorated function
        except Exception as original_exception:
            if user_settings.get_error_handling_email_notifications_enabled() is True:
                email_notification_for_exception(original_exception)
            exception_handler = _map_exception_to_handler(original_exception)

            if sdk_should_handle_errors:
                if exception_handler is not None:
                    eh = _map_exception_to_handler(original_exception)
                    eh.handle_error()
                else:
                    _logger.warning("Exception handler not implemented for this type. Raising original exception for caller to handle.")
                    _logger.error(original_exception)
                    raise original_exception
            else:
                _logger.warning("Per user configuration, AladdinSDK will not attempt to resolve. Raising original exception for caller to handle.")
                _logger.error(original_exception)
                raise original_exception

    return _handler_function
