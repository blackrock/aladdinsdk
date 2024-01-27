from aladdinsdk.api import AladdinAPI
from aladdinsdk.config.asdkconf import dynamic_asdk_config_reload
from aladdinsdk.common.error.asdkerrors import AsdkAdcException


@dynamic_asdk_config_reload
def fetch_adc_connection_access_token(adc_connection_kwargs):
    """
    Fetches ADC connection access token from AccessTokenService

    Args:
        adc_connection_kwargs (_type_): Connection parameters set during ADC client initialization, inflated to include API call parameters

    Raises:
        AsdkAdcException: _description_

    Returns:
        string: OAuth access token for ADC connection
    """
    token_api_instance = AladdinAPI('TokenAPI', **adc_connection_kwargs)
    generate_token_response = token_api_instance.call_api('token_api_generate_token', application_name='studio')
    if not hasattr(generate_token_response, 'access_token'):
        raise AsdkAdcException("Unable to generate ADC connection due to missing refresh_token in TokenAPI response")
    adc_oauth_access_token = (generate_token_response.access_token).strip()
    return adc_oauth_access_token
