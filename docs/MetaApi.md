# openapi_client.MetaApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_query_filter_properties_get**](MetaApi.md#meta_query_filter_properties_get) | **GET** /meta/queryFilterProperties | 
[**meta_query_sort_properties_get**](MetaApi.md#meta_query_sort_properties_get) | **GET** /meta/querySortProperties | 
[**meta_resources_get**](MetaApi.md#meta_resources_get) | **GET** /meta/resources | 


# **meta_query_filter_properties_get**
> MetaQueryFilterPropertiesGet200Response meta_query_filter_properties_get(resource)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.meta_query_filter_properties_get200_response import MetaQueryFilterPropertiesGet200Response
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
    api_instance = openapi_client.MetaApi(api_client)
    resource = 'resource_example' # str | 

    try:
        api_response = api_instance.meta_query_filter_properties_get(resource)
        print("The response of MetaApi->meta_query_filter_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_query_filter_properties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 

### Return type

[**MetaQueryFilterPropertiesGet200Response**](MetaQueryFilterPropertiesGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | queryFilterProperties response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_query_sort_properties_get**
> MetaQueryFilterPropertiesGet200Response meta_query_sort_properties_get(resource)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.meta_query_filter_properties_get200_response import MetaQueryFilterPropertiesGet200Response
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
    api_instance = openapi_client.MetaApi(api_client)
    resource = 'resource_example' # str | 

    try:
        api_response = api_instance.meta_query_sort_properties_get(resource)
        print("The response of MetaApi->meta_query_sort_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_query_sort_properties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 

### Return type

[**MetaQueryFilterPropertiesGet200Response**](MetaQueryFilterPropertiesGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | querySortProperties response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_resources_get**
> MetaResourcesGet200Response meta_resources_get()



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.meta_resources_get200_response import MetaResourcesGet200Response
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
    api_instance = openapi_client.MetaApi(api_client)

    try:
        api_response = api_instance.meta_resources_get()
        print("The response of MetaApi->meta_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_resources_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetaResourcesGet200Response**](MetaResourcesGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resources response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

