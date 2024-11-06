# openapi_client.PurchaseOrderRequestApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_order_request_count_get**](PurchaseOrderRequestApi.md#purchase_order_request_count_get) | **GET** /purchaseOrderRequest/count | count purchaseOrderRequest
[**purchase_order_request_get**](PurchaseOrderRequestApi.md#purchase_order_request_get) | **GET** /purchaseOrderRequest | query purchaseOrderRequest
[**purchase_order_request_id_id_create_blanket_purchase_order_post**](PurchaseOrderRequestApi.md#purchase_order_request_id_id_create_blanket_purchase_order_post) | **POST** /purchaseOrderRequest/id/{id}/createBlanketPurchaseOrder | 
[**purchase_order_request_id_id_create_purchase_order_post**](PurchaseOrderRequestApi.md#purchase_order_request_id_id_create_purchase_order_post) | **POST** /purchaseOrderRequest/id/{id}/createPurchaseOrder | 
[**purchase_order_request_id_id_delete**](PurchaseOrderRequestApi.md#purchase_order_request_id_id_delete) | **DELETE** /purchaseOrderRequest/id/{id} | delete a purchaseOrderRequest
[**purchase_order_request_id_id_get**](PurchaseOrderRequestApi.md#purchase_order_request_id_id_get) | **GET** /purchaseOrderRequest/id/{id} | query a specific purchaseOrderRequest
[**purchase_order_request_id_id_put**](PurchaseOrderRequestApi.md#purchase_order_request_id_id_put) | **PUT** /purchaseOrderRequest/id/{id} | update a purchaseOrderRequest
[**purchase_order_request_post**](PurchaseOrderRequestApi.md#purchase_order_request_post) | **POST** /purchaseOrderRequest | create a purchaseOrderRequest


# **purchase_order_request_count_get**
> AccountingTransactionCountGet200Response purchase_order_request_count_get()

count purchaseOrderRequest

count purchaseOrderRequest

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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)

    try:
        # count purchaseOrderRequest
        api_response = api_instance.purchase_order_request_count_get()
        print("The response of PurchaseOrderRequestApi->purchase_order_request_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_count_get: %s\n" % e)
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

# **purchase_order_request_get**
> PurchaseOrderRequestGet200Response purchase_order_request_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query purchaseOrderRequest

query purchaseOrderRequest

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_request_get200_response import PurchaseOrderRequestGet200Response
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query purchaseOrderRequest
        api_response = api_instance.purchase_order_request_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_get: %s\n" % e)
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

[**PurchaseOrderRequestGet200Response**](PurchaseOrderRequestGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseOrderRequest response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_request_id_id_create_blanket_purchase_order_post**
> PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response purchase_order_request_id_id_create_blanket_purchase_order_post(id, purchase_order_request_id_id_create_blanket_purchase_order_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_request_id_id_create_blanket_purchase_order_post200_response import PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response
from openapi_client.models.purchase_order_request_id_id_create_blanket_purchase_order_post_request import PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    id = 'id_example' # str | 
    purchase_order_request_id_id_create_blanket_purchase_order_post_request = openapi_client.PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest() # PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest | 

    try:
        api_response = api_instance.purchase_order_request_id_id_create_blanket_purchase_order_post(id, purchase_order_request_id_id_create_blanket_purchase_order_post_request)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_id_id_create_blanket_purchase_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_id_id_create_blanket_purchase_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order_request_id_id_create_blanket_purchase_order_post_request** | [**PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest**](PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest.md)|  | 

### Return type

[**PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response**](PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createBlanketPurchaseOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_request_id_id_create_purchase_order_post**
> PurchaseOrderIdIdProcessDropshippingPost200Response purchase_order_request_id_id_create_purchase_order_post(id, purchase_order_request_id_id_create_purchase_order_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_id_id_process_dropshipping_post200_response import PurchaseOrderIdIdProcessDropshippingPost200Response
from openapi_client.models.purchase_order_request_id_id_create_purchase_order_post_request import PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    id = 'id_example' # str | 
    purchase_order_request_id_id_create_purchase_order_post_request = openapi_client.PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest() # PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest | 

    try:
        api_response = api_instance.purchase_order_request_id_id_create_purchase_order_post(id, purchase_order_request_id_id_create_purchase_order_post_request)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_id_id_create_purchase_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_id_id_create_purchase_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order_request_id_id_create_purchase_order_post_request** | [**PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest**](PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest.md)|  | 

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
**200** | createPurchaseOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_request_id_id_delete**
> purchase_order_request_id_id_delete(id, dry_run=dry_run)

delete a purchaseOrderRequest

delete a purchaseOrderRequest

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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a purchaseOrderRequest
        api_instance.purchase_order_request_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_id_id_delete: %s\n" % e)
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
**204** | purchaseOrderRequest delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_request_id_id_get**
> PurchaseOrderRequest purchase_order_request_id_id_get(id)

query a specific purchaseOrderRequest

query a specific purchaseOrderRequest

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_request import PurchaseOrderRequest
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific purchaseOrderRequest
        api_response = api_instance.purchase_order_request_id_id_get(id)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PurchaseOrderRequest**](PurchaseOrderRequest.md)

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

# **purchase_order_request_id_id_put**
> PurchaseOrderRequest purchase_order_request_id_id_put(id, purchase_order_request, dry_run=dry_run)

update a purchaseOrderRequest

update purchaseOrderRequest

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_request import PurchaseOrderRequest
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    id = 'id_example' # str | 
    purchase_order_request = openapi_client.PurchaseOrderRequest() # PurchaseOrderRequest | 
    dry_run = True # bool |  (optional)

    try:
        # update a purchaseOrderRequest
        api_response = api_instance.purchase_order_request_id_id_put(id, purchase_order_request, dry_run=dry_run)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_order_request** | [**PurchaseOrderRequest**](PurchaseOrderRequest.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseOrderRequest**](PurchaseOrderRequest.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseOrderRequest update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_order_request_post**
> PurchaseOrderRequest purchase_order_request_post(purchase_order_request, dry_run=dry_run)

create a purchaseOrderRequest

create a purchaseOrderRequest

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_order_request import PurchaseOrderRequest
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
    api_instance = openapi_client.PurchaseOrderRequestApi(api_client)
    purchase_order_request = openapi_client.PurchaseOrderRequest() # PurchaseOrderRequest | 
    dry_run = True # bool |  (optional)

    try:
        # create a purchaseOrderRequest
        api_response = api_instance.purchase_order_request_post(purchase_order_request, dry_run=dry_run)
        print("The response of PurchaseOrderRequestApi->purchase_order_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderRequestApi->purchase_order_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_request** | [**PurchaseOrderRequest**](PurchaseOrderRequest.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseOrderRequest**](PurchaseOrderRequest.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | purchaseOrderRequest create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

