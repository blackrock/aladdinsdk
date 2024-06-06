"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import re
import snowflake.connector
from snowflake.snowpark import Session
from snowflake.connector.pandas_tools import write_pandas
from typing import Literal
from aladdinsdk.common.authentication.adc import AdcAuthUtil
from aladdinsdk.common.error.asdkerrors import AsdkAdcException
from aladdinsdk.common.error.handler import asdk_exception_handler
from aladdinsdk.config import user_settings
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload
from aladdinsdk.common.retry.adc_retry import adc_retry
import pandas as pd
import logging

_logger = logging.getLogger(__name__)

_ASDK_QUERY_TAG_PATTERN = 'QueryViaSDK-AladdinSDK-{}'
_DEFAULT_SDK_QUERY_TAG_SUFFIX = 'Core'


def update_domain_sdk_query_tag_suffix(domain_sdk_suffix):
    """
    Helper method to append domain specific query tag suffix
    """
    global _DEFAULT_SDK_QUERY_TAG_SUFFIX
    regex = r"^[a-zA-Z0-9\.\/]+$"
    if re.match(regex, domain_sdk_suffix) is not None and len(domain_sdk_suffix) > 0 and len(domain_sdk_suffix) <= 15:
        _DEFAULT_SDK_QUERY_TAG_SUFFIX = domain_sdk_suffix
        _logger.debug(f"Updating SDK query tag to {_ASDK_QUERY_TAG_PATTERN.format(_DEFAULT_SDK_QUERY_TAG_SUFFIX)}")
    else:
        raise AsdkAdcException("QUERY_TAG suffix should be alphanumeric string of max length 15.")


