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

import os
import importlib
import pkgutil
import pathlib
import aladdinsdk.config.internal_settings as internal_settings
from aladdinsdk.common.error.asdkerrors import AsdkApiException
import logging

_logger = logging.getLogger(__name__)

_DOMAIN_SDK_PACKAGE_NAME_PREFIX = 'asdk_plugin'
_DOMAIN_SDK_API_REGISTRY_MODULE = 'api_registry'


class AladdinAPICodegenDetails:
    """
    This class stores details about an API codegen entry in a registry to facilitate look up
    """
    def __init__(self, api_name, api_version, api_module_path, host_url_path, swagger_file_path):
        self.api_name = api_name
        self.api_version = api_version
        self.api_module_path = api_module_path
        self.host_url_path = host_url_path.strip("/")
        self.swagger_file_path = swagger_file_path

        self.api_class_name = "Default" + api_name
        self.api_client = importlib.import_module(api_module_path).ApiClient
        self.api_configuration = importlib.import_module(api_module_path).Configuration
        self.api_default_class = getattr(importlib.import_module(api_module_path), self.api_class_name)

        # list callable endpoint methods, list out all methods in the class except private (starts with '_') or helpers (ends with '_with_http_info')
        self.api_class_methods = list(filter(lambda m: not (m.startswith('_') or m.endswith('_with_http_info')), dir(self.api_default_class)))


def get_api_names():
    # map dict keys to string
    return [x for x in AladdinAPIRegistry.keys()]


def get_api_details(api_name, api_version=None) -> AladdinAPICodegenDetails:
    if api_name not in list(AladdinAPIRegistry.keys()):
        raise AsdkApiException("API not supported for SDK calls at the moment.")

    if api_version is not None:
        return AladdinAPIRegistry[api_name][api_version]
    else:
        # return latest version of API
        api_versions = [x for x in AladdinAPIRegistry[api_name].keys()]
        api_versions.sort()  # Current versioning is only at major level.
        # For semantic versioning use api_versions.sort(key=lambda s: list(map(int, s.replace("v", "").split('.'))))
        if len(api_versions) > 1:
            latest_version = api_versions[:-1][0]
        else:
            latest_version = api_versions[0]  # final entry in sorted list is latest version
        return AladdinAPIRegistry[api_name][latest_version]


# This is a multi-level dictionary storing versioned APIs in the following structure:
# registry = {
#    API_1: {
#       v1: API_1_v1_Details(),
#       v2: API_1_v2_Details(),
#       v3: API_1_v2_Details()
#    },
#    API_2: {
#       v1: API_2_v1_Details(),
#       v2: API_2_v2_Details(),
#       v3: API_3_v3_Details()
#    }
# }
AladdinAPIRegistry = {}
_sdk_supported_apis = []

# AladdinSDK internal API registry
_internal_apis = internal_settings.get_api_allow_list()
_sdk_root_dir = os.path.join(pathlib.Path(__file__).parent.parent.parent)
for internal_api_detail in _internal_apis:
    if 'swagger_file_path' not in internal_api_detail:
        try:
            # API codegen performed for SDK's internally onboarded APIs - swagger files will be under _sdk_root_dir relative to the module
            relative_api_module_path = internal_api_detail['api_module_path'].replace(".", "/")
            swagger_file_path = pathlib.Path(_sdk_root_dir, relative_api_module_path, "swagger.json")
            internal_api_detail['swagger_file_path'] = swagger_file_path
        except Exception:
            _logger.debug(f"Unable to add swagger file path for API entry: {internal_api_detail}")
    _sdk_supported_apis.append(internal_api_detail)

# Domain SDK registry - find any modules with prefix asdk, then invoke fetch_api_details_for_asdk
for asdk_module in [x.name for x in list(pkgutil.iter_modules()) if x.name.startswith(_DOMAIN_SDK_PACKAGE_NAME_PREFIX)]:
    try:
        _api_reg_module = importlib.import_module(f"{asdk_module}.{_DOMAIN_SDK_API_REGISTRY_MODULE}")
        # Prioritize APIs already onboarded via internal settings
        for domain_api in [y for y in _api_reg_module.fetch_api_details_for_asdk() if y not in _sdk_supported_apis]:
            _sdk_supported_apis.append(domain_api)
    except Exception:
        _logger.warning(f"Unable to read a domain plugin for {asdk_module}. APIs under this domain may not be available accurately.")

# Final API registry build with consolidated list
_reg_failed_counter = 0
for ae in _sdk_supported_apis:
    try:
        _api_name = ae['api_name']
        _api_version = ae['api_version']
        _api_codegen_detail = AladdinAPICodegenDetails(ae['api_name'],
                                                       ae['api_version'],
                                                       ae['api_module_path'],
                                                       ae['host_url_path'],
                                                       ae['swagger_file_path'])

        if ae['api_name'] not in AladdinAPIRegistry.keys():
            AladdinAPIRegistry[_api_name] = {
                _api_version: _api_codegen_detail
            }
        else:  # an entry already exists
            if _api_version not in AladdinAPIRegistry[_api_name].keys():
                AladdinAPIRegistry[_api_name][_api_version] = _api_codegen_detail
    except Exception as ex:
        _reg_failed_counter += 1
        _logger.debug(ex)
if _reg_failed_counter > 0:
    _logger.debug("Internal SDK setup warning. Unable to fully setup API registry. Potentially malformed allow list.")
