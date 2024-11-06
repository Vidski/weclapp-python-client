# openapi_client.CalendarEventApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendar_event_count_get**](CalendarEventApi.md#calendar_event_count_get) | **GET** /calendarEvent/count | count calendarEvent
[**calendar_event_get**](CalendarEventApi.md#calendar_event_get) | **GET** /calendarEvent | query calendarEvent
[**calendar_event_id_id_delete**](CalendarEventApi.md#calendar_event_id_id_delete) | **DELETE** /calendarEvent/id/{id} | delete a calendarEvent
[**calendar_event_id_id_get**](CalendarEventApi.md#calendar_event_id_id_get) | **GET** /calendarEvent/id/{id} | query a specific calendarEvent
[**calendar_event_id_id_put**](CalendarEventApi.md#calendar_event_id_id_put) | **PUT** /calendarEvent/id/{id} | update a calendarEvent
[**calendar_event_post**](CalendarEventApi.md#calendar_event_post) | **POST** /calendarEvent | create a calendarEvent


# **calendar_event_count_get**
> AccountingTransactionCountGet200Response calendar_event_count_get()

count calendarEvent

count calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.accounting_transaction_count_get200_response import AccountingTransactionCountGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)

    try:
        # count calendarEvent
        api_response = api_instance.calendar_event_count_get()
        print("The response of CalendarEventApi->calendar_event_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_count_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountingTransactionCountGet200Response**](AccountingTransactionCountGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | count |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_event_get**
> CalendarEventGet200Response calendar_event_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query calendarEvent

query calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.calendar_event_get200_response import CalendarEventGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query calendarEvent
        api_response = api_instance.calendar_event_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of CalendarEventApi->calendar_event_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **serialize_nulls** | **bool**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **properties** | **str**|  | [optional] 
 **include_referenced_entities** | **str**|  | [optional] 

### Return type

[**CalendarEventGet200Response**](CalendarEventGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | calendarEvent response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_event_id_id_delete**
> calendar_event_id_id_delete(id, dry_run=dry_run)

delete a calendarEvent

delete a calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a calendarEvent
        api_instance.calendar_event_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_id_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | calendarEvent delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_event_id_id_get**
> CalendarEvent calendar_event_id_id_get(id)

query a specific calendarEvent

query a specific calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.calendar_event import CalendarEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific calendarEvent
        api_response = api_instance.calendar_event_id_id_get(id)
        print("The response of CalendarEventApi->calendar_event_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get by id |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_event_id_id_put**
> CalendarEvent calendar_event_id_id_put(id, calendar_event, dry_run=dry_run)

update a calendarEvent

update calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.calendar_event import CalendarEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)
    id = 'id_example' # str | 
    calendar_event = openapi_client.CalendarEvent() # CalendarEvent | 
    dry_run = True # bool |  (optional)

    try:
        # update a calendarEvent
        api_response = api_instance.calendar_event_id_id_put(id, calendar_event, dry_run=dry_run)
        print("The response of CalendarEventApi->calendar_event_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **calendar_event** | [**CalendarEvent**](CalendarEvent.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | calendarEvent update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calendar_event_post**
> CalendarEvent calendar_event_post(calendar_event, dry_run=dry_run)

create a calendarEvent

create a calendarEvent

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.calendar_event import CalendarEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CalendarEventApi(api_client)
    calendar_event = openapi_client.CalendarEvent() # CalendarEvent | 
    dry_run = True # bool |  (optional)

    try:
        # create a calendarEvent
        api_response = api_instance.calendar_event_post(calendar_event, dry_run=dry_run)
        print("The response of CalendarEventApi->calendar_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarEventApi->calendar_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_event** | [**CalendarEvent**](CalendarEvent.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | calendarEvent create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

