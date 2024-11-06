# openapi_client.TransportationOrderApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transportation_order_count_get**](TransportationOrderApi.md#transportation_order_count_get) | **GET** /transportationOrder/count | count transportationOrder
[**transportation_order_get**](TransportationOrderApi.md#transportation_order_get) | **GET** /transportationOrder | query transportationOrder
[**transportation_order_id_id_create_pick_post**](TransportationOrderApi.md#transportation_order_id_id_create_pick_post) | **POST** /transportationOrder/id/{id}/createPick | 
[**transportation_order_id_id_create_picking_list_post**](TransportationOrderApi.md#transportation_order_id_id_create_picking_list_post) | **POST** /transportationOrder/id/{id}/createPickingList | 
[**transportation_order_id_id_create_transportation_order_from_unpicked_records_post**](TransportationOrderApi.md#transportation_order_id_id_create_transportation_order_from_unpicked_records_post) | **POST** /transportationOrder/id/{id}/createTransportationOrderFromUnpickedRecords | 
[**transportation_order_id_id_delete**](TransportationOrderApi.md#transportation_order_id_id_delete) | **DELETE** /transportationOrder/id/{id} | delete a transportationOrder
[**transportation_order_id_id_get**](TransportationOrderApi.md#transportation_order_id_id_get) | **GET** /transportationOrder/id/{id} | query a specific transportationOrder
[**transportation_order_id_id_internal_transport_references_for_pick_up_get**](TransportationOrderApi.md#transportation_order_id_id_internal_transport_references_for_pick_up_get) | **GET** /transportationOrder/id/{id}/internalTransportReferencesForPickUp | 
[**transportation_order_id_id_pick_pick_post**](TransportationOrderApi.md#transportation_order_id_id_pick_pick_post) | **POST** /transportationOrder/id/{id}/pickPick | 
[**transportation_order_id_id_put**](TransportationOrderApi.md#transportation_order_id_id_put) | **PUT** /transportationOrder/id/{id} | update a transportationOrder
[**transportation_order_id_id_put_down_internal_transport_reference_post**](TransportationOrderApi.md#transportation_order_id_id_put_down_internal_transport_reference_post) | **POST** /transportationOrder/id/{id}/putDownInternalTransportReference | 
[**transportation_order_post**](TransportationOrderApi.md#transportation_order_post) | **POST** /transportationOrder | create a transportationOrder


# **transportation_order_count_get**
> AccountingTransactionCountGet200Response transportation_order_count_get()

count transportationOrder

count transportationOrder

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
    api_instance = openapi_client.TransportationOrderApi(api_client)

    try:
        # count transportationOrder
        api_response = api_instance.transportation_order_count_get()
        print("The response of TransportationOrderApi->transportation_order_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_count_get: %s\n" % e)
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

# **transportation_order_get**
> TransportationOrderGet200Response transportation_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query transportationOrder

query transportationOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order_get200_response import TransportationOrderGet200Response
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query transportationOrder
        api_response = api_instance.transportation_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TransportationOrderApi->transportation_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_get: %s\n" % e)
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

[**TransportationOrderGet200Response**](TransportationOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transportationOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_create_pick_post**
> TransportationOrderIdIdCreatePickPost200Response transportation_order_id_id_create_pick_post(id, transportation_order_id_id_create_pick_post_request)



create a pick for a transportationOrder  # Endpoint for creating picks  ## Explanation of the `existingReservations` parameter The existingReservations parameter can be used to specify other reserved picks, that need to be part of the transportationOrder. These picks will not be directly linked to the transportationOrder, but considered as parts of the single pick that is created by this endpoint. Processing the transportationOrder will also update the storagePlace and internalTransportReference of the specified picks and editing these picks manually is not possible, while the transportationOrder is still in progress.  The pickId of an existingReservations element must refer to a pick with the exact same * storagePlaceId * internalTransportReferenceId * packagingUnitBaseArticleId * batchNumber * orderItemId  as the remaining parameters. The referenced pick will be split into two picks, if the given quantity does not match its own quantity.  The quantity parameter of this endpoint specifies the total quantity of the transportationOrder pick, the quantity of an existingReservations element is already included in it. The same applies for the serialNumbers parameter.

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order_id_id_create_pick_post200_response import TransportationOrderIdIdCreatePickPost200Response
from openapi_client.models.transportation_order_id_id_create_pick_post_request import TransportationOrderIdIdCreatePickPostRequest
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    transportation_order_id_id_create_pick_post_request = openapi_client.TransportationOrderIdIdCreatePickPostRequest() # TransportationOrderIdIdCreatePickPostRequest | 

    try:
        api_response = api_instance.transportation_order_id_id_create_pick_post(id, transportation_order_id_id_create_pick_post_request)
        print("The response of TransportationOrderApi->transportation_order_id_id_create_pick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_create_pick_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transportation_order_id_id_create_pick_post_request** | [**TransportationOrderIdIdCreatePickPostRequest**](TransportationOrderIdIdCreatePickPostRequest.md)|  | 

### Return type

[**TransportationOrderIdIdCreatePickPost200Response**](TransportationOrderIdIdCreatePickPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPick response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_create_picking_list_post**
> bytearray transportation_order_id_id_create_picking_list_post(id, body)



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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.transportation_order_id_id_create_picking_list_post(id, body)
        print("The response of TransportationOrderApi->transportation_order_id_id_create_picking_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_create_picking_list_post: %s\n" % e)
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

# **transportation_order_id_id_create_transportation_order_from_unpicked_records_post**
> TransportationOrderIdIdCreatePickPost200Response transportation_order_id_id_create_transportation_order_from_unpicked_records_post(id, transportation_order_id_id_create_transportation_order_from_unpicked_records_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order_id_id_create_pick_post200_response import TransportationOrderIdIdCreatePickPost200Response
from openapi_client.models.transportation_order_id_id_create_transportation_order_from_unpicked_records_post_request import TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    transportation_order_id_id_create_transportation_order_from_unpicked_records_post_request = openapi_client.TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest() # TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest | 

    try:
        api_response = api_instance.transportation_order_id_id_create_transportation_order_from_unpicked_records_post(id, transportation_order_id_id_create_transportation_order_from_unpicked_records_post_request)
        print("The response of TransportationOrderApi->transportation_order_id_id_create_transportation_order_from_unpicked_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_create_transportation_order_from_unpicked_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transportation_order_id_id_create_transportation_order_from_unpicked_records_post_request** | [**TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest**](TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest.md)|  | 

### Return type

[**TransportationOrderIdIdCreatePickPost200Response**](TransportationOrderIdIdCreatePickPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createTransportationOrderFromUnpickedRecords response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_delete**
> transportation_order_id_id_delete(id, dry_run=dry_run)

delete a transportationOrder

delete a transportationOrder

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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a transportationOrder
        api_instance.transportation_order_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_delete: %s\n" % e)
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
**204** | transportationOrder delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_get**
> TransportationOrder transportation_order_id_id_get(id)

query a specific transportationOrder

query a specific transportationOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order import TransportationOrder
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific transportationOrder
        api_response = api_instance.transportation_order_id_id_get(id)
        print("The response of TransportationOrderApi->transportation_order_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TransportationOrder**](TransportationOrder.md)

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

# **transportation_order_id_id_internal_transport_references_for_pick_up_get**
> InternalTransportReferenceGet200Response transportation_order_id_id_internal_transport_references_for_pick_up_get(id, ignore_current_loading_equipment=ignore_current_loading_equipment)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.internal_transport_reference_get200_response import InternalTransportReferenceGet200Response
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    ignore_current_loading_equipment = True # bool |  (optional)

    try:
        api_response = api_instance.transportation_order_id_id_internal_transport_references_for_pick_up_get(id, ignore_current_loading_equipment=ignore_current_loading_equipment)
        print("The response of TransportationOrderApi->transportation_order_id_id_internal_transport_references_for_pick_up_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_internal_transport_references_for_pick_up_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ignore_current_loading_equipment** | **bool**|  | [optional] 

### Return type

[**InternalTransportReferenceGet200Response**](InternalTransportReferenceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | internalTransportReferencesForPickUp response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_pick_pick_post**
> TransportationOrderIdIdCreatePickPost200Response transportation_order_id_id_pick_pick_post(id, transportation_order_id_id_pick_pick_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order_id_id_create_pick_post200_response import TransportationOrderIdIdCreatePickPost200Response
from openapi_client.models.transportation_order_id_id_pick_pick_post_request import TransportationOrderIdIdPickPickPostRequest
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    transportation_order_id_id_pick_pick_post_request = openapi_client.TransportationOrderIdIdPickPickPostRequest() # TransportationOrderIdIdPickPickPostRequest | 

    try:
        api_response = api_instance.transportation_order_id_id_pick_pick_post(id, transportation_order_id_id_pick_pick_post_request)
        print("The response of TransportationOrderApi->transportation_order_id_id_pick_pick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_pick_pick_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transportation_order_id_id_pick_pick_post_request** | [**TransportationOrderIdIdPickPickPostRequest**](TransportationOrderIdIdPickPickPostRequest.md)|  | 

### Return type

[**TransportationOrderIdIdCreatePickPost200Response**](TransportationOrderIdIdCreatePickPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pickPick response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_put**
> TransportationOrder transportation_order_id_id_put(id, transportation_order, dry_run=dry_run)

update a transportationOrder

update transportationOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order import TransportationOrder
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    transportation_order = openapi_client.TransportationOrder() # TransportationOrder | 
    dry_run = True # bool |  (optional)

    try:
        # update a transportationOrder
        api_response = api_instance.transportation_order_id_id_put(id, transportation_order, dry_run=dry_run)
        print("The response of TransportationOrderApi->transportation_order_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transportation_order** | [**TransportationOrder**](TransportationOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TransportationOrder**](TransportationOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transportationOrder update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_id_id_put_down_internal_transport_reference_post**
> TransportationOrderIdIdCreatePickPost200Response transportation_order_id_id_put_down_internal_transport_reference_post(id, transportation_order_id_id_put_down_internal_transport_reference_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order_id_id_create_pick_post200_response import TransportationOrderIdIdCreatePickPost200Response
from openapi_client.models.transportation_order_id_id_put_down_internal_transport_reference_post_request import TransportationOrderIdIdPutDownInternalTransportReferencePostRequest
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    id = 'id_example' # str | 
    transportation_order_id_id_put_down_internal_transport_reference_post_request = openapi_client.TransportationOrderIdIdPutDownInternalTransportReferencePostRequest() # TransportationOrderIdIdPutDownInternalTransportReferencePostRequest | 

    try:
        api_response = api_instance.transportation_order_id_id_put_down_internal_transport_reference_post(id, transportation_order_id_id_put_down_internal_transport_reference_post_request)
        print("The response of TransportationOrderApi->transportation_order_id_id_put_down_internal_transport_reference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_id_id_put_down_internal_transport_reference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transportation_order_id_id_put_down_internal_transport_reference_post_request** | [**TransportationOrderIdIdPutDownInternalTransportReferencePostRequest**](TransportationOrderIdIdPutDownInternalTransportReferencePostRequest.md)|  | 

### Return type

[**TransportationOrderIdIdCreatePickPost200Response**](TransportationOrderIdIdCreatePickPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | putDownInternalTransportReference response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transportation_order_post**
> TransportationOrder transportation_order_post(transportation_order, dry_run=dry_run)

create a transportationOrder

create a transportationOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.transportation_order import TransportationOrder
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
    api_instance = openapi_client.TransportationOrderApi(api_client)
    transportation_order = openapi_client.TransportationOrder() # TransportationOrder | 
    dry_run = True # bool |  (optional)

    try:
        # create a transportationOrder
        api_response = api_instance.transportation_order_post(transportation_order, dry_run=dry_run)
        print("The response of TransportationOrderApi->transportation_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportationOrderApi->transportation_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportation_order** | [**TransportationOrder**](TransportationOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TransportationOrder**](TransportationOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | transportationOrder create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

