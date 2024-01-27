# Sample API Calls

## Train Journey API

### Instantiate API client

- Connect using credentials provided in user configuration yaml

    ```py
    from aladdinsdk.api.client import AladdinAPI

    api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
    ```

- Connect using credentials provided by user

    ```py
    from aladdinsdk.api.client import AladdinAPI

    api_instance_train_journey = AladdinAPI("TrainJourneyAPI", default_web_server="https://dev.blackrock.com", api_key="XYZ", username="uname", password="password")
    ```

### Invoking API Endpoints

Each API endpoint is a http swagger path (currently supported http methods: get/put/post/delete/patch). Therefore, a more intuitive invocation format is to simply use the corresponding wrapper methods which take the first parameter as a swagger path and forward all subsequent parameters. <br />
e.g. `api_instance_train_journey.post("/trainJourneys:filter", req_body_json)`

These API calls internally use the `call_api` method of the wrapper class. The first parameter of this method can be:
- swagger http endpoint path and method. e.g. `api_instance_train_journey.call_api(("/trainJourneys:filter", "post"), req_body_json)`
<br /> OR <br />
- the API method to be called on the python codegen class. e.g. `api_instance_train_journey.call_api("train_journey_api_filter_train_journeys", req_body_json)`

All available methods can be listed with `get_api_endpoint_methods()` or `get_api_endpoint_path_tuples()` calls on the API instance. <br />
e.g.
- `api_instance_train_journey.get_api_endpoint_methods()` --> Lists python method names
- `api_instance_train_journey.get_api_endpoint_path_tuples()` --> Lists endpoints as swagger paths and http method tuples

### API calls with request body

- Using json request body

    ```py
    from aladdinsdk.api.client import AladdinAPI

    api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
    req_body_json = {
        "query": {
            "departingStationId": "TS_1441"
        }
    }
    response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json)

    for tj in response.train_journeys:
        print(f"From: {tj.departing_train_station_id}, To: {tj.destination_train_station_id}, Stops: {len(tj.pass_through_station_ids)}, Date: {tj.journey_date}, Duration: {tj.journey_duration}")

    ```

### API Calls with URL params

```py
from aladdinsdk.api.client import AladdinAPI

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")

# Get Train Journey
get_train_journey_response = api_instance_train_journey.get("/trainJourneys/{id}", id="TJ_2")

# Simulate Train Journey - Long Running Operation
get_train_journey_lro_response = api_instance_train_journey.get("/trainJourneys/{id}:run", id="TJ_6")
```

### Disabling Response Deserialization to Object and Type Validations

For some API specifications where types in the protos do not match with the response being sent by the server, a workaround till the service owners fix the underlying issue is to disable response deserialization to python objects. <br /> _Note: This also disables response type validation_

Instead the response is served as a free form dictionary, and values can be by referring keys. (i.e. non-scriptable response)

**IMP NOTE: Check response parsing in this example. Attribute keys are "camelCase" and not "snake_case"**

```py
from aladdinsdk.api.client import AladdinAPI

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
req_body_json = {
    "query": {
        "departingStationId": "TS_1441"
    }
}
response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json, _deserialize_to_object=False)

for tj in response['trainJourneys']:
    print(f"From: {tj['departingTrainStationId']}, To: {tj['destinationTrainStationId']}, Stops: {len(tj['passThroughStationIds'])}, Date: {tj['journeyDate']}, Duration: {tj['journeyDuration']}")
```


### API Calls for Long Running Operations

A simple invocation of a long running operation endpoint will trigger the long running operation. But user will still have to perform polling/status checks on the operation. 

The SDK provides a utility for starting a coroutine which polls for successful completion of a LRO. The polling time interval can be configured in the user settings file (defaults to 10 seconds). This can be overridden using the `status_check_interval` parameter in the LRO utility methods.

Optionally, a callback function can be provided to be called with LRO response as a parameter

**IMP NOTE: Current implementation of LRO endpoints does not provide OpenAPI compliant response schema. Therefore object deserialzation shows incomplete response. It is recommended to use LRO utilities with `_deserialize_to_object` set to `False`**

```py
import asyncio

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")

lro_response = await api_instance_train_journey.call_lro_api(
    start_lro_endpoint=("/trainJourneys/{id}:run", "GET"),
    check_lro_status_endpoint=("/longRunningOperations/{id}", "GET"),
    id="TJ_7", # <---- input parameters / request body for start_lro_endpoint
    _deserialize_to_object=False)

# Note: if no callback function provided, response is returned as is
```

Note: It is recommended to use a http (path, method) tuple while invoking LRO calls.

Complete list of endpoint paths can be found with a call to `get_api_endpoint_path_tuples`.
e.g. `api_instance_train_journey.get_api_endpoint_path_tuples()`

```py
lro_response = await api_instance_train_journey.call_lro_api(
    start_lro_endpoint="train_journey_api_run_train_journey_simulation", # <---- endpoint to start LRO
    check_lro_status_endpoint="train_journey_api_get_longrunning_operation", # <---- endpoint to check LRO status
    id="TJ_7", # <---- input parameters / request body for start_lro_endpoint
    _deserialize_to_object=False)
# Note: if no callback function provided, response is returned as is
```

### API Calls for Long Running Operations - With Callback Function to process final response

```py
import asyncio

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")

def lro_completion_callback_example(lro_response):
    print("==============================DONE==============================")
    print(f"Status: {lro_response.done}")
    print(lro_response.response.json())
    
lro_run = api_instance_train_journey.call_lro_api(
    start_lro_endpoint=("/trainJourneys/{id}:run", "get"),
    check_lro_status_endpoint=("/longRunningOperations/{id}", "get"),
    callback_func=lro_completion_callback_example, 
    id="TJ_7")

asyncio.run(lro_run)
```

### API call - Response transformation

API responses are in JSON form, and can be optionally transformed into another data structure. Here are the supported transformation types:

- JSON to Pandas DataFrame: Converts API response json into a Pandas DataFrame. Pass in optional parameter for `call_api` wrapper: `asdk_transformation_option={'type': "json", 'flatten': None}`

    ```py
    from aladdinsdk.api.client import AladdinAPI

    api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
    req_body_json = {
        "query": {
            "departingStationId": "TS_1441"
        }
    }
    response = api_instance_train_journey.call_api("train_journey_api_filter_train_journeys", req_body_json, asdk_transformation_option={'type': "dataframe", 'flatten': 'train_journeys.[*]'})
    print(response)
    ```
