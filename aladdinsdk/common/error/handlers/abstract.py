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

from abc import ABC, abstractmethod
from enum import Enum, auto


def exception_type_matches(supported_exception_list_entry, original_exception):
    """This method checks if and exception module name and path matches an entry in the handler's supported exceptions list.
    Handlers include a list of exceptions that can be handled. Supported exceptions can be listed as one of:
        - type - exception class
        - string - a fully qualified module path
        - string - containing a wildcard to cover all modules under a given path.
        e.g.: "aladdinsdk.api.codegen.*UnauthorizedException": covers all UnauthorizedException classes under any
                API's openapi generated code under aladdinsdk.api.codegen

    Args:
        supported_exception_list_entry (type | str): exception type or name (fully qualified or partial with wildcard)
        original_exception (Exception): original exception caught by decorator

    Returns:
        boolean: True of exception matches given type
    """
    if type(supported_exception_list_entry) is type:
        return type(original_exception) is supported_exception_list_entry

    # else supported list entry is given as a string
    if "*" in supported_exception_list_entry:
        exception_module_starts_with, exception_module_name = supported_exception_list_entry.split("*")
    elif "." in supported_exception_list_entry:
        exception_module_starts_with, _, exception_module_name = supported_exception_list_entry.rpartition(".")

    exception_class_name = type(original_exception).__name__
    exception_module = type(original_exception).__module__

    return exception_module.startswith(exception_module_starts_with) and exception_class_name == exception_module_name


class AsdkErrorCode(Enum):
    AE000 = auto()  # Errors not supported by AladdinSDK
    AE001 = auto()  # Internal AladdinSDK errors
    AE002 = auto()  # API call errors
    AE003 = auto()  # ADC call errors
    AE004 = auto()  # Domain specific SDK errors


class AbstractAsdkExceptionHandler(ABC):
    """
    Abstract AladdinSDK exception class
    """

    @staticmethod
    @property
    @abstractmethod
    def supported_exception_modules():
        """
        List of exception names that are covered by this handler
        """
        pass

    @staticmethod
    @property
    @abstractmethod
    def error_code(self):
        pass

    @property
    @abstractmethod
    def original_exception(self):
        pass

    @abstractmethod
    def handle_error(self):
        """
        Implementation of this method in the specific exception handlers should attempt to safely remedy the error.
        Sufficient warnings or info logs should be provided to the end users.

        If the exception can not be handled properly, raise the original exception back for the caller to handle.
        """
        pass
