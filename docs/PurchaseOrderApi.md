# openapi_client.PurchaseOrderApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_order_count_get**](PurchaseOrderApi.md#purchase_order_count_get) | **GET** /purchaseOrder/count | count purchaseOrder
[**purchase_order_get**](PurchaseOrderApi.md#purchase_order_get) | **GET** /purchaseOrder | query purchaseOrder
[**purchase_order_id_id_create_dropshipping_delivery_note_pdf_post**](PurchaseOrderApi.md#purchase_order_id_id_create_dropshipping_delivery_note_pdf_post) | **POST** /purchaseOrder/id/{id}/createDropshippingDeliveryNotePdf | 
[**purchase_order_id_id_create_incoming_goods_post**](PurchaseOrderApi.md#purchase_order_id_id_create_incoming_goods_post) | **POST** /purchaseOrder/id/{id}/createIncomingGoods | 
[**purchase_order_id_id_create_purchase_invoice_post**](PurchaseOrderApi.md#purchase_order_id_id_create_purchase_invoice_post) | **POST** /purchaseOrder/id/{id}/createPurchaseInvoice | 
[**purchase_order_id_id_create_supplier_return_post**](PurchaseOrderApi.md#purchase_order_id_id_create_supplier_return_post) | **POST** /purchaseOrder/id/{id}/createSupplierReturn | 
[**purchase_order_id_id_delete**](PurchaseOrderApi.md#purchase_order_id_id_delete) | **DELETE** /purchaseOrder/id/{id} | delete a purchaseOrder
[**purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get**](PurchaseOrderApi.md#purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get) | **GET** /purchaseOrder/id/{id}/downloadLatestDropshippingDeliveryNotePdf | 
[**purchase_order_id_id_download_latest_purchase_order_pdf_get**](PurchaseOrderApi.md#purchase_order_id_id_download_latest_purchase_order_pdf_get) | **GET** /purchaseOrder/id/{id}/downloadLatestPurchaseOrderPdf | 
[**purchase_order_id_id_get**](PurchaseOrderApi.md#purchase_order_id_id_get) | **GET** /purchaseOrder/id/{id} | query a specific purchaseOrder
[**purchase_order_id_id_process_dropshipping_post**](PurchaseOrderApi.md#purchase_order_id_id_process_dropshipping_post) | **POST** /purchaseOrder/id/{id}/processDropshipping | 
[**purchase_order_id_id_put**](PurchaseOrderApi.md#purchase_order_id_id_put) | **PUT** /purchaseOrder/id/{id} | update a purchaseOrder
[**purchase_order_post**](PurchaseOrderApi.md#purchase_order_post) | **POST** /purchaseOrder | create a purchaseOrder


# **purchase_order_count_get**
> AccountingTransactionCountGet200Response purchase_order_count_get()

count purchaseOrder

count purchaseOrder

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
    api_instance = openapi_client.PurchaseOrderApi(api_client)

    try:
        # count purchaseOrder
        api_response = api_instance.purchase_order_count_get()
        print("The response of PurchaseOrderApi->purchase_order_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_count_get: %s\n" % e)
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

# **purchase_order_get**
> PurchaseOrderGet200Response purchase_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query purchaseOrder

query purchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_get200_response import PurchaseOrderGet200Response
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query purchaseOrder
        api_response = api_instance.purchase_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of PurchaseOrderApi->purchase_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_get: %s\n" % e)
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

[**PurchaseOrderGet200Response**](PurchaseOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_create_dropshipping_delivery_note_pdf_post**
> bytearray purchase_order_id_id_create_dropshipping_delivery_note_pdf_post(id, body)



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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.purchase_order_id_id_create_dropshipping_delivery_note_pdf_post(id, body)
        print("The response of PurchaseOrderApi->purchase_order_id_id_create_dropshipping_delivery_note_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_create_dropshipping_delivery_note_pdf_post: %s\n" % e)
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
**200** | createDropshippingDeliveryNotePdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_create_incoming_goods_post**
> IncomingGoodsIdIdAddPurchaseOrdersPost200Response purchase_order_id_id_create_incoming_goods_post(id, purchase_order_id_id_create_incoming_goods_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_add_purchase_orders_post200_response import IncomingGoodsIdIdAddPurchaseOrdersPost200Response
from openapi_client.models.purchase_order_id_id_create_incoming_goods_post_request import PurchaseOrderIdIdCreateIncomingGoodsPostRequest
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    purchase_order_id_id_create_incoming_goods_post_request = openapi_client.PurchaseOrderIdIdCreateIncomingGoodsPostRequest() # PurchaseOrderIdIdCreateIncomingGoodsPostRequest | 

    try:
        api_response = api_instance.purchase_order_id_id_create_incoming_goods_post(id, purchase_order_id_id_create_incoming_goods_post_request)
        print("The response of PurchaseOrderApi->purchase_order_id_id_create_incoming_goods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_create_incoming_goods_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order_id_id_create_incoming_goods_post_request** | [**PurchaseOrderIdIdCreateIncomingGoodsPostRequest**](PurchaseOrderIdIdCreateIncomingGoodsPostRequest.md)|  | 

### Return type

[**IncomingGoodsIdIdAddPurchaseOrdersPost200Response**](IncomingGoodsIdIdAddPurchaseOrdersPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createIncomingGoods response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_create_purchase_invoice_post**
> PurchaseInvoiceIdIdCreateCreditNotePost200Response purchase_order_id_id_create_purchase_invoice_post(id, purchase_order_id_id_create_purchase_invoice_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_invoice_id_id_create_credit_note_post200_response import PurchaseInvoiceIdIdCreateCreditNotePost200Response
from openapi_client.models.purchase_order_id_id_create_purchase_invoice_post_request import PurchaseOrderIdIdCreatePurchaseInvoicePostRequest
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    purchase_order_id_id_create_purchase_invoice_post_request = openapi_client.PurchaseOrderIdIdCreatePurchaseInvoicePostRequest() # PurchaseOrderIdIdCreatePurchaseInvoicePostRequest | 

    try:
        api_response = api_instance.purchase_order_id_id_create_purchase_invoice_post(id, purchase_order_id_id_create_purchase_invoice_post_request)
        print("The response of PurchaseOrderApi->purchase_order_id_id_create_purchase_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_create_purchase_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order_id_id_create_purchase_invoice_post_request** | [**PurchaseOrderIdIdCreatePurchaseInvoicePostRequest**](PurchaseOrderIdIdCreatePurchaseInvoicePostRequest.md)|  | 

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
**200** | createPurchaseInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_create_supplier_return_post**
> IncomingGoodsIdIdCreateCompensationShipmentPost200Response purchase_order_id_id_create_supplier_return_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_compensation_shipment_post200_response import IncomingGoodsIdIdCreateCompensationShipmentPost200Response
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.purchase_order_id_id_create_supplier_return_post(id, body)
        print("The response of PurchaseOrderApi->purchase_order_id_id_create_supplier_return_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_create_supplier_return_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**IncomingGoodsIdIdCreateCompensationShipmentPost200Response**](IncomingGoodsIdIdCreateCompensationShipmentPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createSupplierReturn response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_delete**
> purchase_order_id_id_delete(id, dry_run=dry_run)

delete a purchaseOrder

delete a purchaseOrder

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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a purchaseOrder
        api_instance.purchase_order_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_delete: %s\n" % e)
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
**204** | purchaseOrder delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get**
> bytearray purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get(id)



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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get(id)
        print("The response of PurchaseOrderApi->purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get: %s\n" % e)
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
**200** | downloadLatestDropshippingDeliveryNotePdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_download_latest_purchase_order_pdf_get**
> bytearray purchase_order_id_id_download_latest_purchase_order_pdf_get(id)



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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.purchase_order_id_id_download_latest_purchase_order_pdf_get(id)
        print("The response of PurchaseOrderApi->purchase_order_id_id_download_latest_purchase_order_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_download_latest_purchase_order_pdf_get: %s\n" % e)
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
**200** | downloadLatestPurchaseOrderPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_get**
> PurchaseOrder purchase_order_id_id_get(id)

query a specific purchaseOrder

query a specific purchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order import PurchaseOrder
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific purchaseOrder
        api_response = api_instance.purchase_order_id_id_get(id)
        print("The response of PurchaseOrderApi->purchase_order_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

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

# **purchase_order_id_id_process_dropshipping_post**
> PurchaseOrderIdIdProcessDropshippingPost200Response purchase_order_id_id_process_dropshipping_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_id_id_process_dropshipping_post200_response import PurchaseOrderIdIdProcessDropshippingPost200Response
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.purchase_order_id_id_process_dropshipping_post(id, body)
        print("The response of PurchaseOrderApi->purchase_order_id_id_process_dropshipping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_process_dropshipping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**PurchaseOrderIdIdProcessDropshippingPost200Response**](PurchaseOrderIdIdProcessDropshippingPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | processDropshipping response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_id_id_put**
> PurchaseOrder purchase_order_id_id_put(id, purchase_order, dry_run=dry_run)

update a purchaseOrder

update purchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order import PurchaseOrder
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    purchase_order = openapi_client.PurchaseOrder() # PurchaseOrder | 
    dry_run = True # bool |  (optional)

    try:
        # update a purchaseOrder
        api_response = api_instance.purchase_order_id_id_put(id, purchase_order, dry_run=dry_run)
        print("The response of PurchaseOrderApi->purchase_order_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order** | [**PurchaseOrder**](PurchaseOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseOrder update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_post**
> PurchaseOrder purchase_order_post(purchase_order, dry_run=dry_run)

create a purchaseOrder

create a purchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order import PurchaseOrder
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
    api_instance = openapi_client.PurchaseOrderApi(api_client)
    purchase_order = openapi_client.PurchaseOrder() # PurchaseOrder | 
    dry_run = True # bool |  (optional)

    try:
        # create a purchaseOrder
        api_response = api_instance.purchase_order_post(purchase_order, dry_run=dry_run)
        print("The response of PurchaseOrderApi->purchase_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderApi->purchase_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order** | [**PurchaseOrder**](PurchaseOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | purchaseOrder create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

