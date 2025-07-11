# AladdinSDK

AladdinSDK allows developers to easily integrate BlackRock's Aladdin functionality into their own applications and systems. The goal is to make it easier for everyone to efficiently access and utilize Aladdin APIs and Data Cloud.

## Table of Contents

- [Installation](#installation)
- [Usage/Configurations](#usageconfigurations)
- [AladdinAPI](#aladdinapi)
- [ADC Client](#adc-client)
- [Common Utilities](#common-utilities)
- [DomainSDK Development](#domainsdk-development)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Contact](#contact)

## Installation

- Use new/existing python version 3.9 virtual environment
- Install core AladdinSDK package using pip
  ```sh
  pip install aladdinsdk
  ```    
  - Optionally, SDK's API capabilities can be extended by installing additional plugin packages. Refer [AladdinSDK Plugins section](#AladdinAPI-Plugins) for details.
    </br>
    Example:

      ```sh
      pip install asdk_plugin_trading
      pip install asdk_plugin_investment_research
      ```
  - For local development, installing `keyring` is recommended for easier credential management:

      ```sh
      pip install keyring
      ```

## Usage/Configurations

| Environment Variable Name | Description                                                              | Mandatory | Default | Permitted Values |
|:--------------------------|:-------------------------------------------------------------------------|:---------:|:-------:|:----------------:|
| defaultWebServer          | BlackRock client environment's default web server                        |    Yes    |    -    |         -        |
| ASDK_USER_CONFIG_FILE     | Path to AladdinSDK configuration to be used. </br>Refer [run-time configurations section](#run-time-configurations) for details.                              |    No     |    -    |         -        |
| AGRAPH_SCOPES_ENABLED     | If enabled, adds scopes from swagger specs to oauth access token request |    No     |  True   |    True/False    |

### Run-time configurations

AladdinSDK is highly customizable, allowing users to write clean, readable, and reusable code across different environments. </br>
Configurations enable citizen developers to share code-snippets or projects more easily. Or test applications with different system account credentials by simply changing configurations.

#### Pointing to a configuration file

- Users can set (or override the default) configurations by providing their own config file and setting the environment variable `ASDK_USER_CONFIG_FILE`
  - The SDK contains a command line utility to get started with building a configuration file. In the terminal where the package is installed run and follow the prompts:
    ```sh
    aladdinsdk-cli
    ```
- Set the environment variable `DEFAULT_ASDK_CONFIG_FILE` to point to a default configuration file. This is intended for curated python environments and domain SDK developers to dictate the default user experience.

**IMPORTANT**

- Ensure the environment variable `ASDK_USER_CONFIG_FILE` is set _before_ importing `aladdinsdk` module in code.
- To see configurations currently picked by the SDK, invoke this utility:

  ```py
  aladdinsdk.config.print_current_user_config()
  ```

- In 'Aladdin Developer' or similar python development environments, for any config file updates, a kernel restart is always recommended.

In order of **increasing** priority, configuration values can be provided via:
- Default configuration yaml/json file
- User configuration yaml/json file
- Override `ASDK_` environment variables
- Inline parameters passed in ASDK method invocations or object declarations

Under the hood, configuration management is performed using Dynaconf. Custom environment variable prefix is `ASDK_`. This entails: Any of the configurations may be overridden via environment variables (prefixed by "ASDK_" followed by dunder (double underscore) names for nested elements - This is detailed [here](#environment-variable-overrides). )

#### All Supported Configurations

##### API - Basic Auth

Set API.AUTH_TYPE as `Basic Auth`

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| API: <br/>&nbsp;&nbsp; AUTH_TYPE:                                                                                                 | Dictates which authentication mechanism to use for making API calls. <br /> (ASDK_API__AUTH_TYPE)                                                                                                                                                                                                          |                `Basic Auth`                 |                   `Basic Auth` / `OAuth`                   |
| API: <br/>&nbsp;&nbsp; TOKEN:                                                                                                     | API Token registered via Studio UI. Required only for Basic Auth  <br /> (ASDK_API__TOKEN)                                                                                                                                                                                                                 |                      -                      |                             -                              |
| USER_CREDENTIALS: <br/>&nbsp;&nbsp; USERNAME:                                                                                     | User name to be used to connect to Aladdin. <br /> (ASDK_USER_CREDENTIALS__USERNAME)                                                                                                                                                                                                                       |                      -                      |                             -                              |
| USER_CREDENTIALS: <br/>&nbsp;&nbsp; PASSWORD:                                                                                     | User password to be used to connect to Aladdin.  <br /> Not mandatory, SDK will defer to USER_CREDENTIALS.PASSWORD_FILEPATH value. <br />  Alternatively, if running in local mode, will use OS credential manager for storing password. <br /> (ASDK_USER_CREDENTIALS__PASSWORD)                          |                      -                      |                             -                              |
| USER_CREDENTIALS: <br/>&nbsp;&nbsp; PASSWORD_FILEPATH:                                                                            | Filepath pointing to file storing user's password in plain text (NOT RECOMMENDED).  <br /> Not mandatory if password provided in plain text in  <br /> USER_CREDENTIALS.PASSWORD setting (NOT RECOMMENDED), or if running in local mode. <br /> (ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH)                 |                      -                      |                             -                              |
| USER_CREDENTIALS: <br/>&nbsp;&nbsp; ENCRYPTED_PASSWORD_FILEPATH:                                                                  | Filepath pointing to file storing user's password in encrypted format.  <br /> If encryption_filepath not provided, then default encryption key will be used.  <br /> (ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH)                                                                                 |                      -                      |                             -                              |
| USER_CREDENTIALS: <br/>&nbsp;&nbsp; ENCRYPTION_FILEPATH:                                                                          | Filepath pointing to file storing encryption key used for password encryption/decryption.  <br /> Not mandatory. If provided, will be used in conjunction with  <br /> USER_CREDENTIALS.PASSWORD_FILEPATH to get user password for API connections. <br /> (ASDK_USER_CREDENTIALS__ENCRYPTION_FILEPATH)    |                      -                      |                             -                              |

##### API - OAuth

Set API.AUTH_TYPE as `OAuth`

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| API: <br/>&nbsp;&nbsp; AUTH_TYPE:                                                                                                 | Dictates which authentication mechanism to use for making API calls. <br /> (ASDK_API__AUTH_TYPE)                                                                                                                                                                                                          |                `Basic Auth`                 |                   `Basic Auth` / `OAuth`                   |
| API: <br/>&nbsp;&nbsp; AUTH_FLOW_TYPE:                                                                                            | Dictates which authentication flow to use for making API calls with oauth. <br /> (ASDK_API__AUTH_FLOW_TYPE)                                                                                                                                                                                               |                      -                      |           `refresh_token` / `client_credentials`           |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; AUTH_SERVER_PROXY:                                                    | Proxy for connecting to OAuth server for getting access token using client secret, id and refresh_token  <br /> (API_OAUTH__AUTH_SERVER_PROXY)                                                                                                                                                             |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; AUTH_SERVER_URL:                                                      | OAuth server url for getting access token using client secret, id and refresh_token  <br /> (API_OAUTH__AUTH_SERVER_URL)                                                                                                                                                                                   |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; CLIENT_ID:                                                            | Client ID needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_ID)                                                                                                                                                                                               |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; CLIENT_SECRET:                                                        | Client Secret needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_SECRET)                                                                                                                                                                                       |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; REFRESH_TOKEN:                                                        | Refresh token needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__REFRESH_TOKEN)                                                                                                                                                                                       |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ACCESS_TOKEN:                                                         | Access token used directly for making API calls. <br /> (ASDK_API__OAUTH__ACCESS_TOKEN)                                                                                                                                                                                                                    |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; CLIENT_DETAILS_FILEPATH:                                              | Filepath where Client ID and Secret are stored and needed for  <br /> generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_DETAILS_FILEPATH)                                                                                                                                |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; REFRESH_TOKEN_FILEPATH:                                               | Filepath where Refresh Token is stored and needed for generating  <br /> Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__REFRESH_TOKEN_FILEPATH)                                                                                                                                         |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ACCESS_TOKEN_FILEPATH:                                                | Filepath where Access token is stored and can be used directly for making API calls. <br /> (ASDK_API__OAUTH__ACCESS_TOKEN_FILEPATH)                                                                                                                                                                       |                      -                      |                             -                              |

##### API - Generic

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| API: <br/>&nbsp;&nbsp; LRO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STATUS_CHECK_INTERVAL:                                                  | Used for `call_lro_api` method to determine polling interval between status checks.  <br /> The value can be overridden using `status_check_interval` parameter for call_lro_api method  <br /> (ASDK_API__LRO__STATUS_CHECK_INTERVAL)                                                                     |                10 (seconds)                 |                             -                              |
| API: <br/>&nbsp;&nbsp; LRO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STATUS_CHECK_TIMEOUT:                                                   | Used for `call_lro_api` method to determine timeout for status checks.  <br /> The value can be overridden using `timeout` parameter for call_lro_api method  <br /> (ASDK_API__LRO__STATUS_CHECK_TIMEOUT)                                                                                                 |                300 (seconds)                |                             -                              |
| API: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STOP_AFTER_ATTEMPT:                                                   | Retry up to certain amount of attempts for API retry logic. <br /> (ASDK_API__RETRY__STOP_AFTER_ATTEMPT)                                                                                                                                                                                                   |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; WAIT_FIXED:                                                           | Wait time in seconds before retry for API retry logic. <br /> (ASDK_API__RETRY__WAIT_FIXED)                                                                                                                                                                                                                |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STOP_AFTER_DELAY:                                                     | Retry up to certain amount of delay for API retry logic. <br /> (ASDK_API__RETRY__STOP_AFTER_DELAY)                                                                                                                                                                                                        |                      -                      |                             -                              |
| API: <br/>&nbsp;&nbsp; PAGINATION: <br/>&nbsp;&nbsp;&nbsp;&nbsp; MAX_PAGES                                                        | Config value used to determine the maximum number of subsequent api calls made for pagination                                                                                                                                                                                                              |                      5                      |                             -                              |
| API: <br/>&nbsp;&nbsp; PAGINATION: <br/>&nbsp;&nbsp;&nbsp;&nbsp; MAX_PAGE_SIZE                                                    | Config value used to determine the maximum number of retrieved from each api call                                                                                                                                                                                                                          |                     10                      |                             -                              |
| API: <br/>&nbsp;&nbsp; PAGINATION: <br/>&nbsp;&nbsp;&nbsp;&nbsp; TIMEOUT                                                          | Config value used to determine the maximum timeout value. This will terminate the api call request and retrieve the response obtain thus far.                                                                                                                                                              |                    300s                     |                             -                              |
| API: <br/>&nbsp;&nbsp; PAGINATION: <br/>&nbsp;&nbsp;&nbsp;&nbsp; INTERVAL                                                         | Config value used to determine the maximum interval value. This will set the interval time between each api call.                                                                                                                                                                                          |                     2s                      |                             -                              |

##### ADC

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| ADC: <br/>&nbsp;&nbsp; CONNECTION_TYPE:                                                                                           | Type of connector to use for Snowflake connection. Defaults to Snowflake's <br />  python connector, but users can choose to use Snowpark connection object as well. <br /> (ASDK_ADC__CONNECTION_TYPE)                                                                                                    |        `snowflake-connector-python`         | `snowflake-connector-python` / `snowflake-snowpark-python` |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; AUTHENTICATOR:                                                         | Snowflake connection authenticator type  <br /> (ASDK_ADC__CONN__AUTHENTICATOR)                                                                                                                                                                                                                            |                   `oauth`                   |                 `oauth` / `snowflake_jwt`                  |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; OAUTH: <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ACCESS_TOKEN:         | If using oauth authenticator, and not relying on TokenAPI, users can provide <br />  the oauth access token for ADC connections here. <br /> (ASDK_ADC__CONN__OAUTH__ACCESS_TOKEN)                                                                                                                         |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; RSA: <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRIVATE_KEY_FILEPATH:   | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is path to file containing RSA private key.  <br /> Should be provided with passphrase. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY_FILEPATH)                                                                           |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; RSA: <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRIVATE_KEY_PASSPHRASE: | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is passphrase to be used to decrypt private key file.  <br /> Should be provided with private key file path. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY_PASSPHRASE)                                                    |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; RSA: <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRIVATE_KEY:            | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is the private key value (including BEGIN and END lines, and new line characters). <br /> Can be used instead of private key filepath. Should be provided with passphrase. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY) |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ACCOUNT:                                                               | Snowflake Account, used to create private URL for connection.  <br /> Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__ACCOUNT)                                                                                                                                                                 |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ROLE:                                                                  | Snowflake user role to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__ROLE)                                                                                                                                                                                                          |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; WAREHOUSE:                                                             | Snowflake virtual warehouse to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__WAREHOUSE)                                                                                                                                                                                             |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; DATABASE:                                                              | Snowflake database to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__DATABASE)                                                                                                                                                                                                       |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; CONN: <br/>&nbsp;&nbsp;&nbsp;&nbsp; SCHEMA:                                                                | Snowflake schema to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__SCHEMA)                                                                                                                                                                                                           |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STOP_AFTER_ATTEMPT:                                                   | Retry up to certain amount of attempts for ADC retry logic. <br /> (ASDK_ADC__RETRY__STOP_AFTER_ATTEMPT)                                                                                                                                                                                                   |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; WAIT_FIXED:                                                           | Wait time in seconds before retry for ADC retry logic. <br /> (ASDK_ADC__RETRY__WAIT_FIXED)                                                                                                                                                                                                                |                      -                      |                             -                              |
| ADC: <br/>&nbsp;&nbsp; RETRY: <br/>&nbsp;&nbsp;&nbsp;&nbsp; STOP_AFTER_DELAY:                                                     | Retry up to certain amount of delay. for ADC retry logic  <br /> (ASDK_ADC__RETRY__STOP_AFTER_DELAY)                                                                                                                                                                                                       |                      -                      |                             -                              |

##### Storage

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| STORAGE: <br/>&nbsp;&nbsp; S3: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ENDPOINT_URL                                                         | The URL to use for Storage S3 workspace.                                                                                                                                                                                                                                                                   |    `https://sgs3api.blackrock.com:8082`     |                             -                              |
| STORAGE: <br/>&nbsp;&nbsp; S3: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ACCESS_KEY_ID                                                        | The access key to use when creating the client. <br /> To be sourced from S3 Storage Integration in a Studio Project. <br /> If value set, it is prioritized over CREDENTIALS_FILE.                                                                                                                        |                      -                      |                             -                              |
| STORAGE: <br/>&nbsp;&nbsp; S3: <br/>&nbsp;&nbsp;&nbsp;&nbsp; SECRET_ACCESS_KEY                                                    | The secret key to use when creating the client. <br /> To be sourced from S3 Storage Integration in a Studio Project. <br /> If value set, it is prioritized over CREDENTIALS_FILE.                                                                                                                        |                      -                      |                             -                              |
| STORAGE: <br/>&nbsp;&nbsp; S3: <br/>&nbsp;&nbsp;&nbsp;&nbsp; BUCKET_NAME                                                          | Name of Bucket assigned to user/project workspace. <br /> To be sourced from S3 Storage Integration in a Studio Project.                                                                                                                                                                                   |                      -                      |                             -                              |
| STORAGE: <br/>&nbsp;&nbsp; S3: <br/>&nbsp;&nbsp;&nbsp;&nbsp; CREDENTIALS_FILE                                                     | Path to a file containing Access Key ID and Secret Access Key. <br /> This should be a yaml with the following keys: `access_key_id` and `secret_access_key`.                                                                                                                                              |                      -                      |                             -                              |


##### Batch Processing

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| BATCH: <br/>&nbsp;&nbsp; BUFFER: <br/>&nbsp;&nbsp;&nbsp;&nbsp; MAX_SIZE:                                                          | For batch processing, in SDKActionBuffer set the maximum number of actions that can be added to buffer.  <br /> Adding any additional actions will result in a ValueError.                                                                                                                                 |                      -                      |                             -                              |
| BATCH: <br/>&nbsp;&nbsp; SEQUENTIAL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; INTERVAL:                                                      | For batch processing, when running sequentially, actions may be configured to run at specific intervals                                                                                                                                                                                                    |                      -                      |                             -                              |
| BATCH: <br/>&nbsp;&nbsp; PARALLEL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; MAX_WORKERS:                                                     | For batch processing, when running in parallel, the SDKActionBuffer uses ThreadPoolExecutor. This configuration <br /> allows users to set the max worker count, to ensure resources are utilized efficiently.                                                                                             |                      -                      |                             -                              |


##### Misc.

| Configuration Key                                                                                                                 | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                         |                   Default                   |                      Permitted Values                      |
|:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|:----------------------------------------------------------:|
| RUN_MODE:                                                                                                                         | AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions. <br /> There is also a test mode used by SDK developers. <br /> (ASDK_RUN_MODE)                                                                                                                                   |                   `local`                   |                `local` / `compute` / `test`                |
| LOG_LEVEL:                                                                                                                        | Log level to be set during execution. Value picked initially at any aladdinsdk module import. <br /> (ASDK_LOG_LEVEL)                                                                                                                                                                                      |                    INFO                     |         DEBUG / INFO / WARNING / ERROR / CRITICAL          |
| LOG: <br/>&nbsp;&nbsp; EXPORT <br/>&nbsp;&nbsp;&nbsp;&nbsp; ENABLED:                                                              | Write log output to a separate file for each run. File name format is 'run-(timestamp).log'                                                                                                                                                                                                                |                    False                    |                        True / False                        |
| LOG: <br/>&nbsp;&nbsp; EXPORT <br/>&nbsp;&nbsp;&nbsp;&nbsp; LOCATION:                                                             | Folder location for log files to be written for each run.                                                                                                                                                                                                                                                  | `./.asdk_logs` (under current working dir.) |       (location where user has permission to write)        |
| EXPORT: <br/>&nbsp;&nbsp; OVERWRITE_DATA:                                                                                         | Config value to be used when exporting to a file that already has data.  <br /> Value picked when user uses export utility to export data to file  <br /> (ASDK_EXPORT__OVERWRITE_DATA)                                                                                                                    |                    False                    |                        True / False                        |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; STUDIO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ACTION:                                                    | Describes the method in which the user will receive the notification <br /> Defaults to 'STUDIO_NOTIFICATION_ACTION_UNSPECIFIED'                                                                                                                                                                           |                      -                      | 'STUDIO_NOTIFICATION_ACTION_UNSPECIFIED' /  <br /> 'STUDIO_NOTIFICATION_ACTION_SMTP' / <br /> 'STUDIO_NOTIFICATION_ACTION_PUSH' |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; STUDIO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; EVENT_NAME:                                                | This is the name of the event specific to the type of notification                                                                                                                                                                                                                                         |                      -                      |                           -                                |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; STUDIO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; EVENT_TYPE:                                                | This  is the type of Studio notification. <br /> Defaults to 'STUDIO_NOTIFICATION_EVENT_TYPE_UNSPECIFIED'                                                                                                                                                                                                  |                      -                      | 'STUDIO_NOTIFICATION_EVENT_TYPE_UNSPECIFIED' / <br /> 'STUDIO_NOTIFICATION_EVENT_TYPE_ACM' / <br /> 'STUDIO_NOTIFICATION_EVENT_TYPE_COMPUTE' / <br /> 'STUDIO_NOTIFICATION_EVENT_TYPE_API' / <br /> 'STUDIO_NOTIFICATION_EVENT_TYPE_SPACE' / <br /> 'STUDIO_NOTIFICATION_EVENT_TYPE_PROJECT' |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; STUDIO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ENTITY_NAME:                                               | The name of the targeted notification receiver                                                                                                                                                                                                                                                             |                      -                      |                           -                                |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; STUDIO: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ENTITY_TYPE:                                               | The entity type of the notification receiver. Defaults to "STUDIO_ENTITY_TYPE_UNSPECIFIED"                                                                                                                                                                                                                 |                      -                      | 'STUDIO_ENTITY_TYPE_UNSPECIFIED' / <br /> 'STUDIO_ENTITY_TYPE_USER' / <br /> 'STUDIO_ENTITY_TYPE_PROJECT' / <br /> 'STUDIO_ENTITY_TYPE_SPACE' |
| ERROR_HANDLING: <br/>&nbsp;&nbsp; EMAIL_NOTIFICATIONS: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ENABLED:                                     | Config value used to enable error email notifications in the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING__EMAIL_NOTIFICATIONS__ENABLED)                                                                                                            |                      -                      |                        True / False                        |
| ERROR_HANDLING: <br/>&nbsp;&nbsp; EMAIL_NOTIFICATIONS: <br/>&nbsp;&nbsp;&nbsp;&nbsp; TO:                                          | List of recipients the user wants to send an error email notifications to in the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING__EMAIL_NOTIFICATIONS__TO)                                                                                             |                      -                      |                     List of recipients                     |
| ERROR_HANDLING: <br/>&nbsp;&nbsp; EMAIL_NOTIFICATIONS: <br/>&nbsp;&nbsp;&nbsp;&nbsp; ON_EXCEPTION_TYPES:                          | List of exceptions for which to send email notifications to users related to the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING - <br /> __EMAIL_NOTIFICATIONS__ON_EXCEPTION_TYPES)                                                                   |                      -                      |                     List of exceptions                     |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; EMAIL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; EMAIL_HOST:                                                 | Config value to be used for setting the email host.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_HOST)                                                                                                                          |                      -                      |                      Valid email host                      |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; EMAIL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; EMAIL_USERNAME:                                             | Config value to be used for setting the email login username.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_USERNAME)                                                                                                            |                      -                      |                    User email username                     |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; EMAIL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; EMAIL_PASSWORD:                                             | Config value to be used for setting the email login password.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_PASSWORD)                                                                                                            |                      -                      |                    User email password                     |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; EMAIL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; TO:                                                         | List of recipients the user wants to send email notifications to in the sdk.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__TO)                                                                                                         |                      -                      |                     List of recipients                     |
| NOTIFICATIONS: <br/>&nbsp;&nbsp; EMAIL: <br/>&nbsp;&nbsp;&nbsp;&nbsp; SENDER:                                                     | Config value to be used for setting the sender email value.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__SENDER)                                                                                                                      |                      -                      |                     User sender email                      |


