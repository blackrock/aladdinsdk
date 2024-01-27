import datetime
import json
from unittest import TestCase, mock
import os
from test.resources.testdata.exportdata.api_unserializable_test_object import ApiUnserializableTestObject
from test.resources.testdata.exportdata.api_serializable_test_object import ApiSerializableTestObject
from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
from test.resources.testutils import utils
import pandas as pd


class TestCommonExportsWithOverWriteDataSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.exports import export
        self.test_subject = export
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_csv_export_valid(self):
        input_1 = pd.DataFrame([1, 2, 3])
        result_1 = self.test_subject.export_data(input_1, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_1)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_2 = [1, 2, 3]
        result_2 = self.test_subject.export_data(input_2, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_2)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        with self.assertRaises(AsdkExportDataException) as context:
            input_3 = [self.get_unserializable_input_response_object(), self.get_unserializable_input_response_object()]
            self.test_subject.export_data(input_3, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
            self.assertTrue('Export Data Exception' in context.exception)

        input_4 = {"A": 1, "B": 2}
        result_4 = self.test_subject.export_data(input_4, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_4)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_5 = "abcdefg"
        result_5 = self.test_subject.export_data(input_5, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_5)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_6 = self.get_input_json()
        result_6 = self.test_subject.export_data(input_6, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_6)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_7 = 123
        result_7 = self.test_subject.export_data(input_7, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_7)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_8 = self.get_serializable_input_response_object()
        result_8 = self.test_subject.export_data(input_8, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_8)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        input_9 = self.get_input_json()
        result_9 = self.test_subject.export_data(input_9, './test/resources/testdata/exportdata/export_csv_file_test.csv', 'csv')
        self.assertTrue(result_9)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_csv_file_test.csv'))

        os.remove('./test/resources/testdata/exportdata/export_csv_file_test.csv')

    def test_excel_export_valid(self):
        input_1 = pd.DataFrame([1, 2, 3])
        result_1 = self.test_subject.export_data(input_1, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_1)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_2 = [1, 2, 3]
        result_2 = self.test_subject.export_data(input_2, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_2)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_3 = self.get_input_json()
        result_3 = self.test_subject.export_data(input_3, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_3)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_4 = [self.get_unserializable_input_response_object(), self.get_unserializable_input_response_object()]
        with self.assertRaises(AsdkExportDataException) as context:
            self.test_subject.export_data(input_4, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
            self.assertTrue('Export Data Exception' in context.exception)

        input_5 = {"A": 1, "B": 2}
        result_5 = self.test_subject.export_data(input_5, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_5)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_6 = "abcdefg"
        result_6 = self.test_subject.export_data(input_6, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_6)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_7 = 123
        result_7 = self.test_subject.export_data(input_7, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_7)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_8 = [[1, 2, 3], [4, 5, 6]]
        result_8 = self.test_subject.export_data(input_8, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_8)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_9 = self.get_serializable_input_response_object()
        result_9 = self.test_subject.export_data(input_9, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_9)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        input_10 = self.get_input_json()
        result_10 = self.test_subject.export_data(input_10, './test/resources/testdata/exportdata/export_excel_file_test.xlsx', 'excel')
        self.assertTrue(result_10)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_excel_file_test.xlsx'))

        os.remove('./test/resources/testdata/exportdata/export_excel_file_test.xlsx')

    def test_json_export_valid(self):
        input_1 = pd.DataFrame([1, 2, 3])
        result_1 = self.test_subject.export_data(input_1, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_1)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_2 = [1, 2, 3]
        result_2 = self.test_subject.export_data(input_2, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_2)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_3 = [[1, 2, 3], [4, 5, 6]]
        result_3 = self.test_subject.export_data(input_3, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_3)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_4 = [self.get_unserializable_input_response_object(), self.get_unserializable_input_response_object()]
        with self.assertRaises(AsdkExportDataException) as context:
            self.test_subject.export_data(input_4, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
            self.assertTrue('Export Data Exception' in context.exception)

        input_5 = {"A": 1, "B": 2}
        result_5 = self.test_subject.export_data(input_5, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_5)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_6 = "abcdefg"
        result_6 = self.test_subject.export_data(input_6, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_6)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_7 = self.get_input_json()
        result_7 = self.test_subject.export_data(input_7, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_7)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        input_8 = self.get_serializable_input_response_object()
        result_8 = self.test_subject.export_data(input_8, './test/resources/testdata/exportdata/export_json_file_test.json', 'json')
        self.assertTrue(result_8)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_json_file_test.json'))

        os.remove('./test/resources/testdata/exportdata/export_json_file_test.json')

    def test_pickle_export_valid(self):
        input_1 = pd.DataFrame([1, 2, 3])
        result_1 = self.test_subject.export_data(input_1, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_1)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_2 = [1, 2, 3]
        result_2 = self.test_subject.export_data(input_2, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_2)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_3 = [self.get_unserializable_input_response_object().__dict__, self.get_unserializable_input_response_object().__dict__]
        result_3 = self.test_subject.export_data(input_3, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_3)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_4 = [self.get_unserializable_input_response_object(), self.get_unserializable_input_response_object()]
        result_4 = self.test_subject.export_data(input_4, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_4)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_5 = {"A": 1, "B": 2}
        result_5 = self.test_subject.export_data(input_5, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_5)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_6 = "abcdefg"
        result_6 = self.test_subject.export_data(input_6, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_6)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        input_7 = self.get_unserializable_input_response_object()
        result_7 = self.test_subject.export_data(input_7, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_7)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        # exception for pickle export
        with mock.patch('aladdinsdk.common.exports.export_pickle.write_pickle', side_effect=Exception('Exception')):
            with self.assertRaises(Exception) as context:
                file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

        input_8 = self.get_input_json()
        result_8 = self.test_subject.export_data(input_8, './test/resources/testdata/exportdata/export_pickle_file_test.pkl', 'pickle')
        self.assertTrue(result_8)
        self.assertTrue(self.does_file_have_content('./test/resources/testdata/exportdata/export_pickle_file_test.pkl'))

        os.remove('./test/resources/testdata/exportdata/export_pickle_file_test.pkl')

    def test_file_validation(self):
        # test incorrect path
        with self.assertRaises(AsdkExportDataException) as context:
            file_path = './test/resourcess/testdata/exportdata/test_export_file.csv'
            self.test_subject.export_data([1, 2, 3], file_path, 'csv')
            self.assertTrue('Unable to validate file path and permissions' in context.exception)

        # test data already existing in file and overwrite flag set
        file_path_2 = './test/resources/testdata/exportdata/test_export_file.json'
        open(file_path_2, 'w')
        df = pd.DataFrame([1, 2, 3])
        df.to_json(file_path_2)
        result_2 = self.test_subject.export_data([1, 2, 3], file_path_2, 'json')
        self.assertTrue(result_2)
        os.remove(file_path_2)

        # test new empty file
        file_path_3 = './test/resources/testdata/exportdata/test_export_file.json'
        open(file_path_3, 'w')
        result_3 = self.test_subject.export_data([1, 2, 3], file_path_3, 'json')
        self.assertTrue(result_3)
        os.remove(file_path_3)

        with self.assertRaises(AsdkExportDataException) as context:
            file_path = './test/resourcess/testdata/exportdata/test_export_file.csv'
            self.test_subject.export_data([1, 2, 3], file_path, 'csv')
            self.assertTrue('Unable to validate file path and permissions' in context.exception)

        # test file that doesn't exist
        file_path_4 = './test/resources/testdata/exportdata/test_export_file.pkl'
        result_4 = self.test_subject.export_data([1, 2, 3], file_path_4, 'pickle')
        self.assertTrue(result_4)
        os.remove(file_path_4)

    def test_write_json_exception(self):
        file_path = './test/resources/testdata/exportdata/export_json_file_test.json'
        with mock.patch('aladdinsdk.common.exports.export_json.json.dumps', side_effect=TypeError('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.export_data([1, 2, 3], file_path, 'json')
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

    def test_write_pickle_exception(self):
        file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
        with mock.patch('aladdinsdk.common.exports.utils.write_file_util.pickle.dump', side_effect=TypeError('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.export_data([{1: 1}], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

    def test_file_validation_exception(self):
        file_path = './test/resources/testdata/exportdata/test.pkl'
        with mock.patch('os.access', side_effect=Exception('Exception')):
            with self.assertRaises(Exception) as context:
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

    def test_get_supported_types(self):
        result = self.test_subject.get_supported_export_types()
        self.assertEqual(result, ['csv', 'excel', 'json', 'pickle'])

    def test_invalid_supported_types(self):
        file_path = './test/resources/testdata/exportdata/test_export_file.pkl'
        result = self.test_subject.export_data([1, 2, 3], file_path, 'pkl')
        self.assertFalse(result)

    def test_export_class_exception_raised(self):
        with mock.patch('aladdinsdk.common.exports.export.validate_file_and_path', side_effect=Exception('Exception')):
            with self.assertRaises(Exception) as context:
                file_path = './test/resources/testdata/exportdata/test_export_file.pkl'
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

    def test_write_util_exception(self):
        # for json
        with mock.patch('os.stat', side_effect=OSError('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                file_path = './test/resources/testdata/exportdata/export_json_file_test.json'
                self.test_subject.export_data([1, 2, 3], file_path, 'json')
                self.assertTrue('Exception' in context.exception)

        # for pickle
        with mock.patch('aladdinsdk.common.exports.utils.write_file_util.write_pickle', side_effect=Exception('Exception')):
            with self.assertRaises(Exception) as context:
                file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

    def test_export_data_other_exception(self):
        # test Type Error
        with mock.patch('aladdinsdk.common.exports.export.validate_file_and_path', side_effect=TypeError('Exception')):
            with self.assertRaises(TypeError) as context:
                file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

        # test Value Error
        with mock.patch('aladdinsdk.common.exports.export.validate_file_and_path', side_effect=ValueError('Exception')):
            with self.assertRaises(ValueError) as context:
                file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)

    def does_file_have_content(self, file_path):
        return os.stat(file_path).st_size != 0

    def clear_file(self, file_path):
        open(file_path, 'w')

    def get_unserializable_input_response_object(self):
        return ApiUnserializableTestObject()

    def get_serializable_input_response_object(self):
        return ApiSerializableTestObject()

    def get_input_json(self):
        input_obj = {
            'key1': 1,
            'key2': True,
            'key3': datetime.date(2020, 1, 5).isoformat(),
            'key4': [1, 2, 3],
            'key5': datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc).isoformat()
        }
        return json.dumps(input_obj)


class TestCommonExportsWithoutOverWriteDataSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_incomplete.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.exports import export
        self.test_subject = export
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_file_validation_without_overwrite_data_set(self):
        # test data already existing in file and overwrite flag not set
        file_path = './test/resources/testdata/exportdata/test_export_file.csv'
        open(file_path, 'w')
        df = pd.DataFrame([1, 2, 3])
        df.to_csv(file_path, sep='\t')
        result = self.test_subject.export_data([1, 2, 3], file_path, 'csv')
        self.assertFalse(result)
        os.remove(file_path)

    def test_new_file_validation_without_date_format_set(self):
        # test new empty file and date format not set
        file_path = './test/resources/testdata/exportdata/test_new_file.xlsx'
        open(file_path, 'w')
        with self.assertRaises(AsdkExportDataException) as context:
            file_path = './test/resources/testdata/exportdata/test_new_file.xlsx'
            self.test_subject.export_data(self.get_unserializable_input_response_object().__dict__, file_path, 'excel')
            self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

    def test_file_validation_exception_without_date_format_set(self):
        # test new empty file and date format not set
        file_path = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
        open(file_path, 'wb')
        with mock.patch('aladdinsdk.common.exports.export.validate_file_and_path', side_effect=AsdkExportDataException('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.export_data([1, 2, 3], file_path, 'pickle')
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

    def test_write_file_util_exceptions(self):
        # test exception when writing to json
        file_path = './test/resources/testdata/exportdata/export_json_file_test.json'
        open(file_path, 'w')
        with mock.patch('aladdinsdk.common.exports.export.export_data', side_effect=AsdkExportDataException('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.export_data([1, 2, 3], file_path, 'json')
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

    def get_unserializable_input_response_object(self):
        return ApiUnserializableTestObject()

    def get_serializable_input_response_object(self):
        return ApiSerializableTestObject()


class TestCommonExportsWithMalformedOverWriteDataSet(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_malformed_overwrite_data.yaml",
            })
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.exports import export
        self.test_subject = export
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_export_raises_error(self):
        # test file with existing data
        file_path = './test/resources/testdata/exportdata/export_csv_file_test.csv'
        df = pd.DataFrame([1, 2, 3])
        df.to_csv(file_path, sep='\t')
        with self.assertRaises(AsdkExportDataException) as context:
            input_1 = pd.DataFrame([1, 2, 3])
            self.test_subject.export_data(input_1, file_path, 'csv')
            self.assertTrue('Overwrite data flag type incorrect' in context.exception)
        os.remove(file_path)


class TestWriteUtil(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {})
        self.env_patcher.start()
        utils.reload_modules()
        from aladdinsdk.common.exports.utils import write_file_util
        self.test_subject = write_file_util
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_write_raises_error(self):
        # test write json exception
        file_path = './test/resources/testdata/exportdata/export_json_file_test.json'
        open(file_path, 'w')
        with mock.patch('builtins.open', side_effect=OSError('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.write_json([1, 2, 3], file_path)
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path)

        # test write pickle exception
        file_path_2 = './test/resources/testdata/exportdata/export_pickle_file_test.pkl'
        open(file_path_2, 'wb')
        with mock.patch('builtins.open', side_effect=OSError('Exception')):
            with self.assertRaises(AsdkExportDataException) as context:
                self.test_subject.write_pickle([1, 2, 3], file_path_2)
                self.assertTrue('Exception' in context.exception)
        os.remove(file_path_2)
