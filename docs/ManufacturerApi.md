# openapi_client.ManufacturerApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manufacturer_count_get**](ManufacturerApi.md#manufacturer_count_get) | **GET** /manufacturer/count | count manufacturer
[**manufacturer_get**](ManufacturerApi.md#manufacturer_get) | **GET** /manufacturer | query manufacturer
[**manufacturer_id_id_delete**](ManufacturerApi.md#manufacturer_id_id_delete) | **DELETE** /manufacturer/id/{id} | delete a manufacturer
[**manufacturer_id_id_get**](ManufacturerApi.md#manufacturer_id_id_get) | **GET** /manufacturer/id/{id} | query a specific manufacturer
[**manufacturer_id_id_put**](ManufacturerApi.md#manufacturer_id_id_put) | **PUT** /manufacturer/id/{id} | update a manufacturer
[**manufacturer_post**](ManufacturerApi.md#manufacturer_post) | **POST** /manufacturer | create a manufacturer


# **manufacturer_count_get**
> AccountingTransactionCountGet200Response manufacturer_count_get()

count manufacturer

count manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)

    try:
        # count manufacturer
        api_response = api_instance.manufacturer_count_get()
        print("The response of ManufacturerApi->manufacturer_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_count_get: %s\n" % e)
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

# **manufacturer_get**
> ArticleAccountingCodeGet200Response manufacturer_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query manufacturer

query manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query manufacturer
        api_response = api_instance.manufacturer_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ManufacturerApi->manufacturer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_get: %s\n" % e)
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
**200** | manufacturer response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturer_id_id_delete**
> manufacturer_id_id_delete(id, dry_run=dry_run)

delete a manufacturer

delete a manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a manufacturer
        api_instance.manufacturer_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_id_id_delete: %s\n" % e)
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
**204** | manufacturer delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturer_id_id_get**
> CustomValue manufacturer_id_id_get(id)

query a specific manufacturer

query a specific manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific manufacturer
        api_response = api_instance.manufacturer_id_id_get(id)
        print("The response of ManufacturerApi->manufacturer_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_id_id_get: %s\n" % e)
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

# **manufacturer_id_id_put**
> CustomValue manufacturer_id_id_put(id, custom_value, dry_run=dry_run)

update a manufacturer

update manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)
    id = 'id_example' # str | 
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # update a manufacturer
        api_response = api_instance.manufacturer_id_id_put(id, custom_value, dry_run=dry_run)
        print("The response of ManufacturerApi->manufacturer_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_id_id_put: %s\n" % e)
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
**200** | manufacturer update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manufacturer_post**
> CustomValue manufacturer_post(custom_value, dry_run=dry_run)

create a manufacturer

create a manufacturer

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
    api_instance = openapi_client.ManufacturerApi(api_client)
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # create a manufacturer
        api_response = api_instance.manufacturer_post(custom_value, dry_run=dry_run)
        print("The response of ManufacturerApi->manufacturer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManufacturerApi->manufacturer_post: %s\n" % e)
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
**201** | manufacturer create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

