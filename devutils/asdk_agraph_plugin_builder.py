import os
import glob
import yaml
import subprocess
import tempfile
import json
import argparse
import platform
import pathlib

"""
Utility to onboard APIs to SDK
"""

# Run constants
_ASDK_PLUGIN_MODULE_PREFIX = "asdk_plugin_"
_openapi_generator_cli_version = "6.6.0"
_OPENAPI_GENERATOR_JAR_DOWNLOAD_LINK = f'https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/{_openapi_generator_cli_version}/openapi-generator-cli-{_openapi_generator_cli_version}.jar'  # noqa: E501
platform_os = platform.platform()
_ASDK_PLUGIN_BUILDER_REPO = os.getcwd()
if 'Windows' in platform_os:
    _ASDK_PLUGIN_BUILDER_REPO = pathlib.PureWindowsPath(os.getcwd()).as_posix()

_openapi_generator_jar_filepath = os.path.join(_ASDK_PLUGIN_BUILDER_REPO, 'resources', 'openapi-generator-cli.jar')


# Helper methods
def _run_command(command_array, message):
    """Given a command array, join with spaces and run.

    Args:
        command_array (_type_): Sequence of program arguments or else a single string. By default, the program to execute is the first item in
            args if args is a sequence. If args is a string, the interpretation is platform-dependent.
        message (_type_): Message to log what the command achieves
    """
    result = None
    platform_os = platform.platform()
    if 'Windows' in platform_os:
        if 'sudo' in command_array:
            command_array.remove('sudo')
        try:
            result = subprocess.run(command_array, stdout=subprocess.PIPE)
        except Exception:
            print(f"subprocess.run failed failed trying subprocess.run for {' '.join(command_array)}")
            os.system(" ".join(command_array))
    else:
        result = subprocess.run(command_array, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if _verbose:
        print(f"{message}: " + " ".join(command_array))

    if result is not None and hasattr(result, "returncode") and result.returncode == 0:
        return True
    else:
        print(result)
        return False


def _update_asdk_repo_codegen_section(api_name, api_version, api_module_path):
    """
    Method to update ASDK's codegen sections. Particularly codegen allow list yaml file.

    In case of delete operations, this method should be run with delete mode set to true. The method will then check
    the config file for an existing entry of given API name and delete that entry from the list. It will also delete all
    files under the codegen package referenced by the deleted entry.

    Args:
        delete_mode (bool, optional): Run update method in delete mode. Defaults to False.
    """
    __codegen_api_allow_list_path = "aladdinsdk/api/codegen/codegen_allow_list.yaml"

    # Load the YAML file into a Python dictionary
    _codegen_api_allow_list = {'CODEGEN_API_SETTINGS': {'ALLOW_LIST': []}}
    if os.path.exists(__codegen_api_allow_list_path):
        with open(__codegen_api_allow_list_path, "r") as file:
            _codegen_api_allow_list = yaml.safe_load(file)

    # Update the entry in the dictionary
    _filtered_api_list = [x for x in _codegen_api_allow_list['CODEGEN_API_SETTINGS']['ALLOW_LIST'] if x['api_name'] != api_name]

    # i.e. if running in onboard mode, append new api entry to file
    api_swagger_target_location = os.path.join(*api_module_path.split('.'))
    with open(f"{api_swagger_target_location}/swagger.json", "r") as file:
        _target_swagger_json = json.load(file)

    _filtered_api_list.append({
        'api_module_path': api_module_path,
        'api_name': api_name,
        'api_version': api_version,
        'host_url_path': _target_swagger_json['basePath']
    })

    # Always keep the autogenerated config list in sorted order of api_name
    _filtered_api_list = sorted(_filtered_api_list, key=lambda x: x['api_name'])
    _codegen_api_allow_list['CODEGEN_API_SETTINGS']['ALLOW_LIST'] = _filtered_api_list

    # Write the updated dictionary back to the YAML file
    with open(__codegen_api_allow_list_path, "w") as file:
        file.write("######################################################.\n")
        file.write("# THIS FILE IS AUTO-GENERATED. DO NOT UPDATE MANUALLY.\n")
        file.write("# For local testing developers need to run codegen utility \n")
        file.write("# as described in contribution guidelines.\n")
        file.write("######################################################.\n")
        yaml.dump(_codegen_api_allow_list, file)
    print("Registry settings file updated.")


def _generate_target_api_details_from_agraph_swagger_spec(agraph_swagger_file_path):
    """Given path to an Aladdin Graph swagger file, read API name, version and generate module path from 'info.x-aladdin-spec-id'.
    Assumption here is x-aladdin-spec-id is of the format 'agraph.<domain>.<segment>.<api>.<VERSION>.<API_NAME>'

    Args:
        agraph_swagger_file_path (FileDescriptorOrPath): Path to swagger file for API to onboard

    Raises:
        Exception: _description_

    Returns:
        api_name, api_version, api_module_path: name and version of the API from x-aladdin-spec-id, and target module path for the API
    """
    try:
        with open(agraph_swagger_file_path, "r") as file:
            swagger_json_data = json.load(file)
            x_aladdin_spec_id = swagger_json_data['info']['x-aladdin-spec-id']
            spec_id_split = x_aladdin_spec_id.split('.')
            if spec_id_split[0] == "agraph":
                spec_id_split.pop(0)

            api_name = spec_id_split.pop()
            api_ver = spec_id_split.pop()
            api_module_path = ".".join(['aladdinsdk', 'api', 'codegen', *spec_id_split])
            return api_name, api_ver, api_module_path
    except KeyError:
        raise Exception("Incorrect swagger file encountered. "
                        "Info section needs to have 'x-aladdin-spec-id' to help identify API name, version and module path")
    except IndexError:
        raise Exception("Insufficient or incorrect value for x-aladdin-spec-id. "
                        "Expecting following format: agraph.<domain name>.<segement name>.<api group>.<version>.<API Name>")
    except Exception as e:
        print("unexpected error", e)
        return None, None, None


def _onboard_api_using_swagger(path_to_agraph_openapi_spec_file):
    """Given a path to agraph swagger file, uses openapi-codegen to create a python client and copy code into target module
    - Creates a temporary python client project
    - Rsync and copies code, swagger and requirements files under given target location
    - Updates api list configuration file

    Args:
        path_to_agraph_openapi_spec_file (_type_): Absolute path to a agraph swagger file to be used for codegen

    Returns:
        tuple: API Name-Version, Generated APIs target module
    """
    api_name, api_ver, api_module_path = _generate_target_api_details_from_agraph_swagger_spec(path_to_agraph_openapi_spec_file)
    if api_name is None or api_ver is None or api_module_path is None:
        raise Exception("Insufficient API information in swagger files")

    # using api_module_path, generate target API location
    target_api_directory = os.path.join(*api_module_path.split('.'))

    print(f"Onboarding API - {api_name}-{api_ver}.")
    is_successful = True

    # create a temporary codegen repo
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f'[API: {api_name}-{api_ver}] - created temporary directory', temp_dir)
        if 'Windows' in platform_os:
            temp_dir = pathlib.PureWindowsPath(temp_dir).as_posix()
            print(f'[API: {api_name}-{api_ver}] - windows updated temporary directory', temp_dir)

        python_codegen_command = ["java", "-jar", _openapi_generator_jar_filepath, "generate",
                                  "-i", path_to_agraph_openapi_spec_file,
                                  "-g", "python-nextgen",
                                  "-o", temp_dir,
                                  "--package-name", api_module_path,
                                  "--api-name-suffix", api_name]
        is_successful = is_successful and _run_command(python_codegen_command,
                                                       message=f"[API: {api_name}-{api_ver}] - Generate python client code using swagger spec")

        is_successful = is_successful and _run_command(["rm", "-rf", target_api_directory],
                                                       message=f"[API: {api_name}-{api_ver}] - Remove existing codegen dir if present")
        is_successful = is_successful and _run_command(["mkdir", "-pv", target_api_directory],
                                                       message=f"[API: {api_name}-{api_ver}] - Create target directory for codegen")

        cp_command_swagger = ["cp", path_to_agraph_openapi_spec_file, os.path.join(target_api_directory, "swagger.json")]
        is_successful = is_successful and _run_command(cp_command_swagger,
                                                       message=f"[API: {api_name}-{api_ver}] - Copy swagger file under target directory")

        rsync_command = ["rsync", "-a", os.path.join(temp_dir, target_api_directory), target_api_directory]
        is_successful = is_successful and _run_command(rsync_command,
                                                       message=f"[API: {api_name}-{api_ver}] - Rsync python client code into sdk repo's "
                                                       "codegen package under newly created target directory")

    print(f"[API: {api_name}-{api_ver}] - Openapi codegen steps done successfully ({is_successful}). Proceeding with ASDK updates...")
    _update_asdk_repo_codegen_section(api_name=api_name, api_version=api_ver, api_module_path=api_module_path)

    if is_successful:
        print(f"[API: {api_name}-{api_ver}] - API Onboarding complete. Result: 'success'")
    else:
        print(f"[API: {api_name}-{api_ver}] - API Onboarding complete. Result: 'fail/partial-success'")
    return f"{api_name}-{api_ver}"


