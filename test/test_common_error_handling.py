from unittest import TestCase, mock
import os

from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkEmailNotificationException, AsdkSetupException
from aladdinsdk.common.error.handlers.abstract import exception_type_matches
from test.resources.testutils import utils


class TestCommonErrorAbstractUtil(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
        })
        self.env_patcher.start()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_exception_type_matches(self):
        from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkSetupException

        test_exception = AsdkApiException("TEST")
        self.assertTrue(exception_type_matches(AsdkApiException, test_exception))
        self.assertTrue(exception_type_matches("aladdinsdk.common.error.asdkerrors.AsdkApiException", test_exception))
        self.assertTrue(exception_type_matches("aladdinsdk.common*AsdkApiException", test_exception))

        self.assertFalse(exception_type_matches(AsdkSetupException, test_exception))
        self.assertFalse(exception_type_matches("aladdinsdk.common.error.asdkerrors.AsdkSetupException", test_exception))
        self.assertFalse(exception_type_matches("aladdinsdk.common*AsdkSetupException", test_exception))


class TestCommonErrorHandlingDisabled(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_error_handling_disabled.yaml",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_exception_raised_but_handling_disabled(self):
        from aladdinsdk.api.client import AladdinAPI
        from aladdinsdk.common.error.asdkerrors import AsdkApiException

        test_subject = AladdinAPI('TrainJourneyAPI')

        with self.assertRaises(AsdkApiException) as context:
            test_subject.get_api_endpoint_signature('non_existent_endpoint')
            self.assertTrue('Incorrect endpoint path/method passed' in context.exception)


class TestCommonErrorHandlerUtils(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
        })
        self.env_patcher.start()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_exception_type_match_from_lists(self):
        from aladdinsdk.common.error.handler import _exception_in_supported_list

        from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkSetupException, AsdkExportDataException
        test_supported_list_success_1 = [AsdkApiException, AsdkSetupException, AsdkExportDataException]
        test_supported_list_success_2 = ["aladdinsdk.common.error.asdkerrors.AsdkApiException",
                                         "aladdinsdk.common.error.asdkerrors.AsdkSetupException",
                                         "aladdinsdk.common.error.asdkerrors.AsdkExportDataException"]
        test_supported_list_failure = [AsdkSetupException]
        test_exception = AsdkApiException("TEST")
        test_exception_2 = AsdkExportDataException("TEST")

        self.assertTrue(_exception_in_supported_list(test_supported_list_success_1, test_exception))
        self.assertTrue(_exception_in_supported_list(test_supported_list_success_2, test_exception))
        self.assertTrue(_exception_in_supported_list(test_supported_list_success_2, test_exception_2))

        self.assertFalse(_exception_in_supported_list(test_supported_list_failure, test_exception))

    def test_exception_map_to_handler(self):
        from aladdinsdk.common.error.handler import _map_exception_to_handler

        from aladdinsdk.common.error.asdkerrors import AsdkApiException
        from pydantic.error_wrappers import ValidationError

        from aladdinsdk.common.error.handlers.api import APIExceptionHandler

        self.assertEqual(type(_map_exception_to_handler(AsdkApiException("TEST"))), APIExceptionHandler)
        self.assertEqual(type(_map_exception_to_handler(ValidationError(None, "TEST"))), APIExceptionHandler)

    def test_register_handler_class_success(self):
        from aladdinsdk.common.error.handler import register_handler_class, _asdk_exception_handlers
        from aladdinsdk.common.error.handlers import abstract

        class TestNewExtendedHandler(abstract.AbstractAsdkExceptionHandler):
            supported_exception_modules = [
                ZeroDivisionError
            ]

            original_exception = None

            error_code = abstract.AsdkErrorCode.AE004

            def __init__(self, original_exception):
                self.original_exception = original_exception

            def handle_error(self):
                # sample test error handler class for unit testing, does not need implementation
                pass

        self.assertEqual(len(_asdk_exception_handlers), 3)
        register_handler_class(TestNewExtendedHandler)
        self.assertEqual(len(_asdk_exception_handlers), 4)
        self.assertIn(TestNewExtendedHandler, _asdk_exception_handlers)

    def test_register_handler_class_failure(self):
        from aladdinsdk.common.error.handler import register_handler_class

        class NotAValidHandler():
            # Empty class definition that does not extend AbstractAsdkExceptionHandler
            pass

        with self.assertRaises(AsdkSetupException) as context:
            register_handler_class(NotAValidHandler)
            self.assertEqual("Unable to register provided exception handler. Must be an implementation of AbstractAsdkExceptionHandler.",
                             context.exception)


class TestCommonErrorHandlerApiHandler(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_api_handle_error(self):
        from aladdinsdk.api.client import AladdinAPI
        from pydantic.error_wrappers import ValidationError
        from aladdinsdk.api.codegen.platform.infrastructure.token.v1.TokenAPI.exceptions import UnauthorizedException

        test_subject = AladdinAPI('TrainJourneyAPI')

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            mock_filter_call.side_effect = UnauthorizedException("Mock UnauthorizedException")
            with self.assertRaises(UnauthorizedException) as context:
                test_subject.call_api('train_journey_api_filter_train_journeys', {"payload_key": "payload value"})
                self.assertIn("Mock UnauthorizedException", context.exception.message)

        with mock.patch.object(test_subject.instance, 'train_journey_api_filter_train_journeys_with_http_info') as mock_filter_call:
            from pydantic import BaseModel, Field

            class A(BaseModel):
                a: str = Field(None, alias="А")

            mock_filter_call.side_effect = ValidationError("", A)
            with self.assertRaises(ValidationError) as context:
                test_subject.call_api('train_journey_api_filter_train_journeys', {"payload_key": "payload value"})
                self.assertTrue("Mock ValidationError" in context.exception)


class TestCommonErrorHandlerExportDataHandler(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_export_data_handle_error(self):
        from aladdinsdk.common.exports import export
        test_subject = export

        with mock.patch('aladdinsdk.common.exports.export_pickle.write_pickle', side_effect=OSError('Exception')):
            with self.assertRaises(OSError) as context:
                file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
                test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)


class TestCommonErrorHandlerEmailNotifications(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_error_email_notifications_set.yaml",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_export_data_handle_error(self):
        from aladdinsdk.common.error.notifications import email_notifications_for_errors
        self.test_subject = email_notifications_for_errors

        with mock.patch('aladdinsdk.common.error.notifications.email_notifications_for_errors.send_email_notification',
                        side_effect=AsdkEmailNotificationException):
            with self.assertRaises(Exception) as context:
                test_exception = AsdkApiException("TEST")
                self.test_subject.email_notification_for_exception(test_exception)
                self.assertTrue('Unable to send email notification for exception' in context.exception)
