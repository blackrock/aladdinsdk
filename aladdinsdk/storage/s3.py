import boto3.s3
import yaml
import boto3

from botocore.client import BaseClient
from botocore.config import Config
from botocore.exceptions import ClientError

from aladdinsdk.common.error.asdkerrors import AsdkStorageException
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload
import logging

_logger = logging.getLogger(__name__)


class S3Client():
    """
    S3Client class to interact with S3 storage.
    """

    _endpoint_url: str
    _s3_credentials_file: str
    _access_key_id: str
    _secret_access_key: str
    _bucket_name: str
    _s3_client: boto3.session.Session.client

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def __init__(self,
                 endpoint_url: str = None,
                 s3_credentials_file: str = None,
                 access_key_id: str = None,
                 secret_access_key: str = None,
                 bucket_name: str = None):
        """
        Initialize S3Client with provided credentials.

        Args:
            endpoint_url (str, optional): StorageGrid S3 URL. Defaults to None.
            s3_credentials_file (str, optional): S3 Credentials file is a yaml file with Access Key ID and Secret Access Key fields. Defaults to None.
            access_key_id (str, optional): S3 bucket Access Key ID. Defaults to None.
            secret_access_key (str, optional): S3 bucket Secret Access Key. Defaults to None.
            bucket_name (str, optional): S3 bucket name. Users can optionally provide bucket name in operational method. Defaults to None.
        """
        self._endpoint_url = endpoint_url if endpoint_url is not None else user_settings.get_storage_s3_endpoint_url()
        self._s3_credentials_file = s3_credentials_file if s3_credentials_file is not None else user_settings.get_storage_s3_credentials_file()
        self._access_key_id = access_key_id if access_key_id is not None else user_settings.get_storage_s3_access_key_id()
        self._secret_access_key = secret_access_key if secret_access_key is not None else user_settings.get_storage_s3_secret_access_key()
        self._bucket_name = bucket_name if bucket_name is not None else user_settings.get_storage_s3_bucket_name()

        if (self._access_key_id is None or self._secret_access_key is None) and (self._s3_credentials_file is not None):
            _logger.debug(f"Reading S3 credentials from file {self._s3_credentials_file}...")
            try:
                with open(self._s3_credentials_file, 'r') as s3integration_creds_key_file:
                    s3integration_creds = yaml.safe_load(s3integration_creds_key_file)
                    # read access key id (prefer 'access_key_id' over the legacy 'access_key')
                    if "accessKey" in s3integration_creds:
                        self._access_key_id = s3integration_creds['accessKey']
                    if "access_key_id" in s3integration_creds:
                        self._access_key_id = s3integration_creds['access_key_id']
                    # read access secret key id (prefer 'access_secret_key' over the legacy 'secret_key')
                    if "secretKey" in s3integration_creds:
                        self._secret_access_key = s3integration_creds['secretKey']
                    if "secret_access_key" in s3integration_creds:
                        self._secret_access_key = s3integration_creds['secret_access_key']
            except Exception as e:
                _logger.warning(f"Failed to read S3 credentials from file {self._s3_credentials_file}: {e}")

        self._s3_client = self._create_s3_client()

    def _create_s3_client(self) -> BaseClient:
        """
        Create boto3 S3 client with provided credentials.

        Raises:
            AsdkStorageException: S3 credentials not provided

        Returns:
            S3: boto3 S3 client
        """
        for key, value in {"endpoint_url": self._endpoint_url,
                           "access_key_id": self._access_key_id,
                           "secret_access_key": self._secret_access_key}.items():
            if value is None:
                _logger.warning(f"Missing S3 {key} in configuration.")

        if None in (self._endpoint_url, self._access_key_id, self._secret_access_key):
            raise AsdkStorageException("S3 credentials not provided. ")

        s3_config = Config(connect_timeout=30, retries={'max_attempts': 1})
        boto3_s3_client = boto3.client('s3',
                                       aws_access_key_id=self._access_key_id,
                                       aws_secret_access_key=self._secret_access_key,
                                       endpoint_url=self._endpoint_url,
                                       verify=True,
                                       config=s3_config)
        _logger.debug(f"Created S3 client with endpoint_url: {self._endpoint_url}")
        return boto3_s3_client

    def get_s3_client(self) -> BaseClient:
        """
        Get the underlying S3 client object.

        Returns:
            BaseClient: boto3 s3 client
        """
        if self._s3_client is None:
            self._s3_client = self._create_s3_client()
        return self._s3_client

    def upload_file(self, filename: str, key: str, bucket_name: str = None):
        """
        Upload a file to an S3 object.

        Args:
            filename (str): Path to the file to upload
            key (str): Name of the key to upload to
            bucket_name (str, optional): Name of the bucket to upload to. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: If unable to upload file
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            self._s3_client.upload_file(Filename=filename, Bucket=bucket_name, Key=key)
            _logger.debug(f"Uploaded file {filename} to bucket {bucket_name} with object_name {key}")
        except ClientError as e:
            raise AsdkStorageException(f"Failed to upload file {filename} to bucket {bucket_name} with object_name {key}") from e

    def upload_fileobj(self, fileobj: any, key: str, bucket_name: str = None):
        """
        Upload a file-like object to S3. Must be in binary mode.

        Args:
            fileobj (any):  A file-like object to upload. At a minimum, it must implement the read method, and must return bytes.
            key (str): The name of the key to upload to.
            bucket_name (str, optional): Name of the bucket to upload to. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: If unable to upload file object
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            self._s3_client.upload_fileobj(Fileobj=fileobj, Bucket=bucket_name, Key=key)
            _logger.debug(f"Uploaded file-like object to bucket {bucket_name} with object_name {key}")
        except Exception as e:
            raise AsdkStorageException(f"Failed to upload file-like object to bucket {bucket_name} with object_name {key}") from e

    def download_file(self, key: str, filename: str, bucket_name: str = None):
        """
        Download an S3 object to a file.

        Args:
            key (str): The nae of the key to download from.
            filename (str): The path to the file to download to.
            bucket_name (str, optional): Name o the bucket to download from. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: If unable to download file
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            self._s3_client.download_file(Bucket=bucket_name, Key=key, Filename=filename)
            _logger.debug(f"Downloaded file with key {key} from bucket {bucket_name} to {filename}")
        except Exception as e:
            raise AsdkStorageException(f"Failed to download file with key {key} from bucket {bucket_name} to {filename}") from e

    def download_fileobj(self, key: str, fileobj: any, bucket_name: str = None):
        """
        Download an object from S3 to a file-like object. The file-like object must be in binary mode.

        Args:
            key (str): The name of the key to download from.
            fileobj (any): A file-like object to download into. At minimum, it must implement the write method and accept bytes.
            bucket_name (str, optional): Name of the bucket to download from. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: _description_
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            self._s3_client.download_fileobj(Bucket=bucket_name, Key=key, Fileobj=fileobj)
            _logger.debug(f"Downloaded file-like object with key {key} from bucket {bucket_name}")
        except Exception as e:
            raise AsdkStorageException(f"Failed to download file-like object with key {key} from bucket {bucket_name}") from e

    def delete_object(self, key: str, bucket_name: str = None):
        """
        Removes an object from a bucket. (The behavior depends on the bucket's versioning state.)

        Args:
            key (str): Key name of the object to delete.
            bucket_name (str, optional): Name of the bucket containing the object. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: If unable to delete object
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            self._s3_client.delete_object(Bucket=bucket_name, Key=key)
            _logger.debug(f"Deleted object with key {key} from bucket {bucket_name}")
        except Exception as e:
            raise AsdkStorageException(f"Failed to delete object with key {key} from bucket {bucket_name}") from e

    def list_objects_in_bucket(self, bucket_name: str = None):
        """
        Returns some or all (up to 1,000) of the objects in a bucket with each request.

        Args:
            bucket_name (str, optional): Name of the bucket containing the objects. Defaults to bucket name set at client creation.

        Raises:
            AsdkStorageException: If unable to list objects

        Returns:
            list: List of objects in the bucket
        """
        if bucket_name is None:
            bucket_name = self._bucket_name
        try:
            response = self._s3_client.list_objects_v2(Bucket=bucket_name)
            object_list_response = response.get('Contents', [])
            _logger.debug(f"Returning listed objects in bucket {bucket_name}")
            return object_list_response
        except Exception as e:
            raise AsdkStorageException(f"Failed to list objects in bucket {bucket_name}") from e
