# openapi_client.VariantArticleAttributeApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variant_article_attribute_count_get**](VariantArticleAttributeApi.md#variant_article_attribute_count_get) | **GET** /variantArticleAttribute/count | count variantArticleAttribute
[**variant_article_attribute_get**](VariantArticleAttributeApi.md#variant_article_attribute_get) | **GET** /variantArticleAttribute | query variantArticleAttribute
[**variant_article_attribute_id_id_delete**](VariantArticleAttributeApi.md#variant_article_attribute_id_id_delete) | **DELETE** /variantArticleAttribute/id/{id} | delete a variantArticleAttribute
[**variant_article_attribute_id_id_get**](VariantArticleAttributeApi.md#variant_article_attribute_id_id_get) | **GET** /variantArticleAttribute/id/{id} | query a specific variantArticleAttribute
[**variant_article_attribute_id_id_put**](VariantArticleAttributeApi.md#variant_article_attribute_id_id_put) | **PUT** /variantArticleAttribute/id/{id} | update a variantArticleAttribute
[**variant_article_attribute_post**](VariantArticleAttributeApi.md#variant_article_attribute_post) | **POST** /variantArticleAttribute | create a variantArticleAttribute


# **variant_article_attribute_count_get**
> AccountingTransactionCountGet200Response variant_article_attribute_count_get()

count variantArticleAttribute

count variantArticleAttribute

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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)

    try:
        # count variantArticleAttribute
        api_response = api_instance.variant_article_attribute_count_get()
        print("The response of VariantArticleAttributeApi->variant_article_attribute_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_count_get: %s\n" % e)
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

# **variant_article_attribute_get**
> VariantArticleAttributeGet200Response variant_article_attribute_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query variantArticleAttribute

query variantArticleAttribute

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article_attribute_get200_response import VariantArticleAttributeGet200Response
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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query variantArticleAttribute
        api_response = api_instance.variant_article_attribute_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of VariantArticleAttributeApi->variant_article_attribute_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_get: %s\n" % e)
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

[**VariantArticleAttributeGet200Response**](VariantArticleAttributeGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | variantArticleAttribute response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_attribute_id_id_delete**
> variant_article_attribute_id_id_delete(id, dry_run=dry_run)

delete a variantArticleAttribute

delete a variantArticleAttribute

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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a variantArticleAttribute
        api_instance.variant_article_attribute_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_id_id_delete: %s\n" % e)
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
**204** | variantArticleAttribute delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_attribute_id_id_get**
> VariantArticleAttribute variant_article_attribute_id_id_get(id)

query a specific variantArticleAttribute

query a specific variantArticleAttribute

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article_attribute import VariantArticleAttribute
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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific variantArticleAttribute
        api_response = api_instance.variant_article_attribute_id_id_get(id)
        print("The response of VariantArticleAttributeApi->variant_article_attribute_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**VariantArticleAttribute**](VariantArticleAttribute.md)

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

# **variant_article_attribute_id_id_put**
> VariantArticleAttribute variant_article_attribute_id_id_put(id, variant_article_attribute, dry_run=dry_run)

update a variantArticleAttribute

update variantArticleAttribute

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article_attribute import VariantArticleAttribute
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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)
    id = 'id_example' # str | 
    variant_article_attribute = openapi_client.VariantArticleAttribute() # VariantArticleAttribute | 
    dry_run = True # bool |  (optional)

    try:
        # update a variantArticleAttribute
        api_response = api_instance.variant_article_attribute_id_id_put(id, variant_article_attribute, dry_run=dry_run)
        print("The response of VariantArticleAttributeApi->variant_article_attribute_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **variant_article_attribute** | [**VariantArticleAttribute**](VariantArticleAttribute.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**VariantArticleAttribute**](VariantArticleAttribute.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | variantArticleAttribute update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variant_article_attribute_post**
> VariantArticleAttribute variant_article_attribute_post(variant_article_attribute, dry_run=dry_run)

create a variantArticleAttribute

create a variantArticleAttribute

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.variant_article_attribute import VariantArticleAttribute
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
    api_instance = openapi_client.VariantArticleAttributeApi(api_client)
    variant_article_attribute = openapi_client.VariantArticleAttribute() # VariantArticleAttribute | 
    dry_run = True # bool |  (optional)

    try:
        # create a variantArticleAttribute
        api_response = api_instance.variant_article_attribute_post(variant_article_attribute, dry_run=dry_run)
        print("The response of VariantArticleAttributeApi->variant_article_attribute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariantArticleAttributeApi->variant_article_attribute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_article_attribute** | [**VariantArticleAttribute**](VariantArticleAttribute.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**VariantArticleAttribute**](VariantArticleAttribute.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | variantArticleAttribute create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

