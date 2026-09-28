import os
from unittest import TestCase, mock
from test.resources.testutils import utils


class _FakeResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json_data = json_data if json_data is not None else {}
        self.text = text
        self.content = text

    def json(self):
        return self._json_data


class TestCommonHttpTimeouts(TestCase):
    """Every outbound requests.* call made by the SDK must carry a timeout (bandit B113)."""

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            "defaultWebServer": "http://dummy.dws.com"
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def _assert_timeout_passed(self, mocked_call):
        mocked_call.assert_called()
        for call in mocked_call.call_args_list:
            self.assertIsNotNone(call.kwargs.get('timeout'),
                                 f"requests call without timeout: {call}")

    @mock.patch('requests.get', return_value=_FakeResponse(200))
    def test_local_token_server_liveness_has_timeout(self, mock_get):
        from aladdinsdk.common.authentication.oauth import local_token_server_client
        self.assertTrue(local_token_server_client._is_local_token_server_running())
        self._assert_timeout_passed(mock_get)

    @mock.patch('requests.get', return_value=_FakeResponse(200, {"access_token": "ACCESS_GRANTED"}))
    def test_local_token_server_token_fetch_has_timeout(self, mock_get):
        from aladdinsdk.common.authentication.oauth import local_token_server_client
        token, _ = local_token_server_client._fetch_access_token_from_local_token_server("session-id")
        self.assertEqual(token, "ACCESS_GRANTED")
        self._assert_timeout_passed(mock_get)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._get_token_url_for_auth_server', return_value='url')
    @mock.patch('aladdinsdk.config.user_settings.get_api_oauth_auth_server_proxy', return_value=None)
    @mock.patch('requests.post', return_value=_FakeResponse(200, {"access_token": "ACCESS_TOKEN123", "expires_in": 3600}))
    def test_oauth_token_request_has_timeout(self, mock_post, _proxy, _url):
        from aladdinsdk.common.authentication.oauth import oauth_token_cred_client
        result = oauth_token_cred_client._retrieve_token_details(client_id='id', client_secret='secret', refresh_token='token',
                                                                 scopes=['offline_access'], auth_flow_type='refresh_token')
        self.assertEqual(result, ('ACCESS_TOKEN123', 3600))
        self._assert_timeout_passed(mock_post)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='test')
    @mock.patch('requests.get', return_value=_FakeResponse(200, {"authorizationServerUri": "https://auth.example"}))
    def test_oauth_server_url_request_has_timeout(self, mock_get, _token):
        from aladdinsdk.common.authentication.oauth import oauth_url_client
        self.assertEqual(oauth_url_client.retrieve_oauth_server_url(), "https://auth.example")
        self._assert_timeout_passed(mock_get)

    @mock.patch('requests.get', return_value=_FakeResponse(200, text="TEST_TOKEN\tTEST_TOKEN_VALUE\n"))
    def test_files_dat_request_has_timeout(self, mock_get):
        from aladdinsdk.common.blkutils import blkutils
        self.assertEqual(blkutils.get_files_dat_token_value("TEST_TOKEN"), "TEST_TOKEN_VALUE")
        self._assert_timeout_passed(mock_get)
