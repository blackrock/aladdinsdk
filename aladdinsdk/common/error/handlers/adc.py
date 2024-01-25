import logging

from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, AsdkErrorCode
from aladdinsdk.common.error.asdkerrors import AsdkAdcException

_logger = logging.getLogger(__name__)


class ADCExceptionHandler(AbstractAsdkExceptionHandler):  # e001
    """
    Exceptions raised by ADC wrapper

    Args:
        AsdkException (_type_): _description_
    """
    supported_exception_modules = [
        AsdkAdcException
        ]

    error_code = AsdkErrorCode.AE003

    original_exception = None

    def __init__(self, original_exception):
        self.original_exception = original_exception

    def handle_error(self):
        _logger.warning(f"Unhandled ADC Exception: {self.original_exception}")
        raise self.original_exception
