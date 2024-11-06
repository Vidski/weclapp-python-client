# openapi_client.StoragePlaceBlockingReasonApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_place_blocking_reason_count_get**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_count_get) | **GET** /storagePlaceBlockingReason/count | count storagePlaceBlockingReason
[**storage_place_blocking_reason_get**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_get) | **GET** /storagePlaceBlockingReason | query storagePlaceBlockingReason
[**storage_place_blocking_reason_id_id_delete**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_delete) | **DELETE** /storagePlaceBlockingReason/id/{id} | delete a storagePlaceBlockingReason
[**storage_place_blocking_reason_id_id_get**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_get) | **GET** /storagePlaceBlockingReason/id/{id} | query a specific storagePlaceBlockingReason
[**storage_place_blocking_reason_id_id_put**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_put) | **PUT** /storagePlaceBlockingReason/id/{id} | update a storagePlaceBlockingReason
[**storage_place_blocking_reason_post**](StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_post) | **POST** /storagePlaceBlockingReason | create a storagePlaceBlockingReason


# **storage_place_blocking_reason_count_get**
> AccountingTransactionCountGet200Response storage_place_blocking_reason_count_get()

count storagePlaceBlockingReason

count storagePlaceBlockingReason

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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)

    try:
        # count storagePlaceBlockingReason
        api_response = api_instance.storage_place_blocking_reason_count_get()
        print("The response of StoragePlaceBlockingReasonApi->storage_place_blocking_reason_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_count_get: %s\n" % e)
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

# **storage_place_blocking_reason_get**
> ArticleAccountingCodeGet200Response storage_place_blocking_reason_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query storagePlaceBlockingReason

query storagePlaceBlockingReason

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_accounting_code_get200_response import ArticleAccountingCodeGet200Response
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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query storagePlaceBlockingReason
        api_response = api_instance.storage_place_blocking_reason_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of StoragePlaceBlockingReasonApi->storage_place_blocking_reason_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_get: %s\n" % e)
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

[**ArticleAccountingCodeGet200Response**](ArticleAccountingCodeGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | storagePlaceBlockingReason response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_blocking_reason_id_id_delete**
> storage_place_blocking_reason_id_id_delete(id, dry_run=dry_run)

delete a storagePlaceBlockingReason

delete a storagePlaceBlockingReason

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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a storagePlaceBlockingReason
        api_instance.storage_place_blocking_reason_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_id_id_delete: %s\n" % e)
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
**204** | storagePlaceBlockingReason delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_blocking_reason_id_id_get**
> CustomValue storage_place_blocking_reason_id_id_get(id)

query a specific storagePlaceBlockingReason

query a specific storagePlaceBlockingReason

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific storagePlaceBlockingReason
        api_response = api_instance.storage_place_blocking_reason_id_id_get(id)
        print("The response of StoragePlaceBlockingReasonApi->storage_place_blocking_reason_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CustomValue**](CustomValue.md)

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

# **storage_place_blocking_reason_id_id_put**
> CustomValue storage_place_blocking_reason_id_id_put(id, custom_value, dry_run=dry_run)

update a storagePlaceBlockingReason

update storagePlaceBlockingReason

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)
    id = 'id_example' # str | 
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # update a storagePlaceBlockingReason
        api_response = api_instance.storage_place_blocking_reason_id_id_put(id, custom_value, dry_run=dry_run)
        print("The response of StoragePlaceBlockingReasonApi->storage_place_blocking_reason_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_value** | [**CustomValue**](CustomValue.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomValue**](CustomValue.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | storagePlaceBlockingReason update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_blocking_reason_post**
> CustomValue storage_place_blocking_reason_post(custom_value, dry_run=dry_run)

create a storagePlaceBlockingReason

create a storagePlaceBlockingReason

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.StoragePlaceBlockingReasonApi(api_client)
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # create a storagePlaceBlockingReason
        api_response = api_instance.storage_place_blocking_reason_post(custom_value, dry_run=dry_run)
        print("The response of StoragePlaceBlockingReasonApi->storage_place_blocking_reason_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceBlockingReasonApi->storage_place_blocking_reason_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_value** | [**CustomValue**](CustomValue.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomValue**](CustomValue.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | storagePlaceBlockingReason create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

