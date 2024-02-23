# AladdinSDK

AladdinSDK allows developers to easily integrate BlackRock's Aladdin functionality into their own applications and systems. The goal is to make it easier for everyone to efficiently access and utilize Aladdin APIs and Data Cloud.

## Table of Contents

- [AladdinSDK](#aladdinsdk)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Core Features](#core-features)
  - [DomainSDK Development](#domainsdk-development)
  - [Contributing](#contributing)
  - [License](#license)
  - [Credits](#credits)
  - [Contact](#contact)

## Installation

### Using AladdinSDK in your environment

- Compatible python version: 3.9
- Install using pip
    ```sh
    pip install aladdinsdk
    ```
    _For local development, installing `keyring` is recommended for easier credential management_
    ```sh
    pip install keyring
    ```
- Set BlackRock's `defaultWebServer` environment variable
- Optionally, create a local user configuration file or set essential environment variables. Refer [run-time configurations section](#run-time-configurations) for details.

### Setting up this repository for developing AladdinSDK

- Clone the project locally:
  ```sh
  gh repo clone blackrock/aladdinsdk
  ```
- Create python venv. Ensure python virtual environment version is 3.9.
  ```
  python -m venv venv
  source venv/bin/activate
  ```
- Install dependencies
  ```sh
  pip install -r requirements.txt
  ```
- Set BlackRock's `defaultWebServer`

#### Managing APIs (Note: This section is temporary and API management will be decoupled from core SDK)

- The supported API specs are stored under [./resources/api_specs](./resources/api_specs/)
- To add/update/delete APIs, perform the code generation steps locally:
  - Update the contents of the api_specs folder appropriately.
  - Run the code generation utility script using this command:
    ```sh
    python devutils/asdk_agraph_api_codegen.py -osd resources/api_specs
    ```
  - Verify changes by running API calls locally, then create a PR to add these changes to the repository

## Usage

### Environment Variables

| Environment Variable Name | Description                                                              | Mandatory | Default | Permitted Values |
|:--------------------------|:-------------------------------------------------------------------------|:---------:|:-------:|:----------------:|
| defaultWebServer          | BlackRock client environment's default web server                        |    Yes    |    -    |         -        |
| ASDK_USER_CONFIG_FILE     | Path to AladdinSDK configuration to be used                              |    No     |    -    |         -        |
| AGRAPH_SCOPES_ENABLED     | If enabled, adds scopes from swagger specs to oauth access token request |    No     |  False  |    True/False    |

### Run-time configurations

AladdinSDK is highly customizable. This allows the code to be clean, readable, and reusable across environments. 
E.g. 
- Citizen developers may share code-snippets or projects and be able to run with their credentials. 
- Developer may be able to test applications with different system account credentials by simply changing configuration.

In order of **increasing** priority, configurations can be provided via:
- Default configuration yaml/json file
- User configuration yaml/json file
- Override `ASDK_` environment variables
- Inline parameters passed in ASDK method invocations or object declarations

Under the hood, configuration management is performed using Dynaconf. Custom environment variable prefix is `ASDK_`. This entails: Any of the configurations may be overridden via environment variables (prefixed by "ASDK_" followed by dunder (double underscore) names for nested elements - This is detailed [here](#environment-variable-overrides). )

#### Pointing to a configuration file

- The SDK offers the ability to set a default configuration file to be preloaded at initialization. Set the environment variable `DEFAULT_ASDK_CONFIG_FILE` to point to the configuration file path. This is intended for curated notebook owners and domain SDK developers to dictate the default SDK experience.
- End users can set (or override the default) configurations by providing their own config file and setting the environment variable `ASDK_USER_CONFIG_FILE`
  - The SDK provides a utility to get started with building this configuration file. Installing `aladdinsdk` installs a `aladdinsdk-cli` CLI. Running this in your terminal will walk you through the steps to get started.
    ```sh
    pip install aladdinsdk
    aladdinsdk-cli
    ```


To see configurations currently picked by the SDK, invoke this utility:

```py
aladdinsdk.config.print_current_user_config()
```

**IMPORTANT**
  - Ensure the environment variable `ASDK_USER_CONFIG_FILE` is set before importing `aladdinsdk` module in code.
  - In Aladdin Developer or similar python development environments, for any config file updates, a kernel restart is always recommended.

#### All Supported Configurations

| Configuration Key                             | Description <br /> (Override environment variable)                                                                                                                                                                                                                                                                                 | Mandatory |                                     Default                                     | Permitted Values |
|:----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------:|:-------------------------------------------------------------------------------:| :--------------: |
| RUN_MODE                                      | AladdinSDK can run on a developer's local machine or in Aladdin Studio Compute sessions. <br /> There is also a test mode used by SDK developers. <br /> (ASDK_RUN_MODE)                                                                                                                                                           |    No     |                                     `local`                                     | `local` / `compute` / `test` |
| API.TOKEN                                     | API Token registered via Studio UI. Required only for Basic Auth  <br /> (ASDK_API__TOKEN)                                                                                                                                                                                                                                         |    No     |                                        -                                        | - |
| API.AUTH_TYPE                                 | Dictates which authentication mechanism to use for making API calls. <br /> (ASDK_API__AUTH_TYPE)                                                                                                                                                                                                                                  |    No     |                                  `Basic Auth`                                   | `Basic Auth` / `OAuth` |
| API.AUTH_FLOW_TYPE                            | Dictates which authentication flow to use for making API calls with oauth. <br /> (ASDK_API__AUTH_FLOW_TYPE)                                                                                                                                                                                                                       |    No     |                                        -                                        | `refresh_token` / `client_credentials` |
| API.OAUTH.AUTH_SERVER_PROXY                   | Proxy for connecting to OAuth server for getting access token using client secret, id and refresh_token  <br /> (API_OAUTH__AUTH_SERVER_PROXY)                                                                                                                                                                                     |    No     |                                        -                                        | - |
| API.OAUTH.AUTH_SERVER_URL                     | OAuth server url for getting access token using client secret, id and refresh_token  <br /> (API_OAUTH__AUTH_SERVER_URL)                                                                                                                                                                                                           |    No     |                                        -                                        | - |
| API.OAUTH.CLIENT_ID                           | Client ID needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_ID)                                                                                                                                                                                                                       |    No     |                                        -                                        | - |
| API.OAUTH.CLIENT_SECRET                       | Client Secret needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_SECRET)                                                                                                                                                                                                               |    No     |                                        -                                        | - |
| API.OAUTH.REFRESH_TOKEN                       | Refresh token needed for generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__REFRESH_TOKEN)                                                                                                                                                                                                               |    No     |                                        -                                        | - |
| API.OAUTH.ACCESS_TOKEN                        | Access token used directly for making API calls. <br /> (ASDK_API__OAUTH__ACCESS_TOKEN)                                                                                                                                                                                                                                            |    No     |                                        -                                        | - |
| API.OAUTH.CLIENT_DETAILS_FILEPATH             | Filepath where Client ID and Secret are stored and needed for  <br /> generating Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__CLIENT_DETAILS_FILEPATH)                                                                                                                                                        |    No     |                                        -                                        | - |
| API.OAUTH.REFRESH_TOKEN_FILEPATH              | Filepath where Refresh Token is stored and needed for generating  <br /> Oauth access token for making API calls. <br /> (ASDK_API__OAUTH__REFRESH_TOKEN_FILEPATH)                                                                                                                                                                 |    No     |                                        -                                        | - |
| API.OAUTH.ACCESS_TOKEN_FILEPATH               | Filepath where Access token is stored and can be used directly for making API calls. <br /> (ASDK_API__OAUTH__ACCESS_TOKEN_FILEPATH)                                                                                                                                                                                               |    No     |                                        -                                        | - |
| API.LRO.STATUS_CHECK_INTERVAL                 | Used for `call_lro_api` method to determine polling interval between status checks.  <br /> The value can be overridden using `status_check_interval` parameter for call_lro_api method  <br /> (ASDK_API__LRO__STATUS_CHECK_INTERVAL)                                                                                             |    No     |                                  10 (seconds)                                   | - |
| API.LRO.STATUS_CHECK_TIMEOUT                  | Used for `call_lro_api` method to determine timeout for status checks.  <br /> The value can be overridden using `timeout` parameter for call_lro_api method  <br /> (ASDK_API__LRO__STATUS_CHECK_TIMEOUT)                                                                                                                         |    No     |                                  300 (seconds)                                  | - |
| API.RETRY.STOP_AFTER_ATTEMPT                  | Retry up to certain amount of attempts for API retry logic. <br /> (ASDK_API__RETRY__STOP_AFTER_ATTEMPT)                                                                                                                                                                                                                           |    No     |                                        -                                        | - |
| API.RETRY.WAIT_FIXED                          | Wait time in seconds before retry for API retry logic. <br /> (ASDK_API__RETRY__WAIT_FIXED)                                                                                                                                                                                                                                        |    No     |                                        -                                        | - |
| API.RETRY.STOP_AFTER_DELAY                    | Retry up to certain amount of delay for API retry logic. <br /> (ASDK_API__RETRY__STOP_AFTER_DELAY)                                                                                                                                                                                                                                |    No     |                                        -                                        | - |
| ADC.CONNECTION_TYPE                           | Type of connector to use for Snowflake connection. Defaults to Snowflake's <br />  python connector, but users can choose to use Snowpark connection object as well. <br /> (ASDK_ADC__CONNECTION_TYPE)                                                                                                                            |    No     |                          `snowflake-connector-python`                           | `snowflake-connector-python` / `snowflake-snowpark-python` |
| ADC.CONN.AUTHENTICATOR                        | Snowflake connection authenticator type  <br /> (ASDK_ADC__CONN__AUTHENTICATOR)                                                                                                                                                                                                                                                    |    No     |                                      `oauth`                                    | `oauth` / `snowflake_jwt` |
| ADC.CONN.OAUTH.ACCESS_TOKEN                   | If using oauth authenticator, and not relying on TokenAPI, users can provide <br />  the oauth access token for ADC connections here. <br /> (ASDK_ADC__CONN__OAUTH__ACCESS_TOKEN)                                                                                                                                                 |    No     |                                        -                                        | - |
| ADC.CONN.RSA.PRIVATE_KEY_FILEPATH             | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is path to file containing RSA private key.  <br /> Should be provided with passphrase. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY_FILEPATH)                                                                                                   |    No     |                                        -                                        | - |
| ADC.CONN.RSA.PRIVATE_KEY_PASSPHRASE           | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is passphrase to be used to decrypt private key file.  <br /> Should be provided with private key file path. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY_PASSPHRASE)                                                                            |    No     |                                        -                                        | - |
| ADC.CONN.RSA.PRIVATE_KEY                      | If using snowflake_jwt authenticator, provide RSA key details.  <br /> This attribute is the private key value itself.  <br /> Can be used instead of private key filepath and passphrase combination. <br /> (ASDK_ADC__CONN__RSA__PRIVATE_KEY)                                                                                   |    No     |                                        -                                        | - |
| ADC.CONN.ACCOUNT                              | Snowflake Account, used to create private URL for connection.  <br /> Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__ACCOUNT)                                                                                                                                                                                         |    No     |                                        -                                        | - |
| ADC.CONN.ROLE                                 | Snowflake user role to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__ROLE)                                                                                                                                                                                                                                  |    No     |                                        -                                        | - |
| ADC.CONN.WAREHOUSE                            | Snowflake virtual warehouse to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__WAREHOUSE)                                                                                                                                                                                                                     |    No     |                                        -                                        | - |
| ADC.CONN.DATABASE                             | Snowflake database to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__DATABASE)                                                                                                                                                                                                                               |    No     |                                        -                                        | - |
| ADC.CONN.SCHEMA                               | Snowflake schema to be used. Mandatory only for ADC connections. <br /> (ASDK_ADC__CONN__SCHEMA)                                                                                                                                                                                                                                   |    No     |                                        -                                        | - |
| ADC.RETRY.STOP_AFTER_ATTEMPT                  | Retry up to certain amount of attempts for ADC retry logic. <br /> (ASDK_ADC__RETRY__STOP_AFTER_ATTEMPT)                                                                                                                                                                                                                           |    No     |                                        -                                        | - |
| ADC.RETRY.WAIT_FIXED                          | Wait time in seconds before retry for ADC retry logic. <br /> (ASDK_ADC__RETRY__WAIT_FIXED)                                                                                                                                                                                                                                        |    No     |                                        -                                        | - |
| ADC.RETRY.STOP_AFTER_DELAY                    | Retry up to certain amount of delay. for ADC retry logic  <br /> (ASDK_ADC__RETRY__STOP_AFTER_DELAY)                                                                                                                                                                                                                               |    No     |                                        -                                        | - |
| USER_CREDENTIALS.USERNAME                     | User name to be used to connect to Aladdin. <br /> (ASDK_USER_CREDENTIALS__USERNAME)                                                                                                                                                                                                                                               |    Yes    |                                        -                                        | - |
| USER_CREDENTIALS.PASSWORD                     | User password to be used to connect to Aladdin.  <br /> Not mandatory, SDK will defer to USER_CREDENTIALS.PASSWORD_FILEPATH value. <br />  Alternatively, if running in local mode, will use OS credential manager for storing password. <br /> (ASDK_USER_CREDENTIALS__PASSWORD)                                                  |    No     |                                        -                                        | - |
| USER_CREDENTIALS.PASSWORD_FILEPATH            | Filepath pointing to file storing user's password in plain text (NOT RECOMMENDED).  <br /> Not mandatory if password provided in plain text in  <br /> USER_CREDENTIALS.PASSWORD setting (NOT RECOMMENDED), or if running in local mode. <br /> (ASDK_USER_CREDENTIALS__PASSWORD_FILEPATH)                                         |    No     |                                        -                                        | - |
| USER_CREDENTIALS.ENCRYPTED_PASSWORD_FILEPATH  | Filepath pointing to file storing user's password in encrypted format.  <br /> If encryption_filepath not provided, then default encryption key will be used.  <br /> Not mandatory if password provided in plain text in  <br /> USER_CREDENTIALS.PASSWORD setting (NOT RECOMMENDED), or if running in local mode. <br /> (ASDK_USER_CREDENTIALS__ENCRYPTED_PASSWORD_FILEPATH)  |    No     |                                        -                                        | - |
| USER_CREDENTIALS.ENCRYPTION_FILEPATH          | Filepath pointing to file storing encryption key used for password encryption/decryption.  <br /> Not mandatory. If provided, will be used in conjunction with  <br /> USER_CREDENTIALS.PASSWORD_FILEPATH to get user password for API connections. <br /> (ASDK_USER_CREDENTIALS__ENCRYPTION_FILEPATH)                            |    No     |                                        -                                        | - |
| LOG_LEVEL                                     | Log level to be set during execution. Value picked initially at any aladdinsdk module import. <br /> (ASDK_LOG_LEVEL)                                                                                                                                                                                                              |    No     |                                      INFO                                       | DEBUG / INFO / WARNING / ERROR / CRITICAL |
| EXPORT.OVERWRITE_DATA                         | Config value to be used when exporting to a file that already has data.  <br /> Value picked when user uses export utility to export data to file  <br /> (ASDK_EXPORT__OVERWRITE_DATA)                                                                                                                                            |    No     |                                      False                                      | True / False  
| NOTIFICATIONS.EMAIL.EMAIL_HOST                | Config value to be used for setting the email host.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_HOST)                                                                                                                                                  |    No     |                                        -                                        | Valid email host
| NOTIFICATIONS.EMAIL.EMAIL_USERNAME            | Config value to be used for setting the email login username.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_USERNAME)                                                                                                                                    |    No     |                                        -                                        | User email username
| NOTIFICATIONS.EMAIL.EMAIL_PASSWORD            | Config value to be used for setting the email login password.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__EMAIL_PASSWORD)                                                                                                                                    |    No     |                                        -                                        | User email password
| NOTIFICATIONS.EMAIL.TO                        | List of recipients the user wants to send email notifications to in the sdk.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__TO)                                                                                                                                 |    No     |                                        -                                        | List of recipients
| NOTIFICATIONS.EMAIL.SENDER                    | Config value to be used for setting the sender email value.  <br /> Value picked when user uses email notification utility to send emails  <br /> (ASDK_NOTIFICATIONS__EMAIL__SENDER)                                                                                                                                              |    No     |                                        -                                        | User sender email
| ERROR_HANDLING.EMAIL_NOTIFICATIONS.ENABLED    | Config value used to enable error email notifications in the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING__EMAIL_NOTIFICATIONS__ENABLED)                                                                                                                                    |    No     |                                        -                                        | True / False
| ERROR_HANDLING.EMAIL_NOTIFICATIONS.TO         | List of recipients the user wants to send an error email notifications to in the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING__EMAIL_NOTIFICATIONS__TO)                                                                                                                     |    No     |                                        -                                        | List of recipients
| ERROR_HANDLING. <br/>&nbsp; EMAIL_NOTIFICATIONS.ON_EXCEPTION_TYPES  | List of exceptions for which to send email notifications to users related to the sdk.  <br /> Value checked when error occurs in the SDK  <br /> (ASDK_NOTIFICATIONS__ERROR_HANDLING__EMAIL_NOTIFICATIONS__ON_EXCEPTION_TYPES)                                                                               |    No     |                                        -                                        | List of exceptions

