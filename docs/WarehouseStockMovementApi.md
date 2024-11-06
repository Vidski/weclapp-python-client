# openapi_client.WarehouseStockMovementApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warehouse_stock_movement_book_direct_stock_transfer_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_direct_stock_transfer_post) | **POST** /warehouseStockMovement/bookDirectStockTransfer | 
[**warehouse_stock_movement_book_from_loading_equipment_place_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_from_loading_equipment_place_post) | **POST** /warehouseStockMovement/bookFromLoadingEquipmentPlace | 
[**warehouse_stock_movement_book_incoming_movement_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_incoming_movement_post) | **POST** /warehouseStockMovement/bookIncomingMovement | 
[**warehouse_stock_movement_book_onto_internal_transport_reference_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_onto_internal_transport_reference_post) | **POST** /warehouseStockMovement/bookOntoInternalTransportReference | 
[**warehouse_stock_movement_book_outgoing_movement_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_outgoing_movement_post) | **POST** /warehouseStockMovement/bookOutgoingMovement | 
[**warehouse_stock_movement_book_to_loading_equipment_place_post**](WarehouseStockMovementApi.md#warehouse_stock_movement_book_to_loading_equipment_place_post) | **POST** /warehouseStockMovement/bookToLoadingEquipmentPlace | 
[**warehouse_stock_movement_count_get**](WarehouseStockMovementApi.md#warehouse_stock_movement_count_get) | **GET** /warehouseStockMovement/count | count warehouseStockMovement
[**warehouse_stock_movement_get**](WarehouseStockMovementApi.md#warehouse_stock_movement_get) | **GET** /warehouseStockMovement | query warehouseStockMovement
[**warehouse_stock_movement_id_id_get**](WarehouseStockMovementApi.md#warehouse_stock_movement_id_id_get) | **GET** /warehouseStockMovement/id/{id} | query a specific warehouseStockMovement


# **warehouse_stock_movement_book_direct_stock_transfer_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_direct_stock_transfer_post(warehouse_stock_movement_book_direct_stock_transfer_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_direct_stock_transfer_post_request import WarehouseStockMovementBookDirectStockTransferPostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_direct_stock_transfer_post_request = openapi_client.WarehouseStockMovementBookDirectStockTransferPostRequest() # WarehouseStockMovementBookDirectStockTransferPostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_direct_stock_transfer_post(warehouse_stock_movement_book_direct_stock_transfer_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_direct_stock_transfer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_direct_stock_transfer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_direct_stock_transfer_post_request** | [**WarehouseStockMovementBookDirectStockTransferPostRequest**](WarehouseStockMovementBookDirectStockTransferPostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookDirectStockTransfer response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_book_from_loading_equipment_place_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_from_loading_equipment_place_post(warehouse_stock_movement_book_from_loading_equipment_place_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_from_loading_equipment_place_post_request import WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_from_loading_equipment_place_post_request = openapi_client.WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest() # WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_from_loading_equipment_place_post(warehouse_stock_movement_book_from_loading_equipment_place_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_from_loading_equipment_place_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_from_loading_equipment_place_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_from_loading_equipment_place_post_request** | [**WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest**](WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookFromLoadingEquipmentPlace response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_book_incoming_movement_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_incoming_movement_post(warehouse_stock_movement_book_incoming_movement_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_incoming_movement_post_request import WarehouseStockMovementBookIncomingMovementPostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_incoming_movement_post_request = openapi_client.WarehouseStockMovementBookIncomingMovementPostRequest() # WarehouseStockMovementBookIncomingMovementPostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_incoming_movement_post(warehouse_stock_movement_book_incoming_movement_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_incoming_movement_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_incoming_movement_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_incoming_movement_post_request** | [**WarehouseStockMovementBookIncomingMovementPostRequest**](WarehouseStockMovementBookIncomingMovementPostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookIncomingMovement response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_book_onto_internal_transport_reference_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_onto_internal_transport_reference_post(warehouse_stock_movement_book_onto_internal_transport_reference_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_onto_internal_transport_reference_post_request import WarehouseStockMovementBookOntoInternalTransportReferencePostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_onto_internal_transport_reference_post_request = openapi_client.WarehouseStockMovementBookOntoInternalTransportReferencePostRequest() # WarehouseStockMovementBookOntoInternalTransportReferencePostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_onto_internal_transport_reference_post(warehouse_stock_movement_book_onto_internal_transport_reference_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_onto_internal_transport_reference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_onto_internal_transport_reference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_onto_internal_transport_reference_post_request** | [**WarehouseStockMovementBookOntoInternalTransportReferencePostRequest**](WarehouseStockMovementBookOntoInternalTransportReferencePostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookOntoInternalTransportReference response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_book_outgoing_movement_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_outgoing_movement_post(warehouse_stock_movement_book_outgoing_movement_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_outgoing_movement_post_request import WarehouseStockMovementBookOutgoingMovementPostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_outgoing_movement_post_request = openapi_client.WarehouseStockMovementBookOutgoingMovementPostRequest() # WarehouseStockMovementBookOutgoingMovementPostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_outgoing_movement_post(warehouse_stock_movement_book_outgoing_movement_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_outgoing_movement_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_outgoing_movement_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_outgoing_movement_post_request** | [**WarehouseStockMovementBookOutgoingMovementPostRequest**](WarehouseStockMovementBookOutgoingMovementPostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookOutgoingMovement response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_book_to_loading_equipment_place_post**
> WarehouseStockMovementGet200Response warehouse_stock_movement_book_to_loading_equipment_place_post(warehouse_stock_movement_book_to_loading_equipment_place_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_book_to_loading_equipment_place_post_request import WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    warehouse_stock_movement_book_to_loading_equipment_place_post_request = openapi_client.WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest() # WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest | 

    try:
        api_response = api_instance.warehouse_stock_movement_book_to_loading_equipment_place_post(warehouse_stock_movement_book_to_loading_equipment_place_post_request)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_book_to_loading_equipment_place_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_book_to_loading_equipment_place_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_stock_movement_book_to_loading_equipment_place_post_request** | [**WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest**](WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest.md)|  | 

### Return type

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | bookToLoadingEquipmentPlace response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_count_get**
> AccountingTransactionCountGet200Response warehouse_stock_movement_count_get()

count warehouseStockMovement

count warehouseStockMovement

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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)

    try:
        # count warehouseStockMovement
        api_response = api_instance.warehouse_stock_movement_count_get()
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_count_get: %s\n" % e)
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

# **warehouse_stock_movement_get**
> WarehouseStockMovementGet200Response warehouse_stock_movement_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query warehouseStockMovement

query warehouseStockMovement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement_get200_response import WarehouseStockMovementGet200Response
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query warehouseStockMovement
        api_response = api_instance.warehouse_stock_movement_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_get: %s\n" % e)
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

[**WarehouseStockMovementGet200Response**](WarehouseStockMovementGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | warehouseStockMovement response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warehouse_stock_movement_id_id_get**
> WarehouseStockMovement warehouse_stock_movement_id_id_get(id)

query a specific warehouseStockMovement

query a specific warehouseStockMovement

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.warehouse_stock_movement import WarehouseStockMovement
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
    api_instance = openapi_client.WarehouseStockMovementApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific warehouseStockMovement
        api_response = api_instance.warehouse_stock_movement_id_id_get(id)
        print("The response of WarehouseStockMovementApi->warehouse_stock_movement_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseStockMovementApi->warehouse_stock_movement_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WarehouseStockMovement**](WarehouseStockMovement.md)

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

