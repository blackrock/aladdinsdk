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

from aladdinsdk.common.error.asdkerrors import AsdkSetupException, AsdkEmailNotificationException, AsdkExportDataException

_logger = logging.getLogger(__name__)


class AsdkInternalExceptionHandler(AbstractAsdkExceptionHandler):
    """
    Exceptions that occur during AladdinSDK's internal operational logic

    Args:
        Exception (_type_): _description_
    """
    supported_exception_modules = [
        AsdkSetupException,
        AsdkExportDataException,
        AsdkEmailNotificationException
    ]

    original_exception = None

    error_code = AsdkErrorCode.AE001

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def handle_error(self):
        _logger.error(f"{self.original_exception} occurred. Error code {self.error_code}")
        if exception_type_matches(AsdkExportDataException, self.original_exception):
            _logger.warning("ASDK Utility Exception: Export Data")
            raise self.original_exception
        elif exception_type_matches(AsdkEmailNotificationException, self.original_exception):
            _logger.warning("ASDK Utility Exception: Email Notification")
            raise self.original_exception
        else:
            _logger.warning("Unhandled ASDK Internal Exception.")
            raise self.original_exception
