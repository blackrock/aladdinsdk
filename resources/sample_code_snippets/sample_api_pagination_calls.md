# Sample Paginated API Calls
This document provides examples of how to make paginated API calls. This builds on the sample_api_calls.md document.

- [Set up the API client and invoking API Endpoints](#Set-up-the-API-client-and-invoking-API-Endpoints)
- [Pagination Options](#Pagination-Options)
    - [_asdk_pagination_options](#_asdk_pagination_options)
    - [User Configuration Yaml](#User-Configuration-Yaml)
- [Paginated Response](#Paginated-Response)
- [Sample Code - Valid Params](#Sample-Code---Valid-Params)
- [Sample Code - Invalid Params](#Sample-Code---Invalid-Params)

## Set up the API client and invoking API Endpoints

- This can be done by setting credentials in user configuration file or via Aladdin API
-  Authentication is required to make API calls.

Please refer to sample_api_calls.md for more details on authentication (Basic Auth or OAuth) details.

The code below sets up the client for TrainJourneyAPI and creates a request body for the API call.
<br> Please note that the request body does not contain information related to pagination.
```python
from aladdinsdk.api.client import AladdinAPI

api_instance_train_journey = AladdinAPI("TrainJourneyAPI")
req_body_json = {
    "query": {
        "departingStationId": "TS_1441"
    }
}
```
## Pagination Options
- Please note:
    - Any field set in `_asdk_pagination_options` or the user configuration yaml file for pagination will default to 1 if 0 or a negative value is passed in.
    - Any field set with an invalid type (for example, page token takes a string, user passes in an int), will default to no pagination.
### _asdk_pagination_options
In order to invoke the endpoint with pagination, the following code can be used:
```python
    response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json, _asdk_pagination_options={'page_size': 10, 'number_of_pages': 4})
```

The `_asdk_pagination_options` parameter is used to specify the pagination options. The following parameter can be passed in:
- `page_size`: The number of records to be fetched in a single page.
- `number_of_pages`: The number of pages to be fetched. The number set here will be the total number of api calls made subsequently to fetch the data.
- `page_token`: The page token keeps track of the next page that can be fetched but in most cases this will be empty. Pass in a token here if you want to fetch from a specific page.
- `timeout`: The time in seconds to wait for the response. If the response is not received within the timeout, the request will be aborted and the responses retrieved till that point will be returned.
- `interval`: The time between each subsequent request to fetch the next page.

`_asdk_pagination_options` can be set the same way for api calls that have a request body and for api calls with URL params.

The `_asdk_pagination_options` have associated default values. When setting `_asdk_pagination_options`, all fields are options. If a specific field is not set, the field will be set to the default value.
```default values
page_size = 10
number_of_pages = 5
page_token = None
timeout = 300
interval = 2
```

If `_asdk_pagination_options` is not set, pagination will not be applied and the response will be returned as is.
```python
    response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json)
```

### User Configuration Yaml
The values set in `_asdk_pagination_options` can have a maximum number that can be set via user configuration yaml file.
```yaml
API:
  PAGINATION:
    MAX_PAGE_SIZE: 10
    MAX_PAGES: 5
    TIMEOUT: 300
    INTERVAL: 2
```

In the example above, the max number of pages retrieved for any api call is 5 and the max number of records fetched in a single page is 10. The timeout is set to 300 seconds and the interval between each subsequent request is 2 seconds.

Fields set in `_asdk_pagination_options` will take priority over values set in the config file. For any fields that are not set by the
user, the values will be set to a default value unless the configuration yaml contains a value.

For example, let's say a user sets the following in the `_asdk_pagination_options`
```python
    response = api_instance_train_journey.post("/trainJourneys:filter", req_body_json, _asdk_pagination_options={'page_size': 50, 'number_of_pages': 3})
```

This is the user's yaml file:
```yaml
API:
  PAGINATION:
    MAX_PAGE_SIZE: 10
    MAX_PAGES: 5
    TIMEOUT: 3
```

In this case, the follow values will be used for pagination:
```default values
page_size = 50
number_of_pages = 3
page_token = ""
timeout = 3
interval = 2
```

## Paginated Response
Paginated responses will be returned as a list of responses. Each response will contain the data (please refer to the respective api's response for the structure and fields) and a next page token field. The next page token can be used to fetch the next page.
```python
for response in responses:
  for tj in response.train_journeys:
    print(
      f"From: {tj.departing_train_station_id}, To: {tj.destination_train_station_id}, Stops: {len(tj.pass_through_station_ids)}, Date: {tj.journey_date}, Duration: {tj.journey_duration}")
```

## Sample Code - Valid Params
The code below demonstrates how to make paginated API calls and parse through the response received.
```python
from aladdinsdk.api.client import AladdinAPI
api_instance = AladdinAPI("TrainJourneyAPI")

responses = api_instance.get("/trainJourneys", _asdk_pagination_options={'page_size': 2, 'page_token': ''})

print("\nTrain Journey API Response:")
for response in responses:
    for tj in response.train_journeys:
      print(
        f"From: {tj.departing_train_station_id}, To: {tj.destination_train_station_id}, Stops: {len(tj.pass_through_station_ids)}, Date: {tj.journey_date}, Duration: {tj.journey_duration}")
```


## Sample Code - Invalid Params
*Please note that the response returned here is not a list but rather the first page of the response. This is because the page token is invalid and the response is returned as is.*

The code below demonstrates how to make paginated API calls and parse through the response received.

```python
from aladdinsdk.api.client import AladdinAPI
api_instance = AladdinAPI("TrainJourneyAPI")

responses = api_instance.get("/trainJourneys", _asdk_pagination_options={'page_size': 2, 'page_token': 0})

print("\nTrain Journey API Response:")
for tj in responses.train_journeys:
  print(
    f"From: {tj.departing_train_station_id}, To: {tj.destination_train_station_id}, Stops: {len(tj.pass_through_station_ids)}, Date: {tj.journey_date}, Duration: {tj.journey_duration}")
```