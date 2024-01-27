from aladdinsdk.config.asdkconf import AsdkConf, dynamic_asdk_config_reload

# Path to configurations in internal settings
_conf_key_internal_api_allow_list = "CODEGEN_API_SETTINGS.ALLOW_LIST"


# Internal API allow list
@dynamic_asdk_config_reload
def get_api_allow_list():
    return AsdkConf.get(_conf_key_internal_api_allow_list)
