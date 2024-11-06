# openapi_client.TicketFaqApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_faq_count_get**](TicketFaqApi.md#ticket_faq_count_get) | **GET** /ticketFaq/count | count ticketFaq
[**ticket_faq_get**](TicketFaqApi.md#ticket_faq_get) | **GET** /ticketFaq | query ticketFaq
[**ticket_faq_id_id_delete**](TicketFaqApi.md#ticket_faq_id_id_delete) | **DELETE** /ticketFaq/id/{id} | delete a ticketFaq
[**ticket_faq_id_id_get**](TicketFaqApi.md#ticket_faq_id_id_get) | **GET** /ticketFaq/id/{id} | query a specific ticketFaq
[**ticket_faq_id_id_put**](TicketFaqApi.md#ticket_faq_id_id_put) | **PUT** /ticketFaq/id/{id} | update a ticketFaq
[**ticket_faq_post**](TicketFaqApi.md#ticket_faq_post) | **POST** /ticketFaq | create a ticketFaq


# **ticket_faq_count_get**
> AccountingTransactionCountGet200Response ticket_faq_count_get()

count ticketFaq

count ticketFaq

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
    api_instance = openapi_client.TicketFaqApi(api_client)

    try:
        # count ticketFaq
        api_response = api_instance.ticket_faq_count_get()
        print("The response of TicketFaqApi->ticket_faq_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_count_get: %s\n" % e)
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

# **ticket_faq_get**
> TicketFaqGet200Response ticket_faq_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ticketFaq

query ticketFaq

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_faq_get200_response import TicketFaqGet200Response
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
    api_instance = openapi_client.TicketFaqApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ticketFaq
        api_response = api_instance.ticket_faq_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TicketFaqApi->ticket_faq_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_get: %s\n" % e)
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

[**TicketFaqGet200Response**](TicketFaqGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketFaq response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_faq_id_id_delete**
> ticket_faq_id_id_delete(id, dry_run=dry_run)

delete a ticketFaq

delete a ticketFaq

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
    api_instance = openapi_client.TicketFaqApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ticketFaq
        api_instance.ticket_faq_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_id_id_delete: %s\n" % e)
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
**204** | ticketFaq delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_faq_id_id_get**
> TicketFaq ticket_faq_id_id_get(id)

query a specific ticketFaq

query a specific ticketFaq

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_faq import TicketFaq
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
    api_instance = openapi_client.TicketFaqApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticketFaq
        api_response = api_instance.ticket_faq_id_id_get(id)
        print("The response of TicketFaqApi->ticket_faq_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketFaq**](TicketFaq.md)

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

# **ticket_faq_id_id_put**
> TicketFaq ticket_faq_id_id_put(id, ticket_faq, dry_run=dry_run)

update a ticketFaq

update ticketFaq

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_faq import TicketFaq
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
    api_instance = openapi_client.TicketFaqApi(api_client)
    id = 'id_example' # str | 
    ticket_faq = openapi_client.TicketFaq() # TicketFaq | 
    dry_run = True # bool |  (optional)

    try:
        # update a ticketFaq
        api_response = api_instance.ticket_faq_id_id_put(id, ticket_faq, dry_run=dry_run)
        print("The response of TicketFaqApi->ticket_faq_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_faq** | [**TicketFaq**](TicketFaq.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketFaq**](TicketFaq.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketFaq update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_faq_post**
> TicketFaq ticket_faq_post(ticket_faq, dry_run=dry_run)

create a ticketFaq

create a ticketFaq

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_faq import TicketFaq
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
    api_instance = openapi_client.TicketFaqApi(api_client)
    ticket_faq = openapi_client.TicketFaq() # TicketFaq | 
    dry_run = True # bool |  (optional)

    try:
        # create a ticketFaq
        api_response = api_instance.ticket_faq_post(ticket_faq, dry_run=dry_run)
        print("The response of TicketFaqApi->ticket_faq_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketFaqApi->ticket_faq_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_faq** | [**TicketFaq**](TicketFaq.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketFaq**](TicketFaq.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ticketFaq create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