class ADCClient():
    """
    ADC Client class for maintaining Aladdin Data Cloud connections.
    This client interface lets users connect to BlackRock's Aladdin Data Cloud using
    Snowflake or Snowpark connectors
    """

    @asdk_exception_handler
    @dynamic_asdk_config_reload
    def __init__(self,
                 account: str = user_settings.get_adc_conn_account(),
                 role: str = user_settings.get_adc_conn_role(),
                 warehouse: str = user_settings.get_adc_conn_warehouse(),
                 database: str = user_settings.get_adc_conn_database(),
                 schema: str = user_settings.get_adc_conn_schema(),
                 session_parameters: dict = None,
                 connection_type: str = None,
                 **kwargs):
        """
        Instantiate an ADC client instance.
        User may pass in optional parameters to override default or configured values.

        Priority order:
        - Value passed in API Client instantiation
        - Value set as environment variable
        - Value set in user settings file

        Args:
            account: ADC (Snowflake) account link
            role (string, optional): Snowflake user role to be used. Defaults to value set as
                "ASDK_ADC__CONN__ROLE", or "adc.conn.role" in settings yaml, None if not configured.
            warehouse (string, optional): Snowflake virtual warehouse to be used. Defaults to value
            set as "ASDK_ADC__CONN__WAREHOUSE", or "adc.conn.warehouse" in settings yaml,
                None if not configured.
            database (string, optional): Snowflake database to be used. Defaults to value set as
                "ASDK_ADC__CONN__DATABASE", or "adc.conn.database" in settings yaml, None if not configured.
            schema (string, optional): Snowflake schema to be used. Defaults to value set as
                "ASDK_ADC__CONN__SCHEMA", or "adc.conn.schema" in settings yaml, None if not configured.
            session_parameters (dict, optional): Session parameters to be used for snowflake connection.
            adc_conn_authenticator (string, optional): Authenticator type for snowflake connection.
                Should be one of ["snowflake_jwt", "oauth"]. Defaults to "oauth".
            adc_conn_rsa_private_key_passphrase (string, optional): Passphrase for RSA key authentication used for snowflake_jwt
                connection authentication. To be provided as private key filepath and passphrase combination (instead of private key).
                For empty passphrase provide empty string, not None.
                Defaults to None.
            adc_conn_rsa_private_key_filepath (string, optional): Filepath to RSA private key file used for snowflake_jwt
                connection authentication. To be provided as private key filepath and passphrase combination (instead of private key).
                Defaults to None.
            adc_conn_rsa_private_key (string, optional): RSA private key to be used for snowflake_jwt
                connection authentication. To be provided instead of private key filepath and passphrase combination.
                Defaults to None.
            api_key (string, optional): API Key. Defaults to value set as "ASDK_API__TOKEN" environment
                variable, or "api.token" in settings yaml, None if not configured.
            auth_type (_type_, optional): API Authentication Type. Must be in ["Basic Auth", "OAuth"].
                Defaults to value set as "ASDK_API__AUTH_TYPE" or "api.auth_type" in settings yaml.
            auth_flow_type (_type_, optional): : API Authentication Type. Must be in
                ["refresh_token", "client_credentials"]. Defaults to value set as
                "ASDK_API__AUTH_FLOW_TYPE" or "api.auth_flow_type" in settings yaml.
            username (string, optional): Username. Defaults to value set as "ASDK_USER_CREDENTIALS__USERNAME"
                environment variable, or "user_credentials.username" in settings yaml, None if not configured.
            password (string, optional): Password. Defaults to value set as "ASDK_USER_CREDENTIALS__PASSWORD"
                environment variable, or "user_credentials.password" in settings yaml, None if not configured.
            client_id (string, optional): Client ID for Application to be used by oauth flow.
                Defaults to None.
            client_secret (string, optional): Client Secret for Application to be used by oauth flow.
                Defaults to None.
            refresh_token (string, optional): Refresh Token for Application to be used by oauth flow.
                Defaults to None.
            adc_oauth_access_token (string, optional): ADC Oauth Access Token. Defaults to None.
            auth_server_proxy (string, optional): API Auth Server Proxy for Oauth. Defaults to value set as
                "ASDK_OAUTH__AUTH_SERVER_PROXY" environment variable, or "oauth.auth_server_proxy" in
                settings yaml, None if not configured.
            auth_server_url (string, optional): API Auth Server URL for Oauth. Defaults to value set as
                "ASDK_OAUTH__AUTH_SERVER_URL" environment variable, or "oauth.auth_server_url" in settings
                yaml, None if not configured.
            password_filepath (string, optional): Password filepath (Basic Auth). Defaults to value set as
                "ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH" environment variable, or
                "user_credentials.password_filepath" in settings yaml, None if not configured.
            encrypted_password_filepath (string, optional): Encrypted Password filepath (Basic Auth).
                Defaults to value set as "ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH"
                environment variable, or "user_credentials.encrypted_password_filepath" in settings yaml,
                None if not configured.
            encryption_filepath (string, optional): Encryption filepath. Defaults to value set as
                "ASDK_USER_CREDENTIALS__ENCRYPTED_FILEPATH" environment variable, or
                "user_credentials.encryption_filepath" in settings yaml, None if not configured.
        """
        self._adc_auth_util = AdcAuthUtil(**kwargs)

        self._connection_type = connection_type if connection_type is not None else \
            user_settings.get_adc_connection_type()
        if self._connection_type not in [user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON,
                                         user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON]:
            error_msg = f"Invalid connection type. ADCClient currently supports the following connection types: \
                {[user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON, user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON]}"
            _logger.error(error_msg)
            raise AsdkAdcException(error_msg)

        self._account = account
        self._role = role
        self._warehouse = warehouse
        self._database = database
        self._schema = schema

        self._session_parameters = {}
        if session_parameters is not None:
            # user provided session parameters
            self._session_parameters = session_parameters
        self._add_sdk_query_tag()

        self._connection = self._generate_adc_connection()

    def _add_sdk_query_tag(self):
        """
        Helper to add SDK query tag to session parameters.
        If user provided session parameters contain a query tag, append the SDK query tag to it.
        """
        _sdk_query_tag = _ASDK_QUERY_TAG_PATTERN.format(_DEFAULT_SDK_QUERY_TAG_SUFFIX)
        if self._session_parameters.get('QUERY_TAG') is not None:
            # user has also provided some query tag values, append it to sdk query tag
            query_tag = ','.join([_sdk_query_tag, self._session_parameters.get('QUERY_TAG')])
            self._session_parameters['QUERY_TAG'] = query_tag
        else:
            # user has not provided any query tag values, use default sdk query tag
            self._session_parameters['QUERY_TAG'] = _sdk_query_tag

    @asdk_exception_handler
    @adc_retry
    @dynamic_asdk_config_reload
    def query_sql(self, sql: str,
                  index_col: list[str] = None,
                  coerce_float: bool = True,
                  params=None,
                  parse_dates=None,
                  columns: list[str] = None,
                  chunksize: int = None):
        """
        Read SQL query or database table into a DataFrame

        Args:
            sql (str): SQL query to be executed or a table name.
            index_col (list[str], optional): Column(s) to set as index(MultiIndex). Defaults to None.
            coerce_float (bool, optional): Attempts to convert values of non-string, non-numeric objects (like
                    decimal.Decimal) to floating point, useful for SQL result sets. Defaults to True.
                    For snowflake connector python only.
            params (_type_, optional): List of parameters to pass to execute method.  The syntax used
                    to pass parameters is database driver dependent. Check your
                    database driver documentation for which of the five syntax styles,
                    described in PEP 249's paramstyle, is supported.
                    Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}. Defaults to None.
                    For snowflake connector python only.
            parse_dates (_type_, optional): - List of column names to parse as dates.
                    - Dict of ``{column_name: format string}`` where format string is
                    strftime compatible in case of parsing string times, or is one of
                    (D, s, ns, ms, us) in case of parsing integer timestamps.
                    - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
                    to the keyword arguments of :func:`pandas.to_datetime`
                    Especially useful with databases without native Datetime support,
                    such as SQLite. Defaults to None.
                    For snowflake connector python only.
            columns (list[str], optional): List of column names to select from SQL table
                    (only used when reading a table). Defaults to None.
                    For snowflake connector python only.
            chunksize (int, optional): If specified, return an iterator where `chunksize` is the
                    number of rows to include in each chunk. Defaults to None.
                    For snowflake connector python only.

        Returns:
            DataFrame or Iterator[DataFrame]: Result of query in pandas dataframe
        """
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON:
            conn = self.get_connection()
            read_resp_df = conn.sql(sql).toPandas()
            return read_resp_df
        elif self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON:
            conn = self.get_connection()
            read_resp_df = pd.read_sql(sql=sql,
                                       con=conn,
                                       index_col=index_col,
                                       coerce_float=coerce_float,
                                       params=params,
                                       parse_dates=parse_dates,
                                       columns=columns,
                                       chunksize=chunksize)
            return read_resp_df

    @asdk_exception_handler
    @adc_retry
    @dynamic_asdk_config_reload
    def write_frame(self, df: pd.DataFrame,
                    table_name: str,
                    database: str = None,
                    schema: str = None,
                    chunk_size: int = None,
                    compression: str = "gzip",
                    on_error: str = "abort_statement",
                    parallel: int = 4,
                    quote_identifiers: bool = True,
                    auto_create_table: bool = False,
                    overwrite: bool = False,
                    table_type: Literal["", "temp", "temporary", "transient"] = ""):
        """
        Write dataframe into given table

        Args:
            df (pd.DataFrame): Dataframe we'd like to write back.
            table_name (str): Table name where we want to insert into.
            database (str, optional): Database schema and table is in, if not provided the default one will be used (Default value = None).
            schema (str, optional):  Schema table is in, if not provided the default one will be used (Default value = None).
            chunk_size (int, optional): Number of elements to be inserted once, if not provided all elements will be dumped once
                                        (Default value = None).
            compression (str, optional): The compression used on the Parquet files, can only be gzip, or snappy. Gzip gives supposedly a
                                        better compression, while snappy is faster. Use whichever is more appropriate (Default value = 'gzip').
            on_error (str, optional): Action to take when COPY INTO statements fail, default follows documentation at:
                                        https://docs.snowflake.com/en/sql-reference/sql/copy-into-table.html#copy-options-copyoptions
                                        (Default value = 'abort_statement').
            parallel (int, optional): Number of threads to be used when uploading chunks, default follows documentation at:
                                        https://docs.snowflake.com/en/sql-reference/sql/put.html#optional-parameters (Default value = 4).
            quote_identifiers (bool, optional): By default, identifiers, specifically database, schema, table and column names
                                        (from df.columns) will be quoted. If set to False, identifiers are passed on to Snowflake without quoting.
                                        I.e. identifiers will be coerced to uppercase by Snowflake.  (Default value = True)
            auto_create_table (bool, optional): When true, will automatically create a table with corresponding columns for each column in
                                        the passed in DataFrame. The table will not be created if it already exists
            overwrite (bool, optional): When true, and if auto_create_table is true, then it drops the table. Otherwise, it
                                        truncates the table. In both cases it will replace the existing contents of the table with that of the passed
                                        in Pandas DataFrame.
            table_type (Literal["", "temp", "temporary", "transient"], optional): The table type of to-be-created table. The supported table types
                                        include ``temp``/``temporary``
                                        and ``transient``. Empty means permanent table as per SQL convention.

        Returns:
            For snowflake connector python:
                Returns the COPY INTO command's results to verify ingestion in the form of a tuple of whether all chunks were
                ingested correctly, # of chunks, # of ingested rows
            For snowflake snowpark python:
                Returns a Snowpark :class:`DataFrame` object referring to the table where the
                pandas DataFrame was written to.
        """
        write_pandas_params = {
            'df': df,
            'table_name': table_name,
            'database': database,
            'schema': schema,
            'chunk_size': chunk_size,
            'compression': compression,
            'on_error': on_error,
            'parallel': parallel,
            'quote_identifiers': quote_identifiers,
            'auto_create_table': auto_create_table,
            'overwrite': overwrite,
            'table_type': table_type
        }

        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON:
            conn = self.get_connection()
            tbl = conn.write_pandas(**write_pandas_params)
            return tbl
        elif self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON:
            conn = self.get_connection()
            write_pandas_params['conn'] = conn
            is_success, chunks_count, ingested_row_count, _ = write_pandas(**write_pandas_params)
            return is_success, chunks_count, ingested_row_count

    @asdk_exception_handler
    def get_connection(self):
        """
        Get Snowflake or Snowpark connection object. If the connection is not active, create a new connection

        Returns:
            snowflake connector: A Snowflake or Snowpark connection object
        """
        if self._is_connection_active():
            return self._connection
        else:
            self._connection = self._generate_adc_connection()
            return self._connection

    @asdk_exception_handler
    def close_connection(self):
        """
        Close Snowflake or Snowpark connection object

        Returns:
            bool: True if connection is closed successfully
        """
        if self._is_connection_active():
            return self._connection.close()
        else:
            _logger.warning('Attempted to close a connection that did not exist, or was not active')
            return False

    @asdk_exception_handler
    def reconnect(self):
        """
        Reconnect to ADC using connection object
        """
        if self._is_connection_active():
            self._connection.close()
        self._connection = self._generate_adc_connection()

    @asdk_exception_handler
    def use_warehouse(self, warehouse: str):
        """
        Switch to a different warehouse

        Args:
            warehouse (string): Snowflake warehouse to use for this session
        """
        if warehouse is not None:
            self._execute_with_cursor(f"USE WAREHOUSE {warehouse}")
            self._warehouse = warehouse

    @asdk_exception_handler
    def use_role(self, role: str):
        """
        Switch to a different role

        Args:
            role (str): Snowflake role to use for this session
        """
        if role is not None:
            self._execute_with_cursor(f"USE ROLE {role}")
            self._role = role

    @asdk_exception_handler
    def use_database(self, database: str):
        """
        Switch to a different ADC database

        Args:
            database (str): Snowflake database to use for this session
        """
        if database is not None:
            self._execute_with_cursor(f"USE DATABASE {database}")
            self._database = database

    @asdk_exception_handler
    def use_schema(self, schema: str):
        """
        Switch to a different ADC schema

        Args:
            schema (str): Snowflake schema to use for this session
        """
        if schema is not None:
            self._execute_with_cursor(f"USE SCHEMA {schema}")
            self._schema = schema

    def _generate_adc_connection(self):
        """
        Generate a Snowflake or Snowpark connection object using user provided credentials and connection details.

        Returns:
            snowflake connector: A Snowflake or Snowpark connection object
        """
        sf_connection_params = self._adc_auth_util.generate_sf_connection_params(self)
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON:
            adc_conn = snowflake.connector.connect(**sf_connection_params)
        elif self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON:
            adc_conn = Session.builder.configs(sf_connection_params).create()
        return adc_conn

    def _is_connection_active(self):
        """
        Check if current ADC connection is active

        Returns:
            bool: True if connection is active
        """
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON:
            return self._connection is not None and not self._connection.is_closed()
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON:
            return self._connection is not None and not self._connection._conn.is_closed()

    def _execute_with_cursor(self, sql):
        """
        Execute SQL using Snowflake or Snowpark connection object

        Args:
            sql (str): SQL query to be executed

        Returns:
            cursor: Snowflake or Snowpark cursor object
        """
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON:
            return self.get_connection().cursor().execute(sql)
        if self._connection_type == user_settings.CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON:
            return self._connection._conn._cursor.execute(sql)