**Note:**
- Any of the configurations can be overridden by setting environment variables prefixed with "ASDK_" (e.g. to override `mode`, set an environment variable `ASDK_MODE`)
- For nested keys, use dunder, i.e. double underscore, to denote access to nested elements (e.g. to override `api.token`, set an environment variable `ASDK_API__TOKEN`)

### Sample files

- Sample YAML configuration make API calls (OAuth):
  ```yaml
  RUN_MODE: local
  API:
    AUTH_TYPE: "OAuth"
    OAUTH:
      ACCESS_TOKEN: <access token for API calls>
  USER_CREDENTIALS:
    USERNAME: <user name>
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


## Core Features

### AladdinAPI

AladdinSDK provides an API client `AladdinAPI` which wraps over OpenAPI generated python client code based on Aladdin Graph API's swagger specifications.

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

### ADC Client

ADC (Snowflake) access is provided via the ADCClient. This is a wrapper around snowflake-connector-python or snowflake-snowpark-python (connection type is configurable).

The ADC Client provides the following capabilities:
- Authentication: Using 'oauth' or 'snowflake_jwt' (i.e. RSA Keys) authenticator types for snowflake connectors
- Session management:
    - connection establish, close, re-connect
    - update role, database, schema, warehouse

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

#### ADC Connection Authentication Types

##### OAuth

In the above simple example, ADCClient will attempt to fetch an OAuth AccessToken from Aladdin's TokenAPI.
Here, the assumptions are:
- User has provided API connection details as part of the configuration or ADCClient initialization.
- User has authenticated with the ADC OAuth client application by logging into Aladdin Studio UI.

##### RSA Keys

In this type, the user is required to follow steps to generate keys in PEM format.

1. Generate a private-public key pair under 'Keys' directory. Note: Remember the `passphrase` entered during these steps:

    ```sh
    mkdir Keys
    cd Keys
    openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8
    openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
    ```

2. From Snowflake UI, call Stored Procedure to append the public key to Aladdin user account:

    ```sql
    CALL ALADDIN.PUBLIC.UPDATE_PUB_KEY_SP('<Contents of rsa_key.pub file without BEGIN/END line>','KEY1');
    ```

3. Using the AladdinSDK configurations provide one of the following details:
    - Private Key value to be added to snowflake connection - ADC.CONN.RSA.PRIVATE_KEY   
    
    OR
    
    - Private key passphrase - ADC.CONN.RSA.PRIVATE_KEY_PASSPHRASE
    - Path to file containing private key file - ADC.CONN.RSA.PRIVATE_KEY_FILEPATH


### Utilities

#### Data Transformations

Data transformation is a common action performed on API responses. This utility aims to provide generic transformation capabilities via simple interface.

Currently supported transformations:

- JSON to Pandas Dataframe

Example [code snippet for data transformations](resources/sample_code_snippets/sample_data_transformations.py)

#### Data Exports

Exporting data to persistent storage helps store intermediate steps or final results to a file system.
Generic file formats exports currently supported:

- json
- csv
- xlsx
- pkl

Example [code snippet for data exports](resources/sample_code_snippets/sample_export_data_calls.md)

#### Notifications - Email

E-mail notification utility can be used to programmatically send emails
 
- User can enable email notifications by adding their email username, email password, email host and email sender values in the user config file under the `NOTIFICATIONS.EMAIL` section in user settings file
- As part of the email, the user can provide list of recipients, list of cc email ids, email subject, email body and attachments

Example [code snippet for email notifications](resources/sample_code_snippets/sample_send_email_notification.md)

#### Error Notifications - Email

The e-mail utility is additionally integrated with the error handling mechanism. This enables users to receive emails for any exceptions that may occur while executing their scripts / scheduled jobs.
 
- User can enable email notifications on errors by setting `NOTIFICATIONS.EMAIL` and `ERROR_HANDLING.EMAIL_NOTIFICATIONS` sections in user settings file
- For more details refer to the supported configuration table above

#### Error handler registration
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


## DomainSDK Development

Teams interested in building their business specific SDKs can build on top of AladdinSDK.
Core AladdinSDK provides generic solutions for SDK development, so DomainSDK developers can focus on specific business IP. DomainSDK users have access to all the aforementioned configurations, utilities and mechanisms.

### Configurations
- DomainSDK developers can fix/lock out certain configurations as needed
- (TBD) DomainSDK developers can add additional configurable options

### Error Handlers
- Where applicable, DomainSDK developers can add bespoke Error Codes by raising a PR to this repository
- Error handler registration can be done as mentioned above.


## Contributing

Guidelines for contributing to the project:
  - [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
  - [CONTRIBUTING.md](./CONTRIBUTING.md)
  - [Adding an Aladdin Graph API](./APIOnboardingCodegen.md)

## License

The license for the project:
  - [LICENSE](./LICENSE)

## Credits

Core Contributors:
- Vedant Naik
- Harshita Das
- Eli Kalish
- Infant Vasanth

Special Thanks:
- Mike Bowen
- Ginsiu Cheng
- Oleg Zakrevskiy
- David Li
- Anilkumar Mabagapu

Libraries:
- [Dynaconf](https://www.dynaconf.com/)
- [Tencity](https://tenacity.readthedocs.io/en/latest/)

Resources:
- Aladdin Graph APIs
- Aladdin Data Cloud

## Contact

Contact information for questions or feedback.
