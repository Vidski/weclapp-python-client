# openapi_client.PurchaseOpenItemApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_open_item_count_get**](PurchaseOpenItemApi.md#purchase_open_item_count_get) | **GET** /purchaseOpenItem/count | count purchaseOpenItem
[**purchase_open_item_get**](PurchaseOpenItemApi.md#purchase_open_item_get) | **GET** /purchaseOpenItem | query purchaseOpenItem
[**purchase_open_item_id_id_create_payment_application_post**](PurchaseOpenItemApi.md#purchase_open_item_id_id_create_payment_application_post) | **POST** /purchaseOpenItem/id/{id}/createPaymentApplication | 
[**purchase_open_item_id_id_get**](PurchaseOpenItemApi.md#purchase_open_item_id_id_get) | **GET** /purchaseOpenItem/id/{id} | query a specific purchaseOpenItem


# **purchase_open_item_count_get**
> AccountingTransactionCountGet200Response purchase_open_item_count_get()

count purchaseOpenItem

count purchaseOpenItem

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
    api_instance = openapi_client.PurchaseOpenItemApi(api_client)

    try:
        # count purchaseOpenItem
        api_response = api_instance.purchase_open_item_count_get()
        print("The response of PurchaseOpenItemApi->purchase_open_item_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOpenItemApi->purchase_open_item_count_get: %s\n" % e)
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

# **purchase_open_item_get**
> PurchaseOpenItemGet200Response purchase_open_item_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query purchaseOpenItem

query purchaseOpenItem

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_open_item_get200_response import PurchaseOpenItemGet200Response
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
    api_instance = openapi_client.PurchaseOpenItemApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query purchaseOpenItem
        api_response = api_instance.purchase_open_item_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of PurchaseOpenItemApi->purchase_open_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOpenItemApi->purchase_open_item_get: %s\n" % e)
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

[**PurchaseOpenItemGet200Response**](PurchaseOpenItemGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseOpenItem response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_open_item_id_id_create_payment_application_post**
> PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response purchase_open_item_id_id_create_payment_application_post(id, purchase_open_item_id_id_create_payment_application_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_open_item_id_id_create_payment_application_post200_response import PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response
from openapi_client.models.purchase_open_item_id_id_create_payment_application_post_request import PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest
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
    api_instance = openapi_client.PurchaseOpenItemApi(api_client)
    id = 'id_example' # str | 
    purchase_open_item_id_id_create_payment_application_post_request = openapi_client.PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest() # PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest | 

    try:
        api_response = api_instance.purchase_open_item_id_id_create_payment_application_post(id, purchase_open_item_id_id_create_payment_application_post_request)
        print("The response of PurchaseOpenItemApi->purchase_open_item_id_id_create_payment_application_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOpenItemApi->purchase_open_item_id_id_create_payment_application_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_open_item_id_id_create_payment_application_post_request** | [**PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest**](PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest.md)|  | 

### Return type

[**PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response**](PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPaymentApplication response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_open_item_id_id_get**
> PurchaseOpenItem purchase_open_item_id_id_get(id)

query a specific purchaseOpenItem

query a specific purchaseOpenItem

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_open_item import PurchaseOpenItem
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
    api_instance = openapi_client.PurchaseOpenItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific purchaseOpenItem
        api_response = api_instance.purchase_open_item_id_id_get(id)
        print("The response of PurchaseOpenItemApi->purchase_open_item_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOpenItemApi->purchase_open_item_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PurchaseOpenItem**](PurchaseOpenItem.md)

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

