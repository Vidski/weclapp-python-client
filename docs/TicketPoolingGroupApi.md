# openapi_client.TicketPoolingGroupApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_pooling_group_count_get**](TicketPoolingGroupApi.md#ticket_pooling_group_count_get) | **GET** /ticketPoolingGroup/count | count ticketPoolingGroup
[**ticket_pooling_group_get**](TicketPoolingGroupApi.md#ticket_pooling_group_get) | **GET** /ticketPoolingGroup | query ticketPoolingGroup
[**ticket_pooling_group_id_id_get**](TicketPoolingGroupApi.md#ticket_pooling_group_id_id_get) | **GET** /ticketPoolingGroup/id/{id} | query a specific ticketPoolingGroup


# **ticket_pooling_group_count_get**
> AccountingTransactionCountGet200Response ticket_pooling_group_count_get()

count ticketPoolingGroup

count ticketPoolingGroup

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
    api_instance = openapi_client.TicketPoolingGroupApi(api_client)

    try:
        # count ticketPoolingGroup
        api_response = api_instance.ticket_pooling_group_count_get()
        print("The response of TicketPoolingGroupApi->ticket_pooling_group_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketPoolingGroupApi->ticket_pooling_group_count_get: %s\n" % e)
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

# **ticket_pooling_group_get**
> TicketPoolingGroupGet200Response ticket_pooling_group_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ticketPoolingGroup

query ticketPoolingGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_pooling_group_get200_response import TicketPoolingGroupGet200Response
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
    api_instance = openapi_client.TicketPoolingGroupApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ticketPoolingGroup
        api_response = api_instance.ticket_pooling_group_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TicketPoolingGroupApi->ticket_pooling_group_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketPoolingGroupApi->ticket_pooling_group_get: %s\n" % e)
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

[**TicketPoolingGroupGet200Response**](TicketPoolingGroupGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketPoolingGroup response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_pooling_group_id_id_get**
> TicketPoolingGroup ticket_pooling_group_id_id_get(id)

query a specific ticketPoolingGroup

query a specific ticketPoolingGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_pooling_group import TicketPoolingGroup
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
    api_instance = openapi_client.TicketPoolingGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticketPoolingGroup
        api_response = api_instance.ticket_pooling_group_id_id_get(id)
        print("The response of TicketPoolingGroupApi->ticket_pooling_group_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketPoolingGroupApi->ticket_pooling_group_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketPoolingGroup**](TicketPoolingGroup.md)

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

