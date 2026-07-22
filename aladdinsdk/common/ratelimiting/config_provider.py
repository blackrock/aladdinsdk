import logging
from abc import ABC, abstractmethod

from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
from aladdinsdk.config import user_settings

_logger = logging.getLogger(__name__)


class RateLimitConfigProvider(ABC):
    """
    Abstract base class for rate limit configuration providers.
    Implementations are responsible for returning rate limit configurations
    keyed by endpoint method name for a given API.
    """

    @abstractmethod
    def fetch_rate_limits(self, api_name):
        """
        Fetch rate limit configurations for the given API.

        :param api_name: Name of the API
        :type api_name: str

        :returns: Mapping of endpoint method name to RateLimitConfig
        :rtype: dict[str, RateLimitConfig]
        """
        pass


class StaticRateLimitConfigProvider(RateLimitConfigProvider):
    """
    Rate limit configuration provider that reads limits from the user settings configuration file.

    Expected configuration structure in user settings YAML:
        api:
          rate_limiting:
            enabled: true
            overrides:
              <APIName>:
                enabled: true
                endpoints:
                  <endpoint_method_name>:
                    enabled: true
                    max_calls: 100
                    window_seconds: 60
    """

    def fetch_rate_limits(self, api_name):
        """
        Fetch rate limit configurations from the user settings file.

        :param api_name: Name of the API
        :type api_name: str

        :returns: Mapping of endpoint method name to RateLimitConfig
        :rtype: dict[str, RateLimitConfig]
        """
        overrides = user_settings.get_api_rate_limiting_overrides()

        if not overrides or not isinstance(overrides, dict):
            return {}

        api_overrides = overrides.get(api_name, None)
        if api_overrides is None or not isinstance(api_overrides, dict):
            return {}

        # Check per-API enabled flag
        if not api_overrides.get('enabled', True):
            return {}

        endpoints = api_overrides.get('endpoints', {})
        if not endpoints or not isinstance(endpoints, dict):
            return {}

        result = {}
        for endpoint_name, endpoint_config in endpoints.items():
            parsed = self._parse_endpoint_config(api_name, endpoint_name, endpoint_config)
            if parsed is not None:
                result[endpoint_name] = parsed

        return result

    @staticmethod
    def _parse_endpoint_config(api_name, endpoint_name, endpoint_config):
        """
        Parse a single endpoint's rate limit configuration.

        :param api_name: Name of the API (used for log messages)
        :type api_name: str
        :param endpoint_name: Name of the endpoint method
        :type endpoint_name: str
        :param endpoint_config: Raw endpoint configuration dict
        :type endpoint_config: dict

        :returns: Parsed rate limit config, or None if invalid/disabled
        :rtype: RateLimitConfig or None
        """
        if not isinstance(endpoint_config, dict):
            return None

        if not endpoint_config.get('enabled', True):
            return None

        max_calls = endpoint_config.get('max_calls', None)
        window_seconds = endpoint_config.get('window_seconds', None)

        if max_calls is None or window_seconds is None:
            return None

        try:
            return RateLimitConfig(
                max_calls=int(max_calls),
                window_seconds=int(window_seconds)
            )
        except (ValueError, TypeError):
            _logger.warning(f"Invalid rate limit config for {api_name}.{endpoint_name}, skipping.")
            return None