def _build_api_with_swagger_files(api_swagger_files):
    """Given paths to swagger files that need to be packaged into the plugin and the target location details, use openapi-generator
    to generate python clients in a temporary location, and copy python code modules into target location under the similar
    domain/segment/api structure. Return list of completed APIs and skipped APIs (with error/reasons for skipping)

    Args:
        api_swagger_files (_type_): _description_

    Returns:
        _type_: _description_
    """
    completed_apis_to_spec_map = {}
    skipped_api_specs_to_reason_map = {}

    for api_swagger_file in api_swagger_files:
        try:
            completed_api = _onboard_api_using_swagger(api_swagger_file)
            completed_apis_to_spec_map[completed_api] = api_swagger_file
        except Exception as e:
            skipped_api_specs_to_reason_map[api_swagger_file] = str(e)

    return completed_apis_to_spec_map, skipped_api_specs_to_reason_map


def add_api_to_asdk(api_swagger_files):
    """Generate plugin and return execution summary for this domain.
    Add supplementary files for plugin artifacts:
        api_registry.py - To help AladdinSDK understand available APIs in this domain library
        setup.py - For plugin installation. Details in setup.py are updated for the plugin

    Args:
        api_swagger_files (_type_): _description_
        plugin_name (_type_): _description_

    Returns:
        _type_: execution summary map entires for this domain
    """
    # generate domain plugin
    _completed_apis_to_spec_map, _skipped_api_specs_to_reason_map = _build_api_with_swagger_files(api_swagger_files)

    print(f"Completed with {len(_completed_apis_to_spec_map)} API codegen runs.")
    print_run_summary(_completed_apis_to_spec_map, _skipped_api_specs_to_reason_map)


