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

from aladdinsdk.config import user_settings
from aladdinsdk.common.retry.utils import create_retry_decorator, create_retry_wait_strategy, create_retry_stop_strategy

_api_retry_wait = create_retry_wait_strategy(user_settings.get_api_retry_wait_fixed())

_api_retry_stop = create_retry_stop_strategy(user_settings.get_api_retry_stop_after_delay(), user_settings.get_api_retry_stop_after_attempt())

api_retry = create_retry_decorator(_api_retry_wait, _api_retry_stop)
