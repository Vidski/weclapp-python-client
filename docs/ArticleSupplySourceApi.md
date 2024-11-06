# openapi_client.ArticleSupplySourceApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**article_supply_source_count_get**](ArticleSupplySourceApi.md#article_supply_source_count_get) | **GET** /articleSupplySource/count | count articleSupplySource
[**article_supply_source_get**](ArticleSupplySourceApi.md#article_supply_source_get) | **GET** /articleSupplySource | query articleSupplySource
[**article_supply_source_id_id_delete**](ArticleSupplySourceApi.md#article_supply_source_id_id_delete) | **DELETE** /articleSupplySource/id/{id} | delete a articleSupplySource
[**article_supply_source_id_id_get**](ArticleSupplySourceApi.md#article_supply_source_id_id_get) | **GET** /articleSupplySource/id/{id} | query a specific articleSupplySource
[**article_supply_source_id_id_put**](ArticleSupplySourceApi.md#article_supply_source_id_id_put) | **PUT** /articleSupplySource/id/{id} | update a articleSupplySource
[**article_supply_source_post**](ArticleSupplySourceApi.md#article_supply_source_post) | **POST** /articleSupplySource | create a articleSupplySource


# **article_supply_source_count_get**
> AccountingTransactionCountGet200Response article_supply_source_count_get()

count articleSupplySource

count articleSupplySource

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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)

    try:
        # count articleSupplySource
        api_response = api_instance.article_supply_source_count_get()
        print("The response of ArticleSupplySourceApi->article_supply_source_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_count_get: %s\n" % e)
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

# **article_supply_source_get**
> ArticleSupplySourceGet200Response article_supply_source_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query articleSupplySource

query articleSupplySource

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_supply_source_get200_response import ArticleSupplySourceGet200Response
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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query articleSupplySource
        api_response = api_instance.article_supply_source_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ArticleSupplySourceApi->article_supply_source_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_get: %s\n" % e)
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

[**ArticleSupplySourceGet200Response**](ArticleSupplySourceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleSupplySource response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_supply_source_id_id_delete**
> article_supply_source_id_id_delete(id, dry_run=dry_run)

delete a articleSupplySource

delete a articleSupplySource

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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a articleSupplySource
        api_instance.article_supply_source_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_id_id_delete: %s\n" % e)
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
**204** | articleSupplySource delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_supply_source_id_id_get**
> ArticleSupplySource article_supply_source_id_id_get(id)

query a specific articleSupplySource

query a specific articleSupplySource

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_supply_source import ArticleSupplySource
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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific articleSupplySource
        api_response = api_instance.article_supply_source_id_id_get(id)
        print("The response of ArticleSupplySourceApi->article_supply_source_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArticleSupplySource**](ArticleSupplySource.md)

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

# **article_supply_source_id_id_put**
> ArticleSupplySource article_supply_source_id_id_put(id, article_supply_source, dry_run=dry_run)

update a articleSupplySource

update articleSupplySource

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_supply_source import ArticleSupplySource
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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)
    id = 'id_example' # str | 
    article_supply_source = openapi_client.ArticleSupplySource() # ArticleSupplySource | 
    dry_run = True # bool |  (optional)

    try:
        # update a articleSupplySource
        api_response = api_instance.article_supply_source_id_id_put(id, article_supply_source, dry_run=dry_run)
        print("The response of ArticleSupplySourceApi->article_supply_source_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_supply_source** | [**ArticleSupplySource**](ArticleSupplySource.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleSupplySource**](ArticleSupplySource.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleSupplySource update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_supply_source_post**
> ArticleSupplySource article_supply_source_post(article_supply_source, dry_run=dry_run)

create a articleSupplySource

create a articleSupplySource

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_supply_source import ArticleSupplySource
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
    api_instance = openapi_client.ArticleSupplySourceApi(api_client)
    article_supply_source = openapi_client.ArticleSupplySource() # ArticleSupplySource | 
    dry_run = True # bool |  (optional)

    try:
        # create a articleSupplySource
        api_response = api_instance.article_supply_source_post(article_supply_source, dry_run=dry_run)
        print("The response of ArticleSupplySourceApi->article_supply_source_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleSupplySourceApi->article_supply_source_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_supply_source** | [**ArticleSupplySource**](ArticleSupplySource.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleSupplySource**](ArticleSupplySource.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | articleSupplySource create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

