# openapi_client.QuotationApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotation_count_get**](QuotationApi.md#quotation_count_get) | **GET** /quotation/count | count quotation
[**quotation_get**](QuotationApi.md#quotation_get) | **GET** /quotation | query quotation
[**quotation_id_id_accept_post**](QuotationApi.md#quotation_id_id_accept_post) | **POST** /quotation/id/{id}/accept | 
[**quotation_id_id_create_new_version_post**](QuotationApi.md#quotation_id_id_create_new_version_post) | **POST** /quotation/id/{id}/createNewVersion | 
[**quotation_id_id_create_quotation_pdf_post**](QuotationApi.md#quotation_id_id_create_quotation_pdf_post) | **POST** /quotation/id/{id}/createQuotationPdf | 
[**quotation_id_id_delete**](QuotationApi.md#quotation_id_id_delete) | **DELETE** /quotation/id/{id} | delete a quotation
[**quotation_id_id_download_latest_quotation_pdf_get**](QuotationApi.md#quotation_id_id_download_latest_quotation_pdf_get) | **GET** /quotation/id/{id}/downloadLatestQuotationPdf | 
[**quotation_id_id_get**](QuotationApi.md#quotation_id_id_get) | **GET** /quotation/id/{id} | query a specific quotation
[**quotation_id_id_inquire_post**](QuotationApi.md#quotation_id_id_inquire_post) | **POST** /quotation/id/{id}/inquire | 
[**quotation_id_id_put**](QuotationApi.md#quotation_id_id_put) | **PUT** /quotation/id/{id} | update a quotation
[**quotation_post**](QuotationApi.md#quotation_post) | **POST** /quotation | create a quotation


# **quotation_count_get**
> AccountingTransactionCountGet200Response quotation_count_get()

count quotation

count quotation

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
    api_instance = openapi_client.QuotationApi(api_client)

    try:
        # count quotation
        api_response = api_instance.quotation_count_get()
        print("The response of QuotationApi->quotation_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_count_get: %s\n" % e)
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

# **quotation_get**
> QuotationGet200Response quotation_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query quotation

query quotation

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation_get200_response import QuotationGet200Response
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
    api_instance = openapi_client.QuotationApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query quotation
        api_response = api_instance.quotation_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of QuotationApi->quotation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_get: %s\n" % e)
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

[**QuotationGet200Response**](QuotationGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quotation response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_accept_post**
> quotation_id_id_accept_post(id, quotation_id_id_accept_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation_id_id_accept_post_request import QuotationIdIdAcceptPostRequest
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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    quotation_id_id_accept_post_request = openapi_client.QuotationIdIdAcceptPostRequest() # QuotationIdIdAcceptPostRequest | 

    try:
        api_instance.quotation_id_id_accept_post(id, quotation_id_id_accept_post_request)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_accept_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **quotation_id_id_accept_post_request** | [**QuotationIdIdAcceptPostRequest**](QuotationIdIdAcceptPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | accept response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_create_new_version_post**
> QuotationIdIdCreateNewVersionPost200Response quotation_id_id_create_new_version_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation_id_id_create_new_version_post200_response import QuotationIdIdCreateNewVersionPost200Response
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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.quotation_id_id_create_new_version_post(id, body)
        print("The response of QuotationApi->quotation_id_id_create_new_version_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_create_new_version_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**QuotationIdIdCreateNewVersionPost200Response**](QuotationIdIdCreateNewVersionPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createNewVersion response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_create_quotation_pdf_post**
> bytearray quotation_id_id_create_quotation_pdf_post(id, body)



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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.quotation_id_id_create_quotation_pdf_post(id, body)
        print("The response of QuotationApi->quotation_id_id_create_quotation_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_create_quotation_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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
**200** | createQuotationPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_delete**
> quotation_id_id_delete(id, dry_run=dry_run)

delete a quotation

delete a quotation

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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a quotation
        api_instance.quotation_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_delete: %s\n" % e)
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
**204** | quotation delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_download_latest_quotation_pdf_get**
> bytearray quotation_id_id_download_latest_quotation_pdf_get(id)



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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.quotation_id_id_download_latest_quotation_pdf_get(id)
        print("The response of QuotationApi->quotation_id_id_download_latest_quotation_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_download_latest_quotation_pdf_get: %s\n" % e)
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
**200** | downloadLatestQuotationPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_get**
> Quotation quotation_id_id_get(id)

query a specific quotation

query a specific quotation

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation import Quotation
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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific quotation
        api_response = api_instance.quotation_id_id_get(id)
        print("The response of QuotationApi->quotation_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Quotation**](Quotation.md)

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

# **quotation_id_id_inquire_post**
> QuotationIdIdCreateNewVersionPost200Response quotation_id_id_inquire_post(id, quotation_id_id_inquire_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation_id_id_create_new_version_post200_response import QuotationIdIdCreateNewVersionPost200Response
from openapi_client.models.quotation_id_id_inquire_post_request import QuotationIdIdInquirePostRequest
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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    quotation_id_id_inquire_post_request = openapi_client.QuotationIdIdInquirePostRequest() # QuotationIdIdInquirePostRequest | 

    try:
        api_response = api_instance.quotation_id_id_inquire_post(id, quotation_id_id_inquire_post_request)
        print("The response of QuotationApi->quotation_id_id_inquire_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_inquire_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **quotation_id_id_inquire_post_request** | [**QuotationIdIdInquirePostRequest**](QuotationIdIdInquirePostRequest.md)|  | 

### Return type

[**QuotationIdIdCreateNewVersionPost200Response**](QuotationIdIdCreateNewVersionPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | inquire response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_id_id_put**
> Quotation quotation_id_id_put(id, quotation, dry_run=dry_run)

update a quotation

update quotation

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation import Quotation
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
    api_instance = openapi_client.QuotationApi(api_client)
    id = 'id_example' # str | 
    quotation = openapi_client.Quotation() # Quotation | 
    dry_run = True # bool |  (optional)

    try:
        # update a quotation
        api_response = api_instance.quotation_id_id_put(id, quotation, dry_run=dry_run)
        print("The response of QuotationApi->quotation_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **quotation** | [**Quotation**](Quotation.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Quotation**](Quotation.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quotation update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotation_post**
> Quotation quotation_post(quotation, dry_run=dry_run)

create a quotation

create a quotation

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.quotation import Quotation
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
    api_instance = openapi_client.QuotationApi(api_client)
    quotation = openapi_client.Quotation() # Quotation | 
    dry_run = True # bool |  (optional)

    try:
        # create a quotation
        api_response = api_instance.quotation_post(quotation, dry_run=dry_run)
        print("The response of QuotationApi->quotation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotationApi->quotation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quotation** | [**Quotation**](Quotation.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Quotation**](Quotation.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | quotation create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

