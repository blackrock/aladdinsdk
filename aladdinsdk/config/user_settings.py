import os
from dynaconf import Validator
from aladdinsdk.config.asdkconf import AsdkConf, dynamic_asdk_config_reload
from aladdinsdk.common.blkutils import blkutils

# Path to configuration in user config file, and permitted values
_conf_key_run_mode = "run_mode"
CONF_RUN_MODE_LOCAL = "local"
CONF_RUN_MODE_ALADDIN_COMPUTE = "aladdin-compute"
_CONF_RUN_MODE_TEST = "test"

ALADDIN_COMPUTE_SECRETS_KEYENC_PATH = "/secrets/key.enc"
ALADDIN_COMPUTE_CLIENT_DETAILS_PATH = "/secrets/api-oauth-app-client-details.yaml"
ALADDIN_COMPUTE_CLIENT_REFRESH_TOKEN_PATH = "/secrets/api-oauth-app-user-refresh-token.yaml"
ALADDIN_COMPUTE_CLIENT_API_ACCESS_TOKEN_PATH = "/secrets/api-oauth-app-access-token.yaml"
## API Keys
_conf_key_api_auth_type = "api.auth_type"
CONF_API_AUTH_TYPE_BASIC_AUTH = "Basic Auth"
CONF_API_AUTH_TYPE_OAUTH = "OAuth"
_conf_key_api_auth_flow_type = "api.auth_flow_type"
CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN = "refresh_token"
CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS = "client_credentials"

## API Oauth Credential Keys
_conf_key_api_oauth_client_id = "api.oauth.client_id"
_conf_key_api_oauth_client_secret = "api.oauth.client_secret"
_conf_key_api_oauth_refresh_token = "api.oauth.refresh_token"
_conf_key_api_oauth_access_token = "api.oauth.access_token"
_conf_key_api_oauth_client_details_filepath = "api.oauth.client_details_filepath"
_conf_key_api_oauth_refresh_token_filepath = "api.oauth.refresh_token_filepath"
_conf_key_api_oauth_access_token_filepath = "api.oauth.access_token_filepath"
_conf_key_api_oauth_auth_server_proxy = "api.oauth.auth_server_proxy"
_conf_key_api_oauth_auth_server_url = "api.oauth.auth_server_url"

_conf_key_api_token = "api.token"
_conf_key_api_lro_status_check_interval = "api.lro.status_check_interval"
_conf_key_api_lro_status_check_timeout = "api.lro.status_check_timeout"

## ADC Keys
_conf_key_adc_connection_type = "adc.connection_type"
CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON = "snowflake-connector-python"
CONF_ADC_CONN_TYPE_SNOWFLAKE_SNOWPARK_PYTHON = "snowflake-snowpark-python"

_conf_key_adc_conn_account = "adc.conn.account"
_conf_key_adc_conn_role = "adc.conn.role"
_conf_key_adc_conn_warehouse = "adc.conn.warehouse"
_conf_key_adc_conn_database = "adc.conn.database"
_conf_key_adc_conn_schema = "adc.conn.schema"

## User Credential Keys
_conf_key_user_credentials_username = "user_credentials.username"
_conf_key_user_credentials_password = "user_credentials.password"
_conf_key_user_credentials_encrypted_password_filepath = "user_credentials.encrypted_password_filepath"
_conf_key_user_credentials_password_filepath = "user_credentials.password_filepath"
_conf_key_user_credentials_encryption_filepath = "user_credentials.encryption_filepath"

##Logging Keys
_conf_key_logging_keys = "log_level"
CONF_LOG_LEVEL_DEBUG = 'DEBUG'
CONF_LOG_LEVEL_INFO = 'INFO'
CONF_LOG_LEVEL_WARNING = 'WARNING'
CONF_LOG_LEVEL_ERROR = 'ERROR'
CONF_LOG_LEVEL_CRITICAL = 'CRITICAL'

## Error Handling
_conf_key_error_handler_active = "error_handler.active"
CONF_ERROR_HANDLER_ACTIVE_TRUE = True
CONF_ERROR_HANDLER_ACTIVE_FALSE = False

## API Retry Settings
_conf_API_retry_stop_after_attempt = "api.retry.stop_after_attempt"
_conf_API_retry_wait_fixed = "api.retry.wait_fixed"
_conf_API_retry_stop_after_delay = "api.retry.stop_after_delay"

## ADC Retry Settings
_conf_ADC_retry_stop_after_attempt = "adc.retry.stop_after_attempt"
_conf_ADC_retry_wait_fixed = "adc.retry.wait_fixed"
_conf_ADC_retry_stop_after_delay = "adc.retry.stop_after_delay"

## Export Data Settings
_conf_export_overwrite_data = "export.overwrite_data"

## Email Notification Settings
_conf_notifications_email_host = "notifications.email.email_host"
_conf_notifications_email_sender = "notifications.email.sender"
_conf_notifications_email_to = "notifications.email.to"
_conf_notifications_email_username = "notifications.email.email_username"
_conf_notifications_email_password = "notifications.email.email_password"

