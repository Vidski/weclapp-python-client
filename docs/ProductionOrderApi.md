# openapi_client.ProductionOrderApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**production_order_count_get**](ProductionOrderApi.md#production_order_count_get) | **GET** /productionOrder/count | count productionOrder
[**production_order_fast_production_booking_post**](ProductionOrderApi.md#production_order_fast_production_booking_post) | **POST** /productionOrder/fastProductionBooking | 
[**production_order_get**](ProductionOrderApi.md#production_order_get) | **GET** /productionOrder | query productionOrder
[**production_order_id_id_create_picking_list_post**](ProductionOrderApi.md#production_order_id_id_create_picking_list_post) | **POST** /productionOrder/id/{id}/createPickingList | 
[**production_order_id_id_delete**](ProductionOrderApi.md#production_order_id_id_delete) | **DELETE** /productionOrder/id/{id} | delete a productionOrder
[**production_order_id_id_download_latest_production_order_pdf_get**](ProductionOrderApi.md#production_order_id_id_download_latest_production_order_pdf_get) | **GET** /productionOrder/id/{id}/downloadLatestProductionOrderPdf | 
[**production_order_id_id_get**](ProductionOrderApi.md#production_order_id_id_get) | **GET** /productionOrder/id/{id} | query a specific productionOrder
[**production_order_id_id_put**](ProductionOrderApi.md#production_order_id_id_put) | **PUT** /productionOrder/id/{id} | update a productionOrder
[**production_order_post**](ProductionOrderApi.md#production_order_post) | **POST** /productionOrder | create a productionOrder


# **production_order_count_get**
> AccountingTransactionCountGet200Response production_order_count_get()

count productionOrder

count productionOrder

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
    api_instance = openapi_client.ProductionOrderApi(api_client)

    try:
        # count productionOrder
        api_response = api_instance.production_order_count_get()
        print("The response of ProductionOrderApi->production_order_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_count_get: %s\n" % e)
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

# **production_order_fast_production_booking_post**
> ProductionOrderFastProductionBookingPost200Response production_order_fast_production_booking_post(production_order_fast_production_booking_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_order_fast_production_booking_post200_response import ProductionOrderFastProductionBookingPost200Response
from openapi_client.models.production_order_fast_production_booking_post_request import ProductionOrderFastProductionBookingPostRequest
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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    production_order_fast_production_booking_post_request = openapi_client.ProductionOrderFastProductionBookingPostRequest() # ProductionOrderFastProductionBookingPostRequest | 

    try:
        api_response = api_instance.production_order_fast_production_booking_post(production_order_fast_production_booking_post_request)
        print("The response of ProductionOrderApi->production_order_fast_production_booking_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_fast_production_booking_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_order_fast_production_booking_post_request** | [**ProductionOrderFastProductionBookingPostRequest**](ProductionOrderFastProductionBookingPostRequest.md)|  | 

### Return type

[**ProductionOrderFastProductionBookingPost200Response**](ProductionOrderFastProductionBookingPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | fastProductionBooking response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_order_get**
> ProductionOrderGet200Response production_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query productionOrder

query productionOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_order_get200_response import ProductionOrderGet200Response
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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query productionOrder
        api_response = api_instance.production_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ProductionOrderApi->production_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_get: %s\n" % e)
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

[**ProductionOrderGet200Response**](ProductionOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_order_id_id_create_picking_list_post**
> bytearray production_order_id_id_create_picking_list_post(id, body)



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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.production_order_id_id_create_picking_list_post(id, body)
        print("The response of ProductionOrderApi->production_order_id_id_create_picking_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_id_id_create_picking_list_post: %s\n" % e)
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

# **production_order_id_id_delete**
> production_order_id_id_delete(id, dry_run=dry_run)

delete a productionOrder

delete a productionOrder

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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a productionOrder
        api_instance.production_order_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_id_id_delete: %s\n" % e)
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
**204** | productionOrder delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_order_id_id_download_latest_production_order_pdf_get**
> bytearray production_order_id_id_download_latest_production_order_pdf_get(id)



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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.production_order_id_id_download_latest_production_order_pdf_get(id)
        print("The response of ProductionOrderApi->production_order_id_id_download_latest_production_order_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_id_id_download_latest_production_order_pdf_get: %s\n" % e)
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
**200** | downloadLatestProductionOrderPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_order_id_id_get**
> ProductionOrder production_order_id_id_get(id)

query a specific productionOrder

query a specific productionOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_order import ProductionOrder
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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific productionOrder
        api_response = api_instance.production_order_id_id_get(id)
        print("The response of ProductionOrderApi->production_order_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProductionOrder**](ProductionOrder.md)

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

# **production_order_id_id_put**
> ProductionOrder production_order_id_id_put(id, production_order, dry_run=dry_run)

update a productionOrder

update productionOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_order import ProductionOrder
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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    id = 'id_example' # str | 
    production_order = openapi_client.ProductionOrder() # ProductionOrder | 
    dry_run = True # bool |  (optional)

    try:
        # update a productionOrder
        api_response = api_instance.production_order_id_id_put(id, production_order, dry_run=dry_run)
        print("The response of ProductionOrderApi->production_order_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **production_order** | [**ProductionOrder**](ProductionOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionOrder**](ProductionOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionOrder update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_order_post**
> ProductionOrder production_order_post(production_order, dry_run=dry_run)

create a productionOrder

create a productionOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_order import ProductionOrder
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
    api_instance = openapi_client.ProductionOrderApi(api_client)
    production_order = openapi_client.ProductionOrder() # ProductionOrder | 
    dry_run = True # bool |  (optional)

    try:
        # create a productionOrder
        api_response = api_instance.production_order_post(production_order, dry_run=dry_run)
        print("The response of ProductionOrderApi->production_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionOrderApi->production_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_order** | [**ProductionOrder**](ProductionOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionOrder**](ProductionOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | productionOrder create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

