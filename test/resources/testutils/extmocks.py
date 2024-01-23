

# This method will be used by the mock to replace requests.get
def mocked_successful_requests_get(*args):
    class MockResponse:
        def __init__(self):
            self.text = 'SNOWFLAKE_DSWRITE \t mock_snowflake_dswrite \n DUMMY_FILESDAT_KEY \t DUMMY_FILESDAT_VAL \n'
            self.status_code = 200
    return MockResponse()
    
def mocked_successful_requests_get_with_token(*args):
    class MockResponse:
        def __init__(self):
            self.text = 'TEST_TOKEN \t TEST_TOKEN_VALUE \n FOOBAR \t BARBAZ \n DUMMY_FILESDAT_KEY \t DUMMY_FILESDAT_VAL \n'
            self.status_code = 200
    return MockResponse()

def mocked_successful_requests_get_without_token(*args):
    class MockResponse:
        def __init__(self):
            self.text = 'FOOBAR \t BARBAZ \n DUMMY_FILESDAT_KEY \t DUMMY_FILESDAT_VAL \n'
            self.status_code = 200
    return MockResponse()