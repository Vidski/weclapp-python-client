# openapi_client.PurchaseInvoiceApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_invoice_count_get**](PurchaseInvoiceApi.md#purchase_invoice_count_get) | **GET** /purchaseInvoice/count | count purchaseInvoice
[**purchase_invoice_get**](PurchaseInvoiceApi.md#purchase_invoice_get) | **GET** /purchaseInvoice | query purchaseInvoice
[**purchase_invoice_id_id_create_credit_note_post**](PurchaseInvoiceApi.md#purchase_invoice_id_id_create_credit_note_post) | **POST** /purchaseInvoice/id/{id}/createCreditNote | 
[**purchase_invoice_id_id_delete**](PurchaseInvoiceApi.md#purchase_invoice_id_id_delete) | **DELETE** /purchaseInvoice/id/{id} | delete a purchaseInvoice
[**purchase_invoice_id_id_download_latest_purchase_invoice_document_get**](PurchaseInvoiceApi.md#purchase_invoice_id_id_download_latest_purchase_invoice_document_get) | **GET** /purchaseInvoice/id/{id}/downloadLatestPurchaseInvoiceDocument | 
[**purchase_invoice_id_id_get**](PurchaseInvoiceApi.md#purchase_invoice_id_id_get) | **GET** /purchaseInvoice/id/{id} | query a specific purchaseInvoice
[**purchase_invoice_id_id_put**](PurchaseInvoiceApi.md#purchase_invoice_id_id_put) | **PUT** /purchaseInvoice/id/{id} | update a purchaseInvoice
[**purchase_invoice_post**](PurchaseInvoiceApi.md#purchase_invoice_post) | **POST** /purchaseInvoice | create a purchaseInvoice


# **purchase_invoice_count_get**
> AccountingTransactionCountGet200Response purchase_invoice_count_get()

count purchaseInvoice

count purchaseInvoice

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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)

    try:
        # count purchaseInvoice
        api_response = api_instance.purchase_invoice_count_get()
        print("The response of PurchaseInvoiceApi->purchase_invoice_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_count_get: %s\n" % e)
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

# **purchase_invoice_get**
> PurchaseInvoiceGet200Response purchase_invoice_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query purchaseInvoice

query purchaseInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice_get200_response import PurchaseInvoiceGet200Response
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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query purchaseInvoice
        api_response = api_instance.purchase_invoice_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of PurchaseInvoiceApi->purchase_invoice_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_get: %s\n" % e)
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

[**PurchaseInvoiceGet200Response**](PurchaseInvoiceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_invoice_id_id_create_credit_note_post**
> PurchaseInvoiceIdIdCreateCreditNotePost200Response purchase_invoice_id_id_create_credit_note_post(id, purchase_invoice_id_id_create_credit_note_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice_id_id_create_credit_note_post200_response import PurchaseInvoiceIdIdCreateCreditNotePost200Response
from openapi_client.models.purchase_invoice_id_id_create_credit_note_post_request import PurchaseInvoiceIdIdCreateCreditNotePostRequest
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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    id = 'id_example' # str | 
    purchase_invoice_id_id_create_credit_note_post_request = openapi_client.PurchaseInvoiceIdIdCreateCreditNotePostRequest() # PurchaseInvoiceIdIdCreateCreditNotePostRequest | 

    try:
        api_response = api_instance.purchase_invoice_id_id_create_credit_note_post(id, purchase_invoice_id_id_create_credit_note_post_request)
        print("The response of PurchaseInvoiceApi->purchase_invoice_id_id_create_credit_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_id_id_create_credit_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_invoice_id_id_create_credit_note_post_request** | [**PurchaseInvoiceIdIdCreateCreditNotePostRequest**](PurchaseInvoiceIdIdCreateCreditNotePostRequest.md)|  | 

### Return type

[**PurchaseInvoiceIdIdCreateCreditNotePost200Response**](PurchaseInvoiceIdIdCreateCreditNotePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createCreditNote response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_invoice_id_id_delete**
> purchase_invoice_id_id_delete(id, dry_run=dry_run)

delete a purchaseInvoice

delete a purchaseInvoice

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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a purchaseInvoice
        api_instance.purchase_invoice_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_id_id_delete: %s\n" % e)
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
**204** | purchaseInvoice delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_invoice_id_id_download_latest_purchase_invoice_document_get**
> bytearray purchase_invoice_id_id_download_latest_purchase_invoice_document_get(id)



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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.purchase_invoice_id_id_download_latest_purchase_invoice_document_get(id)
        print("The response of PurchaseInvoiceApi->purchase_invoice_id_id_download_latest_purchase_invoice_document_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_id_id_download_latest_purchase_invoice_document_get: %s\n" % e)
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
**200** | downloadLatestPurchaseInvoiceDocument response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_invoice_id_id_get**
> PurchaseInvoice purchase_invoice_id_id_get(id)

query a specific purchaseInvoice

query a specific purchaseInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice import PurchaseInvoice
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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific purchaseInvoice
        api_response = api_instance.purchase_invoice_id_id_get(id)
        print("The response of PurchaseInvoiceApi->purchase_invoice_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

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

# **purchase_invoice_id_id_put**
> PurchaseInvoice purchase_invoice_id_id_put(id, purchase_invoice, dry_run=dry_run)

update a purchaseInvoice

update purchaseInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice import PurchaseInvoice
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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    id = 'id_example' # str | 
    purchase_invoice = openapi_client.PurchaseInvoice() # PurchaseInvoice | 
    dry_run = True # bool |  (optional)

    try:
        # update a purchaseInvoice
        api_response = api_instance.purchase_invoice_id_id_put(id, purchase_invoice, dry_run=dry_run)
        print("The response of PurchaseInvoiceApi->purchase_invoice_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_invoice** | [**PurchaseInvoice**](PurchaseInvoice.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseInvoice update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_invoice_post**
> PurchaseInvoice purchase_invoice_post(purchase_invoice, dry_run=dry_run)

create a purchaseInvoice

create a purchaseInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice import PurchaseInvoice
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
    api_instance = openapi_client.PurchaseInvoiceApi(api_client)
    purchase_invoice = openapi_client.PurchaseInvoice() # PurchaseInvoice | 
    dry_run = True # bool |  (optional)

    try:
        # create a purchaseInvoice
        api_response = api_instance.purchase_invoice_post(purchase_invoice, dry_run=dry_run)
        print("The response of PurchaseInvoiceApi->purchase_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->purchase_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_invoice** | [**PurchaseInvoice**](PurchaseInvoice.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | purchaseInvoice create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

