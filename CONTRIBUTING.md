# Contributing to AladdinSDK

Thank you for your interest in contributing to AladdinSDK! We welcome all contributions, big or small. To ensure that contributions are properly tracked and attributed, we require that all contributors sign off on their work using the Developer Certificate of Origin (DCO).

## What is the Developer Certificate of Origin?

The Developer Certificate of Origin (DCO) is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project. It is a simple statement that must be included in every Git commit message, indicating that the contributor accepts the DCO.

### How to Sign Off on Your Work

To sign off on your work, simply add the following line to the end of your Git commit message:

```bash
Signed-off-by: [Your Name] <[your email address]>
```

This indicates that you accept and agree to the DCO. You may include this line manually, or you can add it automatically by using the -s or --signoff option when committing:

```bash
git commit -s -m "Your commit message"
```

### Contributions without a Signed DCO

Contributions without a properly signed DCO cannot be accepted into the project. If you submit a contribution without a signed DCO, we will ask you to sign it before we can accept your contribution.

### Additional Resources

For more information about the Developer Certificate of Origin, please see the DCO 1.1 FAQ.

Thank you for your understanding and cooperation! We look forward to your contributions.

## Setting up this repository for contributing to AladdinSDK

- Clone the project locally:
  ```sh
  gh repo clone blackrock/aladdinsdk
  ```
- Create python venv. Ensure python virtual environment version is 3.9.
  ```
  python -m venv venv
  source venv/bin/activate
  ```
- Install dependencies
  ```sh
  pip install -r requirements.txt
  ```
- Set BlackRock's `defaultWebServer`

### Testing
- Ensure repository has at least 80% code coverage.
- Install `pytest`, `pytest-cov` and `coverage` via pip. Run the following command to check code coverage:
    ```sh
    pytest test/ --cov=aladdinsdk --cov-report= && coverage report -m
    ```

## General Development Guidelines 
- Use python 3.9+ (tested with 3.9.10)

### Styling 
- Follow PEP8, unless otherwise noted 

### Branching, versioning and releases

- Branch types:
    - `main`: Stable tested code 
    - `feat/` or `fix/`: Feature/fix branches for contributions

- Versions: Follow [semver](https://semver.org/) for versioning. Any pushed tag will trigger publish pipeline.

## SDK Folder Structure
The following section outlines the high-level SDK project folder structure:
 
    .
    ├── Project guidelines/documentations, requirements.txt and CI/CD pipelines
    ├── aladdinsdk: 
        ├── adc: adc client wrapper
        ├── api: api client wrapper
        ├── common: core utility and support modules
        ├── config: configuration management module 
    ├── test: Test files for code coverage


## Configurations 
- Honor common environment variables for global configurations.
- Checklist for adding any new configurable attribute:
    - Provide ability to override configuration in code where applicable
    - Add user_settings method to get configured value
    - Add documentation about the attribute in README.md
    - If not already present, add dynamic config reload decorator to methods referencing the new attribute

## Logging
- Use Python's standard [logging module](https://docs.python.org/3/library/logging.html)
- Provide a named logger for the library 
- Use consistent logging levels across all APIs
    - Use the CRITICAL logging level for any statements that need to be logged at all times
    - Use the ERROR logging level for errors where app is unlikely to recover
    - Use the WARNING logging level for failures to perform intended task and raise an exception
    - Use the INFO logging level for normal operations
    - Use the DEBUG logging level for detailed trouble shooting 
- Allow user to log to local file
- Do not log any sensitive data

## Error handling and Exceptions 
- AladdinSDK provides a general error handler decorator which can handle specific types of errors. Here are some features related to the built in error handler:
    - Users can activate/deactivate the error handler via their configuration file. By default error handling is active.
    - Use existing exception types from source and map them to built-in exception handlers
    - Include original error messages in the output 
    - If error cannot be handled appropriately, the handlers will raise the original error for callers to handle
- Error handler decorator can be added to any method in the SDK to wrap the method in a "try-except" block.
In the event of an error, the handler method maps the raised exception to a corresponding error handler.
- Error handler classes are extensions of AbstractAsdkExceptionHandler. These include a list of exception types that can be handled by the class and implementation of handle error method which attempts to safely handle the exception. If the exception can not be handled safely, it is logged for reference and raised again for the caller to handle.

## Retry 
The following section outlines how we are implementing the retry logic across the SDK client and calls.
- Use the common retry module for API retry logic
    - On client SDK instantiation, SDK client loads in the default or user defined retry policy.
    - We will be using the [tenacity library](https://tenacity.readthedocs.io/en/latest/) for retries.
    - On each function definition within the SDK, we will use the @retry decorator from tenacity along with the retry policy settings and default python logging module. 

### Retry policies
- Users can define their own retry settings via ASDK configurations. 
- Retry parameters 
    - Max Retry Attempts: maximum times a particular function call should be retried 
    - Max Retry Interval: fixed duration in between each retry call
    - Fixed duration: maximum duration to retry calls before failing
