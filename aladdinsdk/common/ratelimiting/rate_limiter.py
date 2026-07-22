import time
import threading
import logging
from dataclasses import dataclass

_logger = logging.getLogger(__name__)


@dataclass
class RateLimitConfig:
    """
    Configuration for rate limiting a specific API endpoint.

    :param max_calls: Maximum number of calls allowed within the time window
    :type max_calls: int
    :param window_seconds: Duration of the time window in seconds
    :type window_seconds: int
    """
    max_calls: int
    window_seconds: int


class _RateLimitWindow:
    """
    Tracks the state of a rate limit window for a single (api_name, endpoint_method) key.
    """
    def __init__(self):
        self.call_count = 0
        self.window_start_time = time.monotonic()
        self.lock = threading.Lock()


class RateLimitRegistry:
    """
    Module-level singleton registry that tracks API call counts per (api_name, endpoint_method)
    within sliding time windows. Thread-safe.
    """
    _instance = None
    _init_lock = threading.Lock()

    def __new__(cls):
        with cls._init_lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._windows = {}
                cls._instance._registry_lock = threading.Lock()
        return cls._instance

    def _get_or_create_window(self, key):
        """
        Get existing window or create a new one for the given key.

        :param key: Tuple of (api_name, endpoint_method)
        :type key: tuple

        :returns: Rate limit window for the key
        :rtype: _RateLimitWindow
        """
        if key not in self._windows:
            with self._registry_lock:
                if key not in self._windows:
                    self._windows[key] = _RateLimitWindow()
        return self._windows[key]

    def _reset_if_expired(self, window, config):
        """
        Reset the window's call count and start time if the current window has expired.

        :param window: The rate limit window to check
        :type window: _RateLimitWindow
        :param config: The rate limit configuration
        :type config: RateLimitConfig
        """
        now = time.monotonic()
        if now - window.window_start_time >= config.window_seconds:
            window.call_count = 0
            window.window_start_time = now

    def acquire(self, api_name, endpoint_method, config):
        """
        Attempt to acquire a slot within the rate limit window.
        Increments the call counter if within the limit.

        :param api_name: Name of the API
        :type api_name: str
        :param endpoint_method: Name of the endpoint method
        :type endpoint_method: str
        :param config: Rate limit configuration for this endpoint
        :type config: RateLimitConfig

        :returns: True if the call is allowed, False if the rate limit has been reached
        :rtype: bool
        """
        key = (api_name, endpoint_method)
        window = self._get_or_create_window(key)
        with window.lock:
            self._reset_if_expired(window, config)
            if window.call_count < config.max_calls:
                window.call_count += 1
                _logger.debug(f"Rate limit acquire for {key}: {window.call_count}/{config.max_calls}")
                return True
            _logger.debug(f"Rate limit reached for {key}: {window.call_count}/{config.max_calls}")
            return False

    def time_until_reset(self, api_name, endpoint_method, config):
        """
        Calculate the time remaining until the current rate limit window resets.

        :param api_name: Name of the API
        :type api_name: str
        :param endpoint_method: Name of the endpoint method
        :type endpoint_method: str
        :param config: Rate limit configuration for this endpoint
        :type config: RateLimitConfig

        :returns: Seconds until the window resets (minimum 0)
        :rtype: float
        """
        key = (api_name, endpoint_method)
        window = self._get_or_create_window(key)
        with window.lock:
            elapsed = time.monotonic() - window.window_start_time
            remaining = config.window_seconds - elapsed
            return max(remaining, 0)

    def reset(self, api_name=None, endpoint_method=None):
        """
        Reset rate limit tracking. If api_name and endpoint_method are provided, resets only that key.
        If no arguments are provided, resets all tracked windows.

        :param api_name: Name of the API. Defaults to None (reset all).
        :type api_name: str, optional
        :param endpoint_method: Name of the endpoint method. Defaults to None (reset all).
        :type endpoint_method: str, optional
        """
        with self._registry_lock:
            if api_name is not None and endpoint_method is not None:
                key = (api_name, endpoint_method)
                if key in self._windows:
                    del self._windows[key]
            else:
                self._windows.clear()
