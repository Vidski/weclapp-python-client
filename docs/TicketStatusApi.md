# openapi_client.TicketStatusApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_status_count_get**](TicketStatusApi.md#ticket_status_count_get) | **GET** /ticketStatus/count | count ticketStatus
[**ticket_status_get**](TicketStatusApi.md#ticket_status_get) | **GET** /ticketStatus | query ticketStatus
[**ticket_status_id_id_delete**](TicketStatusApi.md#ticket_status_id_id_delete) | **DELETE** /ticketStatus/id/{id} | delete a ticketStatus
[**ticket_status_id_id_get**](TicketStatusApi.md#ticket_status_id_id_get) | **GET** /ticketStatus/id/{id} | query a specific ticketStatus
[**ticket_status_id_id_put**](TicketStatusApi.md#ticket_status_id_id_put) | **PUT** /ticketStatus/id/{id} | update a ticketStatus
[**ticket_status_post**](TicketStatusApi.md#ticket_status_post) | **POST** /ticketStatus | create a ticketStatus


# **ticket_status_count_get**
> AccountingTransactionCountGet200Response ticket_status_count_get()

count ticketStatus

count ticketStatus

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
    api_instance = openapi_client.TicketStatusApi(api_client)

    try:
        # count ticketStatus
        api_response = api_instance.ticket_status_count_get()
        print("The response of TicketStatusApi->ticket_status_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_count_get: %s\n" % e)
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

# **ticket_status_get**
> TicketStatusGet200Response ticket_status_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ticketStatus

query ticketStatus

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_status_get200_response import TicketStatusGet200Response
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
    api_instance = openapi_client.TicketStatusApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ticketStatus
        api_response = api_instance.ticket_status_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TicketStatusApi->ticket_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_get: %s\n" % e)
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

[**TicketStatusGet200Response**](TicketStatusGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketStatus response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_status_id_id_delete**
> ticket_status_id_id_delete(id, dry_run=dry_run)

delete a ticketStatus

delete a ticketStatus

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
    api_instance = openapi_client.TicketStatusApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ticketStatus
        api_instance.ticket_status_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_id_id_delete: %s\n" % e)
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
**204** | ticketStatus delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_status_id_id_get**
> TicketStatus ticket_status_id_id_get(id)

query a specific ticketStatus

query a specific ticketStatus

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_status import TicketStatus
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
    api_instance = openapi_client.TicketStatusApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticketStatus
        api_response = api_instance.ticket_status_id_id_get(id)
        print("The response of TicketStatusApi->ticket_status_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketStatus**](TicketStatus.md)

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

# **ticket_status_id_id_put**
> TicketStatus ticket_status_id_id_put(id, ticket_status, dry_run=dry_run)

update a ticketStatus

update ticketStatus

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_status import TicketStatus
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
    api_instance = openapi_client.TicketStatusApi(api_client)
    id = 'id_example' # str | 
    ticket_status = openapi_client.TicketStatus() # TicketStatus | 
    dry_run = True # bool |  (optional)

    try:
        # update a ticketStatus
        api_response = api_instance.ticket_status_id_id_put(id, ticket_status, dry_run=dry_run)
        print("The response of TicketStatusApi->ticket_status_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_status** | [**TicketStatus**](TicketStatus.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketStatus**](TicketStatus.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketStatus update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_status_post**
> TicketStatus ticket_status_post(ticket_status, dry_run=dry_run)

create a ticketStatus

create a ticketStatus

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_status import TicketStatus
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
    api_instance = openapi_client.TicketStatusApi(api_client)
    ticket_status = openapi_client.TicketStatus() # TicketStatus | 
    dry_run = True # bool |  (optional)

    try:
        # create a ticketStatus
        api_response = api_instance.ticket_status_post(ticket_status, dry_run=dry_run)
        print("The response of TicketStatusApi->ticket_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStatusApi->ticket_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_status** | [**TicketStatus**](TicketStatus.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketStatus**](TicketStatus.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ticketStatus create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

