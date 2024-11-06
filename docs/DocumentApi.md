# openapi_client.DocumentApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_copy_post**](DocumentApi.md#document_copy_post) | **POST** /document/copy | 
[**document_count_get**](DocumentApi.md#document_count_get) | **GET** /document/count | count document
[**document_get**](DocumentApi.md#document_get) | **GET** /document | query document
[**document_id_id_copy_post**](DocumentApi.md#document_id_id_copy_post) | **POST** /document/id/{id}/copy | 
[**document_id_id_delete**](DocumentApi.md#document_id_id_delete) | **DELETE** /document/id/{id} | delete a document
[**document_id_id_download_document_version_get**](DocumentApi.md#document_id_id_download_document_version_get) | **GET** /document/id/{id}/downloadDocumentVersion | 
[**document_id_id_download_document_versions_zipped_get**](DocumentApi.md#document_id_id_download_document_versions_zipped_get) | **GET** /document/id/{id}/downloadDocumentVersionsZipped | 
[**document_id_id_download_get**](DocumentApi.md#document_id_id_download_get) | **GET** /document/id/{id}/download | 
[**document_id_id_get**](DocumentApi.md#document_id_id_get) | **GET** /document/id/{id} | query a specific document
[**document_id_id_put**](DocumentApi.md#document_id_id_put) | **PUT** /document/id/{id} | update a document
[**document_id_id_upload_post**](DocumentApi.md#document_id_id_upload_post) | **POST** /document/id/{id}/upload | 
[**document_upload_post**](DocumentApi.md#document_upload_post) | **POST** /document/upload | 


# **document_copy_post**
> DocumentCopyPost200Response document_copy_post(document_copy_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document_copy_post200_response import DocumentCopyPost200Response
from openapi_client.models.document_copy_post_request import DocumentCopyPostRequest
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
    api_instance = openapi_client.DocumentApi(api_client)
    document_copy_post_request = openapi_client.DocumentCopyPostRequest() # DocumentCopyPostRequest | 

    try:
        api_response = api_instance.document_copy_post(document_copy_post_request)
        print("The response of DocumentApi->document_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_copy_post_request** | [**DocumentCopyPostRequest**](DocumentCopyPostRequest.md)|  | 

### Return type

[**DocumentCopyPost200Response**](DocumentCopyPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | copy response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_count_get**
> AccountingTransactionCountGet200Response document_count_get(entity_id, entity_name)

count document

count document

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
    api_instance = openapi_client.DocumentApi(api_client)
    entity_id = 'entity_id_example' # str | 
    entity_name = 'entity_name_example' # str | 

    try:
        # count document
        api_response = api_instance.document_count_get(entity_id, entity_name)
        print("The response of DocumentApi->document_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **entity_name** | **str**|  | 

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

# **document_get**
> DocumentGet200Response document_get(entity_id, entity_name, page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query document

query document

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document_get200_response import DocumentGet200Response
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
    api_instance = openapi_client.DocumentApi(api_client)
    entity_id = 'entity_id_example' # str | 
    entity_name = 'entity_name_example' # str | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query document
        api_response = api_instance.document_get(entity_id, entity_name, page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of DocumentApi->document_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **entity_name** | **str**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **serialize_nulls** | **bool**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **properties** | **str**|  | [optional] 
 **include_referenced_entities** | **str**|  | [optional] 

### Return type

[**DocumentGet200Response**](DocumentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | document response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_copy_post**
> DocumentCopyPost200Response document_id_id_copy_post(id, document_id_id_copy_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document_copy_post200_response import DocumentCopyPost200Response
from openapi_client.models.document_id_id_copy_post_request import DocumentIdIdCopyPostRequest
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    document_id_id_copy_post_request = openapi_client.DocumentIdIdCopyPostRequest() # DocumentIdIdCopyPostRequest | 

    try:
        api_response = api_instance.document_id_id_copy_post(id, document_id_id_copy_post_request)
        print("The response of DocumentApi->document_id_id_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **document_id_id_copy_post_request** | [**DocumentIdIdCopyPostRequest**](DocumentIdIdCopyPostRequest.md)|  | 

### Return type

[**DocumentCopyPost200Response**](DocumentCopyPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | copy response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_delete**
> document_id_id_delete(id, dry_run=dry_run)

delete a document

delete a document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a document
        api_instance.document_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_delete: %s\n" % e)
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
**204** | document delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_download_document_version_get**
> bytearray document_id_id_download_document_version_get(id, id2)



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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    id2 = 'id_example' # str | 

    try:
        api_response = api_instance.document_id_id_download_document_version_get(id, id2)
        print("The response of DocumentApi->document_id_id_download_document_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_download_document_version_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **id2** | **str**|  | 

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
**200** | downloadDocumentVersion response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_download_document_versions_zipped_get**
> bytearray document_id_id_download_document_versions_zipped_get(id, filename=filename, ids=ids)



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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    filename = 'filename_example' # str |  (optional)
    ids = ['ids_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.document_id_id_download_document_versions_zipped_get(id, filename=filename, ids=ids)
        print("The response of DocumentApi->document_id_id_download_document_versions_zipped_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_download_document_versions_zipped_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **filename** | **str**|  | [optional] 
 **ids** | [**List[str]**](str.md)|  | [optional] 

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
**200** | downloadDocumentVersionsZipped response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_download_get**
> bytearray document_id_id_download_get(id)



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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.document_id_id_download_get(id)
        print("The response of DocumentApi->document_id_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | download response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_get**
> Document document_id_id_get(id)

query a specific document

query a specific document

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document import Document
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific document
        api_response = api_instance.document_id_id_get(id)
        print("The response of DocumentApi->document_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Document**](Document.md)

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

# **document_id_id_put**
> Document document_id_id_put(id, document, dry_run=dry_run)

update a document

update document

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document import Document
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    document = openapi_client.Document() # Document | 
    dry_run = True # bool |  (optional)

    try:
        # update a document
        api_response = api_instance.document_id_id_put(id, document, dry_run=dry_run)
        print("The response of DocumentApi->document_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **document** | [**Document**](Document.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | document update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_id_id_upload_post**
> DocumentCopyPost200Response document_id_id_upload_post(id, body, comment=comment)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document_copy_post200_response import DocumentCopyPost200Response
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 'id_example' # str | 
    body = None # bytearray | 
    comment = 'comment_example' # str |  (optional)

    try:
        api_response = api_instance.document_id_id_upload_post(id, body, comment=comment)
        print("The response of DocumentApi->document_id_id_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_id_id_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **bytearray**|  | 
 **comment** | **str**|  | [optional] 

### Return type

[**DocumentCopyPost200Response**](DocumentCopyPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/pdf, image/jpeg, image/png
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | upload response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_upload_post**
> DocumentCopyPost200Response document_upload_post(entity_name, entity_id, name, body, description=description, document_type=document_type)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.document_copy_post200_response import DocumentCopyPost200Response
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
    api_instance = openapi_client.DocumentApi(api_client)
    entity_name = 'entity_name_example' # str | 
    entity_id = 'entity_id_example' # str | 
    name = 'name_example' # str | 
    body = None # bytearray | 
    description = 'description_example' # str |  (optional)
    document_type = 'document_type_example' # str |  (optional)

    try:
        api_response = api_instance.document_upload_post(entity_name, entity_id, name, body, description=description, document_type=document_type)
        print("The response of DocumentApi->document_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->document_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_name** | **str**|  | 
 **entity_id** | **str**|  | 
 **name** | **str**|  | 
 **body** | **bytearray**|  | 
 **description** | **str**|  | [optional] 
 **document_type** | **str**|  | [optional] 

### Return type

[**DocumentCopyPost200Response**](DocumentCopyPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/pdf, image/jpeg, image/png
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | upload response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

