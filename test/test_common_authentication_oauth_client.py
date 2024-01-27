from unittest import TestCase, mock
import os

import requests
from test.resources.testutils import utils


class TestCommonAuthenticationOauthUrlClient(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.authentication.oauth import oauth_url_client
        self.test_subject = oauth_url_client
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if 'test' in args[0]:
            return MockResponse({"authorizationServerUri": "https://test.blackrock.com/api/oauth2/default/v1/token"}, 200)
        elif 'error' in args[0]:
            return MockResponse({"error": "exception occurred"}, 400)
        return MockResponse(None, 404)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='test')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.get', side_effect=mocked_requests_get)
    def test_get_auth_server_response_success(self, token, requests):
        result = self.test_subject.retrieve_oauth_server_url()
        self.assertEqual(result, 'https://test.blackrock.com/api/oauth2/default/v1/token')

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='test')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.get', side_effect=requests.exceptions.RequestException)
    def test_get_auth_server_request_error_for_server_url(self, token, requests):
        from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
        with self.assertRaises(AsdkOAuthException) as context:
            self.test_subject.retrieve_oauth_server_url()
            self.assertTrue('Problem connecting to authentication server' in context.exception)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='error')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.get', side_effect=mocked_requests_get)
    def test_get_auth_server_response_error(self, token, requests):
        from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
        with self.assertRaises(AsdkOAuthException) as context:
            self.test_subject.retrieve_oauth_server_url()
            self.assertTrue('Request to authentication server failed' in context.exception)

    def test_auth_server_response(self):
        test_json = {
            "id": "DEV",
            "createTime": "2023-05-03T10:11:16.360Z",
            "modifyTime": "2023-06-16T14:33:32.099Z",
            "creator": "tobudulu",
            "modifier": "tobudulu",
            "identityProviderState": "STATE_UNSPECIFIED",
            "authorizationServerUri": "https://test.blackrock.com/api/oauth2/default/v1/authorize"
        }
        result = self.test_subject._get_auth_server_url_from_response(test_json)
        self.assertEqual(result, 'https://test.blackrock.com/api/oauth2/default/v1/authorize')

    def test_failure_to_get_auth_server_response(self):
        from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
        test_json = {
            "id": "DEV",
            "createTime": "2023-05-03T10:11:16.360Z",
            "modifyTime": "2023-06-16T14:33:32.099Z",
            "creator": "tobudulu",
            "modifier": "tobudulu",
            "identityProviderState": "STATE_UNSPECIFIED",
        }
        with self.assertRaises(AsdkOAuthException) as context:
            self.test_subject._get_auth_server_url_from_response(test_json)
            self.assertEqual('Failed to retrieve oauth server url', context.exception)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='test')
    def test_url_creation(self, token):
        result = self.test_subject._get_url_for_auth()
        self.assertEqual(result, 'https://test.blackrock.com/api/oauth2/default/v1/authorize')

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.get_files_dat_token_value', return_value='BLK')
    def test_url_creation_blk(self, token):
        result = self.test_subject._get_url_for_auth()
        self.assertEqual(result, 'https://webster.bfm.com/api/oauth2/default/v1/authorize')


