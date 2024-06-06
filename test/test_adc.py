from unittest import TestCase, mock
from unittest.mock import MagicMock, Mock
import os
import importlib

from test.resources.testutils import utils, extmocks
import pandas.testing as pandastesting


class TestAdcClientInit(TestCase):
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

    @mock.patch("aladdinsdk.adc.client.ADCClient._generate_adc_connection", return_value=None)
    def test_session_parameter_and_query_tag_behavior(self, generate_conn_mock):
        from aladdinsdk.adc.client import ADCClient
        # Default behavior
        test_subject = ADCClient()
        self.assertEqual(test_subject._session_parameters, {'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'})
        # Setting custom query tag
        test_subject = ADCClient(session_parameters={'QUERY_TAG': 'FOOBAR'})
        self.assertEqual(test_subject._session_parameters, {'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core,FOOBAR'})
        # Setting custom session params without query tag
        test_subject = ADCClient(session_parameters={'SAMPLE_ATTR': 'FOOBAR'})
        self.assertEqual(test_subject._session_parameters, {'SAMPLE_ATTR': 'FOOBAR', 'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'})
        # Setting custom session params without query tag
        from aladdinsdk.common.metrics import update_domain_sdk_metrics_suffix
        update_domain_sdk_metrics_suffix("TEST")
        # Setting custom session params without query tag but updated domain sdk query tag
        test_subject = ADCClient(session_parameters={'SAMPLE_ATTR': 'FOOBAR'})
        self.assertEqual(test_subject._session_parameters, {'SAMPLE_ATTR': 'FOOBAR', 'QUERY_TAG': 'QueryViaSDK-AladdinSDK-TEST'})

    def test_query_tag_behavior(self):
        # test for invalid domain prefix
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException
        with self.assertRaises(AsdkAdcException) as context:
            from aladdinsdk.adc.client import update_domain_sdk_query_tag_suffix
            test_suffix = "#&I^"
            update_domain_sdk_query_tag_suffix(test_suffix)
            self.assertIn(context, 'QUERY_TAG suffix should be alphanumeric string of max length 15.')

    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_with_config_values(self, requests_mock, api_patch, sfc_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient()

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        sfc_mock.assert_called_with(
            account='mi6-uke2sf.privatelink',
            authenticator='oauth',
            user='jbond',
            token='goldeneyegoldkey',
            role='SPY',
            warehouse='SPECTRE',
            database='MI_6_EMPS',
            schema='AGENTS',
            session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'}
            )
        sfc_mock.assert_called_once()

        self.assertIsNotNone(test_subject.get_connection())

    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_with_config_values_no_proxy_preset(self, requests_mock, api_patch, sfc_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector

        with mock.patch.dict('os.environ'):
            import aladdinsdk.adc.client
            importlib.reload(aladdinsdk.adc.client)
            from aladdinsdk.adc.client import ADCClient

            test_subject = ADCClient()

            api_patch.assert_called_with(
                'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
                encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
                auth_type='Basic Auth', username='jbond'
            )
            api_patch.assert_called_once()
            sfc_mock.assert_called_with(
                account='mi6-uke2sf.privatelink',
                authenticator='oauth',
                user='jbond',
                token='goldeneyegoldkey',
                role='SPY',
                warehouse='SPECTRE',
                database='MI_6_EMPS',
                schema='AGENTS',
                session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'}
                )
            sfc_mock.assert_called_once()

            self.assertIsNotNone(test_subject.get_connection())

    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_with_partial_config_values(self, requests_mock, api_patch, sfc_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_2 = MagicMock()
        token_response_body_2.access_token = "goldeneyegoldkey_2"
        mock_api_client_2 = MagicMock()
        mock_api_client_2.call_api = Mock(return_value=token_response_body_2)
        api_patch.return_value = mock_api_client_2

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(username='M', password="chief")

        api_patch.assert_called_with(
            'TokenAPI', username='M', password='chief', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth'
        )
        api_patch.assert_called_once()
        sfc_mock.assert_called_with(
            account='mi6-uke2sf.privatelink',
            authenticator='oauth',
            user='M',
            token='goldeneyegoldkey_2',
            role='SPY',
            warehouse='SPECTRE',
            database='MI_6_EMPS',
            schema='AGENTS',
            session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'})
        sfc_mock.assert_called_once()

        self.assertIsNotNone(test_subject.get_connection())

    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_failed_to_get_valid_access_token(self, requests_mock, api_patch):
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException
        # Create a mock to return for Token AladdinAPI
        token_response_body = MagicMock()
        delattr(token_response_body, 'access_token')  # API response missing access token
        mock_api_client = MagicMock()
        mock_api_client.call_api = Mock(return_value=token_response_body)
        api_patch.return_value = mock_api_client

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        with self.assertRaises(AsdkAdcException) as context:
            ADCClient()
            self.assertTrue('Unable to generate ADC connection due to missing refresh_token in TokenAPI response' in context.exception)

    @mock.patch('aladdinsdk.adc.client.ADCClient')
    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_with_partial_config_values_and_post_connect_updates(self, requests_mock, api_patch, sfc_mock, adc_conn_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body = MagicMock()
        token_response_body.access_token = "goldeneyegoldkey"
        mock_api_client = MagicMock()
        mock_api_client.call_api = Mock(return_value=token_response_body)
        api_patch.return_value = mock_api_client

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector
        adc_conn_mock.return_value = mock_snowflake_connector

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient()
        mock_cursor = test_subject.get_connection().cursor.return_value

        test_subject.use_warehouse("SIS")
        mock_cursor.execute.assert_called_with("USE WAREHOUSE SIS")

        test_subject.use_role("DIRECTOR")
        mock_cursor.execute.assert_called_with("USE ROLE DIRECTOR")

        test_subject.use_database("EQUIPMENT")
        mock_cursor.execute.assert_called_with("USE DATABASE EQUIPMENT")

        test_subject.use_schema("GADGETS")
        mock_cursor.execute.assert_called_with("USE SCHEMA GADGETS")

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('snowflake.connector.connect')
    @mock.patch('pandas.read_sql')
    def test_adc_query_sql_success(self, pandas_read_sql_mock, sfc_mock, api_patch, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)

        api_patch.return_value = mock_api_client_1

        sfc_mock.return_value = mock_snowflake_connector

        import pandas as pd
        mock_df = pd.DataFrame({'A': []})
        pandas_read_sql_mock.return_value = mock_df

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient()

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        sfc_mock.assert_called_with(
            account='mi6-uke2sf.privatelink',
            authenticator='oauth',
            user='jbond',
            token='goldeneyegoldkey',
            role='SPY',
            warehouse='SPECTRE',
            database='MI_6_EMPS',
            schema='AGENTS',
            session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'})
        sfc_mock.assert_called_once()

        self.assertIsNotNone(test_subject.get_connection())

        df = test_subject.query_sql('SELECT * FROM MISSIONDB.IMPOSSIBLE.CROSSOVER')
        pandastesting.assert_frame_equal(df, mock_df)

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('snowflake.connector.connect')
    @mock.patch('snowflake.connector.pandas_tools.write_pandas')
    def test_adc_write_frame_success(self, sfc_write_pandas_mock, sfc_mock, api_patch, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)

        api_patch.return_value = mock_api_client_1

        sfc_mock.return_value = mock_snowflake_connector
        import pandas as pd
        mock_df = pd.DataFrame()
        sfc_write_pandas_mock.return_value = True, 1, 3, mock_df

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient()

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        sfc_mock.assert_called_with(
            account='mi6-uke2sf.privatelink',
            authenticator='oauth',
            user='jbond',
            token='goldeneyegoldkey',
            role='SPY',
            warehouse='SPECTRE',
            database='MI_6_EMPS',
            schema='AGENTS',
            session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'})
        sfc_mock.assert_called_once()

        mock_sf_conn = test_subject.get_connection()
        self.assertIsNotNone(mock_sf_conn)

        is_success, chunks_count, ingested_row_count = test_subject.write_frame(mock_df, "SAMPLE_TABLE_NAME")
        sfc_write_pandas_mock.assert_called_once_with(conn=mock_sf_conn,
                                                      df=mock_df,
                                                      table_name="SAMPLE_TABLE_NAME",
                                                      database=None,
                                                      schema=None,
                                                      chunk_size=None,
                                                      compression="gzip",
                                                      on_error="abort_statement",
                                                      parallel=4,
                                                      quote_identifiers=True,
                                                      auto_create_table=False,
                                                      overwrite=False,
                                                      table_type="")
        self.assertEqual(ingested_row_count, 3)


class TestAdcClientWithBasicAuthArgsAndKwargsInit(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_partial_adc_config.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_using_basic_auth_with_kwargs(self, requests_mock, api_patch, sfc_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(username="test_user", password="test_password", auth_type="Basic Auth")

        api_patch.assert_called_with(
            'TokenAPI', password='test_password', api_key='hippopotomonstrosesquippedaliophobia', auth_type='Basic Auth', username='test_user'
        )
        api_patch.assert_called_once()
        sfc_mock.assert_called_with(
            account='mi6-uke2sf.privatelink',
            authenticator='oauth',
            user='test_user',
            token='goldeneyegoldkey',
            role='SPY',
            warehouse='SPECTRE',
            database='MI_6_EMPS',
            schema='AGENTS',
            session_parameters={'QUERY_TAG': 'QueryViaSDK-AladdinSDK-Core'}
            )
        sfc_mock.assert_called_once()

        self.assertIsNotNone(test_subject.get_connection())


class TestAdcClientWithOAuthArgsAndKwargsInit(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "ASDK_USER_CONFIG_FILE": "test/resources/testdata/sample_user_settings_incomplete.yaml",
            "ASDK_DEFAULTWEBSERVER": "http://dummy.dws.com"
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.connector.connect')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_adc_initialization_using_oauth_with_kwargs(self, api_patch, sfc_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        # Mock snowflake connection
        mock_snowflake_connection = MagicMock()
        mock_snowflake_connection.connector = "mock_connector"
        mock_snowflake_connector = MagicMock()
        mock_snowflake_connector.connect = Mock(return_value=mock_snowflake_connection)
        sfc_mock.return_value = mock_snowflake_connector

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(username="test_user", client_id="id", client_secret="secret", auth_type="OAuth", auth_flow_type="client_credentials")

        api_patch.assert_called_with(
            'TokenAPI', username='test_user', api_key='hippopotomonstrosesquippedaliophobia', client_id="id", client_secret="secret",
            auth_type="OAuth", auth_flow_type="client_credentials"
        )
        api_patch.assert_called_once()
        self.assertIsNotNone(test_subject.get_connection())


class TestAdcClientSnowparkConnectivity(TestCase):
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

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_get_adc_connection_for_snowpark(self, api_patch, sf_session_mock, sf_session_builder_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False
        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        self.assertIsNotNone(test_subject.get_connection())

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    def test_get_adc_connection_error_for_non_conntype(self, requests_mock):
        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient
        from aladdinsdk.common.error.asdkerrors import AsdkAdcException

        with self.assertRaises(AsdkAdcException) as context:
            ADCClient(connection_type="INCORRECT_TYPE")
            self.assertTrue('Invalid connection type. ADCClient currently supports the following connection types' in context.exception)

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    def test_adc_snowpark_query_sql_success(self, sf_session_mock, sf_session_builder_mock, api_patch, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        from snowflake.snowpark import Session
        test_local_session = Session.builder.config('local_testing', True).create()
        mock_df = test_local_session.create_dataframe([(1, "one"), (2, "two")], schema=["col_a", "col_b"])

        # Mock snowflake snowpark connection
        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False

        mock_snowpark_session.sql = MagicMock()
        mock_snowpark_session.sql.return_value = mock_df

        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient
        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()

        self.assertIsNotNone(test_subject.get_connection())

        df = test_subject.query_sql('SELECT * FROM MISSIONDB.IMPOSSIBLE.CROSSOVER')
        self.assertIsNotNone(df)

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('snowflake.snowpark.session.Session.write_pandas')
    def test_adc_snowpark_write_frame_success(self, write_pandas_mock, sf_session_mock, sf_session_builder_mock, api_patch, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        # Mock snowflake snowpark connection
        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False

        sf_session_mock.return_value = mock_snowpark_session

        from snowflake.snowpark import Session
        test_local_session = Session.builder.config('local_testing', True).create()
        from snowflake.snowpark.table import Table
        mock_tbl = Table(table_name="SAMPLE_TABLE_NAME", session=test_local_session)
        write_pandas_mock.return_value = mock_tbl

        import pandas as pd
        mock_df = pd.DataFrame()

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()

        returned_tbl = test_subject.write_frame(mock_df, "SAMPLE_TABLE_NAME")
        self.assertIsNotNone(returned_tbl)

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_close_connection_snowflake_snowpark(self, api_patch, sf_session_mock, sf_session_builder_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False
        mock_snowpark_session.close.return_value = None
        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        self.assertIsNotNone(test_subject.get_connection())
        self.assertIsNone(test_subject.close_connection())

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_close_non_existent_connection_snowflake_snowpark(self, api_patch, sf_session_mock, sf_session_builder_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = True
        mock_snowpark_session.close.return_value = None
        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        self.assertIsNotNone(test_subject.get_connection())
        self.assertFalse(test_subject.close_connection())

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_reconnect_snowflake_snowpark(self, api_patch, sf_session_mock, sf_session_builder_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body_1 = MagicMock()
        token_response_body_1.access_token = "goldeneyegoldkey"
        mock_api_client_1 = MagicMock()
        mock_api_client_1.call_api = Mock(return_value=token_response_body_1)
        api_patch.return_value = mock_api_client_1

        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False
        mock_snowpark_session.close.return_value = None
        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")

        api_patch.assert_called_with(
            'TokenAPI', password='am_db9', password_filepath='test/resources/testdata/sample_encrypted_password.txt',
            encryption_filepath='test/resources/testdata/sample_encryption_key.txt', api_key='hippopotomonstrosesquippedaliophobia',
            auth_type='Basic Auth', username='jbond'
        )
        api_patch.assert_called_once()
        self.assertIsNotNone(test_subject.get_connection())
        test_subject.reconnect()
        self.assertIsNotNone(test_subject.get_connection())

    @mock.patch('requests.get', side_effect=extmocks.mocked_successful_requests_get)
    @mock.patch('snowflake.snowpark.Session.builder.configs')
    @mock.patch('snowflake.snowpark.Session.SessionBuilder.create')
    @mock.patch('aladdinsdk.common.authentication.adc.AladdinAPI')
    def test_get_adc_connection_snowpark_with_partial_config_values_and_post_connect_updates(self, mock_auth_adc_api, sf_session_mock,
                                                                                             sf_session_builder_mock, requests_mock):
        # Create a mock to return for Token AladdinAPI
        token_response_body = MagicMock()
        token_response_body.access_token = "goldeneyegoldkey"
        mock_api_client = MagicMock()
        mock_api_client.call_api = Mock(return_value=token_response_body)
        mock_auth_adc_api.return_value = mock_api_client

        # Mock snowflake snowpark connection
        mock_snowpark_session = MagicMock()
        mock_snowpark_session.configure_mock(_conn=MagicMock())
        mock_snowpark_session._conn.is_closed.return_value = False
        sf_session_mock.return_value = mock_snowpark_session

        import aladdinsdk.adc.client
        importlib.reload(aladdinsdk.adc.client)
        from aladdinsdk.adc.client import ADCClient

        test_subject = ADCClient(connection_type="snowflake-snowpark-python")
        mock_cursor = test_subject._connection._conn._cursor

        test_subject.use_warehouse("SIS")
        mock_cursor.execute.assert_called_with("USE WAREHOUSE SIS")

        test_subject.use_role("DIRECTOR")
        mock_cursor.execute.assert_called_with("USE ROLE DIRECTOR")

        test_subject.use_database("EQUIPMENT")
        mock_cursor.execute.assert_called_with("USE DATABASE EQUIPMENT")

        test_subject.use_schema("GADGETS")
        mock_cursor.execute.assert_called_with("USE SCHEMA GADGETS")
