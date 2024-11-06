# openapi_client.ShipmentApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_count_get**](ShipmentApi.md#shipment_count_get) | **GET** /shipment/count | count shipment
[**shipment_get**](ShipmentApi.md#shipment_get) | **GET** /shipment | query shipment
[**shipment_id_id_create_picking_list_post**](ShipmentApi.md#shipment_id_id_create_picking_list_post) | **POST** /shipment/id/{id}/createPickingList | 
[**shipment_id_id_create_return_labels_post**](ShipmentApi.md#shipment_id_id_create_return_labels_post) | **POST** /shipment/id/{id}/createReturnLabels | 
[**shipment_id_id_create_sales_invoice_post**](ShipmentApi.md#shipment_id_id_create_sales_invoice_post) | **POST** /shipment/id/{id}/createSalesInvoice | 
[**shipment_id_id_create_shipping_label_pdf_post**](ShipmentApi.md#shipment_id_id_create_shipping_label_pdf_post) | **POST** /shipment/id/{id}/createShippingLabelPdf | 
[**shipment_id_id_create_shipping_labels_post**](ShipmentApi.md#shipment_id_id_create_shipping_labels_post) | **POST** /shipment/id/{id}/createShippingLabels | 
[**shipment_id_id_delete**](ShipmentApi.md#shipment_id_id_delete) | **DELETE** /shipment/id/{id} | delete a shipment
[**shipment_id_id_download_latest_delivery_note_pdf_get**](ShipmentApi.md#shipment_id_id_download_latest_delivery_note_pdf_get) | **GET** /shipment/id/{id}/downloadLatestDeliveryNotePdf | 
[**shipment_id_id_download_latest_picking_list_pdf_get**](ShipmentApi.md#shipment_id_id_download_latest_picking_list_pdf_get) | **GET** /shipment/id/{id}/downloadLatestPickingListPdf | 
[**shipment_id_id_download_latest_shipping_label_pdf_get**](ShipmentApi.md#shipment_id_id_download_latest_shipping_label_pdf_get) | **GET** /shipment/id/{id}/downloadLatestShippingLabelPdf | 
[**shipment_id_id_get**](ShipmentApi.md#shipment_id_id_get) | **GET** /shipment/id/{id} | query a specific shipment
[**shipment_id_id_put**](ShipmentApi.md#shipment_id_id_put) | **PUT** /shipment/id/{id} | update a shipment
[**shipment_post**](ShipmentApi.md#shipment_post) | **POST** /shipment | create a shipment


# **shipment_count_get**
> AccountingTransactionCountGet200Response shipment_count_get()

count shipment

count shipment

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
    api_instance = openapi_client.ShipmentApi(api_client)

    try:
        # count shipment
        api_response = api_instance.shipment_count_get()
        print("The response of ShipmentApi->shipment_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_count_get: %s\n" % e)
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

# **shipment_get**
> ShipmentGet200Response shipment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query shipment

query shipment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_get200_response import ShipmentGet200Response
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
    api_instance = openapi_client.ShipmentApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query shipment
        api_response = api_instance.shipment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ShipmentApi->shipment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_get: %s\n" % e)
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

[**ShipmentGet200Response**](ShipmentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_create_picking_list_post**
> bytearray shipment_id_id_create_picking_list_post(id, body)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.shipment_id_id_create_picking_list_post(id, body)
        print("The response of ShipmentApi->shipment_id_id_create_picking_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_create_picking_list_post: %s\n" % e)
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
**200** | createPickingList response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_create_return_labels_post**
> DocumentGet200Response shipment_id_id_create_return_labels_post(id, body)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.shipment_id_id_create_return_labels_post(id, body)
        print("The response of ShipmentApi->shipment_id_id_create_return_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_create_return_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**DocumentGet200Response**](DocumentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createReturnLabels response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_create_sales_invoice_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response shipment_id_id_create_sales_invoice_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_credit_note_post200_response import IncomingGoodsIdIdCreateCreditNotePost200Response
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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.shipment_id_id_create_sales_invoice_post(id, body)
        print("The response of ShipmentApi->shipment_id_id_create_sales_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_create_sales_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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
**200** | createSalesInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_create_shipping_label_pdf_post**
> ArchivedEmailIdIdRemoveReferencePost200Response shipment_id_id_create_shipping_label_pdf_post(id, name, body, description=description)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 
    body = None # bytearray | 
    description = 'description_example' # str |  (optional)

    try:
        api_response = api_instance.shipment_id_id_create_shipping_label_pdf_post(id, name, body, description=description)
        print("The response of ShipmentApi->shipment_id_id_create_shipping_label_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_create_shipping_label_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 
 **body** | **bytearray**|  | 
 **description** | **str**|  | [optional] 

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
**200** | createShippingLabelPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_create_shipping_labels_post**
> DocumentGet200Response shipment_id_id_create_shipping_labels_post(id, body)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.shipment_id_id_create_shipping_labels_post(id, body)
        print("The response of ShipmentApi->shipment_id_id_create_shipping_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_create_shipping_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**DocumentGet200Response**](DocumentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createShippingLabels response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_delete**
> shipment_id_id_delete(id, dry_run=dry_run)

delete a shipment

delete a shipment

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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a shipment
        api_instance.shipment_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_delete: %s\n" % e)
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
**204** | shipment delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_download_latest_delivery_note_pdf_get**
> bytearray shipment_id_id_download_latest_delivery_note_pdf_get(id)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.shipment_id_id_download_latest_delivery_note_pdf_get(id)
        print("The response of ShipmentApi->shipment_id_id_download_latest_delivery_note_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_download_latest_delivery_note_pdf_get: %s\n" % e)
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
**200** | downloadLatestDeliveryNotePdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_download_latest_picking_list_pdf_get**
> bytearray shipment_id_id_download_latest_picking_list_pdf_get(id)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.shipment_id_id_download_latest_picking_list_pdf_get(id)
        print("The response of ShipmentApi->shipment_id_id_download_latest_picking_list_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_download_latest_picking_list_pdf_get: %s\n" % e)
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
**200** | downloadLatestPickingListPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_download_latest_shipping_label_pdf_get**
> bytearray shipment_id_id_download_latest_shipping_label_pdf_get(id)



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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.shipment_id_id_download_latest_shipping_label_pdf_get(id)
        print("The response of ShipmentApi->shipment_id_id_download_latest_shipping_label_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_download_latest_shipping_label_pdf_get: %s\n" % e)
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
**200** | downloadLatestShippingLabelPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_id_id_get**
> Shipment shipment_id_id_get(id)

query a specific shipment

query a specific shipment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment import Shipment
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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific shipment
        api_response = api_instance.shipment_id_id_get(id)
        print("The response of ShipmentApi->shipment_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Shipment**](Shipment.md)

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

# **shipment_id_id_put**
> Shipment shipment_id_id_put(id, shipment, dry_run=dry_run)

update a shipment

update shipment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment import Shipment
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
    api_instance = openapi_client.ShipmentApi(api_client)
    id = 'id_example' # str | 
    shipment = openapi_client.Shipment() # Shipment | 
    dry_run = True # bool |  (optional)

    try:
        # update a shipment
        api_response = api_instance.shipment_id_id_put(id, shipment, dry_run=dry_run)
        print("The response of ShipmentApi->shipment_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shipment** | [**Shipment**](Shipment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipment update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_post**
> Shipment shipment_post(shipment, dry_run=dry_run)

create a shipment

create a shipment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment import Shipment
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
    api_instance = openapi_client.ShipmentApi(api_client)
    shipment = openapi_client.Shipment() # Shipment | 
    dry_run = True # bool |  (optional)

    try:
        # create a shipment
        api_response = api_instance.shipment_post(shipment, dry_run=dry_run)
        print("The response of ShipmentApi->shipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentApi->shipment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment** | [**Shipment**](Shipment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | shipment create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

