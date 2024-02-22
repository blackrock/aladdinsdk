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

from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed
import logging

_logger = logging.getLogger(__name__)


def log_retry_failure(retry_state):
    _logger.log(logging.ERROR, 'Retrying %s: attempt %s ended with: %s',
                retry_state.fn, retry_state.attempt_number, retry_state.outcome)
    raise retry_state.outcome.exception()


def skip_retry(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner


def create_retry_wait_strategy(retry_wait_fixed):
    retry_wait_strategy = None
    if retry_wait_fixed is not None:
        retry_wait_strategy = wait_fixed(retry_wait_fixed)
    return retry_wait_strategy


def create_retry_stop_strategy(retry_stop_after_delay, retry_stop_after_attempt):
    retry_stop_strategy = None
    if retry_stop_after_delay is not None and retry_stop_after_attempt is not None:
        retry_stop_strategy = (stop_after_delay(retry_stop_after_delay) | stop_after_attempt(retry_stop_after_attempt))
    elif retry_stop_after_delay is None and retry_stop_after_attempt is not None:
        retry_stop_strategy = (stop_after_attempt(retry_stop_after_attempt))
    elif retry_stop_after_delay is not None and retry_stop_after_attempt is None:
        retry_stop_strategy = (stop_after_delay(retry_stop_after_delay))
    return retry_stop_strategy


def create_retry_decorator(retry_wait_strategy, retry_stop_strategy):
    retry_decorator = None
    if retry_wait_strategy is not None and retry_stop_strategy is not None:
        retry_decorator = retry(wait=retry_wait_strategy, stop=retry_stop_strategy, retry_error_callback=log_retry_failure)
    elif retry_wait_strategy is None and retry_stop_strategy is not None:
        retry_decorator = retry(stop=retry_stop_strategy, retry_error_callback=log_retry_failure)
    elif retry_wait_strategy is not None and retry_stop_strategy is None:
        retry_decorator = retry(wait=retry_wait_strategy, retry_error_callback=log_retry_failure)
    else:
        retry_decorator = skip_retry
    return retry_decorator