## Error Notification Settings
_conf_error_handling_email_notifications_enabled = "error_handling.email_notifications.enabled"
_conf_error_handling_email_notifications_to = "error_handling.email_notifications.to"
_conf_error_handling_email_notifications_exception_types = "error_handling.email_notifications.on_exception_types"

# User settings validations
AsdkConf.validators.register(
    Validator(_conf_key_run_mode, 
              is_in=[CONF_RUN_MODE_LOCAL, CONF_RUN_MODE_ALADDIN_COMPUTE, _CONF_RUN_MODE_TEST]),
    Validator(_conf_key_api_auth_type, 
              is_in=[CONF_API_AUTH_TYPE_BASIC_AUTH, CONF_API_AUTH_TYPE_OAUTH]),
    Validator(_conf_key_api_auth_flow_type, 
              is_in=[CONF_API_AUTH_FLOW_TYPE_REFRESH_TOKEN, CONF_API_AUTH_FLOW_TYPE_CLIENT_CREDENTIALS]),
    Validator(_conf_key_error_handler_active,
              is_in=[CONF_ERROR_HANDLER_ACTIVE_TRUE, CONF_ERROR_HANDLER_ACTIVE_FALSE]),
    Validator(_conf_API_retry_stop_after_attempt,
              is_type_of=int),
    Validator(_conf_API_retry_wait_fixed,
              is_type_of=int),
    Validator(_conf_API_retry_stop_after_delay,
              is_type_of=int),
    Validator(_conf_ADC_retry_stop_after_attempt,
              is_type_of=int),
    Validator(_conf_ADC_retry_wait_fixed,
              is_type_of=int),
    Validator(_conf_ADC_retry_stop_after_delay,
              is_type_of=int),
    )

#Log Level Config Validations
AsdkConf.validators.register(
    Validator(_conf_key_logging_keys, 
              is_in=[CONF_LOG_LEVEL_DEBUG, CONF_LOG_LEVEL_INFO, CONF_LOG_LEVEL_WARNING,CONF_LOG_LEVEL_ERROR,CONF_LOG_LEVEL_CRITICAL])
    )

AsdkConf.validators.validate_all()

# Primary getters for SDK
@dynamic_asdk_config_reload
def get_run_mode():
    return AsdkConf.get(_conf_key_run_mode, CONF_RUN_MODE_ALADDIN_COMPUTE)

## API
@dynamic_asdk_config_reload
def get_api_auth_type():
    return AsdkConf.get(_conf_key_api_auth_type, CONF_API_AUTH_TYPE_OAUTH)

@dynamic_asdk_config_reload
def get_api_auth_flow_type():
    return AsdkConf.get(_conf_key_api_auth_flow_type)

## API credentials - oauth
@dynamic_asdk_config_reload
def get_api_oauth_client_id():
    return AsdkConf.get(_conf_key_api_oauth_client_id)

@dynamic_asdk_config_reload
def get_api_oauth_client_secret():
    return AsdkConf.get(_conf_key_api_oauth_client_secret)

@dynamic_asdk_config_reload
def get_api_oauth_refresh_token():
    return AsdkConf.get(_conf_key_api_oauth_refresh_token)

@dynamic_asdk_config_reload
def get_api_oauth_access_token():
    return AsdkConf.get(_conf_key_api_oauth_access_token)

@dynamic_asdk_config_reload
def get_api_oauth_client_details_filepath():
    if AsdkConf.get(_conf_key_run_mode) == CONF_RUN_MODE_ALADDIN_COMPUTE:
        return AsdkConf.get(_conf_key_api_oauth_client_details_filepath, ALADDIN_COMPUTE_CLIENT_DETAILS_PATH)
    else:
        return AsdkConf.get(_conf_key_api_oauth_client_details_filepath)

@dynamic_asdk_config_reload
def get_api_oauth_refresh_token_filepath():
    if AsdkConf.get(_conf_key_run_mode) == CONF_RUN_MODE_ALADDIN_COMPUTE:
        return AsdkConf.get(_conf_key_api_oauth_refresh_token_filepath, ALADDIN_COMPUTE_CLIENT_REFRESH_TOKEN_PATH) 
    else: 
        return AsdkConf.get(_conf_key_api_oauth_refresh_token_filepath)

@dynamic_asdk_config_reload
def get_api_oauth_access_token_filepath():
    if AsdkConf.get(_conf_key_run_mode) == CONF_RUN_MODE_ALADDIN_COMPUTE:
        return AsdkConf.get(_conf_key_api_oauth_access_token_filepath, ALADDIN_COMPUTE_CLIENT_API_ACCESS_TOKEN_PATH) 
    else:
        return AsdkConf.get(_conf_key_api_oauth_access_token_filepath)

@dynamic_asdk_config_reload
def get_api_oauth_auth_server_proxy():
    return AsdkConf.get(_conf_key_api_oauth_auth_server_proxy)

@dynamic_asdk_config_reload
def get_api_oauth_auth_server_url():
    return AsdkConf.get(_conf_key_api_oauth_auth_server_url)

