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
from aladdinsdk.common.blkutils.blkutils import SDK_HELP_MESSAGE_SUFFIX

from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, AsdkErrorCode, exception_type_matches

from aladdinsdk.config import user_settings
from aladdinsdk.common.secrets import keyringutil

from pydantic.error_wrappers import ValidationError

_logger = logging.getLogger(__name__)


class APIExceptionHandler(AbstractAsdkExceptionHandler):  # e001
    """
    Exceptions raised by API wrapper

    Args:
        AsdkException (_type_): _description_
    """

    _api_call_unauthorized_exception_wildcard = "aladdinsdk.api.codegen.*UnauthorizedException"

    supported_exception_modules = [
        _api_call_unauthorized_exception_wildcard,
        ValidationError
        ]

    original_exception = None

    error_code = AsdkErrorCode.AE002

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def handle_error(self):
        if exception_type_matches(self._api_call_unauthorized_exception_wildcard, self.original_exception):
            self._handle_unauthorized_exception()
        elif exception_type_matches(ValidationError, self.original_exception):
            self._handle_pydantic_validation_error()

    # Helper methods to handle specific types of errors

    def _handle_unauthorized_exception(self):
        if user_settings.get_run_mode() == user_settings.CONF_RUN_MODE_LOCAL \
           and user_settings.get_user_password() is None \
           and user_settings.get_api_auth_type() == user_settings.CONF_API_AUTH_TYPE_BASIC_AUTH:
            _logger.warning("UnauthorizedException occurred while running locally. "
                            "Could be invalid credential stored in OS Credential Manager. "
                            "Deleting entry using 'keyring'. Re-enter password for next attempt.")
            keyringutil.delete_user_password()
        else:
            _logger.warning("UnauthorizedException occurred while attempting to run AladdinSDK API client instance. "
                            f"AladdinSDK-APIException unable to handle error. {SDK_HELP_MESSAGE_SUFFIX} on settings up "
                            "proper authentication for AladdinSDK")
            raise self.original_exception

    def _handle_pydantic_validation_error(self):
        _logger.error(f"API request and/or response objects failed schema validation. Error: {self.original_exception}")
        _logger.info("Tip: Use SDK's API related introspection methods or refer API documentation for more information.")
        raise self.original_exception
