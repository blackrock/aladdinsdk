from dataclasses import dataclass
from unittest import TestCase, mock
import os
import asyncio

import pandas as pd

from test.resources.testutils import utils


class TestApiRegistry(TestCase):
    @dataclass
    class CodegenAllowListEntryStruct:
        api_module_path: any = None
        api_name: any = None
        api_version: any = None
        host_url_path: any = None

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_get_api_names(self):
        from aladdinsdk.api.registry import get_api_names
        api_list = get_api_names()
        self.assertIn('TokenAPI', api_list)

    def test_get_api_details_failure_non_existent_api(self):
        from aladdinsdk.api.registry import get_api_details
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        with self.assertRaises(AsdkApiException) as context:
            get_api_details('NonExistentTestAsdkAPI')
            self.assertTrue("API not supported for SDK calls at the moment." in context.exception)

    def test_get_api_details(self):
        from aladdinsdk.api.registry import get_api_details, AladdinAPICodegenDetails

        expected = AladdinAPICodegenDetails(
            'TokenAPI',
            'v1',
            'aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI',
            '/api/platform/infrastructure/token/v1/',
            'aladdinsdk/api/codegen/platform/infrastructure/token/v1/TokenAPI/swagger.json'
        )

        test_case = TestCase()
        test_case.addTypeEqualityFunc(AladdinAPICodegenDetails, lambda first, second, msg:
                                      first.api_name == second.api_name
                                      and first.api_module_path == second.api_module_path
                                      and first.api_class_name == second.api_class_name
                                      and first.host_url_path == second.host_url_path
                                      and first.swagger_file_path == second.swagger_file_path
                                      and first.api_client == second.api_client
                                      and first.api_configuration == second.api_configuration
                                      and first.api_default_class == second.api_default_class
                                      and first.api_class_methods == second.api_class_methods)

        resp = get_api_details('TokenAPI')
        test_case.assertEqual(resp, expected)

    @mock.patch('aladdinsdk.config.internal_settings')
    def test_get_api_details_multiple_versions(self, mock_internal_settings):
        # Currently v2 does not exist, so mock the imports here
        import sys
        from aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1 import TrainJourneyAPI
        sys.modules['aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v2.TrainJourneyAPI'] = TrainJourneyAPI

        mock_internal_settings.get_api_allow_list.return_value = [
            {
                'api_module_path': 'aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI',
                'api_name': 'TokenAPI',
                'api_version': 'v1',
                'host_url_path': '/api/platform/infrastructure/token/v1/'
            },
            {
                'api_module_path': 'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v2.TrainJourneyAPI',
                'api_name': 'TrainJourneyAPI',
                'api_version': 'v2',
                'host_url_path': '/api/reference-architecture/demo/train-journey/v2/'
            },
            {
                'api_module_path': 'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.TrainJourneyAPI',
                'api_name': 'TrainJourneyAPI',
                'api_version': 'v1',
                'host_url_path': '/api/reference-architecture/demo/train-journey/v1/'
            }
        ]

        # reload registry to pick up above mock
        import importlib
        import aladdinsdk
        importlib.reload(aladdinsdk.api.registry)

        from aladdinsdk.api.registry import get_api_details, AladdinAPICodegenDetails

        expected_latest = AladdinAPICodegenDetails(
            'TrainJourneyAPI',
            'v2',
            'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v2.TrainJourneyAPI',
            '/api/reference-architecture/demo/train-journey/v2/',
            'aladdinsdk/api/codegen/reference_architecture/demo/train_journey/v2/train_journey/swagger.json'
        )

        expected_v1 = AladdinAPICodegenDetails(
            'TrainJourneyAPI',
            'v1',
            'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.TrainJourneyAPI',
            '/api/reference-architecture/demo/train-journey/v1/',
            'aladdinsdk/api/codegen/reference_architecture/demo/train_journey/v1/TrainJourneyAPI/swagger.json'
        )

        expected_v2 = AladdinAPICodegenDetails(
            'TrainJourneyAPI',
            'v2',
            'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v2.TrainJourneyAPI',
            '/api/reference-architecture/demo/train-journey/v2/',
            'aladdinsdk/api/codegen/reference_architecture/demo/train_journey/v2/TrainJourneyAPI/swagger.json'
        )

        expected_token_v1 = AladdinAPICodegenDetails(
            'TokenAPI',
            'v1',
            'aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI',
            '/api/platform/infrastructure/token/v1/',
            'aladdinsdk/api/codegen/platform/infrastructure/token/v1/TokenAPI/swagger.json',
        )

        test_case = TestCase()
        test_case.addTypeEqualityFunc(AladdinAPICodegenDetails, lambda first, second, msg:
                                      first.api_name == second.api_name
                                      and first.api_module_path == second.api_module_path
                                      and first.api_class_name == second.api_class_name
                                      and first.host_url_path == second.host_url_path
                                      and first.api_client == second.api_client
                                      and first.api_configuration == second.api_configuration
                                      and first.api_default_class == second.api_default_class
                                      and first.api_class_methods == second.api_class_methods)

        # No version provided for multiple versioned APIs - should give the latest version
        resp = get_api_details('TrainJourneyAPI')
        test_case.assertEqual(resp, expected_latest)

        # Specific version given, should return that version
        resp = get_api_details('TrainJourneyAPI', 'v1')
        test_case.assertEqual(resp, expected_v1)

        # Specific version given, should return that version
        resp = get_api_details('TrainJourneyAPI', 'v2')
        test_case.assertEqual(resp, expected_v2)

        # No version provided for single versioned APIs - should give the only present version
        resp = get_api_details('TokenAPI')
        test_case.assertEqual(resp, expected_token_v1)

    @mock.patch('aladdinsdk.config.internal_settings')
    @mock.patch('logging.Logger.debug')
    def test_get_api_details_failure_to_setup_malformed_allow_list(self, mock_log_debug, mock_internal_settings):

        mock_internal_settings.get_api_allow_list.return_value = [
            {
                'api_module_path': 'aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI',
                'api_version': 'v1',
                'host_url_path': '/api/platform/infrastructure/token/v1/'
            }
        ]
        delattr(mock_internal_settings.get_api_allow_list[0].return_value, 'api_name')

        # reload registry to pick up above mock
        import importlib
        import aladdinsdk
        importlib.reload(aladdinsdk)
        importlib.reload(aladdinsdk.api.registry)
        mock_log_debug.assert_called_with("Internal SDK setup warning. Unable to fully setup API registry. Potentially malformed allow list.")

    @mock.patch('aladdinsdk.config.internal_settings')
    @mock.patch('logging.Logger.debug')
    def test_get_api_details_failure_due_to_exception_getting_internal_swagger_path(self, mock_log_debug, mock_internal_settings):
        mock_internal_settings.get_api_allow_list.return_value = [
            {
                'api_name': 'TestAPIShouldNotExist',
                'api_version': 'v1',
                'host_url_path': '/dummy/hostpath/v1/'
            }
        ]

        # reload registry to pick up above mock
        import importlib
        import aladdinsdk
        importlib.reload(aladdinsdk)
        importlib.reload(aladdinsdk.api.registry)

        from aladdinsdk.api.registry import get_api_names
        self.assertNotIn("TestAPIShouldNotExist", get_api_names())
        mock_log_debug.assert_called()


