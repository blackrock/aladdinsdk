import time
import logging

from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig, RateLimitRegistry
from aladdinsdk.common.ratelimiting.config_provider import (
    RateLimitConfigProvider,
    StaticRateLimitConfigProvider,
)
from aladdinsdk.config import user_settings

_logger = logging.getLogger(__name__)

# Module-level singleton registry instance
_rate_limit_registry = RateLimitRegistry()


def resolve_rate_limit_config(api_name, endpoint_method, user_config):
    """
    Resolve rate limit config for a specific endpoint from user settings.

    :param api_name: Name of the API
    :type api_name: str
    :param endpoint_method: Name of the endpoint method
    :type endpoint_method: str
    :param user_config: Rate limit config from user settings file (may be None)
    :type user_config: RateLimitConfig or None

    :returns: Resolved rate limit config, or None if no config applies
    :rtype: RateLimitConfig or None
    """
    return user_config


def _is_api_rate_limiting_disabled(overrides, api_name):
    """
    Check whether rate limiting is disabled for a given API in the user overrides.

    :param overrides: User override configuration dict (may be None or non-dict)
    :type overrides: dict or None
    :param api_name: Name of the API
    :type api_name: str

    :returns: True if rate limiting is explicitly disabled for this API
    :rtype: bool
    """
    if not isinstance(overrides, dict) or api_name not in overrides:
        return False
    api_override = overrides[api_name]
    return isinstance(api_override, dict) and not api_override.get('enabled', True)


def _is_endpoint_rate_limiting_disabled(overrides, api_name, endpoint_method):
    """
    Check whether rate limiting is disabled for a specific endpoint in the user overrides.

    :param overrides: User override configuration dict (may be None or non-dict)
    :type overrides: dict or None
    :param api_name: Name of the API
    :type api_name: str
    :param endpoint_method: Name of the endpoint method
    :type endpoint_method: str

    :returns: True if rate limiting is explicitly disabled for this endpoint
    :rtype: bool
    """
    if not isinstance(overrides, dict) or api_name not in overrides:
        return False
    api_override = overrides[api_name]
    if not isinstance(api_override, dict):
        return False
    endpoints_override = api_override.get('endpoints', {})
    if not isinstance(endpoints_override, dict) or endpoint_method not in endpoints_override:
        return False
    ep_override = endpoints_override[endpoint_method]
    return isinstance(ep_override, dict) and not ep_override.get('enabled', True)


def build_rate_limit_configs(api_name, endpoint_methods):
    """
    Build the rate limit config map for all endpoints of a given API.
    Fetches configs from user settings, then resolves them per-endpoint.

    :param api_name: Name of the API
    :type api_name: str
    :param endpoint_methods: List of endpoint method names for this API
    :type endpoint_methods: list[str]

    :returns: Mapping of endpoint method name to resolved RateLimitConfig
    :rtype: dict[str, RateLimitConfig]
    """
    # Check global rate limiting toggle
    if not user_settings.get_api_rate_limiting_enabled():
        _logger.debug("Rate limiting is globally disabled via configuration.")
        return {}

    # Check per-API enabled flag from user overrides
    overrides = user_settings.get_api_rate_limiting_overrides()
    if _is_api_rate_limiting_disabled(overrides, api_name):
        _logger.debug(f"Rate limiting disabled for API '{api_name}' via configuration.")
        return {}

    # Fetch from user settings provider
    static_provider = StaticRateLimitConfigProvider()
    user_configs = static_provider.fetch_rate_limits(api_name)

    # Resolve per endpoint
    result = {}
    for ep in user_configs:
        if ep not in endpoint_methods:
            _logger.debug(f"Rate limit config for '{ep}' does not match any known endpoint method, skipping.")
            continue

        if _is_endpoint_rate_limiting_disabled(overrides, api_name, ep):
            _logger.debug(f"Rate limiting disabled for endpoint '{api_name}.{ep}' via configuration.")
            continue

        resolved = resolve_rate_limit_config(
            api_name, ep,
            user_configs.get(ep, None)
        )
        if resolved is not None:
            result[ep] = resolved

    return result


def wait_for_rate_limit(api_name, endpoint_method, config):
    """
    Block until a rate-limit slot is available for the given endpoint, then acquire it.

    :param api_name: Name of the API
    :type api_name: str
    :param endpoint_method: Name of the endpoint method
    :type endpoint_method: str
    :param config: Rate limit configuration for this endpoint
    :type config: RateLimitConfig
    """
    while not _rate_limit_registry.acquire(api_name, endpoint_method, config):
        wait_time = _rate_limit_registry.time_until_reset(api_name, endpoint_method, config)
        _logger.info(
            f"Rate limit reached for {api_name}.{endpoint_method} "
            f"({config.max_calls} calls per {config.window_seconds}s). "
            f"Buffering call, will retry in {wait_time:.2f}s."
        )
        time.sleep(wait_time)


def execute_with_rate_limit(api_name, endpoint_method, config, callable_fn, *args, **kwargs):
    """
    Execute a callable with rate limit enforcement. If the rate limit is reached,
    blocks until the current window resets, then executes the call.

    :param api_name: Name of the API
    :type api_name: str
    :param endpoint_method: Name of the endpoint method
    :type endpoint_method: str
    :param config: Rate limit configuration for this endpoint
    :type config: RateLimitConfig
    :param callable_fn: The function to execute
    :type callable_fn: callable
    :param args: Positional arguments for the callable
    :param kwargs: Keyword arguments for the callable

    :returns: Result of the callable execution
    :rtype: Any
    """
    while not _rate_limit_registry.acquire(api_name, endpoint_method, config):
        wait_time = _rate_limit_registry.time_until_reset(api_name, endpoint_method, config)
        _logger.info(
            f"Rate limit reached for {api_name}.{endpoint_method} "
            f"({config.max_calls} calls per {config.window_seconds}s). "
            f"Buffering call, will retry in {wait_time:.2f}s."
        )
        time.sleep(wait_time)

    return callable_fn(*args, **kwargs)


def get_rate_limit_registry():
    """
    Get the module-level singleton RateLimitRegistry instance.

    :returns: The global rate limit registry
    :rtype: RateLimitRegistry
    """
    return _rate_limit_registry
