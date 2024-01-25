import os
import sys
import json
import requests
import datetime
from unittest import TestCase, mock
from test.resources.testutils import utils
from test.resources.testutils import extmock_streamlit


class TestFetchOauthTokenFromOktaSidecarClient(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_no_details_oktasidecar.yaml",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()

        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    class FakeOktaSidecarResp(object):
        def __init__(self):
            self.accessToken = None
            self.expiresAt = None
            self.status_code = None

        def json(self):
            return json.loads(json.dumps(self.__dict__))

    class FakeOktaSidecarRespPartial(object):
        def __init__(self):
            self.accessToken = None
            self.status_code = None

        def json(self):
            return json.loads(json.dumps(self.__dict__))

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', None)
    def test_oauth_token_success_when_compute_app_type_not_set(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        exp_time = str(datetime.datetime.now() + datetime.timedelta(seconds=3600))
        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 200
        mocked_resp.accessToken = 'ACCESS_GRANTED'
        mocked_resp.expiresAt = exp_time
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time))

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_successfully_fetched_for_streamlit(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_streamlit_pkg_to_mock = 'streamlit'
        orig_streamlit_pkg = sys.modules[optional_streamlit_pkg_to_mock] if optional_streamlit_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_streamlit_pkg_to_mock] = mock.Mock()

        optional_websocket_header_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_websocket_header_pkg_to_mock] if optional_websocket_header_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_websocket_header_pkg_to_mock] = extmock_streamlit

        exp_time = str(datetime.datetime.now() + datetime.timedelta(seconds=3600))
        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 200
        mocked_resp.accessToken = 'ACCESS_GRANTED'
        mocked_resp.expiresAt = exp_time
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time))

        if orig_streamlit_pkg is not None:
            sys.modules[optional_streamlit_pkg_to_mock] = orig_streamlit_pkg

        if orig_pkg is not None:
            sys.modules[optional_websocket_header_pkg_to_mock] = orig_pkg

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_successfully_fetched_for_streamlit_partial_response(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_streamlit_pkg_to_mock = 'streamlit'
        orig_streamlit_pkg = sys.modules[optional_streamlit_pkg_to_mock] if optional_streamlit_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_streamlit_pkg_to_mock] = mock.Mock()

        optional_websocket_header_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_websocket_header_pkg_to_mock] if optional_websocket_header_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_websocket_header_pkg_to_mock] = extmock_streamlit

        mocked_resp = self.FakeOktaSidecarRespPartial()
        mocked_resp.status_code = 200
        mocked_resp.accessToken = 'ACCESS_GRANTED'
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', None))

        if orig_streamlit_pkg is not None:
            sys.modules[optional_streamlit_pkg_to_mock] = orig_streamlit_pkg

        if orig_pkg is not None:
            sys.modules[optional_websocket_header_pkg_to_mock] = orig_pkg

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_incomplete_response(self, mock_requests_get, mock_logger_debug):
        optional_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_pkg_to_mock] if optional_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_pkg_to_mock] = extmock_streamlit

        mocked_resp = self.FakeOktaSidecarRespPartial()
        mocked_resp.status_code = 404
        mocked_resp.content = "{'error': 'error'}"
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import okta_sidecar_client
        result = okta_sidecar_client._fetch_access_token_from_okta_sidecar(developer_uid="XYZ", scopes=[])
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("OAuth token retrieval failed. Response:{'error': 'error'}")

        if orig_pkg is not None:
            sys.modules[optional_pkg_to_mock] = orig_pkg

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_requests_raises_error(self, mock_requests_get, mock_logger_debug):
        optional_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_pkg_to_mock] if optional_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_pkg_to_mock] = extmock_streamlit

        mock_requests_get.side_effect = requests.exceptions.RequestException

        from aladdinsdk.common.authentication.api import okta_sidecar_client
        result = okta_sidecar_client._fetch_access_token_from_okta_sidecar(developer_uid="XYZ", scopes=[])
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Problem connecting to authentication server. Error: ")

        if orig_pkg is not None:
            sys.modules[optional_pkg_to_mock] = orig_pkg

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    def test_oauth_token_unsuccessful_call_to_okta_sidecar(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_pkg_to_mock] if optional_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_pkg_to_mock] = extmock_streamlit

        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 404
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        resp_access_token, resp_ttl = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertIsNone(resp_access_token)
        self.assertIsNone(resp_ttl)

        if orig_pkg is not None:
            sys.modules[optional_pkg_to_mock] = orig_pkg

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_missing_okta_sidecar_ping(self, mock_requests_get, mock_logger_debug):

        optional_pkg_to_mock = 'streamlit.web.server.websocket_headers'
        orig_pkg = sys.modules[optional_pkg_to_mock] if optional_pkg_to_mock in sys.modules.keys() else None
        sys.modules[optional_pkg_to_mock] = extmock_streamlit

        mock_requests_get.side_effect = requests.exceptions.RequestException()

        from aladdinsdk.common.authentication.oauth import okta_sidecar_client
        result = okta_sidecar_client._is_okta_sidecar_running()
        self.assertFalse(result)
        mock_logger_debug.assert_called_with('Okta-sidecar server not available.')

        if orig_pkg is not None:
            sys.modules[optional_pkg_to_mock] = orig_pkg

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', 'dash')
    def test_oauth_token_successfully_fetched_for_dash(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_streamlit_pkg_to_mock = 'flask'
        orig_streamlit_pkg = sys.modules[optional_streamlit_pkg_to_mock] if optional_streamlit_pkg_to_mock in sys.modules.keys() else None
        mocked_dash_module = mock.MagicMock()
        mocked_dash_module.request.headers = {'Developer-Uid': 'XYZ'}
        sys.modules[optional_streamlit_pkg_to_mock] = mocked_dash_module

        exp_time = str(datetime.datetime.now() + datetime.timedelta(seconds=3600))
        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 200
        mocked_resp.accessToken = 'ACCESS_GRANTED'
        mocked_resp.expiresAt = exp_time
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time))

        if orig_streamlit_pkg is not None:
            sys.modules[optional_streamlit_pkg_to_mock] = orig_streamlit_pkg

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('importlib.import_module')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._logger.debug')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', 'dash')
    def test_oauth_token_failure_missing_flask_module(self, mock_logger_debug, mock_importlib, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        def mockedfunc():
            raise Exception('ImportError')

        mock_importlib.side_effect = mockedfunc

        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 200
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Compute App http headers and/or Developer-Uid unavailable. "
                                             "Can not fetch access token from okta-sidecar server.")

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('importlib.import_module')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._logger.debug')
    @mock.patch('aladdinsdk.common.authentication.oauth.okta_sidecar_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_failure_missing_streamlit_module(self, mock_logger_debug, mock_importlib, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        def mockedfunc():
            raise Exception('ImportError')

        mock_importlib.side_effect = mockedfunc

        mocked_resp = self.FakeOktaSidecarResp()
        mocked_resp.status_code = 200
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Compute App http headers and/or Developer-Uid unavailable. "
                                             "Can not fetch access token from okta-sidecar server.")
