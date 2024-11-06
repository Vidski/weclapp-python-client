# openapi_client.ArticleApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**article_count_get**](ArticleApi.md#article_count_get) | **GET** /article/count | count article
[**article_get**](ArticleApi.md#article_get) | **GET** /article | query article
[**article_id_id_change_unit_post**](ArticleApi.md#article_id_id_change_unit_post) | **POST** /article/id/{id}/changeUnit | 
[**article_id_id_create_datasheet_pdf_post**](ArticleApi.md#article_id_id_create_datasheet_pdf_post) | **POST** /article/id/{id}/createDatasheetPdf | 
[**article_id_id_create_label_pdf_post**](ArticleApi.md#article_id_id_create_label_pdf_post) | **POST** /article/id/{id}/createLabelPdf | 
[**article_id_id_delete**](ArticleApi.md#article_id_id_delete) | **DELETE** /article/id/{id} | delete a article
[**article_id_id_download_article_image_get**](ArticleApi.md#article_id_id_download_article_image_get) | **GET** /article/id/{id}/downloadArticleImage | 
[**article_id_id_download_main_article_image_get**](ArticleApi.md#article_id_id_download_main_article_image_get) | **GET** /article/id/{id}/downloadMainArticleImage | 
[**article_id_id_get**](ArticleApi.md#article_id_id_get) | **GET** /article/id/{id} | query a specific article
[**article_id_id_packaging_unit_structure_get**](ArticleApi.md#article_id_id_packaging_unit_structure_get) | **GET** /article/id/{id}/packagingUnitStructure | 
[**article_id_id_put**](ArticleApi.md#article_id_id_put) | **PUT** /article/id/{id} | update a article
[**article_id_id_upload_article_image_post**](ArticleApi.md#article_id_id_upload_article_image_post) | **POST** /article/id/{id}/uploadArticleImage | 
[**article_post**](ArticleApi.md#article_post) | **POST** /article | create a article


# **article_count_get**
> AccountingTransactionCountGet200Response article_count_get()

count article

count article

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
    api_instance = openapi_client.ArticleApi(api_client)

    try:
        # count article
        api_response = api_instance.article_count_get()
        print("The response of ArticleApi->article_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_count_get: %s\n" % e)
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

# **article_get**
> ArticleGet200Response article_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)

query article

query article

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_get200_response import ArticleGet200Response
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
    api_instance = openapi_client.ArticleApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)
    additional_properties = 'additional_properties_example' # str |  (optional)

    try:
        # query article
        api_response = api_instance.article_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)
        print("The response of ArticleApi->article_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_get: %s\n" % e)
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
 **additional_properties** | **str**|  | [optional] 

### Return type

[**ArticleGet200Response**](ArticleGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | article response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_change_unit_post**
> ArchivedEmailIdIdRemoveReferencePost200Response article_id_id_change_unit_post(id, article_id_id_change_unit_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.article_id_id_change_unit_post_request import ArticleIdIdChangeUnitPostRequest
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    article_id_id_change_unit_post_request = openapi_client.ArticleIdIdChangeUnitPostRequest() # ArticleIdIdChangeUnitPostRequest | 

    try:
        api_response = api_instance.article_id_id_change_unit_post(id, article_id_id_change_unit_post_request)
        print("The response of ArticleApi->article_id_id_change_unit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_change_unit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_id_id_change_unit_post_request** | [**ArticleIdIdChangeUnitPostRequest**](ArticleIdIdChangeUnitPostRequest.md)|  | 

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
**200** | changeUnit response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_create_datasheet_pdf_post**
> bytearray article_id_id_create_datasheet_pdf_post(id, article_id_id_create_datasheet_pdf_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_id_id_create_datasheet_pdf_post_request import ArticleIdIdCreateDatasheetPdfPostRequest
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    article_id_id_create_datasheet_pdf_post_request = openapi_client.ArticleIdIdCreateDatasheetPdfPostRequest() # ArticleIdIdCreateDatasheetPdfPostRequest | 

    try:
        api_response = api_instance.article_id_id_create_datasheet_pdf_post(id, article_id_id_create_datasheet_pdf_post_request)
        print("The response of ArticleApi->article_id_id_create_datasheet_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_create_datasheet_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_id_id_create_datasheet_pdf_post_request** | [**ArticleIdIdCreateDatasheetPdfPostRequest**](ArticleIdIdCreateDatasheetPdfPostRequest.md)|  | 

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
**200** | createDatasheetPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_create_label_pdf_post**
> bytearray article_id_id_create_label_pdf_post(id, article_id_id_create_label_pdf_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_id_id_create_label_pdf_post_request import ArticleIdIdCreateLabelPdfPostRequest
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    article_id_id_create_label_pdf_post_request = openapi_client.ArticleIdIdCreateLabelPdfPostRequest() # ArticleIdIdCreateLabelPdfPostRequest | 

    try:
        api_response = api_instance.article_id_id_create_label_pdf_post(id, article_id_id_create_label_pdf_post_request)
        print("The response of ArticleApi->article_id_id_create_label_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_create_label_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_id_id_create_label_pdf_post_request** | [**ArticleIdIdCreateLabelPdfPostRequest**](ArticleIdIdCreateLabelPdfPostRequest.md)|  | 

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
**200** | createLabelPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_delete**
> article_id_id_delete(id, dry_run=dry_run)

delete a article

delete a article

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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a article
        api_instance.article_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_delete: %s\n" % e)
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
**204** | article delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_download_article_image_get**
> bytearray article_id_id_download_article_image_get(id, article_image_id, preview=preview, scale_width=scale_width, scale_height=scale_height)



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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    article_image_id = 'article_image_id_example' # str | 
    preview = True # bool |  (optional)
    scale_width = 56 # int |  (optional)
    scale_height = 56 # int |  (optional)

    try:
        api_response = api_instance.article_id_id_download_article_image_get(id, article_image_id, preview=preview, scale_width=scale_width, scale_height=scale_height)
        print("The response of ArticleApi->article_id_id_download_article_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_download_article_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article_image_id** | **str**|  | 
 **preview** | **bool**|  | [optional] 
 **scale_width** | **int**|  | [optional] 
 **scale_height** | **int**|  | [optional] 

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
**200** | downloadArticleImage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_download_main_article_image_get**
> bytearray article_id_id_download_main_article_image_get(id, preview=preview, scale_width=scale_width, scale_height=scale_height)



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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    preview = True # bool |  (optional)
    scale_width = 56 # int |  (optional)
    scale_height = 56 # int |  (optional)

    try:
        api_response = api_instance.article_id_id_download_main_article_image_get(id, preview=preview, scale_width=scale_width, scale_height=scale_height)
        print("The response of ArticleApi->article_id_id_download_main_article_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_download_main_article_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **preview** | **bool**|  | [optional] 
 **scale_width** | **int**|  | [optional] 
 **scale_height** | **int**|  | [optional] 

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
**200** | downloadMainArticleImage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_get**
> Article article_id_id_get(id)

query a specific article

query a specific article

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article import Article
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific article
        api_response = api_instance.article_id_id_get(id)
        print("The response of ArticleApi->article_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Article**](Article.md)

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

# **article_id_id_packaging_unit_structure_get**
> ArticleIdIdPackagingUnitStructureGet200Response article_id_id_packaging_unit_structure_get(id)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_id_id_packaging_unit_structure_get200_response import ArticleIdIdPackagingUnitStructureGet200Response
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.article_id_id_packaging_unit_structure_get(id)
        print("The response of ArticleApi->article_id_id_packaging_unit_structure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_packaging_unit_structure_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArticleIdIdPackagingUnitStructureGet200Response**](ArticleIdIdPackagingUnitStructureGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | packagingUnitStructure response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_put**
> Article article_id_id_put(id, article, dry_run=dry_run)

update a article

update article

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article import Article
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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    article = openapi_client.Article() # Article | 
    dry_run = True # bool |  (optional)

    try:
        # update a article
        api_response = api_instance.article_id_id_put(id, article, dry_run=dry_run)
        print("The response of ArticleApi->article_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **article** | [**Article**](Article.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Article**](Article.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | article update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_id_id_upload_article_image_post**
> ArchivedEmailIdIdRemoveReferencePost200Response article_id_id_upload_article_image_post(id, name, body, main_image=main_image, article_image_id=article_image_id)



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
    api_instance = openapi_client.ArticleApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 
    body = None # bytearray | 
    main_image = True # bool |  (optional)
    article_image_id = 'article_image_id_example' # str |  (optional)

    try:
        api_response = api_instance.article_id_id_upload_article_image_post(id, name, body, main_image=main_image, article_image_id=article_image_id)
        print("The response of ArticleApi->article_id_id_upload_article_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_id_id_upload_article_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 
 **body** | **bytearray**|  | 
 **main_image** | **bool**|  | [optional] 
 **article_image_id** | **str**|  | [optional] 

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
**200** | uploadArticleImage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_post**
> Article article_post(article, dry_run=dry_run)

create a article

create a article

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article import Article
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
    api_instance = openapi_client.ArticleApi(api_client)
    article = openapi_client.Article() # Article | 
    dry_run = True # bool |  (optional)

    try:
        # create a article
        api_response = api_instance.article_post(article, dry_run=dry_run)
        print("The response of ArticleApi->article_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArticleApi->article_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article** | [**Article**](Article.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Article**](Article.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | article create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

