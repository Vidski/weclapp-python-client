# openapi_client.StoragePlaceSizeApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_place_size_count_get**](StoragePlaceSizeApi.md#storage_place_size_count_get) | **GET** /storagePlaceSize/count | count storagePlaceSize
[**storage_place_size_get**](StoragePlaceSizeApi.md#storage_place_size_get) | **GET** /storagePlaceSize | query storagePlaceSize
[**storage_place_size_id_id_delete**](StoragePlaceSizeApi.md#storage_place_size_id_id_delete) | **DELETE** /storagePlaceSize/id/{id} | delete a storagePlaceSize
[**storage_place_size_id_id_get**](StoragePlaceSizeApi.md#storage_place_size_id_id_get) | **GET** /storagePlaceSize/id/{id} | query a specific storagePlaceSize
[**storage_place_size_id_id_put**](StoragePlaceSizeApi.md#storage_place_size_id_id_put) | **PUT** /storagePlaceSize/id/{id} | update a storagePlaceSize
[**storage_place_size_post**](StoragePlaceSizeApi.md#storage_place_size_post) | **POST** /storagePlaceSize | create a storagePlaceSize


# **storage_place_size_count_get**
> AccountingTransactionCountGet200Response storage_place_size_count_get()

count storagePlaceSize

count storagePlaceSize

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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)

    try:
        # count storagePlaceSize
        api_response = api_instance.storage_place_size_count_get()
        print("The response of StoragePlaceSizeApi->storage_place_size_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_count_get: %s\n" % e)
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

# **storage_place_size_get**
> StoragePlaceSizeGet200Response storage_place_size_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query storagePlaceSize

query storagePlaceSize

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.storage_place_size_get200_response import StoragePlaceSizeGet200Response
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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query storagePlaceSize
        api_response = api_instance.storage_place_size_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of StoragePlaceSizeApi->storage_place_size_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_get: %s\n" % e)
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

[**StoragePlaceSizeGet200Response**](StoragePlaceSizeGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | storagePlaceSize response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_size_id_id_delete**
> storage_place_size_id_id_delete(id, dry_run=dry_run)

delete a storagePlaceSize

delete a storagePlaceSize

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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a storagePlaceSize
        api_instance.storage_place_size_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_id_id_delete: %s\n" % e)
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
**204** | storagePlaceSize delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_size_id_id_get**
> StoragePlaceSize storage_place_size_id_id_get(id)

query a specific storagePlaceSize

query a specific storagePlaceSize

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.storage_place_size import StoragePlaceSize
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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific storagePlaceSize
        api_response = api_instance.storage_place_size_id_id_get(id)
        print("The response of StoragePlaceSizeApi->storage_place_size_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**StoragePlaceSize**](StoragePlaceSize.md)

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

# **storage_place_size_id_id_put**
> StoragePlaceSize storage_place_size_id_id_put(id, storage_place_size, dry_run=dry_run)

update a storagePlaceSize

update storagePlaceSize

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.storage_place_size import StoragePlaceSize
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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)
    id = 'id_example' # str | 
    storage_place_size = openapi_client.StoragePlaceSize() # StoragePlaceSize | 
    dry_run = True # bool |  (optional)

    try:
        # update a storagePlaceSize
        api_response = api_instance.storage_place_size_id_id_put(id, storage_place_size, dry_run=dry_run)
        print("The response of StoragePlaceSizeApi->storage_place_size_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **storage_place_size** | [**StoragePlaceSize**](StoragePlaceSize.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**StoragePlaceSize**](StoragePlaceSize.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | storagePlaceSize update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_place_size_post**
> StoragePlaceSize storage_place_size_post(storage_place_size, dry_run=dry_run)

create a storagePlaceSize

create a storagePlaceSize

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.storage_place_size import StoragePlaceSize
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
    api_instance = openapi_client.StoragePlaceSizeApi(api_client)
    storage_place_size = openapi_client.StoragePlaceSize() # StoragePlaceSize | 
    dry_run = True # bool |  (optional)

    try:
        # create a storagePlaceSize
        api_response = api_instance.storage_place_size_post(storage_place_size, dry_run=dry_run)
        print("The response of StoragePlaceSizeApi->storage_place_size_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StoragePlaceSizeApi->storage_place_size_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_place_size** | [**StoragePlaceSize**](StoragePlaceSize.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**StoragePlaceSize**](StoragePlaceSize.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | storagePlaceSize create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

