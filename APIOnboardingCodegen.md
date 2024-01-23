# AGraph API Code Generation Steps

This repository contains a utility to autogenerate python client code for APIs already onboarded to BlackRock's aladdin-graph project. The implementation is under `devutils/_utils_api_codegen.py`.

Reference aladdin-graph documentation - https://dev.azure.com/1A4D/AladdinGraph/_git/aladdin-graph?path=/.agraph/docs/docs/openapi_generated_client.md&_a=preview

## Pre-requisites:
- Checkout aladdin-graph git repo (https://dev.azure.com/1A4D/AladdinGraph/_git/aladdin-graph) 
- Install aladdin-graph tools (https://dev.blackrock.com/apps/aladdin-graph-docs/#/docs/getting_started?id=install-the-tooling)
    - Verify installation https://dev.blackrock.com/apps/aladdin-graph-docs/#/docs/getting_started?id=check-installation
- Setup openapi-generator:
    - Download openapi-generator-cli jar (specifically version 6.6.0) using: `wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O /<SOME LOCAL PATH>/openapi-generator-cli-6.6.0.jar --no-check-certificate`
    - Set `OPENAPI_GENERATOR_JAR_PATH` environment variable pointing to the downloaded jar: `export OPENAPI_GENERATOR_JAR_PATH=//<SOME LOCAL PATH>/openapi-generator-cli-6.6.0.jar`
  
  *NOTE: SDK is currently built around APIs generated with 6.6.0. Using any other version of the generator may result in incompatible client code*

    [Windows]
    - Download https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar to ~/Downloads folder 
    - Also optionally you can set the environment variable OPENAPI_GENERATOR_JAR_PATH with the JAR path
        - Powershell:
            ```ps
            $env:OPENAPI_GENERATOR_JAR_PATH="C:\Packages\Openapi-Generator-Cli\openapi-generator-cli.jar"
            ```
        - Bash:
            ```sh
            export OPENAPI_GENERATOR_JAR_PATH="C:\Packages\Openapi-Generator-Cli\openapi-generator-cli.jar"
            ```

## Usage

Currently `_util_api_codegen.py` supports two run modes - `onboard` an API to SDK or `delete` an API from SDK.
_**Note:**_ In case of a change to an existing API, simply `delete` the API and then `onboard` again.

### Onboarding an API:

To run the utility in `onboard` mode, you need:
- relative path to API proto file (relative from agraph-repo/defs)
- For Windows users, run this within git bash

Sample command:

```sh
python devutils/_util_api_codegen.py onboard -agr /Users/vnaik/workspace/ado/aladdin-graph -s reference_architecture/reference_architecture/demo/train_journey/v1/train_journey_api.proto
```

A successful util run on onboard mode executes the following steps:
- Generate swagger specification using API proto file and agraph tooling
    - `x-aladdin-spec-id` from the agraph generated swagger specification is used to get API Name and version
- Generate python client code in a temporary location using swagger spec file and openapi-generator jar. Following input parameters are given to openapi-generator cli:
    - API package name - generated using predefined path to codegen packages in SDK and the path to proto file. This puts the generated code under the appropriate target project structure
    - API name suffix - same as given API name. So generated code will have client named "Default<ApiName>"
- Merge the code section of the temporary location in the codegen section of sdk (this) repo. As part of this step, requirements.txt and swagger.json files are also stored under the target location.
- An entry is made in the `aladdinsdk/api/codegen/codegen_allow_list.yaml` file. All entries are always stored in alphabetical order for easy reference and reducing merge conflicts.

### Deleting an API:

To run the utility in `delete` mode, you need:
- Name of API (from allow list)
- Version of API to delete (from allow list)

Sample command:

```sh
python devutils/_util_api_codegen.py delete -dan TrainJourneyAPI -dav v1
```

For a successful run on delete mode following steps are performed:
- Script reads configuration of given API from `aladdinsdk/api/codegen/codegen_allow_list.yaml`. Using the module path information, all files and directories at that location are deleted.
- The entry from `aladdinsdk/api/codegen/codegen_allow_list.yaml` file is deleted. All entries are always stored in alphabetical order for easy reference and reducing merge conflicts.
