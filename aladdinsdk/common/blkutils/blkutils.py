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
import requests
import logging

_logger = logging.getLogger(__name__)

_adc_primary_location_files_dat_key = "SNOWFLAKE_DSWRITE"
_aladdin_studio_kc_sources_file_dat_key = "ALADDIN_STUDIO_KC_SOURCES"
STUDIO_KC_SOURCE_ALADDINSDK = "ALADDINSDK"
KC_GUIDE_PATH = "{}/apps/studio/knowledge-center/get-started-with-aladdinsdk"
DEFAULT_WEB_SERVER = os.environ.get('defaultWebServer')


def get_adc_account_private_link():
    """
    Get the ADC snowflake account link for a client environment

    Returns:
        String: snowflake account link
    """
    adc_primary = get_files_dat_token_value(_adc_primary_location_files_dat_key)
    if adc_primary is not None:
        sf_account = adc_primary + ".privatelink"
        return sf_account
    else:
        _logger.warning("Unable to deduce primary ADC account from files.dat. Try setting account information in SDK configuration.")
        return None


# generic function to read files.dat tokens from url
def get_files_dat_token_value(token_key, default=None):
    """
    Generic function to read files.dat tokens from default web server url

    Args:
        token_key (_type_, required): token key to be read from files.dat
        default (_type_, optional): default value in case token value is not found

    Returns:
        String: token value
    """
    try:
        r = requests.get(DEFAULT_WEB_SERVER + '/std/files.dat')
        val = [p.split('\t')[1].strip() for p in r.text.split('\n') if (len(p.split('\t')) > 1 and p.split('\t')[0].strip() == token_key)]
        return val[0] if len(val) > 0 else default
    except Exception:
        _logger.warning("BlackRock default web server is not set or files.dat tokens unavailable.")
        return default


def render_help_documentation_message():
    kc_guide_link = KC_GUIDE_PATH.format(DEFAULT_WEB_SERVER)
    token_list = get_files_dat_token_value(_aladdin_studio_kc_sources_file_dat_key)
    if token_list is not None and STUDIO_KC_SOURCE_ALADDINSDK in token_list.upper().split(","):
        return f"Please check [knowledge center guide] {kc_guide_link} or README.md for more information"
    else:
        return "Please check README.md for more information"


SDK_HELP_MESSAGE_SUFFIX = render_help_documentation_message()
