# openapi_client.SalesInvoiceApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_invoice_count_get**](SalesInvoiceApi.md#sales_invoice_count_get) | **GET** /salesInvoice/count | count salesInvoice
[**sales_invoice_get**](SalesInvoiceApi.md#sales_invoice_get) | **GET** /salesInvoice | query salesInvoice
[**sales_invoice_id_id_add_sales_orders_post**](SalesInvoiceApi.md#sales_invoice_id_id_add_sales_orders_post) | **POST** /salesInvoice/id/{id}/addSalesOrders | 
[**sales_invoice_id_id_create_credit_note_post**](SalesInvoiceApi.md#sales_invoice_id_id_create_credit_note_post) | **POST** /salesInvoice/id/{id}/createCreditNote | 
[**sales_invoice_id_id_delete**](SalesInvoiceApi.md#sales_invoice_id_id_delete) | **DELETE** /salesInvoice/id/{id} | delete a salesInvoice
[**sales_invoice_id_id_download_latest_sales_invoice_pdf_get**](SalesInvoiceApi.md#sales_invoice_id_id_download_latest_sales_invoice_pdf_get) | **GET** /salesInvoice/id/{id}/downloadLatestSalesInvoicePdf | 
[**sales_invoice_id_id_get**](SalesInvoiceApi.md#sales_invoice_id_id_get) | **GET** /salesInvoice/id/{id} | query a specific salesInvoice
[**sales_invoice_id_id_put**](SalesInvoiceApi.md#sales_invoice_id_id_put) | **PUT** /salesInvoice/id/{id} | update a salesInvoice
[**sales_invoice_post**](SalesInvoiceApi.md#sales_invoice_post) | **POST** /salesInvoice | create a salesInvoice


# **sales_invoice_count_get**
> AccountingTransactionCountGet200Response sales_invoice_count_get()

count salesInvoice

count salesInvoice

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
    api_instance = openapi_client.SalesInvoiceApi(api_client)

    try:
        # count salesInvoice
        api_response = api_instance.sales_invoice_count_get()
        print("The response of SalesInvoiceApi->sales_invoice_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_count_get: %s\n" % e)
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

# **sales_invoice_get**
> SalesInvoiceGet200Response sales_invoice_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query salesInvoice

query salesInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_invoice_get200_response import SalesInvoiceGet200Response
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query salesInvoice
        api_response = api_instance.sales_invoice_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of SalesInvoiceApi->sales_invoice_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_get: %s\n" % e)
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

[**SalesInvoiceGet200Response**](SalesInvoiceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | salesInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_id_id_add_sales_orders_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_invoice_id_id_add_sales_orders_post(id, sales_invoice_id_id_add_sales_orders_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_credit_note_post200_response import IncomingGoodsIdIdCreateCreditNotePost200Response
from openapi_client.models.sales_invoice_id_id_add_sales_orders_post_request import SalesInvoiceIdIdAddSalesOrdersPostRequest
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 
    sales_invoice_id_id_add_sales_orders_post_request = openapi_client.SalesInvoiceIdIdAddSalesOrdersPostRequest() # SalesInvoiceIdIdAddSalesOrdersPostRequest | 

    try:
        api_response = api_instance.sales_invoice_id_id_add_sales_orders_post(id, sales_invoice_id_id_add_sales_orders_post_request)
        print("The response of SalesInvoiceApi->sales_invoice_id_id_add_sales_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_add_sales_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_invoice_id_id_add_sales_orders_post_request** | [**SalesInvoiceIdIdAddSalesOrdersPostRequest**](SalesInvoiceIdIdAddSalesOrdersPostRequest.md)|  | 

### Return type

[**IncomingGoodsIdIdCreateCreditNotePost200Response**](IncomingGoodsIdIdCreateCreditNotePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | addSalesOrders response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_id_id_create_credit_note_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_invoice_id_id_create_credit_note_post(id, purchase_invoice_id_id_create_credit_note_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_credit_note_post200_response import IncomingGoodsIdIdCreateCreditNotePost200Response
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 
    purchase_invoice_id_id_create_credit_note_post_request = openapi_client.PurchaseInvoiceIdIdCreateCreditNotePostRequest() # PurchaseInvoiceIdIdCreateCreditNotePostRequest | 

    try:
        api_response = api_instance.sales_invoice_id_id_create_credit_note_post(id, purchase_invoice_id_id_create_credit_note_post_request)
        print("The response of SalesInvoiceApi->sales_invoice_id_id_create_credit_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_create_credit_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_invoice_id_id_create_credit_note_post_request** | [**PurchaseInvoiceIdIdCreateCreditNotePostRequest**](PurchaseInvoiceIdIdCreateCreditNotePostRequest.md)|  | 

### Return type

[**IncomingGoodsIdIdCreateCreditNotePost200Response**](IncomingGoodsIdIdCreateCreditNotePost200Response.md)

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

# **sales_invoice_id_id_delete**
> sales_invoice_id_id_delete(id, dry_run=dry_run)

delete a salesInvoice

delete a salesInvoice

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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a salesInvoice
        api_instance.sales_invoice_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_delete: %s\n" % e)
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
**204** | salesInvoice delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_id_id_download_latest_sales_invoice_pdf_get**
> bytearray sales_invoice_id_id_download_latest_sales_invoice_pdf_get(id)



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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.sales_invoice_id_id_download_latest_sales_invoice_pdf_get(id)
        print("The response of SalesInvoiceApi->sales_invoice_id_id_download_latest_sales_invoice_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_download_latest_sales_invoice_pdf_get: %s\n" % e)
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
**200** | downloadLatestSalesInvoicePdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_id_id_get**
> SalesInvoice sales_invoice_id_id_get(id)

query a specific salesInvoice

query a specific salesInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_invoice import SalesInvoice
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific salesInvoice
        api_response = api_instance.sales_invoice_id_id_get(id)
        print("The response of SalesInvoiceApi->sales_invoice_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

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

# **sales_invoice_id_id_put**
> SalesInvoice sales_invoice_id_id_put(id, sales_invoice, dry_run=dry_run)

update a salesInvoice

update salesInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_invoice import SalesInvoice
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    id = 'id_example' # str | 
    sales_invoice = openapi_client.SalesInvoice() # SalesInvoice | 
    dry_run = True # bool |  (optional)

    try:
        # update a salesInvoice
        api_response = api_instance.sales_invoice_id_id_put(id, sales_invoice, dry_run=dry_run)
        print("The response of SalesInvoiceApi->sales_invoice_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_invoice** | [**SalesInvoice**](SalesInvoice.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | salesInvoice update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_post**
> SalesInvoice sales_invoice_post(sales_invoice, dry_run=dry_run)

create a salesInvoice

create a salesInvoice

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_invoice import SalesInvoice
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
    api_instance = openapi_client.SalesInvoiceApi(api_client)
    sales_invoice = openapi_client.SalesInvoice() # SalesInvoice | 
    dry_run = True # bool |  (optional)

    try:
        # create a salesInvoice
        api_response = api_instance.sales_invoice_post(sales_invoice, dry_run=dry_run)
        print("The response of SalesInvoiceApi->sales_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->sales_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_invoice** | [**SalesInvoice**](SalesInvoice.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | salesInvoice create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

