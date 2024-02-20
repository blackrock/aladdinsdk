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

from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, AsdkErrorCode, exception_type_matches

from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkEmailNotificationException, AsdkExportDataException
from aladdinsdk.common.error.asdkerrors import AsdkOAuthException, AsdkSetupException

_logger = logging.getLogger(__name__)


class AsdkInternalExceptionHandler(AbstractAsdkExceptionHandler):
    """
    Exceptions that occur during AladdinSDK's internal operational logic

    Args:
        Exception (_type_): _description_
    """
    supported_exception_modules = [
        AsdkSetupException,
        AsdkApiException,
        AsdkExportDataException,
        AsdkEmailNotificationException,
        AsdkOAuthException
    ]

    original_exception = None

    error_code = AsdkErrorCode.AE001

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def handle_error(self):
        _logger.error(f"{self.original_exception} occurred. Error code {self.error_code}")
        if exception_type_matches(AsdkApiException, self.original_exception):
            _logger.info("ASDK Exception Handler Notes:\n\
            For missing credentials related errors:\n\
                Check AladdinSDK documentation around how to pass in authentication details.\n\
                Ensure user configuration file or environment variables are set appropriately.\n\
            To further understand API calls: Use SDK's API related introspection methods to see supported APIs and endpoints:\n\
                aladdinsdk.api.get_api_names - lists all SDK supported APIs \n\
                aladdinsdk.api.AladdinAPI().get_api_endpoint_methods - lists all endpoints that can be called on an API instance \n\
                aladdinsdk.api.AladdinAPI().get_api_endpoint_signature - describes signature of API")
            _logger.warning("SDK cannot automatically remedy this exception. Raising exception for caller to handle.")
            raise self.original_exception
        elif exception_type_matches(AsdkExportDataException, self.original_exception):
            _logger.warning("ASDK Utility Exception: Export Data")
            raise self.original_exception
        elif exception_type_matches(AsdkEmailNotificationException, self.original_exception):
            _logger.warning("ASDK Utility Exception: Email Notification")
            raise self.original_exception
        elif exception_type_matches(AsdkOAuthException, self.original_exception):
            _logger.warning("ASDK OAuth Exception: For oauth related errors: \n\
                         Confirm OAuth client and refresh token secrets are valid. \n \
                         Check AladdinSDK documentation around how to pass in OAuth authentication details. \n\
                         Ensure OAuth configuration file or environment variables are set appropriately.")
            raise self.original_exception
        else:
            _logger.warning("Unhandled ASDK Internal Exception.")
            raise self.original_exception
