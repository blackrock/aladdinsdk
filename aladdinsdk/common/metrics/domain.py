from aladdinsdk.common.error.asdkerrors import AsdkApiException, AsdkAdcException
from aladdinsdk.api.client import update_domain_sdk_user_agent_suffix
from aladdinsdk.adc.client import update_domain_sdk_query_tag_suffix
import logging

_logger = logging.getLogger(__name__)


def update_domain_sdk_metrics_suffix(domain_sdk_suffix):
    try:
        update_domain_sdk_user_agent_suffix(domain_sdk_suffix)
        update_domain_sdk_query_tag_suffix(domain_sdk_suffix)
    except (AsdkApiException, AsdkAdcException) as e:
        _logger.error(f"Invalid domain SDK suffix provided: '{domain_sdk_suffix}'. Error: {e}")
