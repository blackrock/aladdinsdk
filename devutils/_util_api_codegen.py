import os
import re
import sys
import subprocess
import tempfile
import yaml
import json
import argparse
import platform
import pathlib

"""
Utility to onboard APIs to SDK (v1)

Pre-requisites:
    - checkout and setup aladdin-graph repository
    - python 3.9
    - bash
    - openapi-generator v6.3.0+

Sample invocation:
    - Onboarding new API  / Re-creating existing API:
        python _util_api_codegen.py onboard UserGroup -agr /Users/vnaik/workspace/ado/aladdin-graph -s platform/platform/access/user_group/v1/user_group_api.proto
        python _util_api_codegen.py onboard TrainJourney -agr /Users/vnaik/workspace/ado/aladdin-graph -s reference_architecture/reference_architecture/demo/train_journey/v1/train_journey_api.proto
    - Delete previously onboarded API:
        python _util_api_codegen.py delete TrainJourney
"""

# Helper methods
def _run_command(command_array, message=None):
    print("\n")
    platform_os = platform.platform()
    if 'Windows' in platform_os:
        if 'sudo' in command_array:
            command_array.remove('sudo')
        try:
            command_res = subprocess.run(command_array, stdout=subprocess.PIPE).stdout.decode('utf-8')
        except Exception as e:
            print(f"subprocess.run failed failed trying subprocess.run for {' '.join(command_array)}")
            command_res = os.system(" ".join(command_array))
    else: 
        command_res = subprocess.run(command_array, stdout=subprocess.PIPE).stdout.decode('utf-8')

    if message is not None: print(f"Command to: {message}")
    print(" ".join(command_array))
    print(command_res)

def _helper_delete_api_codegen(api_entry_to_delete):
    """
    Helper function to delete API codegen pieces and tidy up any empty modules/packages

    Args:
        api_entry_to_delete (_type_): API entry from allow list yaml file
    """
    _existing_api_code_gen_path = api_entry_to_delete["api_module_path"].replace(".", "/")
    _run_command(["rm", "-rf", _existing_api_code_gen_path], message="Deleting codegen files from ASDK repo.")
    print("Verify changes and confirm appropriate codegen packages are deleted from ASDK repo.")
    
    # After deleting an API under a domain & segment, we need to make sure any empty 
    # directories at domain/segment level are also cleared if no other API is present.
    # For this, travel back from leaf node of the file path and delete directories 
    # which only effectively have "__init__.py" and "__pycache__".
    _clean_up_path = _existing_api_code_gen_path
    while _clean_up_path != os.path.join('aladdinsdk', 'api', 'codegen'):
        if os.path.exists(_clean_up_path):
            dir_contents = os.listdir(_clean_up_path)
            if (len(dir_contents) == 1 and dir_contents[0] == '__init__.py') or \
                (len(dir_contents) == 2 and '__init__.py' in dir_contents and '__pycache__' in dir_contents):
                _run_command(["rm", "-rf", _clean_up_path], message="Clean up empty python module.")
                _clean_up_path = os.sep.join(_clean_up_path.split(os.sep)[:-1])
            else:
                # path contains something other than just init, so it has other APIs. Abort.
                break
        else:
            _clean_up_path = os.sep.join(_clean_up_path.split(os.sep)[:-1])