@dynamic_asdk_config_reload
def get_api_token():
    return AsdkConf.get(_conf_key_api_token)

@dynamic_asdk_config_reload
def get_api_lro_status_check_interval():
    return AsdkConf.get(_conf_key_api_lro_status_check_interval, 10)

@dynamic_asdk_config_reload
def get_api_lro_status_check_timeout():
    return AsdkConf.get(_conf_key_api_lro_status_check_timeout, 300)

## ADC
@dynamic_asdk_config_reload
def get_adc_connection_type():
    return AsdkConf.get(_conf_key_adc_connection_type, CONF_ADC_CONN_TYPE_SNOWFLAKE_CONNECTOR_PYTHON)

@dynamic_asdk_config_reload
def get_adc_conn_account():
    return AsdkConf.get(_conf_key_adc_conn_account, blkutils.get_adc_account_private_link())

@dynamic_asdk_config_reload
def get_adc_conn_role():
    return AsdkConf.get(_conf_key_adc_conn_role)

@dynamic_asdk_config_reload
def get_adc_conn_warehouse():
    return AsdkConf.get(_conf_key_adc_conn_warehouse)

@dynamic_asdk_config_reload
def get_adc_conn_database():
    return AsdkConf.get(_conf_key_adc_conn_database)

@dynamic_asdk_config_reload
def get_adc_conn_schema():
    return AsdkConf.get(_conf_key_adc_conn_schema)

## User credentials
@dynamic_asdk_config_reload
def get_username():
    return AsdkConf.get(_conf_key_user_credentials_username)

@dynamic_asdk_config_reload
def get_encryption_filepath():
    return AsdkConf.get(_conf_key_user_credentials_encryption_filepath)

@dynamic_asdk_config_reload
def get_password_filepath():
    if AsdkConf.get(_conf_key_run_mode) == CONF_RUN_MODE_ALADDIN_COMPUTE and os.path.exists(ALADDIN_COMPUTE_SECRETS_KEYENC_PATH):
        return AsdkConf.get(_conf_key_user_credentials_password_filepath, ALADDIN_COMPUTE_SECRETS_KEYENC_PATH) 
    else:
        return AsdkConf.get(_conf_key_user_credentials_password_filepath)

@dynamic_asdk_config_reload
def get_encrypted_password_filepath():
    return AsdkConf.get(_conf_key_user_credentials_encrypted_password_filepath)

@dynamic_asdk_config_reload
def get_user_password():
    return AsdkConf.get(_conf_key_user_credentials_password)

## SDK Functionality
@dynamic_asdk_config_reload
def get_error_handler_active():
    return AsdkConf.get(_conf_key_error_handler_active, CONF_ERROR_HANDLER_ACTIVE_TRUE)

## Retry configurations
@dynamic_asdk_config_reload
def get_api_retry_stop_after_attempt():
    return AsdkConf.get(_conf_API_retry_stop_after_attempt)

@dynamic_asdk_config_reload
def get_api_retry_wait_fixed():
    return AsdkConf.get(_conf_API_retry_wait_fixed)

@dynamic_asdk_config_reload
def get_api_retry_stop_after_delay():
    return AsdkConf.get(_conf_API_retry_stop_after_delay)

@dynamic_asdk_config_reload
def get_adc_retry_stop_after_attempt():
    return AsdkConf.get(_conf_ADC_retry_stop_after_attempt)

@dynamic_asdk_config_reload
def get_adc_retry_wait_fixed():
    return AsdkConf.get(_conf_ADC_retry_wait_fixed)

@dynamic_asdk_config_reload
def get_adc_retry_stop_after_delay():
    return AsdkConf.get(_conf_ADC_retry_stop_after_delay)

@dynamic_asdk_config_reload
def get_overwrite_data_flag():
    return AsdkConf.get(_conf_export_overwrite_data)

@dynamic_asdk_config_reload
def get_notifications_email_host():
    return AsdkConf.get(_conf_notifications_email_host)

@dynamic_asdk_config_reload
def get_notifications_email_sender():
    return AsdkConf.get(_conf_notifications_email_sender)

@dynamic_asdk_config_reload
def get_notifications_email_to():
    return AsdkConf.get(_conf_notifications_email_to)

@dynamic_asdk_config_reload
def get_notifications_email_username():
    return AsdkConf.get(_conf_notifications_email_username)

@dynamic_asdk_config_reload
def get_notifications_email_password():
    return AsdkConf.get(_conf_notifications_email_password)

@dynamic_asdk_config_reload
def get_error_handling_email_notifications_enabled():
    return AsdkConf.get(_conf_error_handling_email_notifications_enabled, False)

@dynamic_asdk_config_reload
def get_error_handling_email_notifications_to():
    return AsdkConf.get(_conf_error_handling_email_notifications_to)

@dynamic_asdk_config_reload
def get_error_handling_email_notifications_exception_types():
    return AsdkConf.get(_conf_error_handling_email_notifications_exception_types)

## get log_level
def get_log_level():
    return AsdkConf.get(_conf_key_logging_keys, CONF_LOG_LEVEL_INFO)