def _summary_helper_split_skipped_map(_skipped_api_specs_to_reason_map):
    _skipped_due_to_errors = {}
    _skipped_due_to_filtering = {}
    for x in _skipped_api_specs_to_reason_map:
        skip_note = _skipped_api_specs_to_reason_map[x]
        if skip_note == "Filtered out":
            _skipped_due_to_filtering[x] = skip_note
        else:
            _skipped_due_to_errors[x] = skip_note
    return _skipped_due_to_errors, _skipped_due_to_filtering


def print_run_summary(_completed_apis_to_spec_map, _skipped_api_specs_to_reason_map):
    print("\n==========================")
    print("FINAL SUMMARY")
    print("==========================")
    _skipped_due_to_errors, _skipped_due_to_filtering = _summary_helper_split_skipped_map(_skipped_api_specs_to_reason_map)

    if _verbose:
        print(f"Summary: [completed: {len(_completed_apis_to_spec_map)}, "
              f"skipped due to errors: {len(_skipped_due_to_errors)}, filtered out: {len(_skipped_due_to_filtering)}]")
        if len(_completed_apis_to_spec_map) > 0:
            print("\nCompleted APIs:")
            [print(f"{x} - {_completed_apis_to_spec_map[x]}") for x in _completed_apis_to_spec_map]
        if len(_skipped_due_to_errors) > 0:
            print("\nSkipped due to errors APIs:")
            [print(f"{x} - {_skipped_due_to_errors[x]}") for x in _skipped_due_to_errors]
        print("------------------------------------")
    else:
        if len(_completed_apis_to_spec_map) > 0 or len(_skipped_due_to_errors) > 0:
            print(f"Summary: [completed: {len(_completed_apis_to_spec_map)}, "
                  f"skipped due to errors: {len(_skipped_due_to_errors)}, filtered out: {len(_skipped_due_to_filtering)}]")
            print(f"\nCompleted APIs: {[x for x in _completed_apis_to_spec_map]}")
            print("------------------------------------")


# --------------------------------------------------- start ---------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ASDK Codegen Util", description="Utility to generate python clients for aladdin-graph APIs")
    parser.add_argument('-osd', '--openapi-spec-dir', help="AGraph generated Swagger specifications", required=True)
    parser.add_argument('-oj', '--openapi-generator-cli-jar', help="(Optional) Path to openapi-generator-cli jar. If not provided, "
                        f"script will attempt to get from {_OPENAPI_GENERATOR_JAR_DOWNLOAD_LINK}")
    parser.add_argument('-v', '--verbose', help="(Optional) More verbose summary", action='store_true', default=True)

    # Read input args
    args = parser.parse_args()
    print(f"Run args: {args}")

    # source from swagger gen
    _openapi_spec_dir = args.openapi_spec_dir
    # generator jar
    _custom_openapi_generator_jar_filepath = args.openapi_generator_cli_jar
    # filters
    _verbose = args.verbose

    # Get openapi-generator jar file. If path provided via input args, use that instead.
    if _custom_openapi_generator_jar_filepath is not None:
        _openapi_generator_jar_filepath = _custom_openapi_generator_jar_filepath
    else:
        if not pathlib.Path(_openapi_generator_jar_filepath).exists():
            _run_command(['wget', _OPENAPI_GENERATOR_JAR_DOWNLOAD_LINK, '-O', _openapi_generator_jar_filepath, '--no-check-certificate'],
                         message="Get openapi-generator jar")

    # Run plugin builder logic for each key in run config map. Create method responds with completed/skipped APIs within the plugin build.
    # Add these details to a summary map that will be printed out at the end of execution
    summary_map = {}
    api_swagger_files = glob.glob(f"{_openapi_spec_dir}/*.json")
    add_api_to_asdk(api_swagger_files)
