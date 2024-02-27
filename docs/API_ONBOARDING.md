# AGraph API Code Generation Steps

This repository contains a utility to autogenerate python client code using Aladdin Graph API Swagger specifications. The implementation is under `devutils/asdk_agraph_api_codegen.py`, and is invoked at build time.


## Pre-requisites:
- Python 3.9+
- API swagger specification files to perform code-generation on. Collection is maintained under `resources/api_specs`
- (optional) openapi-generator-cli jar  (specifically version 6.6.0)
    - If not provided using the optional `--openapi-generator-cli-jar` argument, the utility script will attempt to download the jar from `https://repo1.maven.org`
  
  *NOTE: SDK is currently built around APIs generated with 6.6.0. Using any other version of the generator may result in incompatible client code*

## Usage

- Add or remove API specification files under `resources/api_specs` directory
- Run `python devutils/asdk_agraph_api_codegen.py -osd resources/api_specs`
    - Optionally provide openapi-generator jar file using `--openapi-generator-cli-jar` arg
    - Add `-v` flag to run in verbose mode

### Note: A successful run of the script executes the following steps:

- `x-aladdin-spec-id` from the agraph generated swagger specification is used to get API Name and version and codegen module path
- Python client code is generated in a temporary location using swagger spec file and openapi-generator jar. Following input parameters are given to openapi-generator cli:
    - API package name - generated using predefined path to codegen packages in SDK and the path to proto file. This puts the generated code under the appropriate target project structure
    - API name suffix - same as given API name. So generated code will have client named "Default<ApiName>"
- Code section of the temporary location is merged in the codegen section of sdk (this) repo. As part of this step swagger.json files are also stored under the target location.
- An entry is made in the `aladdinsdk/api/codegen/codegen_allow_list.yaml` file. All entries are always stored in alphabetical order for easy reference and reducing merge conflicts.