**Note:**
- Any of the configurations can be overridden by setting environment variables prefixed with "ASDK_" (e.g. to override `mode`, set an environment variable `ASDK_MODE`)
- For nested keys, use dunder, i.e. double underscore, to denote access to nested elements (e.g. to override `api.token`, set an environment variable `ASDK_API__TOKEN`)

#### Sample configuration file

- Sample YAML configuration for API (OAuth) and ADC (RSA) connectivity:
  ```yaml
  RUN_MODE: local
  API:
    AUTH_TYPE: "OAuth"
    OAUTH:
      ACCESS_TOKEN: <access token for API calls>
  USER_CREDENTIALS:
    USERNAME: <user name>
  ADC:
    CONN:
      AUTHENTICATOR: "snowflake_jwt"
      RSA:
        PRIVATE_KEY_FILEPATH: "/location/to/secret/rsa_key.p8"
        PRIVATE_KEY_PASSPHRASE: "passphrase_for_rsa_key"
      ACCOUNT: "<ADC account URL, up to and including '.privatelink'>"
      ROLE: <User role to be used for connection>
      WAREHOUSE: <Virtual warehouse to be used to perform query>
      DATABASE: <Database>
      SCHEMA: <Schema>
  ```
- Sample code snippets and user configuration files are provided under [`resources/sample_code_snippets`](resources/sample_code_snippets) directory in this code repository.

