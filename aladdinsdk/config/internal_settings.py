from aladdinsdk.config.asdkconf import AsdkConf, dynamic_asdk_config_reload

# Path to configurations in internal settings
## APIs
_conf_key_internal_api_allow_list = "CODEGEN_API_SETTINGS.ALLOW_LIST"

# Primary getters for SDK
@dynamic_asdk_config_reload
def get_api_allow_list():
    return AsdkConf.get(_conf_key_internal_api_allow_list)