class TestApiClient(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_api_client_init_success(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TokenAPI')
        self.assertIsNotNone(test_subject)

    def test_api_client_endpoint_introspection_success(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TokenAPI')

        endpoint_methods = test_subject.get_api_endpoint_methods()
        self.assertIn('token_api_generate_token', endpoint_methods)

        endpoint_methods = test_subject.get_api_endpoint_path_tuples()
        self.assertIn(('/token:generate', 'get'), endpoint_methods)

        endpoint_signature = test_subject.get_api_endpoint_signature('token_api_generate_token')

        self.assertIsNotNone(endpoint_signature)

    def test_api_client_endpoint_introspection_failure(self):
        from aladdinsdk.api.client import AladdinAPI
        from aladdinsdk.common.error.asdkerrors import AsdkApiException

        test_subject = AladdinAPI('TokenAPI')

        with self.assertRaises(AsdkApiException) as context:
            test_subject.get_api_endpoint_signature('non_existent_endpoint')
            self.assertTrue('Incorrect endpoint path/method passed' in context.exception)

    def test_call_api_with_request_body_success(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.return_value = "TEST_RESPONSE"
                mock_signature_helper.return_value = signature_bkp

                resp = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                             request_body={"payload_key": "payload value"})
                mock_filter_call.assert_called_once_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={"payload_key": "payload value"})
            self.assertEqual(resp, 'TEST_RESPONSE')

    def test_call_api_with_request_body_success_read_data(self):
        from aladdinsdk.api.client import AladdinAPI

        class MockApiResp:
            def __init__(self, data):
                self.data = data

        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.return_value = MockApiResp(data="TEST_RESPONSE")
                mock_signature_helper.return_value = signature_bkp

                resp = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                             request_body={"payload_key": "payload value"})
                mock_filter_call.assert_called_once_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={"payload_key": "payload value"})
            self.assertEqual(resp, 'TEST_RESPONSE')

    def test_call_api_with_request_body_success_read_raw_data(self):
        from aladdinsdk.api.client import AladdinAPI

        class MockApiResp:
            def __init__(self, data):
                self.data = None
                self.raw_data = data

        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.return_value = MockApiResp(data='"TEST_RESPONSE"')
                mock_signature_helper.return_value = signature_bkp

                resp = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                             _deserialize_to_object=False,
                                             request_body={"payload_key": "payload value"})
                mock_filter_call.assert_called_once_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=False,
                    body={"payload_key": "payload value"})
            self.assertEqual(resp, 'TEST_RESPONSE')

    def test_call_api_with_request_body_success_disable_deserialization(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.return_value = utils.UnitTestRESTResponse(None, 200, "", """{"resp_key": "resp_val"}""".encode('utf-8'))
                mock_signature_helper.return_value = signature_bkp

                resp = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                             request_body={"payload_key": "payload value"}, _deserialize_to_object=False)
                mock_filter_call.assert_called_once_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=False,
                    body={"payload_key": "payload value"})
            self.assertEqual(resp, {"resp_key": "resp_val"})

    def test_call_api_with_request_body_success_dataframe(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                class MockApiResp:
                    def json(self):
                        return """
                                {
                                    "id": "0001",
                                    "type": "donut",
                                    "name": "Cake",
                                    "ppu": 0.55,
                                    "batters": {
                                        "batter": [
                                            { "id": "1001", "type": "Regular" },
                                            { "id": "1002", "type": "Chocolate" },
                                            { "id": "1003", "type": "Blueberry" },
                                            { "id": "1004", "type": "Devil's Food" }
                                        ]
                                    },
                                    "topping": [
                                        { "id": "5001", "type": "None" },
                                        { "id": "5002", "type": "Glazed" },
                                        { "id": "5005", "type": "Sugar" },
                                        { "id": "5007", "type": "Powdered Sugar" },
                                        { "id": "5006", "type": "Chocolate with Sprinkles" },
                                        { "id": "5003", "type": "Chocolate" },
                                        { "id": "5004", "type": "Maple" }
                                    ]
                                }
                                """
                mock_filter_call.return_value = MockApiResp()
                mock_signature_helper.return_value = signature_bkp

                resp = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                             request_body={"payload_key": "payload value"},
                                             asdk_transformation_option={'type': "dataframe", 'flatten': "batters.batter.[*]"})
                mock_filter_call.assert_called_once_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={"payload_key": "payload value"})
            expected_data = {'batters.batter.id': ['1001', '1002', '1003', '1004'],
                             'batters.batter.type': ['Regular', 'Chocolate', 'Blueberry', "Devil's Food"],
                             'id': ['0001'] * 4, 'type': ['donut'] * 4, 'name': ['Cake'] * 4, 'ppu': [0.55] * 4}
            expected_df = pd.DataFrame(expected_data)
            self.assertTrue(resp.equals(expected_df))

    def test_call_api_without_request_body_success(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TrainJourneyAPI')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            mock_filter_call.return_value = "TEST_RESPONSE"

            resp = test_subject.call_api('train_journey_api_filter_train_journeys', param_key_1="param value 1")
            mock_filter_call.assert_called_once_with(
                vnd_com_blackrock_request_id=mock.ANY,
                vnd_com_blackrock_origin_timestamp=mock.ANY,
                _headers=mock.ANY,
                body=None,
                _preload_content=True,
                param_key_1="param value 1")
            self.assertEqual(resp, 'TEST_RESPONSE')

    def test_call_api_failure(self):
        from aladdinsdk.api.client import AladdinAPI

        test_subject = AladdinAPI('TrainJourneyAPI')

        with self.assertRaises(Exception) as context:
            test_subject.call_api('FAKE_ENDPOINT', {})
            self.assertTrue('Incorrect endpoint path/method passed' in context.exception)

    def test_call_api_with_request_body_success_paginated_get(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_list_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_list_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123"), Response('TEST_RESPONSE2', "456"),
                                                Response('TEST_RESPONSE3', "789")]
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_list_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _asdk_pagination_options={'page_size': 4, 'number_of_pages': 3, 'timeout': 500})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    page_size=mock.ANY,
                    page_token=mock.ANY
                )
                self.assertEqual(mock_filter_call.call_count, 3)
                self.assertEqual(responses.__len__(), 3)

    def test_call_api_with_request_body_success_paginated_get_raw_data(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_list_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_list_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [{"data": "TEST_RESPONSE1", "nextPageToken": "123"},
                                                {"data": "TEST_RESPONSE2", "nextPageToken": "456"},
                                                {"data": "TEST_RESPONSE3", "nextPageToken": "789"}]
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_list_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _deserialize_to_object=False,
                                                  _asdk_pagination_options={'page_size': 4, 'number_of_pages': 3, 'timeout': 500})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=False,
                    page_size=mock.ANY,
                    page_token=mock.ANY
                )
                self.assertEqual(mock_filter_call.call_count, 3)
                self.assertEqual(responses.__len__(), 3)

    def test_call_api_with_request_body_success_paginated_post(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_filter_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123"), Response('TEST_RESPONSE2', "456"),
                                                Response('TEST_RESPONSE3', "789")]
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _asdk_pagination_options={'page_size': 4, 'number_of_pages': 3, 'timeout': 500})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={'payload_key': 'payload value', 'page_size': mock.ANY, 'page_token': mock.ANY}
                )
                self.assertEqual(mock_filter_call.call_count, 3)
                self.assertEqual(responses.__len__(), 3)

    def test_call_api_with_request_body_success_paginated_less_pages_get(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_list_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_list_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123"), Response('TEST_RESPONSE2', "456"), Response('TEST_RESPONSE3', "")]
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_list_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _asdk_pagination_options={'page_size': 1, 'number_of_pages': 2, 'timeout': 500})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    page_size=mock.ANY,
                    page_token=mock.ANY
                )
                self.assertEqual(mock_filter_call.call_count, 2)
                self.assertEqual(responses.__len__(), 2)

    def test_call_api_with_request_body_success_paginated_timed_out(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_filter_train_journeys_with_http_info") as mock_filter_call_timeout:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call_timeout.return_value = Response('TEST_RESPONSE1', "123")
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _asdk_pagination_options={'page_size': 0, 'number_of_pages': 2, 'timeout': 0, 'interval': 2})

                mock_filter_call_timeout.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={'payload_key': 'payload value', 'page_size': mock.ANY, 'page_token': mock.ANY}
                )
                self.assertEqual(mock_filter_call_timeout.call_count, 2)
                self.assertEqual(responses.__len__(), 2)

    def test_call_api_with_request_body_success_paginated_params_zero(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_filter_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123")]
                mock_signature_helper.return_value = signature_bkp
                responses = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                                  request_body={"payload_key": "payload value"},
                                                  _asdk_pagination_options={'page_size': 0, 'number_of_pages': 0, 'timeout': 0, 'interval': 0,
                                                                            'page_token': ''})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={'payload_key': 'payload value', 'page_size': mock.ANY, 'page_token': mock.ANY}
                )
                self.assertEqual(mock_filter_call.call_count, 1)
                self.assertEqual(responses.__len__(), 1)

    def test_call_api_with_request_body_success_paginated_invalid_params_page_token(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_filter_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123"), Response('TEST_RESPONSE2', "456"),
                                                Response('TEST_RESPONSE3', "789")]
                mock_signature_helper.return_value = signature_bkp
                response = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                                 request_body={"payload_key": "payload value"},
                                                 _asdk_pagination_options={'page_size': 1, 'number_of_pages': 0, 'timeout': 2, 'interval': 0,
                                                                           'page_token': 0})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={'payload_key': 'payload value'}
                )
                self.assertEqual(mock_filter_call.call_count, 1)
                self.assertEqual(response.data_set, 'TEST_RESPONSE1')

    def test_call_api_with_request_body_success_paginated_invalid_params_page_size(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        signature_bkp = test_subject.get_api_endpoint_signature('train_journey_api_filter_train_journeys')

        with mock.patch.object(test_subject.instance, "train_journey_api_filter_train_journeys_with_http_info") as mock_filter_call:
            with mock.patch.object(test_subject, 'get_api_endpoint_signature') as mock_signature_helper:
                mock_filter_call.side_effect = [Response('TEST_RESPONSE1', "123"), Response('TEST_RESPONSE2', "456"),
                                                Response('TEST_RESPONSE3', "789")]
                mock_signature_helper.return_value = signature_bkp
                response = test_subject.call_api(api_endpoint_name='train_journey_api_filter_train_journeys',
                                                 request_body={"payload_key": "payload value"},
                                                 _asdk_pagination_options={'page_size': "1", 'number_of_pages': 0, 'timeout': 2, 'interval': 0,
                                                                           'page_token': ""})

                mock_filter_call.assert_called_with(
                    vnd_com_blackrock_request_id=mock.ANY,
                    vnd_com_blackrock_origin_timestamp=mock.ANY,
                    _headers=mock.ANY,
                    _preload_content=True,
                    body={'payload_key': 'payload value'}
                )
                self.assertEqual(mock_filter_call.call_count, 1)
                self.assertEqual(response.data_set, 'TEST_RESPONSE1')


class TestApiClientLroCalls(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_API__LRO__STATUS_CHECK_INTERVAL": '1',
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    class MockLroApiResponse:
        def __init__(self, done, error, id, meta, response):
            self.done = done
            self.error = error
            self.id = id
            self.meta = meta
            self.response = response

    def test_call_lro_api_success(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = {"done": False, "error": None, "id": 'mock-123-id', "meta": None, "response": None}
            mock_call_api_response_2 = {"done": False, "error": None, "id": 'mock-123-id', "meta": None, "response": None}
            mock_call_api_response_3 = {"done": True, "error": None, "id": 'mock-123-id', "meta": None, "response": {"resp_key": "resp_lro_val"}}
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            resp = asyncio.run(test_subject.call_lro_api(
                start_lro_endpoint="train_journey_api_run_train_journey_simulation",
                check_lro_status_endpoint="train_journey_api_get_longrunning_operation",
                _deserialize_to_object=False
            ))

            self.assertEqual(resp['done'], True)
            self.assertEqual(resp['id'], 'mock-123-id')
            self.assertEqual(resp['response'], {"resp_key": "resp_lro_val"})
            self.assertIsNone(resp['error'])

    def test_call_lro_api_swagger_path_success(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_2 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_3 = TestApiClientLroCalls.MockLroApiResponse(done=True, error=None, id='mock-123-id', meta=None,
                                                                                response='TEST_LRO_RESPONSE')
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            resp = asyncio.run(test_subject.call_lro_api(
                start_lro_endpoint="/trainJourneys/{id}:run",
                check_lro_status_endpoint="/longRunningOperations/{id}"
            ))

            self.assertEqual(resp.done, True)
            self.assertEqual(resp.id, 'mock-123-id')
            self.assertEqual(resp.response, 'TEST_LRO_RESPONSE')
            self.assertIsNone(resp.error)

    def test_call_lro_api_success_before_polling(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = {'done': True, 'error': None, 'id': 'mock-123-id', 'meta': None, 'response': 'TEST_LRO_RESPONSE_DONE_IN_ONE'}
            mock_call_api.side_effect = [
                mock_call_api_response_1,
            ]

            resp = asyncio.run(test_subject.call_lro_api(
                start_lro_endpoint="train_journey_api_run_train_journey_simulation",
                check_lro_status_endpoint="train_journey_api_get_longrunning_operation",
                _deserialize_to_object=False
            ))

            self.assertEqual(resp['done'], True)
            self.assertEqual(resp['id'], 'mock-123-id')
            self.assertEqual(resp['response'], 'TEST_LRO_RESPONSE_DONE_IN_ONE')
            self.assertIsNone(resp['error'])

    def test_call_lro_api_none_response(self):
        from aladdinsdk.api.client import AladdinAPI
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = None
            mock_call_api.side_effect = [
                mock_call_api_response_1,
            ]

            with self.assertRaises(AsdkApiException) as context:
                asyncio.run(test_subject.call_lro_api(
                    start_lro_endpoint="train_journey_api_run_train_journey_simulation",
                    check_lro_status_endpoint="train_journey_api_get_longrunning_operation"
                ))
                self.assertTrue("Long running operation response is empty, unable to get operation ID or status." in context.exception)

    def test_call_lro_api_success_with_callback_deserialize_to_object(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_2 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_3 = TestApiClientLroCalls.MockLroApiResponse(done=True, error=None, id='mock-123-id', meta=None,
                                                                                response={"resp_key": "TEST_LRO_RESPONSE_IN_CALLBACK"})
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            def sample_callback_function(resp):
                self.assertEqual(resp.done, True)
                self.assertEqual(resp.id, 'mock-123-id')
                self.assertEqual(resp.response, {"resp_key": "TEST_LRO_RESPONSE_IN_CALLBACK"})

            asyncio.run(test_subject.call_lro_api(
                start_lro_endpoint="train_journey_api_run_train_journey_simulation",
                check_lro_status_endpoint="train_journey_api_get_longrunning_operation",
                callback_func=sample_callback_function,
                _deserialize_to_object=True
            ))

    def test_call_lro_api_success_with_callback_disable_deserialize_to_object(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = {'done': False, 'error': None, 'id': 'mock-123-id', 'meta': None, 'response': None}
            mock_call_api_response_2 = {'done': False, 'error': None, 'id': 'mock-123-id', 'meta': None, 'response': None}
            mock_call_api_response_3 = {'done': True, 'error': None, 'id': 'mock-123-id', 'meta': None,
                                        'response': {"resp_key": "TEST_LRO_RESPONSE_IN_CALLBACK"}}
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            def sample_callback_function(resp):
                self.assertEqual(resp['done'], True)
                self.assertEqual(resp['id'], 'mock-123-id')
                self.assertEqual(resp['response'], {"resp_key": "TEST_LRO_RESPONSE_IN_CALLBACK"})

            asyncio.run(test_subject.call_lro_api(
                start_lro_endpoint="train_journey_api_run_train_journey_simulation",
                check_lro_status_endpoint="train_journey_api_get_longrunning_operation",
                callback_func=sample_callback_function,
                _deserialize_to_object=False
            ))

    def test_call_lro_status_api_swagger_path_success(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')

        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_2 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_3 = TestApiClientLroCalls.MockLroApiResponse(done=True, error=None, id='mock-123-id', meta=None,
                                                                                response='TEST_LRO_RESPONSE')
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            resp = asyncio.run(test_subject.call_lro_status_api(
                check_lro_status_endpoint="/longRunningOperations/{id}",
                lro_id='mock-123-id'
            ))

            self.assertEqual(resp.done, True)
            self.assertEqual(resp.id, 'mock-123-id')
            self.assertEqual(resp.response, 'TEST_LRO_RESPONSE')
            self.assertIsNone(resp.error)

    @mock.patch("asyncio.wait_for")
    def test_call_lro_status_api_timeout_error(self, mock_wait_for):
        from aladdinsdk.api.client import AladdinAPI
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        test_subject = AladdinAPI('TrainJourneyAPI')

        mock_wait_for.side_effect = asyncio.TimeoutError()

        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api_response_1 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_2 = TestApiClientLroCalls.MockLroApiResponse(done=False, error=None, id='mock-123-id', meta=None, response=None)
            mock_call_api_response_3 = TestApiClientLroCalls.MockLroApiResponse(done=True, error=None, id='mock-123-id', meta=None,
                                                                                response='TEST_LRO_RESPONSE')
            mock_call_api.side_effect = [
                mock_call_api_response_1,
                mock_call_api_response_2,
                mock_call_api_response_3
            ]

            with self.assertRaises(AsdkApiException) as context:
                asyncio.run(test_subject.call_lro_status_api(
                    check_lro_status_endpoint="/longRunningOperations/{id}",
                    lro_id='mock-123-id'
                ))
                self.assertTrue("Long running operation timed out." in context.exception)


class TestApiClientSwaggerExtension(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_swagger_mapping_success(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        api_methods = test_subject.get_api_endpoint_methods()
        mapping_dicts = test_subject._generate_swagger_mappings()
        self.assertEqual(len(mapping_dicts[0]), len(api_methods))
        self.assertEqual(len(mapping_dicts[1]), len(api_methods))
        self.assertTrue(set(api_methods) == set(list(mapping_dicts[0].values())))

    @mock.patch('aladdinsdk.api.registry.AladdinAPICodegenDetails')
    def test_swagger_location_mapped_incorrectly(self, mock_codegen_details):
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        mock_codegen_details.api_name = 'TrainJourneyAPI'
        mock_codegen_details.api_module_path = 'fake_path'
        mock_codegen_details.host_url_path = '/no-path'
        mock_codegen_details.api_class_methods = ["method_one", "method_two"]
        mock_codegen_details.swagger_file_path = mock.MagicMock()
        mock_codegen_details.swagger_file_path.return_value = "non-existent-path"
        mock_codegen_details.swagger_file_path.exists.return_value = False

        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        test_subject._details = mock_codegen_details

        with self.assertRaises(AsdkApiException) as context:
            test_subject._generate_swagger_mappings()
            self.assertTrue("API [TrainJourneyAPI] is mapped to invalid swagger path [non-existent-path] ." in context.exception)

    @mock.patch('aladdinsdk.api.registry.AladdinAPICodegenDetails')
    @mock.patch('logging.Logger.debug')
    def test_swagger_unknown_method_should_not_be_mapped(self, mock_log_debug, mock_codegen_details):
        mock_codegen_details.api_class_methods = ["method_one"]

        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        mock_codegen_details.swagger_file_path = test_subject._details.swagger_file_path
        mock_codegen_details.api_name = test_subject._details.api_name
        test_subject._details = mock_codegen_details

        test_subject._generate_swagger_mappings()
        mock_log_debug.assert_called_with("Unable to map [method_one]. Method may not be callable via REST endpoint wrappers.")

    @mock.patch('aladdinsdk.api.registry.AladdinAPICodegenDetails')
    def test_swagger_location_incorrect(self, mock_codegen_details):
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        mock_codegen_details.api_name = 'TrainJourneyAPI'
        mock_codegen_details.api_module_path = 'fake_path'
        mock_codegen_details.host_url_path = '/no-path'
        mock_codegen_details.api_class_methods = ["method_one", "method_two"]

        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        test_subject._details = mock_codegen_details

        with self.assertRaises(AsdkApiException) as context:
            test_subject._generate_swagger_mappings()
            self.assertTrue("Api module path" in context.exception)

    @mock.patch('aladdinsdk.api.registry.AladdinAPICodegenDetails')
    def test_methods_not_exist(self, mock_codegen_details):
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        mock_codegen_details.api_name = 'TrainJourneyAPI'
        mock_codegen_details.api_module_path = 'aladdinsdk.api.codegen.reference_architecture.demo.train_journey.v1.train_journey'
        mock_codegen_details.host_url_path = 'api/reference-architecture/demo/train-journey/v1'
        mock_codegen_details.api_class_methods = ["method_one", "method_two"]

        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        test_subject._details = mock_codegen_details

        with self.assertRaises(AsdkApiException) as context:
            test_subject._generate_swagger_mappings()
            self.assertIn("Unknown method", str(context.exception))


class TestApiClientRestEndpointMethodMappings(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_get_mapping(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api.return_value = True  # no need to test call_api as part of this unit test
            test_subject.get("/trainJourneys/{id}", "foo", "bar")
            mock_call_api.assert_called_once_with(("/trainJourneys/{id}", "get"), "foo", "bar")

    def test_post_mapping(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api.return_value = True  # no need to test call_api as part of this unit test
            test_subject.post("/trainJourneys", "foo", "bar")
            mock_call_api.assert_called_once_with(("/trainJourneys", "post"), "foo", "bar")

    def test_delete_mapping(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api.return_value = True  # no need to test call_api as part of this unit test
            test_subject.delete("/trainJourneys/{id}", "foo", "bar")
            mock_call_api.assert_called_once_with(("/trainJourneys/{id}", "delete"), "foo", "bar")

    def test_patch_mapping(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        with mock.patch.object(test_subject, 'call_api') as mock_call_api:
            mock_call_api.return_value = True  # no need to test call_api as part of this unit test
            test_subject.patch("/trainJourneys/{trainJourney.id}", "foo", "bar")
            mock_call_api.assert_called_once_with(("/trainJourneys/{trainJourney.id}", "patch"), "foo", "bar")

    def test_put_mapping_non_existent(self):
        from aladdinsdk.api.client import AladdinAPI
        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        test_subject = AladdinAPI('TrainJourneyAPI')
        with self.assertRaises(AsdkApiException) as context:
            test_subject.put("/trainJourneys/{trainJourney.id}", "foo", "bar")
            self.assertIn("Incorrect endpoint path/method passed", str(context.exception))

    def test_endpoint_path_mapping_helper_python_method(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        self.assertEqual(test_subject._endpoint_path_mapping_helper("train_journey_api_create_train_journey"),
                         "train_journey_api_create_train_journey")

    def test_endpoint_path_mapping_helper_tuple(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        self.assertEqual(test_subject._endpoint_path_mapping_helper(("/trainJourneys", "post")), "train_journey_api_create_train_journey")
        self.assertEqual(test_subject._endpoint_path_mapping_helper(("/trainJourneys", "get")), "train_journey_api_list_train_journeys")

    def test_endpoint_path_mapping_helper_swagger_path(self):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        self.assertEqual(test_subject._endpoint_path_mapping_helper("/trainJourneys/{id}"), "train_journey_api_get_train_journey")
        self.assertIn(test_subject._endpoint_path_mapping_helper("/trainJourneys"),
                      ["train_journey_api_create_train_journey", "train_journey_api_list_train_journeys"])

    @mock.patch('logging.Logger.warning')
    def test_endpoint_path_mapping_helper_swagger_path_warning(self, mock_log_warning):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI')
        test_subject._endpoint_path_to_method_mappings[("/fake_swagger_path", "get")] = "fake_endpoint_python_get_method"
        test_subject._endpoint_path_to_method_mappings[("/fake_swagger_path", "put")] = "fake_endpoint_python_put_method"
        self.assertIn(test_subject._endpoint_path_mapping_helper("/fake_swagger_path"),
                      ["fake_endpoint_python_get_method", "fake_endpoint_python_put_method"])
        mock_log_warning.assert_called_with("Multiple methods map to path /fake_swagger_path. "
                                            "Input may need to be more specific - provide a tuple with "
                                            "(path, method) where method is one of ['get', 'put']")


class TestApiOauthComputeSession(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            "NB_USER": "TEST_USER"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()


class TestApiOauthRunLocal(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=["ACCESS_TOKEN123", 3600])
    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_api_client_get_oauth_token_success(self, oauth_token, secret):
        from aladdinsdk.api.client import AladdinAPI
        test_subject = AladdinAPI('TrainJourneyAPI', client_id='id', client_secret='secret', refresh_token='refresh_token')
        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            mock_filter_call.return_value = "TEST_RESPONSE"
            test_subject.call_api("train_journey_api_filter_train_journeys", {"test": "body"})
            self.assertIsNotNone(test_subject)


class TestGetOauthToken(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_oauth_set.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        class TestConfiguration(object):
            def __init__(self):
                self.api_key = {}
        self.test_configuration = TestConfiguration()

    @mock.patch('aladdinsdk.common.authentication.api.oauth_token_cred_client.get_access_token_and_ttl_from_oauth_server',
                return_value=['ACCESS_TOKEN123', 3600])
    def test_api_client_get_oauth_token_from_server(self, oauth_token):
        from aladdinsdk.common.authentication.api import ApiAuthUtil

        api_auth_util = ApiAuthUtil(configuration={}, client_id='id', client_secret='secret', refresh_token='token')
        result = api_auth_util._request_oauth_access_token_tuple(scopes="test.scope")
        self.assertEqual(result, ['ACCESS_TOKEN123', 3600])


class TestGetOauthTokenMissingSecret(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_incomplete.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_api_client_get_oauth_token_exception_missing_secret(self, oauth_param):
        from aladdinsdk.common.authentication.api import ApiAuthUtil

        api_auth_util = ApiAuthUtil(configuration={}, client_id='id', client_secret='secret')
        resp_access_token, resp_ttl = api_auth_util._request_oauth_access_token_tuple(scopes=None)
        self.assertIsNone(resp_access_token)
        self.assertIsNone(resp_ttl)

    @mock.patch('aladdinsdk.common.secrets.fsutil.read_secret_from_file', return_value=None)
    def test_api_client_get_basic_auth_exception_missing_pwd(self, param):
        from aladdinsdk.common.authentication.basicauth import basicauthutil
        from aladdinsdk.common.authentication.api import ApiAuthUtil
        from aladdinsdk.common.error.asdkerrors import AsdkApiException

        ApiAuthUtil(configuration={}, username='user')
        with self.assertRaises(AsdkApiException) as context:
            basicauthutil.fetch_password_from_user_settings()
            self.assertTrue("Insufficient API initialization information" in context.exception)


class Response:
    def __init__(self, data_set, next_page_token):
        self.next_page_token = next_page_token
        self.data_set = data_set
