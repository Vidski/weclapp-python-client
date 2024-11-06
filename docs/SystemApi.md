# openapi_client.SystemApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_create_demo_test_system_post**](SystemApi.md#system_create_demo_test_system_post) | **POST** /system/createDemoTestSystem | 
[**system_demo_test_system_info_get**](SystemApi.md#system_demo_test_system_info_get) | **GET** /system/demoTestSystemInfo | 
[**system_licenses_get**](SystemApi.md#system_licenses_get) | **GET** /system/licenses | 


# **system_create_demo_test_system_post**
> ArchivedEmailIdIdRemoveReferencePost200Response system_create_demo_test_system_post(system_create_demo_test_system_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.system_create_demo_test_system_post_request import SystemCreateDemoTestSystemPostRequest
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
    api_instance = openapi_client.SystemApi(api_client)
    system_create_demo_test_system_post_request = openapi_client.SystemCreateDemoTestSystemPostRequest() # SystemCreateDemoTestSystemPostRequest | 

    try:
        api_response = api_instance.system_create_demo_test_system_post(system_create_demo_test_system_post_request)
        print("The response of SystemApi->system_create_demo_test_system_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_create_demo_test_system_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_create_demo_test_system_post_request** | [**SystemCreateDemoTestSystemPostRequest**](SystemCreateDemoTestSystemPostRequest.md)|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createDemoTestSystem response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_demo_test_system_info_get**
> SystemDemoTestSystemInfoGet200Response system_demo_test_system_info_get()



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.system_demo_test_system_info_get200_response import SystemDemoTestSystemInfoGet200Response
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
    api_instance = openapi_client.SystemApi(api_client)

    try:
        api_response = api_instance.system_demo_test_system_info_get()
        print("The response of SystemApi->system_demo_test_system_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_demo_test_system_info_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemDemoTestSystemInfoGet200Response**](SystemDemoTestSystemInfoGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | demoTestSystemInfo response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_licenses_get**
> SystemLicensesGet200Response system_licenses_get()



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.system_licenses_get200_response import SystemLicensesGet200Response
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
    api_instance = openapi_client.SystemApi(api_client)

    try:
        api_response = api_instance.system_licenses_get()
        print("The response of SystemApi->system_licenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_licenses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemLicensesGet200Response**](SystemLicensesGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | licenses response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

