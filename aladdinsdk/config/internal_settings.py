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

from aladdinsdk.config.asdkconf import AsdkConf, dynamic_asdk_config_reload

# Path to configurations in internal settings
_conf_key_internal_api_allow_list = "CODEGEN_API_SETTINGS.ALLOW_LIST"


# Internal API allow list
@dynamic_asdk_config_reload
def get_api_allow_list():
    return AsdkConf.get(_conf_key_internal_api_allow_list)