def _update_asdk_repo_codegen_section(api_name, api_version, delete_mode=False):
    """
    Method to update ASDK's codegen sections. Particularly codegen allow list yaml file.
    
    In case of delete operations, this method should be run with delete mode set to true. The method will then check
    the config file for an existing entry of given API name and delete that entry from the list. It will also delete all
    files under the codegen package referenced by the deleted entry.

    Args:
        delete_mode (bool, optional): Run update method in delete mode. Defaults to False.
    """
    os.chdir(__asdk_repo)
    print("Confirm/Navigate to working directory is aladdin-sdk repo. Commencing registry settings file updates...")    
    
    # Load the YAML file into a Python dictionary
    _codegen_api_allow_list = {'CODEGEN_API_SETTINGS': {'ALLOW_LIST': []}}
    if os.path.exists(__codegen_api_allow_list_relative_path):
        with open(__codegen_api_allow_list_relative_path, "r") as file:
            _codegen_api_allow_list = yaml.safe_load(file)

    # Update the entry in the dictionary
    _existing_api_entry_list = [x for x in _codegen_api_allow_list['CODEGEN_API_SETTINGS']['ALLOW_LIST'] if x['api_name'] == api_name]
    _filtered_api_list = [x for x in _codegen_api_allow_list['CODEGEN_API_SETTINGS']['ALLOW_LIST'] if x['api_name'] != api_name]

    if delete_mode is True and len(_existing_api_entry_list) > 0:
        _api_entry_to_delete = [ae for ae in _existing_api_entry_list if ae['api_version'] == api_version][0]
        _helper_delete_api_codegen(_api_entry_to_delete)
    elif delete_mode is True and len(_existing_api_entry_list) == 0:
        print("API selected for deletion does not have an entry in config file. Confirm if code is appropriately deleted form codegen package.")
    else:
        # i.e. if running in onboard mode, append new api entry to file
        with open(f"{__target_api_directory}/swagger.json", "r") as file:
            _target_swagger_json = json.load(file)
        
        _filtered_api_list.append({
            'api_module_path': __target_api_module_import,
            'api_name': api_name,
            'api_version': api_version,
            'host_url_path': _target_swagger_json['basePath']
        })

    # Always keep the autogenerated config list in sorted order of api_name
    _filtered_api_list = sorted(_filtered_api_list, key=lambda x: x['api_name'])
    _codegen_api_allow_list['CODEGEN_API_SETTINGS']['ALLOW_LIST'] = _filtered_api_list

    # Write the updated dictionary back to the YAML file
    with open(__codegen_api_allow_list_relative_path, "w") as file:
        file.write("######################################################.\n")
        file.write("# THIS FILE IS AUTO-GENERATED. DO NOT UPDATE MANUALLY.\n")
        file.write("# For local testing developers need to run codegen utility \n")
        file.write("# as described in contribution guidelines.\n")
        file.write("######################################################.\n")
        yaml.dump(_codegen_api_allow_list, file)
    print("Registry settings file updated.")

def _onboard_api():
    """    
    - Creates a temporary python client project
    - Rsync and copies code, swagger and requirements files under given target location
    - Updates api allow list configuration file
    """
    if __path_to_openapi_spec_file is None:
        os.chdir(__agraph_repo_path)
        print("Navigated to AGraph Repo")

        _run_command(["sudo", "agraph", "version"], message="Confirm agraph version.")

        create_swagger = ["sudo", "agraph", "generate", "swagger", "-s", "-i", f"defs/{__path_to_source_api_proto}"]
        _run_command(create_swagger, message=f"Create swagger spec for API. Will be available at {__agraph_gen_swagger_file_path}.")
    
    with open(__agraph_gen_swagger_file_path, "r") as file:
        swagger_json_data = json.load(file)
        x_aladdin_spec_id = swagger_json_data['info']['x-aladdin-spec-id']
        api_name = x_aladdin_spec_id.split('.')[-1:][0]
        api_ver = x_aladdin_spec_id.split('.')[-2:][:1][0]
    

    # create a temporary codegen repo
    with tempfile.TemporaryDirectory() as tdir:
        print('created temporary directory', tdir)
        
        if 'Windows' in platform_os:
            tdir = pathlib.PureWindowsPath(tdir).as_posix()
            print('windows updated temporary directory', tdir)
            local_api_generator_path = os.getenv('OPENAPI_GENERATOR_JAR_PATH', f"{pathlib.PureWindowsPath(os.path.expanduser('~')).as_posix()}/Downloads/openapi-generator-cli-6.3.0.jar")
        else:
            local_api_generator_path = os.getenv('OPENAPI_GENERATOR_JAR_PATH')
        
        if not pathlib.Path(local_api_generator_path).exists():
            print("Set environment variable OPENAPI_GENERATOR_JAR_PATH pointing to a supported version of openapi-generator jar. [6.6.0]")
            return
        
        print('local api generator path', local_api_generator_path)
        python_codegen_command = ["java", "-jar", local_api_generator_path, "generate", "-i", __agraph_gen_swagger_file_path, "-o", tdir, "-g", "python-nextgen", "--package-name", __target_api_module_import, "--api-name-suffix", api_name, "--strict-spec", "false"]
        _run_command(python_codegen_command, message="Generate python client code using swagger spec")

        _run_command(["rm", "-rf", __target_api_directory], message="Remove existing codegen dir if present")
        _run_command(["mkdir", "-pv", __target_api_directory], message="Create target directory for codegen")
        
        if 'Windows' in platform_os:
            rsync_command = ["cp", "-r", f"{tdir}/aladdinsdk/api/codegen/", __sdk_codegen_directory]
            _run_command(rsync_command, message="Rsync python client code into sdk repo's codegen package under newly created target directory")
        else:
            rsync_command = ["rsync", "-a", f"{tdir}/aladdinsdk/api/codegen/", __sdk_codegen_directory]
            _run_command(rsync_command, message="Rsync python client code into sdk repo's codegen package under newly created target directory")
        
        cp_command_requirements = ["cp", f"{tdir}/requirements.txt", f"{__target_api_directory}/requirements.txt"]
        _run_command(cp_command_requirements, message="Copy requirements file under target directory")
        
        cp_command_swagger = ["cp", f"{__agraph_gen_swagger_file_path}", f"{__target_api_directory}/swagger.json"]
        _run_command(cp_command_swagger, message="Copy swagger file under target directory")
    
    print("Openapi codegen steps completed. Proceeding with ASDK updates...")
    _update_asdk_repo_codegen_section(api_name=api_name, api_version=api_ver)
    
    print(f"API Onboarding complete for {api_name}")
        
