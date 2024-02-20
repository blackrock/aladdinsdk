# Error Handler Registration

## Sample domain specific exception

This is an example of an exception class defined in your code. 
The class type is added to a "supported exception modules" list in the handler, as shown later in this document.

Note: An existing exception type can also be added here, but may result in other registered handlers to match for raised exceptions. Therefore, it is recommended that domain SDK developers define their own exception classes where needed.

```py
class DomainException(Exception):
    def __init__(self, message="Domain Exception", *args: object) -> None:
        self.message = message
        super().__init__(self.message, *args)
```

## Create Exception Handler

Handler classes must extend `AbstractAsdkExceptionHandler`.
As part of this:
- Provide list of exceptions that will be handled by this handler
- original_exception - will be set by AladdinSDK's exception handler framework when a handled exception is raised
- Error code - DomainSDK developers can use the generic error code (004) for Domain SDK errors, or request adding a new code via a pull request to AladdinSDK repository
- Handle error - this method is called with the raised exception. Domain sdk developers should write meaningful handler logic here.

```py
from aladdinsdk.common.error.handlers.abstract import AbstractAsdkExceptionHandler, AsdkErrorCode
from domainpkg.common.error.domainerrors import DomainException

class DomainExceptionHandler(AbstractAsdkExceptionHandler):
    supported_exception_modules = [
        DomainException,
    ]
    
    original_exception = None
    
    error_code = AsdkErrorCode.AE004
    
    def __init__(self, original_exception):
        self.original_exception = original_exception
    
    def handle_error(self):
        # Developers to add specific logic here to handle exceptions
        print(f"{self.original_exception} occurred. Error code {self.error_code}")

```

## Register Exception Handler

Registration of exception handler to be done at import, such that handlers are available as soon as user imports SDK library

```py
from aladdinsdk.common.error import handler
handler.register_handler_class(DomainExceptionHandler)
```

## Decorator

Decorate any method with the `asdk_exception_handler` decorator.
With this addition, all raised exceptions are checked in the decorator and mapped to appropriate handlers.

Most AladdinSDK core utility and API-ADC wrapper methods are similarly decorated.

```py
from aladdinsdk.common.error import handler

@handler.asdk_exception_handler
def domain_func():
    import random
    if random.randint(1, 2) == 1:
        raise DomainException("Sample exception")
```

## Important Notes
- Follow best practices for error handling
- Do not silence errors, provide meaningful logs at the very least.
- Do not add same exception in two separate error handler's support_exception_modules list
- Be mindful of AladdinSDK's internal error handlers
