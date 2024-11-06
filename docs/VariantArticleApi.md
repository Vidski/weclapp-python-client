# openapi_client.VariantArticleApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variant_article_count_get**](VariantArticleApi.md#variant_article_count_get) | **GET** /variantArticle/count | count variantArticle
[**variant_article_get**](VariantArticleApi.md#variant_article_get) | **GET** /variantArticle | query variantArticle
[**variant_article_id_id_delete**](VariantArticleApi.md#variant_article_id_id_delete) | **DELETE** /variantArticle/id/{id} | delete a variantArticle
[**variant_article_id_id_get**](VariantArticleApi.md#variant_article_id_id_get) | **GET** /variantArticle/id/{id} | query a specific variantArticle
[**variant_article_id_id_put**](VariantArticleApi.md#variant_article_id_id_put) | **PUT** /variantArticle/id/{id} | update a variantArticle
[**variant_article_post**](VariantArticleApi.md#variant_article_post) | **POST** /variantArticle | create a variantArticle


# **variant_article_count_get**
> AccountingTransactionCountGet200Response variant_article_count_get()

count variantArticle

count variantArticle

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
    api_instance = openapi_client.VariantArticleApi(api_client)

    try:
        # count variantArticle
        api_response = api_instance.variant_article_count_get()
        print("The response of VariantArticleApi->variant_article_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_count_get: %s\n" % e)
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

# **variant_article_get**
> VariantArticleGet200Response variant_article_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query variantArticle

query variantArticle

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article_get200_response import VariantArticleGet200Response
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
    api_instance = openapi_client.VariantArticleApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query variantArticle
        api_response = api_instance.variant_article_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of VariantArticleApi->variant_article_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_get: %s\n" % e)
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

[**VariantArticleGet200Response**](VariantArticleGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | variantArticle response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_id_id_delete**
> variant_article_id_id_delete(id, dry_run=dry_run)

delete a variantArticle

delete a variantArticle

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
    api_instance = openapi_client.VariantArticleApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a variantArticle
        api_instance.variant_article_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_id_id_delete: %s\n" % e)
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
**204** | variantArticle delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_id_id_get**
> VariantArticle variant_article_id_id_get(id)

query a specific variantArticle

query a specific variantArticle

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article import VariantArticle
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
    api_instance = openapi_client.VariantArticleApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific variantArticle
        api_response = api_instance.variant_article_id_id_get(id)
        print("The response of VariantArticleApi->variant_article_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VariantArticle**](VariantArticle.md)

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

# **variant_article_id_id_put**
> VariantArticle variant_article_id_id_put(id, variant_article, dry_run=dry_run)

update a variantArticle

update variantArticle

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article import VariantArticle
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
    api_instance = openapi_client.VariantArticleApi(api_client)
    id = 'id_example' # str | 
    variant_article = openapi_client.VariantArticle() # VariantArticle | 
    dry_run = True # bool |  (optional)

    try:
        # update a variantArticle
        api_response = api_instance.variant_article_id_id_put(id, variant_article, dry_run=dry_run)
        print("The response of VariantArticleApi->variant_article_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **variant_article** | [**VariantArticle**](VariantArticle.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**VariantArticle**](VariantArticle.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | variantArticle update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_post**
> VariantArticle variant_article_post(variant_article, dry_run=dry_run)

create a variantArticle

create a variantArticle

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article import VariantArticle
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
    api_instance = openapi_client.VariantArticleApi(api_client)
    variant_article = openapi_client.VariantArticle() # VariantArticle | 
    dry_run = True # bool |  (optional)

    try:
        # create a variantArticle
        api_response = api_instance.variant_article_post(variant_article, dry_run=dry_run)
        print("The response of VariantArticleApi->variant_article_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleApi->variant_article_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_article** | [**VariantArticle**](VariantArticle.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**VariantArticle**](VariantArticle.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | variantArticle create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

