# openapi_client.ArticleItemGroupApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**article_item_group_count_get**](ArticleItemGroupApi.md#article_item_group_count_get) | **GET** /articleItemGroup/count | count articleItemGroup
[**article_item_group_get**](ArticleItemGroupApi.md#article_item_group_get) | **GET** /articleItemGroup | query articleItemGroup
[**article_item_group_id_id_delete**](ArticleItemGroupApi.md#article_item_group_id_id_delete) | **DELETE** /articleItemGroup/id/{id} | delete a articleItemGroup
[**article_item_group_id_id_get**](ArticleItemGroupApi.md#article_item_group_id_id_get) | **GET** /articleItemGroup/id/{id} | query a specific articleItemGroup
[**article_item_group_id_id_put**](ArticleItemGroupApi.md#article_item_group_id_id_put) | **PUT** /articleItemGroup/id/{id} | update a articleItemGroup
[**article_item_group_post**](ArticleItemGroupApi.md#article_item_group_post) | **POST** /articleItemGroup | create a articleItemGroup


# **article_item_group_count_get**
> AccountingTransactionCountGet200Response article_item_group_count_get()

count articleItemGroup

count articleItemGroup

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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)

    try:
        # count articleItemGroup
        api_response = api_instance.article_item_group_count_get()
        print("The response of ArticleItemGroupApi->article_item_group_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_count_get: %s\n" % e)
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

# **article_item_group_get**
> ArticleItemGroupGet200Response article_item_group_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query articleItemGroup

query articleItemGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_item_group_get200_response import ArticleItemGroupGet200Response
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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query articleItemGroup
        api_response = api_instance.article_item_group_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ArticleItemGroupApi->article_item_group_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_get: %s\n" % e)
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

[**ArticleItemGroupGet200Response**](ArticleItemGroupGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleItemGroup response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_item_group_id_id_delete**
> article_item_group_id_id_delete(id, dry_run=dry_run)

delete a articleItemGroup

delete a articleItemGroup

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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a articleItemGroup
        api_instance.article_item_group_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_id_id_delete: %s\n" % e)
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
**204** | articleItemGroup delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_item_group_id_id_get**
> ArticleItemGroup article_item_group_id_id_get(id)

query a specific articleItemGroup

query a specific articleItemGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_item_group import ArticleItemGroup
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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific articleItemGroup
        api_response = api_instance.article_item_group_id_id_get(id)
        print("The response of ArticleItemGroupApi->article_item_group_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArticleItemGroup**](ArticleItemGroup.md)

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

# **article_item_group_id_id_put**
> ArticleItemGroup article_item_group_id_id_put(id, article_item_group, dry_run=dry_run)

update a articleItemGroup

update articleItemGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_item_group import ArticleItemGroup
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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)
    id = 'id_example' # str | 
    article_item_group = openapi_client.ArticleItemGroup() # ArticleItemGroup | 
    dry_run = True # bool |  (optional)

    try:
        # update a articleItemGroup
        api_response = api_instance.article_item_group_id_id_put(id, article_item_group, dry_run=dry_run)
        print("The response of ArticleItemGroupApi->article_item_group_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_item_group** | [**ArticleItemGroup**](ArticleItemGroup.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleItemGroup**](ArticleItemGroup.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleItemGroup update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_item_group_post**
> ArticleItemGroup article_item_group_post(article_item_group, dry_run=dry_run)

create a articleItemGroup

create a articleItemGroup

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_item_group import ArticleItemGroup
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
    api_instance = openapi_client.ArticleItemGroupApi(api_client)
    article_item_group = openapi_client.ArticleItemGroup() # ArticleItemGroup | 
    dry_run = True # bool |  (optional)

    try:
        # create a articleItemGroup
        api_response = api_instance.article_item_group_post(article_item_group, dry_run=dry_run)
        print("The response of ArticleItemGroupApi->article_item_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleItemGroupApi->article_item_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_item_group** | [**ArticleItemGroup**](ArticleItemGroup.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleItemGroup**](ArticleItemGroup.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | articleItemGroup create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

