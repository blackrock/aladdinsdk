from unittest import TestCase, mock
from test.resources.testutils import utils


class TestCommonAuthenticationOauthConfigUtil(TestCase):
    @classmethod
    def setUpClass(self):
        utils.reload_modules()
        from aladdinsdk.config.utils import oauth_config_util
        self.test_subject = oauth_config_util
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()

    def setUp(self) -> None:
        return super().setUp()

    @mock.patch('webbrowser.open')
    @mock.patch('aladdinsdk.config.utils.oauth_config_util.start_local_auth_handler')
    @mock.patch('requests_oauthlib.OAuth2Session.fetch_token')
    def test_successful_auth_code_flow_handle(self, mock_oauth2_session_fetch_token,
                                              mock_start_local_auth_handler,
                                              mock_webbrowser_open):
        def mock_hit_get():
            import urllib.request
            urllib.request.urlopen("http://localhost:3000/?code=TEST_AUTH_CODE&state=TEST_STATE").read()

        mock_webbrowser_open.side_effect = [mock_hit_get]
        mock_start_local_auth_handler.side_effect = ['TEST_AUTH_CODE2']
        mock_oauth2_session_fetch_token.side_effect = [{'refresh_token': 'TEST_REFRESH_TOKEN'}]
        test_res = self.test_subject.get_refresh_token_from_oauth_server("CLIENT_ID",
                                                              "CLIENT_SECRET",
                                                              ["offline_access"],
                                                              3000,
                                                              "https://fake_auth_url",
                                                              "https://fake_token_url")
        self.assertEqual(test_res, 'TEST_REFRESH_TOKEN')

    def test_unsuccessful_auth_code_flow_handle_missing_secrets(self):
        with self.assertRaises(Exception) as context:
            self.test_subject.get_refresh_token_from_oauth_server(None,
                                                                 None,
                                                                 ["offline_access"],
                                                                 3000,
                                                                 "https://fake_auth_url",
                                                                 "https://fake_token_url")
            self.assertTrue('OAuth application client ID and/or secret missing' in context.exception)

    @mock.patch('webbrowser.open')
    @mock.patch('aladdinsdk.config.utils.oauth_config_util.start_local_auth_handler')
    @mock.patch('requests_oauthlib.OAuth2Session.fetch_token')
    def test_unsuccessful_auth_code_flow_error(self, mock_oauth2_session_fetch_token,
                                               mock_start_local_auth_handler,
                                               mock_webbrowser_open):
        def mock_hit_get():
            import urllib.request
            urllib.request.urlopen("http://localhost:3000/?code=TEST_AUTH_CODE&state=TEST_STATE").read()

        mock_webbrowser_open.side_effect = [mock_hit_get]
        mock_start_local_auth_handler.side_effect = ['TEST_AUTH_CODE2']
        mock_oauth2_session_fetch_token.side_effect = []
        test_res = self.test_subject.get_refresh_token_from_oauth_server("CLIENT_ID",
                                                                         "CLIENT_SECRET",
                                                                         ["offline_access"],
                                                                         3000,
                                                                         "https://fake_auth_url",
                                                                         "https://fake_token_url")
        self.assertEqual(test_res, None)