### Local Secret Management for User Credentials

While working on your personal machine, users may pass in credentials via the following ways (listed in order of priority used by SDK to fetch secrets):
- in API/ADC client class declaration or via user configuration file (under API section)
- OR, using the OS specific credential manager (__recommended__)

AladdinSDK uses [Keyring](https://pypi.org/project/keyring/) internally for secret management __only__ in `local` run mode. Following secrets are supported at the moment:

| Secret | Service Name in keyring | Username in keyring | Used in absence of corresponding configuration entry (& environment variable) |
| :----- | :---------------------- | :------------------ | :--------------------------------------------------- |
| Password, used for API Basic Auth | ASDK-PASSWORD-{defaultWebServer value} | {username} - sourced from configuration file `USER_CREDENTIALS.USERNAME` | `USER_CREDENTIALS.PASSWORD` (& `ASDK_USER_CREDENTIALS__PASSWORD`) |

For AladdinSDK to be able to fetch secrets via keyring -
- Ensure `RUN_MODE` in configuration file is `local`
- DO NOT set corresponding configuration file entry or environment variable for the secret to be stored
- Make an API call using AladdinSDK - in case of missing configuration and keyring entry, AladdinSDK will prompt the user for their password in command line, and store the password in the OS specific credential manager (e.g. MacOS - Keychain Access)


### Aladdin SDK CLI

To help get started with a configuration file, the SDK comes with a command line interface (aladdinsdk-cli). On a terminal, navigate to a location where AladdinSDK is installed and simply run the command:
```sh
aladdinsdk-cli
```

#### Generating OAuth Refresh Token via aladdinsdk-cli

As mentioned earlier, SDK allows for OAuth API calls with either `client_credentials` or `refresh_token` flow.

For Refresh Token flow, user needs to provide `client_id`, `client_secret` and `refresh_token`.
**Client ID** and **Secret** can be sourced from Studio UI by creating a OAuth application under a Project.

When working locally, AladdinSDK CLI provides an option to generate a **Refresh Token**. To use this option:
- Create/Modify OAuth Application under a Project in Studio to include a localhost callback URI - `http://localhost:<PORT>`
    - Where the PORT is any freely available PORT on your computer.
- Open a terminal on your computer (where you have browser access) and start `aladdinsdk-cli`
    - Then select `OAuth` authentication type, and `Refresh Token Flow - Generate Refresh token given Client ID, Secret - (local auth code flow)`
      options for API auth
    - Provide the following values: client ID, secret, localhost callback URI port (from previous step)
    - Select endpoints from the scope list (Note: Selected list must be a subset of scopes setup for the app in Studio UI)
    - The SDK will then open a browser tab for you to authenticate to the environment if you haven't already done so.
    - A successful authentication flow will take you to the next CLI question.
      (An unsuccessful attempt will timeout in 30 seconds, or can be interrupted with Ctrl+C)
    - Follow through the remaining prompts and the SDK will show the refresh token as part of the built configuration (which may be written to a file for future reference)


## AladdinAPI

AladdinSDK provides an API client `AladdinAPI` which wraps over OpenAPI generated python client code based on Aladdin Graph API's swagger specifications.

APIs are made available via plugins that can be installed as any other python package using `pip`. For more details on how these are built, refer [aladdinsdk-plugin-builder](https://github.com/blackrock/aladdinsdk-plugin-builder) project.

The API client provides the following capabilities:
- Authentication: Using Basic Auth or OAuth
- Input parameter validation using pydantic
- Response deserialization to codegen response objects or plain json conversion
    - Note: This can be disabled for APIs using the `_deserialize_to_object` parameter in API call methods
- Retry mechanism
- Error handling (extensible by providing additional handlers)
- LRO Utilities to trigger and poll Long Running Operation endpoint calls

A simple example of an API call is:
```py
from aladdinsdk.api.client import AladdinAPI

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
req_body_json = {
    "query": {
        "departingStationId": "TS_1441"
    }
}
response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json)
```

_Additional examples under [`resources/sample_code_snippets/sample_api_calls.md`](resources/sample_code_snippets/sample_api_calls.md)_

### AladdinAPI Plugins

The core SDK contains pre-packaged APIs used for connectivity and reference/testing. However, additional APIs can be added by simply installing plugin packages as needed.
AladdinSDK will scan installed python packages to find compatible plugins. All APIs in these plugins will be available via AladdinSDK without any additional setup steps.

AladdinSDK's functional capabilities can be extended as needed using API bundles or 'plugins' that can be installed separately.

List of official AladdinSDK API plugins (refer documentation on PyPI for up-to-date list of APIs packaged in each plugin):
- [asdk_plugin_accounting](https://pypi.org/project/asdk_plugin_accounting)
- [asdk_plugin_analytics](https://pypi.org/project/asdk_plugin_analytics)
- [asdk_plugin_clients](https://pypi.org/project/asdk_plugin_clients)
- [asdk_plugin_compliance](https://pypi.org/project/asdk_plugin_compliance)
- [asdk_plugin_data](https://pypi.org/project/asdk_plugin_data)
- [asdk_plugin_investment_operations](https://pypi.org/project/asdk_plugin_investment_operations)
- [asdk_plugin_investment_research](https://pypi.org/project/asdk_plugin_investment_research)
- [asdk_plugin_platform](https://pypi.org/project/asdk_plugin_platform)
- [asdk_plugin_portfolio](https://pypi.org/project/asdk_plugin_portfolio)
- [asdk_plugin_portfolio_management](https://pypi.org/project/asdk_plugin_portfolio_management)
- [asdk_plugin_trading](https://pypi.org/project/asdk_plugin_trading)

Install plugins using pip: `pip install asdk_plugin_<bundle_name>`

For example, to make an 'OrderAPI' call, install the 'trading' plugin which contains this API:
```sh
pip install asdk_plugin_trading
```

```py
from aladdinsdk.api.client import AladdinAPI

api_instance_order = AladdinAPI("OrderAPI")
```

_For more details about plugins, refer [aladdinsdk-plugin-builder](https://github.com/blackrock/aladdinsdk-plugin-builder) project._


## ADC Client

ADC (Snowflake) access is provided via the ADCClient. This is a wrapper around snowflake-connector-python or snowflake-snowpark-python (connection type is configurable).

The ADC Client provides the following capabilities:
- Authentication: Using 'oauth' or 'snowflake_jwt' (i.e. RSA Keys) authenticator types for snowflake connectors
- Session management:
    - connection establish, close, re-connect
    - update role, database, schema, warehouse
    - set [session_parameters](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect#setting-session-parameters) level attributes
        - Note: An SDK query tag is prepended to any user provided query tags

A simple example of an ADC client is:
```py
from aladdinsdk.adc.client import ADCClient

adc_client = ADCClient()

# read data from ADC
df = adc_client.query_sql('SELECT * FROM "CASH_ENTRY" LIMIT 10')

# write data to ADC
is_success, chunks_count, ingested_row_count = adc_client.write_frame(df=df, table_name='TARGET_TABLE_NAME')
```
_Additional examples under [`resources/sample_code_snippets/sample_adc_calls.md`](resources/sample_code_snippets/sample_adc_calls.md)_

### ADC Connection Authentication Types

#### OAuth

For OAuth connectivity, provide the following details in the user configuration file:

```yaml
ADC:
   CONN:
     AUTHENTICATOR: oauth
     OAUTH:
       ACCESS_TOKEN: <valid oauth access token>
```

Note: This configuration is optional for client environments where ADC OAuth is configured via Studio application, SDK's ADCClient will attempt to fetch an OAuth AccessToken from Aladdin's TokenAPI.
Here, the assumptions are:
- User has provided API connection details as part of the configuration or ADCClient initialization.
- User has authenticated with the ADC OAuth client application by logging into Aladdin Studio UI.

#### RSA Keys

For RSA Keys (snowflake_jwt) authentication, follow the below steps to generate RSA key pairs and then provide the following details in the user configuration file:

```yaml
ADC:
   CONN:
     AUTHENTICATOR: snowflake_jwt
     RSA:
       PRIVATE_KEY_FILEPATH: <file path to private key>
       PRIVATE_KEY_PASSPHRASE: <private key passphrase>
```

Follow these steps to generate keys in PEM format first.

1. Generate a private-public key pair under 'Keys' directory. Note: Remember the `passphrase` entered during these steps:

    ```sh
    mkdir Keys
    cd Keys
    openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8
    openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
    ```

2. From Snowflake UI, call Stored Procedure to append the public key to Aladdin user account:

    ```sql
    CALL ALADDINDB.PUBLIC.UPDATE_PUB_KEY_SP('<Contents of rsa_key.pub file without BEGIN/END line>','KEY1');
    ```

3. Using the AladdinSDK configurations provide one of the following details:
    - Private key passphrase - ADC.CONN.RSA.PRIVATE_KEY_PASSPHRASE
    - Private Key encrypted value (including BEGIN and END lines, and new line characters) to be added to snowflake connection - ADC.CONN.RSA.PRIVATE_KEY
    
    OR
    
    - Private key passphrase - ADC.CONN.RSA.PRIVATE_KEY_PASSPHRASE
    - Path to file containing private key file - ADC.CONN.RSA.PRIVATE_KEY_FILEPATH


## Storage

### S3 Client

The S3 Storage client provides a simple way to interact with an S3 integration in a Project.

Pre-requisite: Create a Storage integration on Studio UI under a personal / shared project. This will provide details for access key and bucket name.

Add Storage -> S3 configurations. Sample code snippet:

```py
from aladdinsdk.storage.s3 import S3Client

s3client = S3Client()

s3client.upload_file(filename="/path/to/file.txt", key="test.txt")

s3client.download_file(key="test.txt", filename="/path/to/downloaded_file.txt")

s3client.delete_object(key="test.txt")
```

The wrapper provides underlying client object for users to use the full gamut of boto3 S3.Client methods.
```py
from aladdinsdk.storage.s3 import S3Client

s3client = S3Client()

_client = s3client.get_s3_client()
```

## Common Utilities

### Batch Processing

- AladdinSDK enables users to perform actions in batches. An `SDKAction` is a callable method with its args & kwargs.
- Actions can be performed Sequentially or in Parallel.
- Setting up a batch process:
    - Initialize buffer:
        ```py
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction

        action_buffer = SDKActionBuffer()
        ```
        - Optionally initialize with a max size as follows: `action_buffer = SDKActionBuffer(max_size=5)`
        - Max size can also be configured with `BATCH.BUFFER.MAX_SIZE` configuration
    - Defining SDKActions:
        - First parameter is a callable method
        - Following args/kwargs are used to call the method with during execution of the action
        - example snippet:
            ```py
            from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
            from aladdinsdk.api.client import AladdinAPI
            api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
            req_body_json = { "query": { "departingStationId": "TS_1441" } }

            api_post_action = SDKAction(api_instance_train_journey.post, "/trainJourneys:filter", req_body_json)
            
            api_get_action = SDKAction(api_instance_train_journey.get, '/trainJourneys/{id}', id='TJ_4')
            ```
    - Add actions to buffer
        ```py
        action_buffer.append_action(api_post_action)
        action_buffer.append_action(api_get_action)
        ```
- Run actions sequentially:
    ```py
    action_buffer.run_sequential()
    ```
    - Optionally, run sequentially but at regular intervals: `action_buffer.run_sequential(interval=5)`
    - Interval can be configured using `BATCH.SEQUENTIAL.INTERVAL`
- Run actions in parallel:
    ```py
    action_buffer.run_parallel()
    ```
    - Optionally, run in parallel but with fixed worker thread count: `action_buffer.run_parallel(max_workers=5)`
    - Max workers can be configured using `BATCH.PARALLEL.MAX_WORKERS`
- Once the batch processing is done, the responses (results / errors) are available via `get_response_map` where the response is mapped to actions' unique identifier:
    ```py
    response_map = action_buffer.get_response_map()
    for action_uid in response_map:
        res = response_map[action_uid]
        print(f"result for action {action_uid}: {res}")
    ```
- To clear the action buffer:
    ```py
    action_buffer.clear_actions()
    ```

### Retry Mechanisms

AladdinSDK allows a retry mechanism for failed API or ADC calls. This can be setup quite simply using the `wait_fixed` / `stop_after_attempt` / `stop_after_delay` configurations in the config file or environment variables

- To enable API retries, set the `RETRY` section under `API`:
    ```yaml
    API:
        AUTH_TYPE: Basic Auth
        RETRY:
            wait_fixed: 2
            stop_after_attempt: 3
            stop_after_delay: 7
    ```

- To enable ADC retries, set the `RETRY` section under `ADC`:
    ```yaml
    ADC:
        RETRY:
            wait_fixed: 2
            stop_after_attempt: 3
            stop_after_delay: 7
    ```

### Data Transformations

Data transformation is a common action performed on API responses. This utility aims to provide generic transformation capabilities via simple interface.

Currently supported transformations:

- JSON to Pandas Dataframe

Example [code snippet for data transformations](resources/sample_code_snippets/sample_data_transformations.py)

### Data Exports

Exporting data to persistent storage helps store intermediate steps or final results to a file system.
Generic file formats exports currently supported:

- json
- csv
- xlsx
- pkl

Example [code snippet for data exports](resources/sample_code_snippets/sample_export_data_calls.md)

### Logging

- Users can set log level via the configuration file using the `LOG_LEVEL` key (or `ASDK_LOG_LEVEL` environment variable)
    - Values can be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Log files can also be created for each run to preserve run history. Log file name is `run-(timestamp).log` to help identify which log file is associated with which run.
    - To enable this, simple set `LOG.EXPORT.ENABLED` (or `ASDK_LOG__EXPORT__ENABLED` environment variable) to `True`. This will create a new log file for each run under a `.asdk_logs` folder in the current working directory.
    - Optionally, to export logs to a different folder location, set `LOG.EXPORT.LOCATION` (or `ASDK_LOG__EXPORT__LOCATION` environment variable) to a location where the user has write permissions.

### Error handler registration
AladdinSDK simplifies error handling internally by using a decorator (`asdk_exception_handler`) that intercepts raised exceptions and maps them to specific handlers.
This is decorator and handler framework is made available to AladdinSDK users and DomainSDK developers.

To utilize this capability:
- Raise a PR to add an error code Enum under `AsdkErrorCode`. (Or use the generic domain SDK error code 'AE004')
    - _AladdinSDK users can skip this step and simply use 'AE004'_
- Implement an exception handler class by implementing `AbstractAsdkExceptionHandler`, and configure the newly created enum
- Provide this class definition to the core AladdinSDK by invoking `register_handler_class` e.g.:
    ```py
    from aladdinsdk.common.error import handler
    handler.register_handler_class(DomainExceptionHandler)
    ```
- The decorator `asdk_exception_handler` will now map any matching exceptions to the registered handlers and invoke the `handle_error` method.

Example [code for registering error handlers](resources/sample_code_snippets/sample_error_handler_registration.md)

### Notifications - StudioNotification

AladdinSDK provides a Studio Notifications utility that can be used to programmatically send SMPT/Push notifications using the Studio Subscription and Notification APIs
 
- From a configurtation standpoint, users simply need to setup their API credentials (Basic Auth or OAuth)
- Note - if using OAuth, ensure the right set of scopes are selected
- Users can either configure additional Notifications attributes in the config file, or provide it inline during Studio Notifcation object creation.
- Steps to create a subscription:
    1. Create a StudioNotification object
        ```py
        notification = StudioNotification(notification_action, notification_event_name, notification_event_type,
                                        studio_entity_type, studio_entity_name)
        ```
    2. Create subscription by providing set of recipients:
        ```py
        notification.create_subscription(recipients)
        ```
    3. Notify subscribers. Provide Subject, Message and any Metadata to be included in the notification:
        ```py
        notification.send_notification(subject, message, metadata)
        ```
- A wrapper around this utility `send_studio_smtp_notification` is created to provide a simpler "email" feature. Users can provide recipients, subject, message and metadata for an email to be sent. 
    ```py
    from aladdinsdk.common.notifications.studio_notifications import send_studio_smtp_notification
    send_studio_smtp_notification(
        recipients=["<recipient>@blackrock.com"],
        subject="Test Notification via AladdinSDK",
        message="Sample email message")
    ```

### Notifications - Email

E-mail notification utility can be used to programmatically send emails
 
- User can enable email notifications by adding their email username, email password, email host and email sender values in the user config file under the `NOTIFICATIONS.EMAIL` section in user settings file
- As part of the email, the user can provide list of recipients, list of cc email ids, email subject, email body and attachments

Example [code snippet for email notifications](resources/sample_code_snippets/sample_send_email_notification.md)

### Error Notifications - Email

The e-mail utility is additionally integrated with the error handling mechanism. This enables users to receive emails for any exceptions that may occur while executing their scripts / scheduled jobs.
 
- User can enable email notifications on errors by setting `NOTIFICATIONS.EMAIL` and `ERROR_HANDLING.EMAIL_NOTIFICATIONS` sections in user settings file
- For more details refer to the supported configuration table above

### Pagination
AladdinSDK provides a generic pagination utility that can be used to paginate through API responses. This utility can be used to fetch n pages of data from an API endpoint that supports pagination.

To utilize this capability:
- Pass in _asdk_pagination_options to the API call method
    ```py
    from aladdinsdk.api.client import AladdinAPI
    api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
    req_body_json = {
        "query": {
            "departingStationId": "TS_1441"
        }
    }
    _asdk_pagination_options = {
        "page_size": 5,
        "number_of_pages": 10
    }
    response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json, _asdk_pagination_options=_asdk_pagination_options)
    ```
- _asdk_pagination_options takes the following fields:
    - page_size: Number of records to fetch per api call
    - number_of_pages: Number of pages to fetch (subsequent api calls made)
    - timeout: Maximum time to wait for the entire api method call to complete
    - interval: Time to wait between subsequent api calls
    - page_token: Token to start fetching data from a specific page

- Maximum values for page_size, number_of_pages and timeout can be configured using the following configuration keys in the config file:
    ```yaml
    API:
      PAGINATION:
        MAX_PAGE_SIZE: 10
        MAX_PAGES: 5
        TIMEOUT: 300
        INTERVAL: 2
    ```
- The paginated response will be a list of responses from each page
 ```py
  from aladdinsdk.api.client import AladdinAPI
  api_instance = AladdinAPI("TrainJourneyAPI")

  responses = api_instance.get("/trainJourneys", _asdk_pagination_options={'page_size': 2, 'page_token': ''})

  print("\nTrain Journey API Response:")
  for response in responses:
    for tj in response.train_journeys:
      print(
        f"From: {tj.departing_train_station_id}, To: {tj.destination_train_station_id}, Stops: {len(tj.pass_through_station_ids)}, Date: {tj.journey_date}, Duration: {tj.journey_duration}")
```
Example [code snippet for api pagination](resources/sample_code_snippets/sample_api_pagination_calls.md)

## DomainSDK Development

Teams interested in building their business specific SDKs can build on top of AladdinSDK. Typically, the business logic in these SDKs pertain to specific set of APIs, therefore the SDK developers can simply include the necessary plugin libraries in their `requirements.txt`. This allows their end users to install just one DomainSDK packages, which will include all necessary APIs.

Core AladdinSDK provides generic solutions for SDK development, so DomainSDK developers can focus on specific business IP. DomainSDK users have access to all the aforementioned configurations, utilities and mechanisms.

### Configurations
- DomainSDK users have access to all the above configurations.
- However, DomainSDK developers can fix/lock out certain configurations as needed
- DomainSDK Configurations: SDK Developers can add additional configurable options under a separate section of the configuration file.
    - To avoid clashing with other DomainSDK's being installed, it is recommended the section is named the same as the SDK name:
        </br>
        e.g. For a DomainSDK named `TrainJourneySDK`:</br>
        ```yaml
        RUN_MODE: local
        API:
            AUTH_TYPE: Basic Auth
        TrainJourneySDK:
            T_ID: XYZ
        ```
    - To read the configured value, use the `asdk_conf_get` utility:
        ```py
        from aladdinsdk.config import asdk_conf_get
        asdk_conf_get('TrainJourneySDK.T_ID')  # returns XYZ
        ```
        If no configuration is set, you can provide a default value as follows:
        ```py
        asdk_conf_get('TrainJourneySDK.T_ID', 'PQR')  # returns PQR if not configured via config file or environment variable
        ```

### Error Handlers
- Where applicable, DomainSDK developers may add bespoke Error Codes by raising a PR to this repository
- Error handler registration can be done as mentioned above.

### Metrics

AladdinSDK API and ADC metrics are by default tracked with "AladdinSDK-Core/1.0.0/python" and "QueryViaSDK-AladdinSDK-Core" tags respectively.
In the event domain SDK developers want to track usage from their artifacts only, they are given the option to add a domain specific suffix enabling creation of bespoke metrics dashboards for internal monitoring. </br>
e.g. Setting suffix to "DomainSDK" would tag API calls with "AladdinSDK-DomainSDK/1.0.0/python" and ADC queries with "QueryViaSDK-AladdinSDK-DomainSDK"

To utilize this capability:
- Add this code snippet during initialization, so the suffix value is updated at the time of domain sdk package imports:
    ```py
    from aladdinsdk.common.metrics import update_domain_sdk_metrics_suffix
    update_domain_sdk_metrics_suffix("<DomainSDK>")  # Replace DomainSDK with relevant value
    ```
- **Note:** Suffix value should be alphanumeric with no spaces (may include `.` or `/`), of max length 15

## Contributing

Guidelines for contributing to the project:
  - [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
  - [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

The license for the project:
  - [LICENSE](./LICENSE)

## Credits

Initial code contributions:
- Vedant Naik
- Harshita Das
- David Woodhead
- Infant Vasanth
- Eli Kalish
- Mike Bowen
- Anilkumar Mabagapu
- David Li
- Ginsiu Cheng
- Oleg Zakrevskiy


Resources:
- Aladdin Graph APIs
- Aladdin Data Cloud