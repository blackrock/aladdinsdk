import json
import os
from pathlib import Path
import tempfile
from unittest import TestCase, mock

import pandas as pd
from test.resources.testutils import utils
from test.resources.testutils import extmocks


class TestExportRegistryRegressions(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = mock.patch.dict(os.environ, {
            'ASDK_USER_CONFIG_FILE': 'test/resources/testdata/sample_user_settings_all_values_set.yaml',
            'defaultWebServer': 'http://dummy.dws.com',
        })
        cls.env.start()
        with mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get):
            utils.reload_modules()

    @classmethod
    def tearDownClass(cls):
        cls.env.stop()

    def test_export_to_bare_relative_filename(self):
        from aladdinsdk.common.exports.utils.validate_file_util import validate_file_and_path
        with tempfile.TemporaryDirectory() as directory:
            previous = os.getcwd()
            try:
                os.chdir(directory)
                self.assertTrue(validate_file_and_path('result.json', True))
                self.assertTrue(Path('result.json').exists())
            finally:
                os.chdir(previous)

    def test_model_json_uses_public_serialization(self):
        from aladdinsdk.common.exports.export_json import export_data

        class Model:
            __slots__ = ()

            def to_dict(self):
                return {'portfolioId': 'demo', 'positions': [{'quantity': 3}]}

        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'result.json'
            export_data(Model(), destination)
            self.assertEqual(json.loads(destination.read_text()), Model().to_dict())

    def test_unsupported_json_value_raises_export_exception(self):
        from aladdinsdk.common.exports.export_json import export_data
        from aladdinsdk.common.error.asdkerrors import AsdkExportDataException
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'result.json'
            with self.assertRaises(AsdkExportDataException):
                export_data(object(), destination)
            self.assertFalse(destination.exists())

    def test_dataframe_json_preserves_index(self):
        from aladdinsdk.common.exports.export_json import export_data
        frame = pd.DataFrame({'quantity': [3]}, index=['portfolio'])
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / 'result.json'
            export_data(frame, destination)
            self.assertEqual(json.loads(destination.read_text()), {
                'columns': ['quantity'], 'index': ['portfolio'], 'data': [[3]],
            })

    def test_registry_defaults_to_numerically_latest_major(self):
        from aladdinsdk.api import registry
        for versions in ({'v1': object(), 'v2': object()}, {'v2': object(), 'v10': object(), 'v1': object()}):
            with self.subTest(versions=list(versions)), mock.patch.dict(registry.AladdinAPIRegistry, {'DemoAPI': versions}):
                latest = 'v10' if 'v10' in versions else 'v2'
                self.assertIs(registry.get_api_details('DemoAPI'), versions[latest])
                self.assertIs(registry.get_api_details('DemoAPI', 'v1'), versions['v1'])
