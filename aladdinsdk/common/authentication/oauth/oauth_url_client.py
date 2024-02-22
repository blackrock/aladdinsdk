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

import requests
from typing_extensions import deprecated
from aladdinsdk.common.blkutils.blkutils import get_files_dat_token_value
from aladdinsdk.common.error.asdkerrors import AsdkOAuthException


@deprecated("Using _get_token_url_for_auth_server instead")
def retrieve_oauth_server_url():
    try:
        headers = {
            'accept': 'application/json',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded'
        }
        url = _get_url_for_auth()
        response = requests.get(url, headers=headers, verify=True)
        if response.status_code == 200:
            return _get_auth_server_url_from_response(response.json())
        else:
            raise AsdkOAuthException("Request to authentication server failed", response)
    except (requests.exceptions.RequestException) as e:
        raise AsdkOAuthException("Problem connecting to authentication server", e)


def _get_auth_server_url_from_response(response_json):
    try:
        auth_server_url = response_json["authorizationServerUri"]
        return auth_server_url
    except (AttributeError, KeyError) as e:
        raise AsdkOAuthException("Failed to retrieve oauth server url", e)


def _get_url_for_auth():
    token_auth_url = 'https://{}.com/api/oauth2/default/v1/authorize'
    client_name = get_files_dat_token_value('ClientAbbrev', 'DEV')
    if client_name == 'BLK':
        return token_auth_url.format('webster.bfm')
    else:
        return token_auth_url.format(client_name+'.blackrock')
