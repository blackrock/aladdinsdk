import os
from aladdinsdk.common.error.asdkerrors import AsdkStorageException
from unittest import TestCase, mock
from test.resources.testutils import utils
from botocore.exceptions import ClientError


class TestStorageS3WithoutConfiguration(TestCase):

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
        })
        self.env_patcher.start()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('boto3.client')
    def test_get_client(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client._s3_client = None
        a = s3client.get_s3_client()
        self.assertEqual(a, mock_s3)

    @mock.patch('boto3.client')
    def test_upload_file(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client.upload_file('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
        mock_s3.upload_file.assert_called_once_with(Filename='test/resources/testdata/storage/s3/sample.txt', Bucket='test', Key='test.txt')

    @mock.patch('boto3.client')
    def test_upload_fileobj(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client.upload_fileobj('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
        mock_s3.upload_fileobj.assert_called_once_with(Fileobj='test/resources/testdata/storage/s3/sample.txt', Bucket='test', Key='test.txt')

    @mock.patch('boto3.client')
    def test_download_file(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client.download_file('test.txt', 'test/resources/testdata/storage/s3/sample_download.txt')
        mock_s3.download_file.assert_called_once_with(Bucket='test', Key='test.txt', Filename='test/resources/testdata/storage/s3/sample_download.txt')

    @mock.patch('boto3.client')
    def test_download_fileobj(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client.download_fileobj('test.txt', 'test/resources/testdata/storage/s3/sample_download.txt')
        mock_s3.download_fileobj.assert_called_once_with(Bucket='test', Key='test.txt', Fileobj='test/resources/testdata/storage/s3/sample_download.txt')

    @mock.patch('boto3.client')
    def test_delete_object(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file.yaml", bucket_name="test")
        s3client.delete_object('test.txt')
        mock_s3.delete_object.assert_called_once_with(Bucket='test', Key='test.txt')

    @mock.patch('boto3.client')
    def test_list_objects_in_bucket(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(s3_credentials_file="test/resources/testdata/storage/s3/credentials_file_legacy.yaml", bucket_name="test")
        s3client.list_objects_in_bucket()
        mock_s3.list_objects_v2.assert_called_once_with(Bucket='test')


class TestStorageS3WithConfiguration(TestCase):

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/storage/s3/user_config_creds_file.yaml"
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('boto3.client')
    def test_get_client(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()
        s3client._s3_client = None
        a = s3client.get_s3_client()
        self.assertEqual(a, mock_s3)

    @mock.patch('boto3.client')
    def test_upload_file(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client(bucket_name="test")
        s3client.upload_file('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
        mock_s3.upload_file.assert_called_once_with(Filename='test/resources/testdata/storage/s3/sample.txt', Bucket='test', Key='test.txt')


class TestStorageS3WithConfigurationDetails(TestCase):

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/storage/s3/user_config_creds.yaml"
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('boto3.client')
    def test_get_client(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()
        s3client._s3_client = None
        a = s3client.get_s3_client()
        mock_boto3_client.assert_called_with("s3", aws_access_key_id="dummy-key-id", aws_secret_access_key="dummy-secret-key", endpoint_url="http://localhost:9000", verify=True, config=mock.ANY)
        self.assertEqual(a, mock_s3)

    @mock.patch('boto3.client')
    def test_upload_file(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()
        s3client.upload_file('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
        mock_s3.upload_file.assert_called_once_with(Filename='test/resources/testdata/storage/s3/sample.txt', Bucket='dummy-bucket', Key='test.txt')


class TestStorageS3SetupErrorScenarios(TestCase):

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('boto3.client')
    def test_get_client_error_for_missing_configuration(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        with self.assertRaises(AsdkStorageException) as context:
            _ = S3Client(s3_credentials_file="FAKE_FILEPATH")
            self.assertTrue('S3 credentials not provided' in context.exception)


class TestStorageS3ErrorScenarios(TestCase):

    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com",
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/storage/s3/user_config_creds.yaml"
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('boto3.client')
    def test_get_client_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()
        s3client._s3_client = None
        s3client._endpoint_url = None
        with self.assertRaises(AsdkStorageException) as context:
            s3client.get_s3_client()
            self.assertTrue('S3 credentials not provided' in context.exception)

    @mock.patch('boto3.client')
    def test_upload_file_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.upload_file.side_effect = mock.Mock(side_effect=ClientError({'Error': {'Code': '404', 'Message': 'Not Found'}}, 'upload_file'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.upload_file('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
            self.assertTrue('Failed to upload file' in context.exception)

    @mock.patch('boto3.client')
    def test_upload_fileobj_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.upload_fileobj.side_effect = mock.Mock(side_effect=Exception('upload_fileobj error'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.upload_fileobj('test/resources/testdata/storage/s3/sample.txt', 'test.txt')
            self.assertTrue('Failed to upload file-like object to bucket' in context.exception)

    @mock.patch('boto3.client')
    def test_download_file_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.download_file.side_effect = mock.Mock(side_effect=Exception('download file error'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.download_file('test.txt', 'test/resources/testdata/storage/s3/sample.txt')
            self.assertTrue('Failed to download file' in context.exception)

    @mock.patch('boto3.client')
    def test_download_fileobj_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.download_fileobj.side_effect = mock.Mock(side_effect=Exception('download_fileobj error'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.download_fileobj('test.txt', 'test/resources/testdata/storage/s3/sample.txt')
            self.assertTrue('Failed to download file-like object to bucket' in context.exception)

    @mock.patch('boto3.client')
    def test_delete_object_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.delete_object.side_effect = mock.Mock(side_effect=Exception('delete object error'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.delete_object('test.txt')
            self.assertTrue('Failed to delete object' in context.exception)

    @mock.patch('boto3.client')
    def test_list_objects_in_bucket_error(self, mock_boto3_client):
        mock_s3 = mock.MagicMock()
        mock_s3.list_objects_v2.side_effect = mock.Mock(side_effect=Exception('list objects error'))
        mock_boto3_client.return_value = mock_s3

        from aladdinsdk.storage.s3 import S3Client
        s3client = S3Client()

        with self.assertRaises(AsdkStorageException) as context:
            s3client.list_objects_in_bucket()
            self.assertTrue('Failed to list objects in bucket' in context.exception)