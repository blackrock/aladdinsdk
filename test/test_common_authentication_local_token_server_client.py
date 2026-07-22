"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
"""

import datetime
import json
import os
import sys

import requests
from unittest import TestCase, mock

from test.resources.testutils import extmock_streamlit
from test.resources.testutils import utils


class TestFetchOauthTokenFromLocalTokenServerClient(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_no_details_localtokenserver.yaml",
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

    class FakeLocalTokenServerResp(object):
        def __init__(self):
            self.access_token = None
            self.expires_at = None
            self.status_code = None

        def json(self):
            return json.loads(json.dumps(self.__dict__))

    class FakeLocalTokenServerRespPartial(object):
        def __init__(self):
            self.access_token = None
            self.status_code = None

        def json(self):
            return json.loads(json.dumps(self.__dict__))

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', None)
    def test_oauth_token_success_when_compute_app_type_not_set(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        exp_time_str = '2026-05-28T12:00:00+00:00'
        exp_time_parsed = datetime.datetime.fromisoformat(exp_time_str)
        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 200
        mocked_resp.access_token = 'ACCESS_GRANTED'
        mocked_resp.expires_at = exp_time_str
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time_parsed))

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_successfully_fetched_for_streamlit(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_streamlit_pkg_to_mock = 'streamlit'
        orig_streamlit_pkg = sys.modules.get(optional_streamlit_pkg_to_mock)
        mocked_streamlit = mock.Mock()
        mocked_streamlit.context = extmock_streamlit.context
        sys.modules[optional_streamlit_pkg_to_mock] = mocked_streamlit

        exp_time_str = '2026-05-28T12:00:00Z'
        exp_time_parsed = datetime.datetime.fromisoformat(exp_time_str.replace('Z', '+00:00'))
        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 200
        mocked_resp.access_token = 'ACCESS_GRANTED'
        mocked_resp.expires_at = exp_time_str
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time_parsed))

        if orig_streamlit_pkg is not None:
            sys.modules[optional_streamlit_pkg_to_mock] = orig_streamlit_pkg
        else:
            sys.modules.pop(optional_streamlit_pkg_to_mock, None)

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_successfully_fetched_for_streamlit_partial_response(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_streamlit_pkg_to_mock = 'streamlit'
        orig_streamlit_pkg = sys.modules.get(optional_streamlit_pkg_to_mock)
        mocked_streamlit = mock.Mock()
        mocked_streamlit.context = extmock_streamlit.context
        sys.modules[optional_streamlit_pkg_to_mock] = mocked_streamlit

        mocked_resp = self.FakeLocalTokenServerRespPartial()
        mocked_resp.status_code = 200
        mocked_resp.access_token = 'ACCESS_GRANTED'
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', None))

        if orig_streamlit_pkg is not None:
            sys.modules[optional_streamlit_pkg_to_mock] = orig_streamlit_pkg
        else:
            sys.modules.pop(optional_streamlit_pkg_to_mock, None)

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_non_200_response(self, mock_requests_get, mock_logger_debug):
        mocked_resp = self.FakeLocalTokenServerRespPartial()
        mocked_resp.status_code = 400
        mocked_resp.content = "{'error': 'error'}"
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import local_token_server_client
        result = local_token_server_client._fetch_access_token_from_local_token_server(session_id="XYZ", scopes=[])
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("OAuth token retrieval failed. Response:{'error': 'error'}")

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_requests_raises_error(self, mock_requests_get, mock_logger_debug):
        mock_requests_get.side_effect = requests.exceptions.RequestException

        from aladdinsdk.common.authentication.api import local_token_server_client
        result = local_token_server_client._fetch_access_token_from_local_token_server(session_id="XYZ", scopes=[])
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Problem connecting to authentication server. Error: ")

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    def test_oauth_token_unsuccessful_call_to_local_token_server(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 400
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        resp_access_token, resp_ttl = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertIsNone(resp_access_token)
        self.assertIsNone(resp_ttl)

    @mock.patch('logging.Logger.debug')
    @mock.patch('requests.get')
    def test_oauth_token_failure_missing_local_token_server_ping(self, mock_requests_get, mock_logger_debug):
        mock_requests_get.side_effect = requests.exceptions.RequestException()

        from aladdinsdk.common.authentication.oauth import local_token_server_client
        result = local_token_server_client._is_local_token_server_running()
        self.assertFalse(result)
        mock_logger_debug.assert_called_with('Local token server not available: %r', mock.ANY)

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', 'dash')
    def test_oauth_token_successfully_fetched_for_dash(self, mock_requests_get, mock_oauth_server):
        mock_oauth_server.return_value = None, None

        optional_flask_pkg_to_mock = 'flask'
        orig_flask_pkg = sys.modules[optional_flask_pkg_to_mock] if optional_flask_pkg_to_mock in sys.modules.keys() else None
        mocked_dash_module = mock.MagicMock()
        mocked_dash_module.request.headers = {'X-Session-Id': 'XYZ'}
        sys.modules[optional_flask_pkg_to_mock] = mocked_dash_module

        exp_time_str = '2026-05-28T12:00:00+00:00'
        exp_time_parsed = datetime.datetime.fromisoformat(exp_time_str)
        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 200
        mocked_resp.access_token = 'ACCESS_GRANTED'
        mocked_resp.expires_at = exp_time_str
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, ('ACCESS_GRANTED', exp_time_parsed))

        if orig_flask_pkg is not None:
            sys.modules[optional_flask_pkg_to_mock] = orig_flask_pkg

    @mock.patch('importlib.import_module')
    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._logger.debug')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', 'dash')
    def test_oauth_token_failure_missing_flask_module(self, mock_logger_debug, mock_requests_get, mock_oauth_server, mock_importlib):
        mock_oauth_server.return_value = None, None

        def mockedfunc(*args):
            raise Exception('ImportError')

        mock_importlib.side_effect = mockedfunc

        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 200
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Compute App http headers and/or X-Session-Id unavailable. "
                                             "Can not fetch access token from local token server.")

    @mock.patch('importlib.import_module')
    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server')
    @mock.patch('requests.get')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._logger.debug')
    @mock.patch('aladdinsdk.common.authentication.oauth.local_token_server_client._COMPUTE_APP_TYPE', 'streamlit')
    def test_oauth_token_failure_missing_streamlit_module(self, mock_logger_debug, mock_requests_get, mock_oauth_server, mock_importlib):
        mock_oauth_server.return_value = None, None

        def mockedfunc(*args):
            raise Exception('ImportError')

        mock_importlib.side_effect = mockedfunc

        mocked_resp = self.FakeLocalTokenServerResp()
        mocked_resp.status_code = 200
        mock_requests_get.return_value = mocked_resp

        from aladdinsdk.common.authentication.api import ApiAuthUtil
        api_auth_util = ApiAuthUtil()
        result = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertEqual(result, (None, None))
        mock_logger_debug.assert_called_with("Compute App http headers and/or X-Session-Id unavailable. "
                                             "Can not fetch access token from local token server.")
