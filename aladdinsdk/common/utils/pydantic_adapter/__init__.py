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
from typing import Callable
import json
import re

import pydantic as pydantic_vx
from aladdinsdk.common.utils.pydantic_adapter.rest import RESTClientObject as PydanticV2RESTClientObject

import logging
_logger = logging.getLogger(__name__)

# Check here which version is installed
if pydantic_vx.VERSION.startswith("1."):
    PYDANTIC_LIB_VERSION = "v1"
    _logger.info("Setting up Aladdin SDK with Pydantic v1. Use 'asdk_plugin_*' API plugins. (switch to Pydantic v2 to use 'asdk_plugin_pydv2_*' API plugins)")

    from pydantic import (
        BaseModel,
        Field,
        StrictStr,
        StrictInt,
        StrictBool,
        ValidationError,
        validate_arguments,
        conlist,
        constr,
    )

    # regex that matches strings starting with 'asdk_plugin' but NOT 'asdk_plugin_pydv2'
    PYDANTIC_SDK_PACKAGE_NAME_REGEX = r'asdk_plugin(?!_pydv2)'

    def api_client_rest_adapter(api_client, configuration):
        pass

    # In Pydantic v1, we do not need to remove any argument
    def call_endpoint_helper_argument_pydantic_adapter(*args, **kwargs):
        return args, kwargs

    def get_endpoint_to_call(instance: object, api_endpoint_name: str, _deserialize_to_object: bool) -> Callable:
        return getattr(instance, f"{api_endpoint_name}_with_http_info")

else:
    PYDANTIC_LIB_VERSION = "v2+"
    # This section allows SDK to run in environments where pydantic v2 is installed
    _logger.info("Setting up Aladdin SDK with Pydantic v2. Use 'asdk_plugin_pydv2_*' API plugins. (switch to Pydantic v1 to use 'asdk_plugin_*' API plugins)")

    # Re-export commonly used pydantic symbols for codegen compatibility
    from pydantic.v1 import (
        BaseModel,
        Field,
        StrictStr,
        StrictInt,
        StrictBool,
        ValidationError,
        validate_arguments,
        conlist,
        constr,
    )

    # regex that matches Pydantic v2 plugin package names
    PYDANTIC_SDK_PACKAGE_NAME_REGEX = r'asdk_plugin_pydv2'

    def api_client_rest_adapter(api_client, configuration):
        # if the str(type(api_client)) contains pydv2, then we need to adapt
        # this adapts pydantic v2 clients to urllib3 without affecting pydantic v1 clients
        if re.search(PYDANTIC_SDK_PACKAGE_NAME_REGEX, str(type(api_client))):
            api_client.rest_client = PydanticV2RESTClientObject(configuration)

    # In Pydantic v2, we need to remove _preload_content argument
    def call_endpoint_helper_argument_pydantic_adapter(*args, **kwargs):
        kwargs.pop('_preload_content', None)
        return args, kwargs

    def get_endpoint_to_call(instance: object, api_endpoint_name: str, _deserialize_to_object: bool) -> Callable:
        if (not re.search(PYDANTIC_SDK_PACKAGE_NAME_REGEX, str(type(instance)))) or _deserialize_to_object:
            return getattr(instance, f"{api_endpoint_name}_with_http_info")
        else:
            def decorated_endpoint_to_call(*args, **kwargs):
                endpoint_to_call = getattr(instance, f"{api_endpoint_name}_without_preload_content")
                raw_response = endpoint_to_call(*args, **kwargs)
                response = json.loads(raw_response.data.decode('utf-8'))
                return response
            return decorated_endpoint_to_call
