# openapi_client.ArticleCategoryApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**article_category_count_get**](ArticleCategoryApi.md#article_category_count_get) | **GET** /articleCategory/count | count articleCategory
[**article_category_get**](ArticleCategoryApi.md#article_category_get) | **GET** /articleCategory | query articleCategory
[**article_category_id_id_delete**](ArticleCategoryApi.md#article_category_id_id_delete) | **DELETE** /articleCategory/id/{id} | delete a articleCategory
[**article_category_id_id_download_image_get**](ArticleCategoryApi.md#article_category_id_id_download_image_get) | **GET** /articleCategory/id/{id}/downloadImage | 
[**article_category_id_id_get**](ArticleCategoryApi.md#article_category_id_id_get) | **GET** /articleCategory/id/{id} | query a specific articleCategory
[**article_category_id_id_put**](ArticleCategoryApi.md#article_category_id_id_put) | **PUT** /articleCategory/id/{id} | update a articleCategory
[**article_category_id_id_upload_image_post**](ArticleCategoryApi.md#article_category_id_id_upload_image_post) | **POST** /articleCategory/id/{id}/uploadImage | 
[**article_category_post**](ArticleCategoryApi.md#article_category_post) | **POST** /articleCategory | create a articleCategory


# **article_category_count_get**
> AccountingTransactionCountGet200Response article_category_count_get()

count articleCategory

count articleCategory

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
    api_instance = openapi_client.ArticleCategoryApi(api_client)

    try:
        # count articleCategory
        api_response = api_instance.article_category_count_get()
        print("The response of ArticleCategoryApi->article_category_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_count_get: %s\n" % e)
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

# **article_category_get**
> ArticleCategoryGet200Response article_category_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query articleCategory

query articleCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_category_get200_response import ArticleCategoryGet200Response
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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query articleCategory
        api_response = api_instance.article_category_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ArticleCategoryApi->article_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_get: %s\n" % e)
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

[**ArticleCategoryGet200Response**](ArticleCategoryGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleCategory response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_category_id_id_delete**
> article_category_id_id_delete(id, dry_run=dry_run)

delete a articleCategory

delete a articleCategory

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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a articleCategory
        api_instance.article_category_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_id_id_delete: %s\n" % e)
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
**204** | articleCategory delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_category_id_id_download_image_get**
> bytearray article_category_id_id_download_image_get(id, scale_width=scale_width, scale_height=scale_height, image_id=image_id)



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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    id = 'id_example' # str | 
    scale_width = 56 # int |  (optional)
    scale_height = 56 # int |  (optional)
    image_id = 'image_id_example' # str |  (optional)

    try:
        api_response = api_instance.article_category_id_id_download_image_get(id, scale_width=scale_width, scale_height=scale_height, image_id=image_id)
        print("The response of ArticleCategoryApi->article_category_id_id_download_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_id_id_download_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scale_width** | **int**|  | [optional] 
 **scale_height** | **int**|  | [optional] 
 **image_id** | **str**|  | [optional] 

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
**200** | downloadImage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_category_id_id_get**
> ArticleCategory article_category_id_id_get(id)

query a specific articleCategory

query a specific articleCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_category import ArticleCategory
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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific articleCategory
        api_response = api_instance.article_category_id_id_get(id)
        print("The response of ArticleCategoryApi->article_category_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArticleCategory**](ArticleCategory.md)

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

# **article_category_id_id_put**
> ArticleCategory article_category_id_id_put(id, article_category, dry_run=dry_run)

update a articleCategory

update articleCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_category import ArticleCategory
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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    id = 'id_example' # str | 
    article_category = openapi_client.ArticleCategory() # ArticleCategory | 
    dry_run = True # bool |  (optional)

    try:
        # update a articleCategory
        api_response = api_instance.article_category_id_id_put(id, article_category, dry_run=dry_run)
        print("The response of ArticleCategoryApi->article_category_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_category** | [**ArticleCategory**](ArticleCategory.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleCategory**](ArticleCategory.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | articleCategory update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_category_id_id_upload_image_post**
> ArchivedEmailIdIdRemoveReferencePost200Response article_category_id_id_upload_image_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    id = 'id_example' # str | 
    body = None # bytearray | 

    try:
        api_response = api_instance.article_category_id_id_upload_image_post(id, body)
        print("The response of ArticleCategoryApi->article_category_id_id_upload_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_id_id_upload_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **bytearray**|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/pdf, image/jpeg, image/png
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | uploadImage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_category_post**
> ArticleCategory article_category_post(article_category, dry_run=dry_run)

create a articleCategory

create a articleCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_category import ArticleCategory
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
    api_instance = openapi_client.ArticleCategoryApi(api_client)
    article_category = openapi_client.ArticleCategory() # ArticleCategory | 
    dry_run = True # bool |  (optional)

    try:
        # create a articleCategory
        api_response = api_instance.article_category_post(article_category, dry_run=dry_run)
        print("The response of ArticleCategoryApi->article_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleCategoryApi->article_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_category** | [**ArticleCategory**](ArticleCategory.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ArticleCategory**](ArticleCategory.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | articleCategory create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

