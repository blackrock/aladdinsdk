from unittest import TestCase, mock
import os
from aladdinsdk.common.secrets import fsutil, keyringutil
from test.resources.testutils import utils


class TestCommonSecretsFSUtil(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "defaultWebServer": "http://dummy.dws.com",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def test_read_secret_from_file_default(self):
        content = fsutil.read_secret_from_file('test/resources/non_existent_file.txt', 'default_val')
        self.assertEqual(content, "default_val")

    def test_read_secret_from_file(self):
        content = fsutil.read_secret_from_file('test/resources/testdata/sample_secret_text_file.txt')
        self.assertEqual(content, "shh!thisisasecretdude,readitandforget!")

    def test_read_secret_from_yaml_file_default(self):
        content = fsutil.read_secret_from_yaml_file('test/resources/testdata/sample_vault_inject_1.yaml', 'incorrect_key', 'default_val')
        self.assertEqual(content, "default_val")

        content = fsutil.read_secret_from_yaml_file('test/resources/malformed_yaml_example.yaml', 'foo', 'default_val')
        self.assertEqual(content, "default_val")

        content = fsutil.read_secret_from_yaml_file('test/resources/non_existent_file.yaml', 'foo', 'default_val')
        self.assertEqual(content, "default_val")

        content = fsutil.read_secret_from_yaml_file('test/resources/non_existent_file.yaml', 'foo')
        self.assertIsNone(content)

    def test_read_secret_from_yaml_file_success(self):
        content = fsutil.read_secret_from_yaml_file('test/resources/testdata/sample_vault_inject_1.yaml', 'test_key')
        self.assertEqual(content, "test_val")

    def test_read_secret_from_yaml_file_yaml_error(self):
        content = fsutil.read_secret_from_yaml_file('test/resources/testdata/malformed_yaml_example.yaml', 'test_key')
        self.assertIsNone(content)

    def test_password_encryption(self):
        sample_encrypted_password_file = 'test/resources/testdata/sample_encrypted_password.txt'
        if os.path.isfile(sample_encrypted_password_file):
            os.remove(sample_encrypted_password_file)

        # Encryption
        fsutil.store_encrypted_content_in_file("samplepassword", sample_encrypted_password_file, None,
                                               'test/resources/testdata/sample_encryption_key.txt')
        password_stored = os.path.isfile(sample_encrypted_password_file)
        self.assertEqual(password_stored, True)

        # Decryption
        plain_password = fsutil.decrypt_file_content(sample_encrypted_password_file, None,
                                                     'test/resources/testdata/sample_encryption_key.txt')
        self.assertEqual(plain_password, 'samplepassword')

        # cleanup
        if os.path.isfile(sample_encrypted_password_file):
            os.remove(sample_encrypted_password_file)


class TestCommonSecretsKeyringutil(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_local_test_keyring.yaml",
            "defaultWebServer": "http://dummy.dws.com",
        })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self):
        utils.reload_modules()
        return super().setUp()

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_delete_user_password(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        keyringutil.delete_user_password()
        mock_keyring.delete_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri")

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_delete_user_password_password_delete_error(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_keyring.errors.PasswordDeleteError = Exception
        mock_keyring.delete_password.side_effect = mock_keyring.errors.PasswordDeleteError()
        keyringutil.delete_user_password()
        mock_keyring.delete_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri")

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_store_user_password(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        keyringutil.store_user_password("shakimaan")
        mock_keyring.set_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri", "shakimaan")

    @mock.patch('aladdinsdk.common.secrets.keyringutil.getpass.getpass')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_store_user_password_with_prompt_user(self, mock_is_keyring_available, mock_keyring, mock_getpass):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_getpass.return_value = "shakimaan"

        keyringutil.store_user_password(prompt_user=True)
        mock_keyring.set_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri", "shakimaan")
        self.assertEqual(mock_getpass.call_count, 2)

    @mock.patch('aladdinsdk.common.secrets.keyringutil.getpass.getpass')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_store_user_password_with_prompt_user_twice(self, mock_is_keyring_available, mock_keyring, mock_getpass):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_getpass.side_effect = ["shakimaan", "typo", "shakimaan", "shakimaan"]

        keyringutil.store_user_password(prompt_user=True)
        mock_keyring.set_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri", "shakimaan")
        self.assertEqual(mock_getpass.call_count, 4)

    @mock.patch('aladdinsdk.common.secrets.keyringutil.getpass.getpass')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    def test_store_user_password_with_prompt_user_multiple_times_no_password(self, mock_keyring, mock_getpass):
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_getpass.side_effect = ["shakimaan", "typo", "shakimaan", "typo2", "shaktimaan", "typo3"]

        keyringutil.store_user_password(prompt_user=True)
        mock_keyring.set_password.assert_not_called()
        self.assertEqual(mock_getpass.call_count, 6)  # Number of max retries times 2

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    def test_store_user_password_missing_keyring(self, mock_keyring):
        mock_keyring.get_keyring.return_value = None
        keyringutil.store_user_password("shaktimaan")
        mock_keyring.set_password.assert_not_called()

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_store_user_password_password_set_error(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_keyring.errors.PasswordSetError = Exception
        mock_keyring.set_password.side_effect = mock_keyring.errors.PasswordSetError()
        keyringutil.store_user_password("shaktimaan")
        mock_keyring.set_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri", "shaktimaan")

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_get_user_password(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = True
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_keyring.get_password.return_value = "shaktimaan"
        test_pwd = keyringutil.get_user_password()
        mock_keyring.get_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri")
        self.assertEqual(test_pwd, "shaktimaan")

        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        mock_keyring.get_password.return_value = None
        test_pwd = keyringutil.get_user_password()
        mock_keyring.get_password.assert_called_with("ASDK-PASSWORD-http://dummy.dws.com", "gvmoshastri")
        self.assertEqual(test_pwd, None)

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    @mock.patch('aladdinsdk.common.secrets.keyringutil._is_keyring_available')
    def test_get_user_password_missing_keyring(self, mock_is_keyring_available, mock_keyring):
        mock_is_keyring_available.return_value = False
        mock_keyring.get_keyring.return_value = None
        test_pwd = keyringutil.get_user_password()
        mock_keyring.get_password.assert_not_called()
        self.assertEqual(test_pwd, None)


class TestCommonSecretsKeyringutilNotCalledOutsideLocal(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_all_values_set.yaml",
            "defaultWebServer": "http://dummy.dws.com"})
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self):
        utils.reload_modules()
        return super().setUp()

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    def test_delete_user_password_not_called_outside_local(self, mock_keyring):
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        keyringutil.delete_user_password()
        mock_keyring.delete_password.assert_not_called()

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    def test_store_user_password_not_called_outside_local(self, mock_keyring):
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        keyringutil.store_user_password("shakimaan")
        mock_keyring.set_password.assert_not_called()

    @mock.patch('aladdinsdk.common.secrets.keyringutil._keyring')
    def test_get_user_password_not_called_outside_local(self, mock_keyring):
        mock_keyring.get_keyring.return_value = "TEST_KEYRING"
        keyringutil.get_user_password()
        mock_keyring.get_password.assert_not_called()