class TestCommonAuthenticationOauthCredFlow(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            "defaultWebServer": "http://dummy.dws.com"
        })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.authentication.oauth import oauth_token_cred_client
        self.test_subject = oauth_token_cred_client
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def mocked_requests_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code, content):
                self.json_data = json_data
                self.status_code = status_code
                self.content = content

            def json(self):
                return self.json_data

        if 'url' in args[0]:
            return MockResponse({"access_token": "ACCESS_TOKEN123", "expires_in": 3600}, 200, "Success")
        elif 'error' in args[0]:
            return MockResponse({"error": "exception occurred"}, 400, "Error: Please investigate")
        return MockResponse(None, 404)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._get_token_url_for_auth_server', return_value='url')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=mocked_requests_post)
    @mock.patch('aladdinsdk.config.user_settings.get_api_oauth_auth_server_proxy')
    def test_retrieve_token_details_refresh_token_flow_success_response(self, us_auth_proxy_mock, url, requests):
        us_auth_proxy_mock.return_value = "XYZ"
        result = self.test_subject._retrieve_token_details(client_id='id', client_secret='secret', refresh_token='token',
                                                           scopes='offline_access', auth_flow_type='refresh_token')
        self.assertEqual(result, ('ACCESS_TOKEN123', 3600))

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._get_token_url_for_auth_server', return_value='url')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=mocked_requests_post)
    @mock.patch('aladdinsdk.config.user_settings.get_api_oauth_auth_server_proxy')
    def test_retrieve_token_details_client_credentails_flow_success_response(self, us_auth_proxy_mock, url, requests):
        us_auth_proxy_mock.return_value = "XYZ"
        result = self.test_subject._retrieve_token_details(client_id='id', client_secret='secret', refresh_token=None,
                                                           scopes='offline_access', auth_flow_type='client_credentials')
        self.assertEqual(result, ('ACCESS_TOKEN123', 3600))

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._get_token_url_for_auth_server', return_value='url')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=mocked_requests_post)
    @mock.patch('aladdinsdk.config.user_settings.get_api_oauth_auth_server_proxy')
    def test_retrieve_token_details_when_scopes_not_provided_success_response(self, us_auth_proxy_mock, url, requests):
        us_auth_proxy_mock.return_value = "XYZ"
        result = self.test_subject._retrieve_token_details(client_id='id', client_secret='secret', refresh_token=None,
                                                           scopes=None, auth_flow_type='client_credentials')
        self.assertEqual(result, ('ACCESS_TOKEN123', 3600))

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._get_token_url_for_auth_server', return_value='error')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=mocked_requests_post)
    def test_get_auth_server_response_error(self, url, requests):
        from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
        with self.assertRaises(AsdkOAuthException) as context:
            self.test_subject._retrieve_token_details(client_id='error', client_secret='secret', refresh_token='token',
                                                      scopes='offline_access', auth_flow_type='refresh_token')
            self.assertTrue('OAuth token retrieval failed' in context.exception)

    def test_get_oauth_access_token_from_response(self):
        test_json = {
            "access_token": "ACCESS_TOKEN123",
            "expires_in": 3600
        }
        result = self.test_subject._get_oauth_access_token_and_ttl_from_response(test_json)
        self.assertEqual(result, ('ACCESS_TOKEN123', 3600))

    def test_failure_to_get_oauth_access_token_from_response(self):
        from aladdinsdk.common.error.asdkerrors import AsdkOAuthException
        test_json = {
            "expires_in": 3600
        }
        with self.assertRaises(AsdkOAuthException) as context:
            self.test_subject._get_oauth_access_token_and_ttl_from_response(test_json)
            self.assertEqual('Failed to retrieve oauth access token and token expiry time from server', context.exception)

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client._retrieve_token_details', return_value='ACCESS_TOKEN123')
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=mocked_requests_post)
    def test_get_oauth_access_token_refresh_token_flow_success(self, url, requests):
        result = self.test_subject.get_access_token_and_ttl_from_oauth_server(client_id='id', client_secret='secret', refresh_token='token',
                                                                              scopes='offline_access', auth_flow_type='refresh_token')
        self.assertEqual(result, "ACCESS_TOKEN123")

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_url_client.requests.post', side_effect=requests.exceptions.RequestException)
    def test_get_auth_server_request_error(self, requests):
        resp = self.test_subject.get_access_token_and_ttl_from_oauth_server(client_id='id', client_secret='secret', refresh_token='token',
                                                                            scopes='offline_access', auth_flow_type='refresh_token')
        self.assertEqual(resp, (None, None))

    @mock.patch('logging.Logger.debug')
    def test_get_auth_server_request_error_client_creds_missing_client_details(self, mock_logger_debug):
        from aladdinsdk.common.authentication.oauth import oauth_token_cred_client
        oauth_token_cred_client.SDK_HELP_MESSAGE_SUFFIX = "Please check README.md for more information"
        resp = oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server(client_id=None, client_secret=None, refresh_token=None,
                                                                                  scopes='offline_access', auth_flow_type='client_credentials')
        self.assertEqual(resp, (None, None))
        mock_logger_debug.assert_called()

    @mock.patch('logging.Logger.debug')
    def test_get_auth_server_request_error_refresh_token_missing_details(self, mock_logger_debug):
        from aladdinsdk.common.authentication.oauth import oauth_token_cred_client
        oauth_token_cred_client.SDK_HELP_MESSAGE_SUFFIX = "Please check README.md for more information"
        resp = oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server(client_id=None, client_secret=None, refresh_token=None,
                                                                                  scopes='offline_access', auth_flow_type='refresh_token')
        self.assertEqual(resp, (None, None))
        mock_logger_debug.assert_called()

    @mock.patch('logging.Logger.debug')
    def test_get_auth_server_request_error_refresh_token_missing_refresh_tokens(self, mock_logger_debug):
        from aladdinsdk.common.authentication.oauth import oauth_token_cred_client
        oauth_token_cred_client.SDK_HELP_MESSAGE_SUFFIX = "Please check README.md for more information"
        resp = oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server(client_id="SOMEVAL", client_secret="SOMESECRET",
                                                                                  refresh_token="<no value>", scopes='offline_access',
                                                                                  auth_flow_type='refresh_token')
        self.assertEqual(resp, (None, None))
        mock_logger_debug.assert_called()

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.user_settings.get_api_oauth_auth_server_url', return_value=None)
    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.DEFAULT_WEB_SERVER', "http://dummy.dws.com")
    def test_retrieve_token_details_success(self, auth_server_url):
        self.assertEqual(self.test_subject._get_token_url_for_auth_server(), "http://dummy.dws.com/api/oauth2/default/v1/token")

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.user_settings.get_api_oauth_auth_server_url', return_value=None)
    def test_retrieve_auth_url_from_func_arg(self, user_setting_method_1):
        result = self.test_subject._get_token_url_for_auth_server('https://test')
        self.assertEqual(result, 'https://test/v1/token')

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.user_settings.get_api_oauth_auth_server_proxy', return_value=None)
    def test_get_proxy_for_auth_server(self, user_setting_method_1):
        result = self.test_subject._get_proxy_for_auth_server()
        self.assertEqual(result, {})

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.user_settings.get_api_oauth_auth_server_proxy',
                return_value="https://test-proxy")
    def test_get_proxy_for_auth_server_user_override(self, user_setting_method_1):
        result = self.test_subject._get_proxy_for_auth_server()
        self.assertEqual(result, {'https': 'https://test-proxy'})

    @mock.patch('aladdinsdk.common.authentication.oauth.oauth_token_cred_client.user_settings.get_api_oauth_auth_server_proxy',
                return_value="https://test-proxy")
    def test_get_proxy_for_auth_server_user_func_override(self, user_setting_method_1):
        result = self.test_subject._get_proxy_for_auth_server('https://test-proxy123')
        self.assertEqual(result, {'https': 'https://test-proxy123'})
