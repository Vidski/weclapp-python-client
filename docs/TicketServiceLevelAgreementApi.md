# openapi_client.TicketServiceLevelAgreementApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_service_level_agreement_count_get**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_count_get) | **GET** /ticketServiceLevelAgreement/count | count ticketServiceLevelAgreement
[**ticket_service_level_agreement_get**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_get) | **GET** /ticketServiceLevelAgreement | query ticketServiceLevelAgreement
[**ticket_service_level_agreement_id_id_delete**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_delete) | **DELETE** /ticketServiceLevelAgreement/id/{id} | delete a ticketServiceLevelAgreement
[**ticket_service_level_agreement_id_id_get**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_get) | **GET** /ticketServiceLevelAgreement/id/{id} | query a specific ticketServiceLevelAgreement
[**ticket_service_level_agreement_id_id_put**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_put) | **PUT** /ticketServiceLevelAgreement/id/{id} | update a ticketServiceLevelAgreement
[**ticket_service_level_agreement_post**](TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_post) | **POST** /ticketServiceLevelAgreement | create a ticketServiceLevelAgreement


# **ticket_service_level_agreement_count_get**
> AccountingTransactionCountGet200Response ticket_service_level_agreement_count_get()

count ticketServiceLevelAgreement

count ticketServiceLevelAgreement

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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)

    try:
        # count ticketServiceLevelAgreement
        api_response = api_instance.ticket_service_level_agreement_count_get()
        print("The response of TicketServiceLevelAgreementApi->ticket_service_level_agreement_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_count_get: %s\n" % e)
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

# **ticket_service_level_agreement_get**
> TicketServiceLevelAgreementGet200Response ticket_service_level_agreement_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ticketServiceLevelAgreement

query ticketServiceLevelAgreement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_service_level_agreement_get200_response import TicketServiceLevelAgreementGet200Response
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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ticketServiceLevelAgreement
        api_response = api_instance.ticket_service_level_agreement_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TicketServiceLevelAgreementApi->ticket_service_level_agreement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_get: %s\n" % e)
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

[**TicketServiceLevelAgreementGet200Response**](TicketServiceLevelAgreementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketServiceLevelAgreement response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_service_level_agreement_id_id_delete**
> ticket_service_level_agreement_id_id_delete(id, dry_run=dry_run)

delete a ticketServiceLevelAgreement

delete a ticketServiceLevelAgreement

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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ticketServiceLevelAgreement
        api_instance.ticket_service_level_agreement_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_id_id_delete: %s\n" % e)
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
**204** | ticketServiceLevelAgreement delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_service_level_agreement_id_id_get**
> TicketServiceLevelAgreement ticket_service_level_agreement_id_id_get(id)

query a specific ticketServiceLevelAgreement

query a specific ticketServiceLevelAgreement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_service_level_agreement import TicketServiceLevelAgreement
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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticketServiceLevelAgreement
        api_response = api_instance.ticket_service_level_agreement_id_id_get(id)
        print("The response of TicketServiceLevelAgreementApi->ticket_service_level_agreement_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketServiceLevelAgreement**](TicketServiceLevelAgreement.md)

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

# **ticket_service_level_agreement_id_id_put**
> TicketServiceLevelAgreement ticket_service_level_agreement_id_id_put(id, ticket_service_level_agreement, dry_run=dry_run)

update a ticketServiceLevelAgreement

update ticketServiceLevelAgreement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_service_level_agreement import TicketServiceLevelAgreement
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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)
    id = 'id_example' # str | 
    ticket_service_level_agreement = openapi_client.TicketServiceLevelAgreement() # TicketServiceLevelAgreement | 
    dry_run = True # bool |  (optional)

    try:
        # update a ticketServiceLevelAgreement
        api_response = api_instance.ticket_service_level_agreement_id_id_put(id, ticket_service_level_agreement, dry_run=dry_run)
        print("The response of TicketServiceLevelAgreementApi->ticket_service_level_agreement_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_service_level_agreement** | [**TicketServiceLevelAgreement**](TicketServiceLevelAgreement.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketServiceLevelAgreement**](TicketServiceLevelAgreement.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketServiceLevelAgreement update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_service_level_agreement_post**
> TicketServiceLevelAgreement ticket_service_level_agreement_post(ticket_service_level_agreement, dry_run=dry_run)

create a ticketServiceLevelAgreement

create a ticketServiceLevelAgreement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_service_level_agreement import TicketServiceLevelAgreement
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
    api_instance = openapi_client.TicketServiceLevelAgreementApi(api_client)
    ticket_service_level_agreement = openapi_client.TicketServiceLevelAgreement() # TicketServiceLevelAgreement | 
    dry_run = True # bool |  (optional)

    try:
        # create a ticketServiceLevelAgreement
        api_response = api_instance.ticket_service_level_agreement_post(ticket_service_level_agreement, dry_run=dry_run)
        print("The response of TicketServiceLevelAgreementApi->ticket_service_level_agreement_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketServiceLevelAgreementApi->ticket_service_level_agreement_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_service_level_agreement** | [**TicketServiceLevelAgreement**](TicketServiceLevelAgreement.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketServiceLevelAgreement**](TicketServiceLevelAgreement.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ticketServiceLevelAgreement create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

