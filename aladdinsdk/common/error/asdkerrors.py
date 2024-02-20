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


class AsdkSetupException(Exception):
    """
    Raised for any invalid setup action performed

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="ASDK Setup Exception", *args: object):
        self.message = message
        super().__init__(self.message, *args)


class AsdkApiException(Exception):
    """
    To be raised by AladdinSDK's internal API Wrapper implementation

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="API Wrapper Exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)


class AsdkAdcException(Exception):
    """
    To be raised by AladdinSDK's internal ADC Wrapper implementation

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="ADC Wrapper Exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)


class AsdkExportDataException(Exception):
    """
    To be raised by AladdinSDK's internal export data implementation

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="Export Data Exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)


class AsdkEmailNotificationException(Exception):
    """
    To be raised by AladdinSDK's internal email notification implementation

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="Email Notification Exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)


class AsdkTransformationException(Exception):
    """
    To be raised by utility reading, converting data from one form to another.
        String to json, json to dataset, etc.
    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)


class AsdkOAuthException(Exception):
    """
    Raised for any failed response from OAuth token end point

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="OAuth Token exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)
