# openapi_client.InternalTransportReferenceApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_transport_reference_count_get**](InternalTransportReferenceApi.md#internal_transport_reference_count_get) | **GET** /internalTransportReference/count | count internalTransportReference
[**internal_transport_reference_get**](InternalTransportReferenceApi.md#internal_transport_reference_get) | **GET** /internalTransportReference | query internalTransportReference
[**internal_transport_reference_id_id_create_label_post**](InternalTransportReferenceApi.md#internal_transport_reference_id_id_create_label_post) | **POST** /internalTransportReference/id/{id}/createLabel | 
[**internal_transport_reference_id_id_delete**](InternalTransportReferenceApi.md#internal_transport_reference_id_id_delete) | **DELETE** /internalTransportReference/id/{id} | delete a internalTransportReference
[**internal_transport_reference_id_id_download_latest_label_get**](InternalTransportReferenceApi.md#internal_transport_reference_id_id_download_latest_label_get) | **GET** /internalTransportReference/id/{id}/downloadLatestLabel | 
[**internal_transport_reference_id_id_get**](InternalTransportReferenceApi.md#internal_transport_reference_id_id_get) | **GET** /internalTransportReference/id/{id} | query a specific internalTransportReference
[**internal_transport_reference_id_id_put**](InternalTransportReferenceApi.md#internal_transport_reference_id_id_put) | **PUT** /internalTransportReference/id/{id} | update a internalTransportReference
[**internal_transport_reference_post**](InternalTransportReferenceApi.md#internal_transport_reference_post) | **POST** /internalTransportReference | create a internalTransportReference


# **internal_transport_reference_count_get**
> AccountingTransactionCountGet200Response internal_transport_reference_count_get()

count internalTransportReference

count internalTransportReference

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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)

    try:
        # count internalTransportReference
        api_response = api_instance.internal_transport_reference_count_get()
        print("The response of InternalTransportReferenceApi->internal_transport_reference_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_count_get: %s\n" % e)
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

# **internal_transport_reference_get**
> InternalTransportReferenceGet200Response internal_transport_reference_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query internalTransportReference

query internalTransportReference

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.internal_transport_reference_get200_response import InternalTransportReferenceGet200Response
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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query internalTransportReference
        api_response = api_instance.internal_transport_reference_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_get: %s\n" % e)
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

[**InternalTransportReferenceGet200Response**](InternalTransportReferenceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | internalTransportReference response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transport_reference_id_id_create_label_post**
> bytearray internal_transport_reference_id_id_create_label_post(id, body)



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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.internal_transport_reference_id_id_create_label_post(id, body)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_id_id_create_label_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_id_id_create_label_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

**bytearray**

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/pdf, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createLabel response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transport_reference_id_id_delete**
> internal_transport_reference_id_id_delete(id, dry_run=dry_run)

delete a internalTransportReference

delete a internalTransportReference

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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a internalTransportReference
        api_instance.internal_transport_reference_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_id_id_delete: %s\n" % e)
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
**204** | internalTransportReference delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transport_reference_id_id_download_latest_label_get**
> bytearray internal_transport_reference_id_id_download_latest_label_get(id)



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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.internal_transport_reference_id_id_download_latest_label_get(id)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_id_id_download_latest_label_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_id_id_download_latest_label_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/pdf, image/jpeg, image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | downloadLatestLabel response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transport_reference_id_id_get**
> InternalTransportReference internal_transport_reference_id_id_get(id)

query a specific internalTransportReference

query a specific internalTransportReference

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.internal_transport_reference import InternalTransportReference
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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific internalTransportReference
        api_response = api_instance.internal_transport_reference_id_id_get(id)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InternalTransportReference**](InternalTransportReference.md)

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

# **internal_transport_reference_id_id_put**
> InternalTransportReference internal_transport_reference_id_id_put(id, internal_transport_reference, dry_run=dry_run)

update a internalTransportReference

update internalTransportReference

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.internal_transport_reference import InternalTransportReference
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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    id = 'id_example' # str | 
    internal_transport_reference = openapi_client.InternalTransportReference() # InternalTransportReference | 
    dry_run = True # bool |  (optional)

    try:
        # update a internalTransportReference
        api_response = api_instance.internal_transport_reference_id_id_put(id, internal_transport_reference, dry_run=dry_run)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **internal_transport_reference** | [**InternalTransportReference**](InternalTransportReference.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**InternalTransportReference**](InternalTransportReference.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | internalTransportReference update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transport_reference_post**
> InternalTransportReference internal_transport_reference_post(internal_transport_reference, dry_run=dry_run)

create a internalTransportReference

create a internalTransportReference

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.internal_transport_reference import InternalTransportReference
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
    api_instance = openapi_client.InternalTransportReferenceApi(api_client)
    internal_transport_reference = openapi_client.InternalTransportReference() # InternalTransportReference | 
    dry_run = True # bool |  (optional)

    try:
        # create a internalTransportReference
        api_response = api_instance.internal_transport_reference_post(internal_transport_reference, dry_run=dry_run)
        print("The response of InternalTransportReferenceApi->internal_transport_reference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalTransportReferenceApi->internal_transport_reference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_transport_reference** | [**InternalTransportReference**](InternalTransportReference.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**InternalTransportReference**](InternalTransportReference.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | internalTransportReference create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