################################################ start ################################################

if __name__ == "__main__":    
    
    # Constants
    _RUN_MODE_ONBOARD = "onboard"
    _RUN_MODE_DELETE = "delete"
    __codegen_api_allow_list_relative_path="aladdinsdk/api/codegen/codegen_allow_list.yaml"
    __asdk_repo=os.getcwd()
    platform_os = platform.platform()
    if 'Windows' in platform_os:
        __asdk_repo = pathlib.PureWindowsPath(os.getcwd()).as_posix()
        __sdk_codegen_directory = f"{__asdk_repo}/aladdinsdk/api/"
    else: 
        __sdk_codegen_directory = f"{__asdk_repo}/aladdinsdk/api/codegen"

    parser = argparse.ArgumentParser(prog="ASDK Codegen Util", description="Utility to help SDK developers onboard (or delete) APIs from aladdin-graph.")
    parser.add_argument('mode', help=f"Run mode for this program. Currently supports [{_RUN_MODE_ONBOARD}, {_RUN_MODE_DELETE}].")
    parser.add_argument('-oas', '--openapi-spec', help="(onboard mode - spec) Openapi Spec file path - to be used instead of agraph repo's proto file, for onboarding using a pre-existing swagger specification.")
    parser.add_argument('-agr', '--aladdin-graph-repo', help="(onboard mode - proto) AGraph Repo - Absolute path to aladdin-graph-repo checkout out locally.")
    parser.add_argument('-s', '--source-api-proto-path', help="(onboard mode - spec/proto) Source file - Relative path from aladdin-graph/defs to API proto file which needs to be onboarded.")
    parser.add_argument('-dan', '--delete-api-name', help="(delete mode) Name of API to delete.")
    parser.add_argument('-dav', '--delete-api-version', help="(delete mode) API version to delete.")
    
    args = parser.parse_args()

    # Read program arguments
    __codegen_util_run_mode = args.mode
    __delete_api_name = args.delete_api_name
    __delete_api_version = args.delete_api_version
    __path_to_openapi_spec_file = args.openapi_spec
    __agraph_repo_path = args.aladdin_graph_repo
    __path_to_source_api_proto = args.source_api_proto_path
    
    if __codegen_util_run_mode == _RUN_MODE_ONBOARD: # If run mode, derive additional constants needed for program execution
        __temp_str_splits = __path_to_source_api_proto.rsplit('_api.proto', 1)[0].split("/", 2)
        if __temp_str_splits[0] == __temp_str_splits[1]: # Most agraph API paths have duplicate domain/segment, which needs to be ignored
            __temp_str_splits.pop(0)
        __path_to_target_api_module = '/'.join(__temp_str_splits)

        # Derived constants for this run
        __agraph_gen_swagger_file_path = __path_to_openapi_spec_file if __path_to_openapi_spec_file is not None else f"gen/swagger/{__path_to_target_api_module}_api.swagger.json"
        __target_api_module_import=f"aladdinsdk.api.codegen.{__path_to_target_api_module.replace('/', '.')}"        
        __target_api_directory = f"{__asdk_repo}/aladdinsdk/api/codegen/{__path_to_target_api_module}"
        print("Onboarding a new API. (If previously created, client code will be regenerated.)")
        _onboard_api()
    elif __codegen_util_run_mode == _RUN_MODE_DELETE:
        print("Deleting an API and its registry entry")
        _update_asdk_repo_codegen_section(api_name=__delete_api_name, api_version=__delete_api_version, delete_mode=True)
    else:
        print("Incorrect run mode parameter given.")
        sys.exit(1)
