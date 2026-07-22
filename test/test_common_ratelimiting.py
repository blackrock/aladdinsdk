import os
import time
import threading
from unittest import TestCase, mock
from test.resources.testutils import utils


class TestRateLimitConfig(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_rate_limit_config_creation(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=100, window_seconds=60)
        self.assertEqual(config.max_calls, 100)
        self.assertEqual(config.window_seconds, 60)

    def test_rate_limit_config_equality(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config1 = RateLimitConfig(max_calls=100, window_seconds=60)
        config2 = RateLimitConfig(max_calls=100, window_seconds=60)
        self.assertEqual(config1, config2)


class TestRateLimitRegistry(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitRegistry
        self.registry = RateLimitRegistry()
        self.registry.reset()

    def test_singleton_instance(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitRegistry
        registry1 = RateLimitRegistry()
        registry2 = RateLimitRegistry()
        self.assertIs(registry1, registry2)

    def test_acquire_within_limit(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=3, window_seconds=60)
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))

    def test_acquire_exceeds_limit(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=2, window_seconds=60)
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertFalse(self.registry.acquire("TestAPI", "get_items", config))

    def test_acquire_different_endpoints_independent(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=60)
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertTrue(self.registry.acquire("TestAPI", "list_items", config))
        self.assertFalse(self.registry.acquire("TestAPI", "get_items", config))
        self.assertFalse(self.registry.acquire("TestAPI", "list_items", config))

    def test_acquire_different_apis_independent(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=60)
        self.assertTrue(self.registry.acquire("API_A", "get_items", config))
        self.assertTrue(self.registry.acquire("API_B", "get_items", config))
        self.assertFalse(self.registry.acquire("API_A", "get_items", config))

    def test_window_reset_after_expiry(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=0.1)
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))
        self.assertFalse(self.registry.acquire("TestAPI", "get_items", config))
        time.sleep(0.15)
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))

    def test_time_until_reset(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=10)
        self.registry.acquire("TestAPI", "get_items", config)
        remaining = self.registry.time_until_reset("TestAPI", "get_items", config)
        self.assertGreater(remaining, 0)
        self.assertLessEqual(remaining, 10)

    def test_time_until_reset_no_window(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=10)
        remaining = self.registry.time_until_reset("TestAPI", "new_endpoint", config)
        self.assertGreater(remaining, 0)
        self.assertLessEqual(remaining, 10)

    def test_reset_specific_key(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=60)
        self.registry.acquire("TestAPI", "get_items", config)
        self.assertFalse(self.registry.acquire("TestAPI", "get_items", config))
        self.registry.reset("TestAPI", "get_items")
        self.assertTrue(self.registry.acquire("TestAPI", "get_items", config))

    def test_reset_all(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=60)
        self.registry.acquire("API_A", "get_items", config)
        self.registry.acquire("API_B", "get_items", config)
        self.registry.reset()
        self.assertTrue(self.registry.acquire("API_A", "get_items", config))
        self.assertTrue(self.registry.acquire("API_B", "get_items", config))

    def test_thread_safety(self):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=100, window_seconds=60)
        results = []

        def acquire_many():
            for _ in range(50):
                results.append(self.registry.acquire("TestAPI", "get_items", config))

        threads = [threading.Thread(target=acquire_many) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # 200 attempts, only 100 should succeed
        self.assertEqual(len(results), 200)
        self.assertEqual(sum(results), 100)


class TestRateLimitConfigProviders(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_no_overrides(self, mock_overrides):
        mock_overrides.return_value = {}
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_with_endpoint_config(self, mock_overrides):
        mock_overrides.return_value = {
            'TestAPI': {
                'enabled': True,
                'endpoints': {
                    'get_items': {
                        'enabled': True,
                        'max_calls': 50,
                        'window_seconds': 30
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(len(result), 1)
        self.assertIn('get_items', result)
        self.assertEqual(result['get_items'], RateLimitConfig(max_calls=50, window_seconds=30))

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_api_disabled(self, mock_overrides):
        mock_overrides.return_value = {
            'TestAPI': {
                'enabled': False,
                'endpoints': {
                    'get_items': {
                        'max_calls': 50,
                        'window_seconds': 30
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_endpoint_disabled(self, mock_overrides):
        mock_overrides.return_value = {
            'TestAPI': {
                'enabled': True,
                'endpoints': {
                    'get_items': {
                        'enabled': False,
                        'max_calls': 50,
                        'window_seconds': 30
                    },
                    'list_items': {
                        'enabled': True,
                        'max_calls': 100,
                        'window_seconds': 60
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(len(result), 1)
        self.assertIn('list_items', result)
        self.assertEqual(result['list_items'], RateLimitConfig(max_calls=100, window_seconds=60))

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_invalid_values_skipped(self, mock_overrides):
        mock_overrides.return_value = {
            'TestAPI': {
                'enabled': True,
                'endpoints': {
                    'get_items': {
                        'max_calls': 'not_a_number',
                        'window_seconds': 30
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_missing_api(self, mock_overrides):
        mock_overrides.return_value = {
            'OtherAPI': {
                'endpoints': {
                    'get_items': {
                        'max_calls': 50,
                        'window_seconds': 30
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.config.user_settings.get_api_rate_limiting_overrides')
    def test_static_provider_multiple_endpoints(self, mock_overrides):
        mock_overrides.return_value = {
            'TestAPI': {
                'enabled': True,
                'endpoints': {
                    'get_items': {
                        'max_calls': 50,
                        'window_seconds': 30
                    },
                    'list_items': {
                        'max_calls': 100,
                        'window_seconds': 60
                    }
                }
            }
        }
        from aladdinsdk.common.ratelimiting.config_provider import StaticRateLimitConfigProvider
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        provider = StaticRateLimitConfigProvider()
        result = provider.fetch_rate_limits("TestAPI")
        self.assertEqual(len(result), 2)
        self.assertEqual(result['get_items'], RateLimitConfig(max_calls=50, window_seconds=30))
        self.assertEqual(result['list_items'], RateLimitConfig(max_calls=100, window_seconds=60))


class TestResolveRateLimitConfig(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_none_config(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import resolve_rate_limit_config
        result = resolve_rate_limit_config("API", "ep", None)
        self.assertIsNone(result)

    def test_user_config(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import resolve_rate_limit_config
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        user = RateLimitConfig(max_calls=50, window_seconds=30)
        result = resolve_rate_limit_config("API", "ep", user)
        self.assertEqual(result, user)


class TestBuildRateLimitConfigs(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.user_settings')
    def test_globally_disabled(self, mock_us):
        mock_us.get_api_rate_limiting_enabled.return_value = False
        from aladdinsdk.common.ratelimiting.rate_limit_helper import build_rate_limit_configs
        result = build_rate_limit_configs("TestAPI", ["get_items"])
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.user_settings')
    def test_per_api_disabled(self, mock_us):
        mock_us.get_api_rate_limiting_enabled.return_value = True
        mock_us.get_api_rate_limiting_overrides.return_value = {
            'TestAPI': {'enabled': False}
        }
        from aladdinsdk.common.ratelimiting.rate_limit_helper import build_rate_limit_configs
        result = build_rate_limit_configs("TestAPI", ["get_items"])
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.StaticRateLimitConfigProvider')
    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.user_settings')
    def test_build_with_user_config(self, mock_us, mock_static_cls):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        mock_us.get_api_rate_limiting_enabled.return_value = True
        mock_us.get_api_rate_limiting_overrides.return_value = {}
        mock_static_cls.return_value.fetch_rate_limits.return_value = {
            'get_items': RateLimitConfig(max_calls=50, window_seconds=30)
        }
        from aladdinsdk.common.ratelimiting.rate_limit_helper import build_rate_limit_configs
        result = build_rate_limit_configs("TestAPI", ["get_items", "list_items"])
        self.assertIn('get_items', result)
        self.assertEqual(result['get_items'], RateLimitConfig(max_calls=50, window_seconds=30))
        self.assertNotIn('list_items', result)

    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.StaticRateLimitConfigProvider')
    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.user_settings')
    def test_build_skips_unknown_endpoints(self, mock_us, mock_static_cls):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        mock_us.get_api_rate_limiting_enabled.return_value = True
        mock_us.get_api_rate_limiting_overrides.return_value = {}
        mock_static_cls.return_value.fetch_rate_limits.return_value = {
            'unknown_endpoint': RateLimitConfig(max_calls=100, window_seconds=60)
        }
        from aladdinsdk.common.ratelimiting.rate_limit_helper import build_rate_limit_configs
        result = build_rate_limit_configs("TestAPI", ["get_items"])
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.StaticRateLimitConfigProvider')
    @mock.patch('aladdinsdk.common.ratelimiting.rate_limit_helper.user_settings')
    def test_per_endpoint_disabled_in_overrides(self, mock_us, mock_static_cls):
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        mock_us.get_api_rate_limiting_enabled.return_value = True
        mock_us.get_api_rate_limiting_overrides.return_value = {
            'TestAPI': {
                'enabled': True,
                'endpoints': {
                    'get_items': {'enabled': False, 'max_calls': 50, 'window_seconds': 30}
                }
            }
        }
        mock_static_cls.return_value.fetch_rate_limits.return_value = {
            'get_items': RateLimitConfig(max_calls=100, window_seconds=60)
        }
        from aladdinsdk.common.ratelimiting.rate_limit_helper import build_rate_limit_configs
        result = build_rate_limit_configs("TestAPI", ["get_items"])
        self.assertEqual(result, {})


class TestWaitForRateLimit(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import get_rate_limit_registry
        get_rate_limit_registry().reset()

    def test_wait_acquires_immediately_within_limit(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import wait_for_rate_limit, get_rate_limit_registry
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=3, window_seconds=60)
        start = time.monotonic()
        wait_for_rate_limit("TestAPI", "wait_test", config)
        elapsed = time.monotonic() - start
        self.assertLess(elapsed, 0.1)

    def test_wait_blocks_when_limit_reached(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import wait_for_rate_limit, get_rate_limit_registry
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=0.2)

        # First acquire should succeed immediately
        wait_for_rate_limit("TestAPI", "wait_block_test", config)

        # Second call should block until window resets
        start = time.monotonic()
        wait_for_rate_limit("TestAPI", "wait_block_test", config)
        elapsed = time.monotonic() - start
        self.assertGreaterEqual(elapsed, 0.1)

    def test_wait_concurrent_threads_all_acquire(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import wait_for_rate_limit, get_rate_limit_registry
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=2, window_seconds=0.2)
        results = []
        errors = []

        def call_wait(thread_id):
            try:
                wait_for_rate_limit("TestAPI", "wait_concurrent", config)
                results.append(thread_id)
            except Exception as e:
                errors.append(e)

        threads = [threading.Thread(target=call_wait, args=(i,)) for i in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        self.assertEqual(len(errors), 0)
        self.assertEqual(len(results), 6)


class TestExecuteWithRateLimit(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import get_rate_limit_registry
        get_rate_limit_registry().reset()

    def test_execute_within_limit(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=5, window_seconds=60)
        result = execute_with_rate_limit("TestAPI", "get_items", config, lambda x: x * 2, 21)
        self.assertEqual(result, 42)

    def test_execute_blocks_when_limit_reached(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=1, window_seconds=0.2)

        # First call should succeed immediately
        result1 = execute_with_rate_limit("TestAPI", "block_test", config, lambda: "first")
        self.assertEqual(result1, "first")

        # Second call should block then succeed after window resets
        start = time.monotonic()
        result2 = execute_with_rate_limit("TestAPI", "block_test", config, lambda: "second")
        elapsed = time.monotonic() - start
        self.assertEqual(result2, "second")
        self.assertGreaterEqual(elapsed, 0.1)

    def test_execute_passes_kwargs(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=5, window_seconds=60)

        def fn_with_kwargs(a, b, multiplier=1):
            return (a + b) * multiplier

        result = execute_with_rate_limit(
            "TestAPI", "get_items", config,
            fn_with_kwargs, 3, 4, multiplier=2
        )
        self.assertEqual(result, 14)

    def test_execute_propagates_exception(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=5, window_seconds=60)

        def failing_fn():
            raise ValueError("test error")

        with self.assertRaises(ValueError) as ctx:
            execute_with_rate_limit("TestAPI", "get_items", config, failing_fn)
        self.assertIn("test error", str(ctx.exception))

    def test_execute_multiple_calls_within_window(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=3, window_seconds=60)
        results = []
        for i in range(3):
            results.append(execute_with_rate_limit("TestAPI", "multi_test", config, lambda x: x, i))
        self.assertEqual(results, [0, 1, 2])

    def test_execute_concurrent_threads_all_succeed(self):
        from aladdinsdk.common.ratelimiting.rate_limit_helper import execute_with_rate_limit
        from aladdinsdk.common.ratelimiting.rate_limiter import RateLimitConfig
        config = RateLimitConfig(max_calls=2, window_seconds=0.2)
        results = []
        errors = []
        lock = threading.Lock()

        def call_execute(thread_id):
            try:
                result = execute_with_rate_limit(
                    "TestAPI", "exec_concurrent", config,
                    lambda tid: tid, thread_id
                )
                with lock:
                    results.append(result)
            except Exception as e:
                with lock:
                    errors.append(e)

        threads = [threading.Thread(target=call_execute, args=(i,)) for i in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=5)

        self.assertEqual(len(errors), 0)
        self.assertEqual(len(results), 6)
        self.assertEqual(sorted(results), [0, 1, 2, 3, 4, 5])
