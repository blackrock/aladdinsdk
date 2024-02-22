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

from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, AsdkErrorCode
from aladdinsdk.common.error.asdkerrors import AsdkAdcException

_logger = logging.getLogger(__name__)


class ADCExceptionHandler(AbstractAsdkExceptionHandler):  # e001
    """
    Exceptions raised by ADC wrapper

    Args:
        AsdkException (_type_): _description_
    """
    supported_exception_modules = [
        AsdkAdcException
        ]

    error_code = AsdkErrorCode.AE003

    original_exception = None

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def handle_error(self):
        _logger.warning(f"Unhandled ADC Exception: {self.original_exception}")
        raise self.original_exception
