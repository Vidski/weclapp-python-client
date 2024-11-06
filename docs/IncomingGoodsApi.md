# openapi_client.IncomingGoodsApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incoming_goods_count_get**](IncomingGoodsApi.md#incoming_goods_count_get) | **GET** /incomingGoods/count | count incomingGoods
[**incoming_goods_get**](IncomingGoodsApi.md#incoming_goods_get) | **GET** /incomingGoods | query incomingGoods
[**incoming_goods_id_id_add_purchase_orders_post**](IncomingGoodsApi.md#incoming_goods_id_id_add_purchase_orders_post) | **POST** /incomingGoods/id/{id}/addPurchaseOrders | 
[**incoming_goods_id_id_create_compensation_shipment_post**](IncomingGoodsApi.md#incoming_goods_id_id_create_compensation_shipment_post) | **POST** /incomingGoods/id/{id}/createCompensationShipment | 
[**incoming_goods_id_id_create_credit_note_post**](IncomingGoodsApi.md#incoming_goods_id_id_create_credit_note_post) | **POST** /incomingGoods/id/{id}/createCreditNote | 
[**incoming_goods_id_id_create_return_labels_post**](IncomingGoodsApi.md#incoming_goods_id_id_create_return_labels_post) | **POST** /incomingGoods/id/{id}/createReturnLabels | 
[**incoming_goods_id_id_create_supplier_return_post**](IncomingGoodsApi.md#incoming_goods_id_id_create_supplier_return_post) | **POST** /incomingGoods/id/{id}/createSupplierReturn | 
[**incoming_goods_id_id_delete**](IncomingGoodsApi.md#incoming_goods_id_id_delete) | **DELETE** /incomingGoods/id/{id} | delete a incomingGoods
[**incoming_goods_id_id_get**](IncomingGoodsApi.md#incoming_goods_id_id_get) | **GET** /incomingGoods/id/{id} | query a specific incomingGoods
[**incoming_goods_id_id_incoming_bookings_get**](IncomingGoodsApi.md#incoming_goods_id_id_incoming_bookings_get) | **GET** /incomingGoods/id/{id}/incomingBookings | 
[**incoming_goods_id_id_put**](IncomingGoodsApi.md#incoming_goods_id_id_put) | **PUT** /incomingGoods/id/{id} | update a incomingGoods
[**incoming_goods_id_id_update_incoming_bookings_post**](IncomingGoodsApi.md#incoming_goods_id_id_update_incoming_bookings_post) | **POST** /incomingGoods/id/{id}/updateIncomingBookings | 
[**incoming_goods_post**](IncomingGoodsApi.md#incoming_goods_post) | **POST** /incomingGoods | create a incomingGoods


# **incoming_goods_count_get**
> AccountingTransactionCountGet200Response incoming_goods_count_get()

count incomingGoods

count incomingGoods

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
    api_instance = openapi_client.IncomingGoodsApi(api_client)

    try:
        # count incomingGoods
        api_response = api_instance.incoming_goods_count_get()
        print("The response of IncomingGoodsApi->incoming_goods_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_count_get: %s\n" % e)
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

# **incoming_goods_get**
> IncomingGoodsGet200Response incoming_goods_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query incomingGoods

query incomingGoods

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_get200_response import IncomingGoodsGet200Response
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query incomingGoods
        api_response = api_instance.incoming_goods_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of IncomingGoodsApi->incoming_goods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_get: %s\n" % e)
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

[**IncomingGoodsGet200Response**](IncomingGoodsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | incomingGoods response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_add_purchase_orders_post**
> IncomingGoodsIdIdAddPurchaseOrdersPost200Response incoming_goods_id_id_add_purchase_orders_post(id, incoming_goods_id_id_add_purchase_orders_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_add_purchase_orders_post200_response import IncomingGoodsIdIdAddPurchaseOrdersPost200Response
from openapi_client.models.incoming_goods_id_id_add_purchase_orders_post_request import IncomingGoodsIdIdAddPurchaseOrdersPostRequest
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    incoming_goods_id_id_add_purchase_orders_post_request = openapi_client.IncomingGoodsIdIdAddPurchaseOrdersPostRequest() # IncomingGoodsIdIdAddPurchaseOrdersPostRequest | 

    try:
        api_response = api_instance.incoming_goods_id_id_add_purchase_orders_post(id, incoming_goods_id_id_add_purchase_orders_post_request)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_add_purchase_orders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_add_purchase_orders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **incoming_goods_id_id_add_purchase_orders_post_request** | [**IncomingGoodsIdIdAddPurchaseOrdersPostRequest**](IncomingGoodsIdIdAddPurchaseOrdersPostRequest.md)|  | 

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
**200** | addPurchaseOrders response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_create_compensation_shipment_post**
> IncomingGoodsIdIdCreateCompensationShipmentPost200Response incoming_goods_id_id_create_compensation_shipment_post(id, body)



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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.incoming_goods_id_id_create_compensation_shipment_post(id, body)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_create_compensation_shipment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_create_compensation_shipment_post: %s\n" % e)
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
**200** | createCompensationShipment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_create_credit_note_post**
> IncomingGoodsIdIdCreateCreditNotePost200Response incoming_goods_id_id_create_credit_note_post(id, body)



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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.incoming_goods_id_id_create_credit_note_post(id, body)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_create_credit_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_create_credit_note_post: %s\n" % e)
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
**200** | createCreditNote response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_create_return_labels_post**
> DocumentGet200Response incoming_goods_id_id_create_return_labels_post(id, body)



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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.incoming_goods_id_id_create_return_labels_post(id, body)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_create_return_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_create_return_labels_post: %s\n" % e)
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

# **incoming_goods_id_id_create_supplier_return_post**
> IncomingGoodsIdIdCreateCompensationShipmentPost200Response incoming_goods_id_id_create_supplier_return_post(id, incoming_goods_id_id_create_supplier_return_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_create_compensation_shipment_post200_response import IncomingGoodsIdIdCreateCompensationShipmentPost200Response
from openapi_client.models.incoming_goods_id_id_create_supplier_return_post_request import IncomingGoodsIdIdCreateSupplierReturnPostRequest
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    incoming_goods_id_id_create_supplier_return_post_request = openapi_client.IncomingGoodsIdIdCreateSupplierReturnPostRequest() # IncomingGoodsIdIdCreateSupplierReturnPostRequest | 

    try:
        api_response = api_instance.incoming_goods_id_id_create_supplier_return_post(id, incoming_goods_id_id_create_supplier_return_post_request)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_create_supplier_return_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_create_supplier_return_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **incoming_goods_id_id_create_supplier_return_post_request** | [**IncomingGoodsIdIdCreateSupplierReturnPostRequest**](IncomingGoodsIdIdCreateSupplierReturnPostRequest.md)|  | 

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

# **incoming_goods_id_id_delete**
> incoming_goods_id_id_delete(id, dry_run=dry_run)

delete a incomingGoods

delete a incomingGoods

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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a incomingGoods
        api_instance.incoming_goods_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_delete: %s\n" % e)
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
**204** | incomingGoods delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_get**
> IncomingGoods incoming_goods_id_id_get(id)

query a specific incomingGoods

query a specific incomingGoods

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods import IncomingGoods
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific incomingGoods
        api_response = api_instance.incoming_goods_id_id_get(id)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**IncomingGoods**](IncomingGoods.md)

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

# **incoming_goods_id_id_incoming_bookings_get**
> IncomingGoodsIdIdIncomingBookingsGet200Response incoming_goods_id_id_incoming_bookings_get(id)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_incoming_bookings_get200_response import IncomingGoodsIdIdIncomingBookingsGet200Response
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.incoming_goods_id_id_incoming_bookings_get(id)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_incoming_bookings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_incoming_bookings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**IncomingGoodsIdIdIncomingBookingsGet200Response**](IncomingGoodsIdIdIncomingBookingsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | incomingBookings response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_put**
> IncomingGoods incoming_goods_id_id_put(id, incoming_goods, dry_run=dry_run)

update a incomingGoods

update incomingGoods

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods import IncomingGoods
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    incoming_goods = openapi_client.IncomingGoods() # IncomingGoods | 
    dry_run = True # bool |  (optional)

    try:
        # update a incomingGoods
        api_response = api_instance.incoming_goods_id_id_put(id, incoming_goods, dry_run=dry_run)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **incoming_goods** | [**IncomingGoods**](IncomingGoods.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**IncomingGoods**](IncomingGoods.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | incomingGoods update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_id_id_update_incoming_bookings_post**
> IncomingGoodsIdIdIncomingBookingsGet200Response incoming_goods_id_id_update_incoming_bookings_post(id, incoming_goods_id_id_update_incoming_bookings_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods_id_id_incoming_bookings_get200_response import IncomingGoodsIdIdIncomingBookingsGet200Response
from openapi_client.models.incoming_goods_id_id_update_incoming_bookings_post_request import IncomingGoodsIdIdUpdateIncomingBookingsPostRequest
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    id = 'id_example' # str | 
    incoming_goods_id_id_update_incoming_bookings_post_request = openapi_client.IncomingGoodsIdIdUpdateIncomingBookingsPostRequest() # IncomingGoodsIdIdUpdateIncomingBookingsPostRequest | 

    try:
        api_response = api_instance.incoming_goods_id_id_update_incoming_bookings_post(id, incoming_goods_id_id_update_incoming_bookings_post_request)
        print("The response of IncomingGoodsApi->incoming_goods_id_id_update_incoming_bookings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_id_id_update_incoming_bookings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **incoming_goods_id_id_update_incoming_bookings_post_request** | [**IncomingGoodsIdIdUpdateIncomingBookingsPostRequest**](IncomingGoodsIdIdUpdateIncomingBookingsPostRequest.md)|  | 

### Return type

[**IncomingGoodsIdIdIncomingBookingsGet200Response**](IncomingGoodsIdIdIncomingBookingsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updateIncomingBookings response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incoming_goods_post**
> IncomingGoods incoming_goods_post(incoming_goods, dry_run=dry_run)

create a incomingGoods

create a incomingGoods

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.incoming_goods import IncomingGoods
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
    api_instance = openapi_client.IncomingGoodsApi(api_client)
    incoming_goods = openapi_client.IncomingGoods() # IncomingGoods | 
    dry_run = True # bool |  (optional)

    try:
        # create a incomingGoods
        api_response = api_instance.incoming_goods_post(incoming_goods, dry_run=dry_run)
        print("The response of IncomingGoodsApi->incoming_goods_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IncomingGoodsApi->incoming_goods_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incoming_goods** | [**IncomingGoods**](IncomingGoods.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**IncomingGoods**](IncomingGoods.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | incomingGoods create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

