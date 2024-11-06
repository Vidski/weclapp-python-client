# openapi_client.CustomAttributeDefinitionApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_attribute_definition_count_get**](CustomAttributeDefinitionApi.md#custom_attribute_definition_count_get) | **GET** /customAttributeDefinition/count | count customAttributeDefinition
[**custom_attribute_definition_get**](CustomAttributeDefinitionApi.md#custom_attribute_definition_get) | **GET** /customAttributeDefinition | query customAttributeDefinition
[**custom_attribute_definition_id_id_delete**](CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_delete) | **DELETE** /customAttributeDefinition/id/{id} | delete a customAttributeDefinition
[**custom_attribute_definition_id_id_get**](CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_get) | **GET** /customAttributeDefinition/id/{id} | query a specific customAttributeDefinition
[**custom_attribute_definition_id_id_put**](CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_put) | **PUT** /customAttributeDefinition/id/{id} | update a customAttributeDefinition
[**custom_attribute_definition_post**](CustomAttributeDefinitionApi.md#custom_attribute_definition_post) | **POST** /customAttributeDefinition | create a customAttributeDefinition
[**custom_attribute_definition_read_order_get**](CustomAttributeDefinitionApi.md#custom_attribute_definition_read_order_get) | **GET** /customAttributeDefinition/readOrder | 
[**custom_attribute_definition_update_order_post**](CustomAttributeDefinitionApi.md#custom_attribute_definition_update_order_post) | **POST** /customAttributeDefinition/updateOrder | 


# **custom_attribute_definition_count_get**
> AccountingTransactionCountGet200Response custom_attribute_definition_count_get()

count customAttributeDefinition

count customAttributeDefinition

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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)

    try:
        # count customAttributeDefinition
        api_response = api_instance.custom_attribute_definition_count_get()
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_count_get: %s\n" % e)
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

# **custom_attribute_definition_get**
> CustomAttributeDefinitionGet200Response custom_attribute_definition_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query customAttributeDefinition

query customAttributeDefinition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition_get200_response import CustomAttributeDefinitionGet200Response
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query customAttributeDefinition
        api_response = api_instance.custom_attribute_definition_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_get: %s\n" % e)
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

[**CustomAttributeDefinitionGet200Response**](CustomAttributeDefinitionGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | customAttributeDefinition response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attribute_definition_id_id_delete**
> custom_attribute_definition_id_id_delete(id, dry_run=dry_run)

delete a customAttributeDefinition

delete a customAttributeDefinition

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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a customAttributeDefinition
        api_instance.custom_attribute_definition_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_id_id_delete: %s\n" % e)
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
**204** | customAttributeDefinition delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attribute_definition_id_id_get**
> CustomAttributeDefinition custom_attribute_definition_id_id_get(id)

query a specific customAttributeDefinition

query a specific customAttributeDefinition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition import CustomAttributeDefinition
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific customAttributeDefinition
        api_response = api_instance.custom_attribute_definition_id_id_get(id)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CustomAttributeDefinition**](CustomAttributeDefinition.md)

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

# **custom_attribute_definition_id_id_put**
> CustomAttributeDefinition custom_attribute_definition_id_id_put(id, custom_attribute_definition, dry_run=dry_run)

update a customAttributeDefinition

update customAttributeDefinition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition import CustomAttributeDefinition
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    id = 'id_example' # str | 
    custom_attribute_definition = openapi_client.CustomAttributeDefinition() # CustomAttributeDefinition | 
    dry_run = True # bool |  (optional)

    try:
        # update a customAttributeDefinition
        api_response = api_instance.custom_attribute_definition_id_id_put(id, custom_attribute_definition, dry_run=dry_run)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_attribute_definition** | [**CustomAttributeDefinition**](CustomAttributeDefinition.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomAttributeDefinition**](CustomAttributeDefinition.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | customAttributeDefinition update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attribute_definition_post**
> CustomAttributeDefinition custom_attribute_definition_post(custom_attribute_definition, dry_run=dry_run)

create a customAttributeDefinition

create a customAttributeDefinition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition import CustomAttributeDefinition
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    custom_attribute_definition = openapi_client.CustomAttributeDefinition() # CustomAttributeDefinition | 
    dry_run = True # bool |  (optional)

    try:
        # create a customAttributeDefinition
        api_response = api_instance.custom_attribute_definition_post(custom_attribute_definition, dry_run=dry_run)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_definition** | [**CustomAttributeDefinition**](CustomAttributeDefinition.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomAttributeDefinition**](CustomAttributeDefinition.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | customAttributeDefinition create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attribute_definition_read_order_get**
> CustomAttributeDefinitionReadOrderGet200Response custom_attribute_definition_read_order_get(entity_type)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition_read_order_get200_response import CustomAttributeDefinitionReadOrderGet200Response
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    entity_type = 'entity_type_example' # str | 

    try:
        api_response = api_instance.custom_attribute_definition_read_order_get(entity_type)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_read_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_read_order_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 

### Return type

[**CustomAttributeDefinitionReadOrderGet200Response**](CustomAttributeDefinitionReadOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | readOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_attribute_definition_update_order_post**
> CustomAttributeDefinitionReadOrderGet200Response custom_attribute_definition_update_order_post(custom_attribute_definition_update_order_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_attribute_definition_read_order_get200_response import CustomAttributeDefinitionReadOrderGet200Response
from openapi_client.models.custom_attribute_definition_update_order_post_request import CustomAttributeDefinitionUpdateOrderPostRequest
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
    api_instance = openapi_client.CustomAttributeDefinitionApi(api_client)
    custom_attribute_definition_update_order_post_request = openapi_client.CustomAttributeDefinitionUpdateOrderPostRequest() # CustomAttributeDefinitionUpdateOrderPostRequest | 

    try:
        api_response = api_instance.custom_attribute_definition_update_order_post(custom_attribute_definition_update_order_post_request)
        print("The response of CustomAttributeDefinitionApi->custom_attribute_definition_update_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeDefinitionApi->custom_attribute_definition_update_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_definition_update_order_post_request** | [**CustomAttributeDefinitionUpdateOrderPostRequest**](CustomAttributeDefinitionUpdateOrderPostRequest.md)|  | 

### Return type

[**CustomAttributeDefinitionReadOrderGet200Response**](CustomAttributeDefinitionReadOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

