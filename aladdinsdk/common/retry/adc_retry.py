from aladdinsdk.config import user_settings
from aladdinsdk.common.retry.utils import create_retry_decorator, create_retry_wait_strategy, create_retry_stop_strategy

_adc_retry_wait = create_retry_wait_strategy(user_settings.get_adc_retry_wait_fixed())

_adc_retry_stop = create_retry_stop_strategy(user_settings.get_adc_retry_stop_after_delay(), user_settings.get_adc_retry_stop_after_attempt())
    
adc_retry = create_retry_decorator(_adc_retry_wait, _adc_retry_stop)
