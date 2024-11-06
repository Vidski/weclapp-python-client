# openapi_client.SalesOrderApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_order_count_get**](SalesOrderApi.md#sales_order_count_get) | **GET** /salesOrder/count | count salesOrder
[**sales_order_default_values_for_create_get**](SalesOrderApi.md#sales_order_default_values_for_create_get) | **GET** /salesOrder/defaultValuesForCreate | 
[**sales_order_get**](SalesOrderApi.md#sales_order_get) | **GET** /salesOrder | query salesOrder
[**sales_order_id_id_cancel_or_manually_close_post**](SalesOrderApi.md#sales_order_id_id_cancel_or_manually_close_post) | **POST** /salesOrder/id/{id}/cancelOrManuallyClose | 
[**sales_order_id_id_create_advance_payment_request_post**](SalesOrderApi.md#sales_order_id_id_create_advance_payment_request_post) | **POST** /salesOrder/id/{id}/createAdvancePaymentRequest | 
[**sales_order_id_id_create_customer_return_post**](SalesOrderApi.md#sales_order_id_id_create_customer_return_post) | **POST** /salesOrder/id/{id}/createCustomerReturn | 
[**sales_order_id_id_create_dropshipping_post**](SalesOrderApi.md#sales_order_id_id_create_dropshipping_post) | **POST** /salesOrder/id/{id}/createDropshipping | 
[**sales_order_id_id_create_part_payment_invoice_post**](SalesOrderApi.md#sales_order_id_id_create_part_payment_invoice_post) | **POST** /salesOrder/id/{id}/createPartPaymentInvoice | 
[**sales_order_id_id_create_prepayment_final_invoice_post**](SalesOrderApi.md#sales_order_id_id_create_prepayment_final_invoice_post) | **POST** /salesOrder/id/{id}/createPrepaymentFinalInvoice | 
[**sales_order_id_id_create_purchase_order_post**](SalesOrderApi.md#sales_order_id_id_create_purchase_order_post) | **POST** /salesOrder/id/{id}/createPurchaseOrder | 
[**sales_order_id_id_create_return_labels_post**](SalesOrderApi.md#sales_order_id_id_create_return_labels_post) | **POST** /salesOrder/id/{id}/createReturnLabels | 
[**sales_order_id_id_create_sales_invoice_post**](SalesOrderApi.md#sales_order_id_id_create_sales_invoice_post) | **POST** /salesOrder/id/{id}/createSalesInvoice | 
[**sales_order_id_id_create_shipment_post**](SalesOrderApi.md#sales_order_id_id_create_shipment_post) | **POST** /salesOrder/id/{id}/createShipment | 
[**sales_order_id_id_create_shipping_labels_post**](SalesOrderApi.md#sales_order_id_id_create_shipping_labels_post) | **POST** /salesOrder/id/{id}/createShippingLabels | 
[**sales_order_id_id_delete**](SalesOrderApi.md#sales_order_id_id_delete) | **DELETE** /salesOrder/id/{id} | delete a salesOrder
[**sales_order_id_id_download_latest_order_confirmation_pdf_get**](SalesOrderApi.md#sales_order_id_id_download_latest_order_confirmation_pdf_get) | **GET** /salesOrder/id/{id}/downloadLatestOrderConfirmationPdf | 
[**sales_order_id_id_get**](SalesOrderApi.md#sales_order_id_id_get) | **GET** /salesOrder/id/{id} | query a specific salesOrder
[**sales_order_id_id_manually_close_post**](SalesOrderApi.md#sales_order_id_id_manually_close_post) | **POST** /salesOrder/id/{id}/manuallyClose | 
[**sales_order_id_id_put**](SalesOrderApi.md#sales_order_id_id_put) | **PUT** /salesOrder/id/{id} | update a salesOrder
[**sales_order_id_id_ship_order_for_external_fulfillment_post**](SalesOrderApi.md#sales_order_id_id_ship_order_for_external_fulfillment_post) | **POST** /salesOrder/id/{id}/shipOrderForExternalFulfillment | 
[**sales_order_id_id_toggle_project_team_post**](SalesOrderApi.md#sales_order_id_id_toggle_project_team_post) | **POST** /salesOrder/id/{id}/toggleProjectTeam | 
[**sales_order_id_id_toggle_services_finished_post**](SalesOrderApi.md#sales_order_id_id_toggle_services_finished_post) | **POST** /salesOrder/id/{id}/toggleServicesFinished | 
[**sales_order_post**](SalesOrderApi.md#sales_order_post) | **POST** /salesOrder | create a salesOrder


# **sales_order_count_get**
> AccountingTransactionCountGet200Response sales_order_count_get()

count salesOrder

count salesOrder

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
    api_instance = openapi_client.SalesOrderApi(api_client)

    try:
        # count salesOrder
        api_response = api_instance.sales_order_count_get()
        print("The response of SalesOrderApi->sales_order_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_count_get: %s\n" % e)
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

# **sales_order_default_values_for_create_get**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_default_values_for_create_get(customer_id, responsible_user_id=responsible_user_id)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    customer_id = 'customer_id_example' # str | 
    responsible_user_id = 'responsible_user_id_example' # str |  (optional)

    try:
        api_response = api_instance.sales_order_default_values_for_create_get(customer_id, responsible_user_id=responsible_user_id)
        print("The response of SalesOrderApi->sales_order_default_values_for_create_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_default_values_for_create_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **responsible_user_id** | **str**|  | [optional] 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | defaultValuesForCreate response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_get**
> SalesOrderGet200Response sales_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)

query salesOrder

query salesOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_get200_response import SalesOrderGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)
    additional_properties = 'additional_properties_example' # str |  (optional)

    try:
        # query salesOrder
        api_response = api_instance.sales_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)
        print("The response of SalesOrderApi->sales_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_get: %s\n" % e)
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

[**SalesOrderGet200Response**](SalesOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | salesOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_cancel_or_manually_close_post**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_id_id_cancel_or_manually_close_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_cancel_or_manually_close_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_cancel_or_manually_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_cancel_or_manually_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cancelOrManuallyClose response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_advance_payment_request_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_order_id_id_create_advance_payment_request_post(id, body)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_advance_payment_request_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_advance_payment_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_advance_payment_request_post: %s\n" % e)
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
**200** | createAdvancePaymentRequest response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_customer_return_post**
> IncomingGoodsIdIdAddPurchaseOrdersPost200Response sales_order_id_id_create_customer_return_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_add_purchase_orders_post200_response import IncomingGoodsIdIdAddPurchaseOrdersPost200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_customer_return_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_customer_return_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_customer_return_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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
**200** | createCustomerReturn response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_dropshipping_post**
> PurchaseOrderIdIdProcessDropshippingPost200Response sales_order_id_id_create_dropshipping_post(id, sales_order_id_id_create_dropshipping_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_id_id_process_dropshipping_post200_response import PurchaseOrderIdIdProcessDropshippingPost200Response
from openapi_client.models.sales_order_id_id_create_dropshipping_post_request import SalesOrderIdIdCreateDropshippingPostRequest
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    sales_order_id_id_create_dropshipping_post_request = openapi_client.SalesOrderIdIdCreateDropshippingPostRequest() # SalesOrderIdIdCreateDropshippingPostRequest | 

    try:
        api_response = api_instance.sales_order_id_id_create_dropshipping_post(id, sales_order_id_id_create_dropshipping_post_request)
        print("The response of SalesOrderApi->sales_order_id_id_create_dropshipping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_dropshipping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_order_id_id_create_dropshipping_post_request** | [**SalesOrderIdIdCreateDropshippingPostRequest**](SalesOrderIdIdCreateDropshippingPostRequest.md)|  | 

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
**200** | createDropshipping response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_part_payment_invoice_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_order_id_id_create_part_payment_invoice_post(id, body)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_part_payment_invoice_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_part_payment_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_part_payment_invoice_post: %s\n" % e)
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
**200** | createPartPaymentInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_prepayment_final_invoice_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_order_id_id_create_prepayment_final_invoice_post(id, body)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_prepayment_final_invoice_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_prepayment_final_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_prepayment_final_invoice_post: %s\n" % e)
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
**200** | createPrepaymentFinalInvoice response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_purchase_order_post**
> PurchaseOrderGet200Response sales_order_id_id_create_purchase_order_post(id, sales_order_id_id_create_purchase_order_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_get200_response import PurchaseOrderGet200Response
from openapi_client.models.sales_order_id_id_create_purchase_order_post_request import SalesOrderIdIdCreatePurchaseOrderPostRequest
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    sales_order_id_id_create_purchase_order_post_request = openapi_client.SalesOrderIdIdCreatePurchaseOrderPostRequest() # SalesOrderIdIdCreatePurchaseOrderPostRequest | 

    try:
        api_response = api_instance.sales_order_id_id_create_purchase_order_post(id, sales_order_id_id_create_purchase_order_post_request)
        print("The response of SalesOrderApi->sales_order_id_id_create_purchase_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_purchase_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_order_id_id_create_purchase_order_post_request** | [**SalesOrderIdIdCreatePurchaseOrderPostRequest**](SalesOrderIdIdCreatePurchaseOrderPostRequest.md)|  | 

### Return type

[**PurchaseOrderGet200Response**](PurchaseOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPurchaseOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_return_labels_post**
> DocumentGet200Response sales_order_id_id_create_return_labels_post(id, body)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_return_labels_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_return_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_return_labels_post: %s\n" % e)
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

# **sales_order_id_id_create_sales_invoice_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response sales_order_id_id_create_sales_invoice_post(id, sales_order_id_id_create_sales_invoice_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_credit_note_post200_response import IncomingGoodsIdIdCreateCreditNotePost200Response
from openapi_client.models.sales_order_id_id_create_sales_invoice_post_request import SalesOrderIdIdCreateSalesInvoicePostRequest
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    sales_order_id_id_create_sales_invoice_post_request = openapi_client.SalesOrderIdIdCreateSalesInvoicePostRequest() # SalesOrderIdIdCreateSalesInvoicePostRequest | 

    try:
        api_response = api_instance.sales_order_id_id_create_sales_invoice_post(id, sales_order_id_id_create_sales_invoice_post_request)
        print("The response of SalesOrderApi->sales_order_id_id_create_sales_invoice_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_sales_invoice_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_order_id_id_create_sales_invoice_post_request** | [**SalesOrderIdIdCreateSalesInvoicePostRequest**](SalesOrderIdIdCreateSalesInvoicePostRequest.md)|  | 

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

# **sales_order_id_id_create_shipment_post**
> IncomingGoodsIdIdCreateCompensationShipmentPost200Response sales_order_id_id_create_shipment_post(id, sales_order_id_id_create_sales_invoice_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_compensation_shipment_post200_response import IncomingGoodsIdIdCreateCompensationShipmentPost200Response
from openapi_client.models.sales_order_id_id_create_sales_invoice_post_request import SalesOrderIdIdCreateSalesInvoicePostRequest
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    sales_order_id_id_create_sales_invoice_post_request = openapi_client.SalesOrderIdIdCreateSalesInvoicePostRequest() # SalesOrderIdIdCreateSalesInvoicePostRequest | 

    try:
        api_response = api_instance.sales_order_id_id_create_shipment_post(id, sales_order_id_id_create_sales_invoice_post_request)
        print("The response of SalesOrderApi->sales_order_id_id_create_shipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_shipment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_order_id_id_create_sales_invoice_post_request** | [**SalesOrderIdIdCreateSalesInvoicePostRequest**](SalesOrderIdIdCreateSalesInvoicePostRequest.md)|  | 

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
**200** | createShipment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_create_shipping_labels_post**
> DocumentGet200Response sales_order_id_id_create_shipping_labels_post(id, body)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_create_shipping_labels_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_create_shipping_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_create_shipping_labels_post: %s\n" % e)
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

# **sales_order_id_id_delete**
> sales_order_id_id_delete(id, dry_run=dry_run)

delete a salesOrder

delete a salesOrder

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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a salesOrder
        api_instance.sales_order_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_delete: %s\n" % e)
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
**204** | salesOrder delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_download_latest_order_confirmation_pdf_get**
> bytearray sales_order_id_id_download_latest_order_confirmation_pdf_get(id)



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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.sales_order_id_id_download_latest_order_confirmation_pdf_get(id)
        print("The response of SalesOrderApi->sales_order_id_id_download_latest_order_confirmation_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_download_latest_order_confirmation_pdf_get: %s\n" % e)
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
**200** | downloadLatestOrderConfirmationPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_get**
> SalesOrder sales_order_id_id_get(id)

query a specific salesOrder

query a specific salesOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order import SalesOrder
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific salesOrder
        api_response = api_instance.sales_order_id_id_get(id)
        print("The response of SalesOrderApi->sales_order_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SalesOrder**](SalesOrder.md)

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

# **sales_order_id_id_manually_close_post**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_id_id_manually_close_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_manually_close_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_manually_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_manually_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | manuallyClose response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_put**
> SalesOrder sales_order_id_id_put(id, sales_order, dry_run=dry_run)

update a salesOrder

update salesOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order import SalesOrder
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    sales_order = openapi_client.SalesOrder() # SalesOrder | 
    dry_run = True # bool |  (optional)

    try:
        # update a salesOrder
        api_response = api_instance.sales_order_id_id_put(id, sales_order, dry_run=dry_run)
        print("The response of SalesOrderApi->sales_order_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sales_order** | [**SalesOrder**](SalesOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | salesOrder update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_ship_order_for_external_fulfillment_post**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_id_id_ship_order_for_external_fulfillment_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_ship_order_for_external_fulfillment_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_ship_order_for_external_fulfillment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_ship_order_for_external_fulfillment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipOrderForExternalFulfillment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_toggle_project_team_post**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_id_id_toggle_project_team_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_toggle_project_team_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_toggle_project_team_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_toggle_project_team_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | toggleProjectTeam response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_id_id_toggle_services_finished_post**
> SalesOrderDefaultValuesForCreateGet200Response sales_order_id_id_toggle_services_finished_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order_default_values_for_create_get200_response import SalesOrderDefaultValuesForCreateGet200Response
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.sales_order_id_id_toggle_services_finished_post(id, body)
        print("The response of SalesOrderApi->sales_order_id_id_toggle_services_finished_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_id_id_toggle_services_finished_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**SalesOrderDefaultValuesForCreateGet200Response**](SalesOrderDefaultValuesForCreateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | toggleServicesFinished response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_post**
> SalesOrder sales_order_post(sales_order, dry_run=dry_run)

create a salesOrder

create a salesOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_order import SalesOrder
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
    api_instance = openapi_client.SalesOrderApi(api_client)
    sales_order = openapi_client.SalesOrder() # SalesOrder | 
    dry_run = True # bool |  (optional)

    try:
        # create a salesOrder
        api_response = api_instance.sales_order_post(sales_order, dry_run=dry_run)
        print("The response of SalesOrderApi->sales_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOrderApi->sales_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_order** | [**SalesOrder**](SalesOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | salesOrder create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

