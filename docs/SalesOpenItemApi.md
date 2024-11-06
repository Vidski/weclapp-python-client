# openapi_client.SalesOpenItemApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_open_item_count_get**](SalesOpenItemApi.md#sales_open_item_count_get) | **GET** /salesOpenItem/count | count salesOpenItem
[**sales_open_item_get**](SalesOpenItemApi.md#sales_open_item_get) | **GET** /salesOpenItem | query salesOpenItem
[**sales_open_item_id_id_create_payment_application_post**](SalesOpenItemApi.md#sales_open_item_id_id_create_payment_application_post) | **POST** /salesOpenItem/id/{id}/createPaymentApplication | 
[**sales_open_item_id_id_get**](SalesOpenItemApi.md#sales_open_item_id_id_get) | **GET** /salesOpenItem/id/{id} | query a specific salesOpenItem


# **sales_open_item_count_get**
> AccountingTransactionCountGet200Response sales_open_item_count_get()

count salesOpenItem

count salesOpenItem

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
    api_instance = openapi_client.SalesOpenItemApi(api_client)

    try:
        # count salesOpenItem
        api_response = api_instance.sales_open_item_count_get()
        print("The response of SalesOpenItemApi->sales_open_item_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOpenItemApi->sales_open_item_count_get: %s\n" % e)
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

# **sales_open_item_get**
> SalesOpenItemGet200Response sales_open_item_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query salesOpenItem

query salesOpenItem

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_open_item_get200_response import SalesOpenItemGet200Response
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
    api_instance = openapi_client.SalesOpenItemApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query salesOpenItem
        api_response = api_instance.sales_open_item_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of SalesOpenItemApi->sales_open_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOpenItemApi->sales_open_item_get: %s\n" % e)
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

[**SalesOpenItemGet200Response**](SalesOpenItemGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | salesOpenItem response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_open_item_id_id_create_payment_application_post**
> SalesOpenItemIdIdCreatePaymentApplicationPost200Response sales_open_item_id_id_create_payment_application_post(id, purchase_open_item_id_id_create_payment_application_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_open_item_id_id_create_payment_application_post_request import PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest
from openapi_client.models.sales_open_item_id_id_create_payment_application_post200_response import SalesOpenItemIdIdCreatePaymentApplicationPost200Response
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
    api_instance = openapi_client.SalesOpenItemApi(api_client)
    id = 'id_example' # str | 
    purchase_open_item_id_id_create_payment_application_post_request = openapi_client.PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest() # PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest | 

    try:
        api_response = api_instance.sales_open_item_id_id_create_payment_application_post(id, purchase_open_item_id_id_create_payment_application_post_request)
        print("The response of SalesOpenItemApi->sales_open_item_id_id_create_payment_application_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOpenItemApi->sales_open_item_id_id_create_payment_application_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_open_item_id_id_create_payment_application_post_request** | [**PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest**](PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest.md)|  | 

### Return type

[**SalesOpenItemIdIdCreatePaymentApplicationPost200Response**](SalesOpenItemIdIdCreatePaymentApplicationPost200Response.md)

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

# **sales_open_item_id_id_get**
> SalesOpenItem sales_open_item_id_id_get(id)

query a specific salesOpenItem

query a specific salesOpenItem

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_open_item import SalesOpenItem
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
    api_instance = openapi_client.SalesOpenItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific salesOpenItem
        api_response = api_instance.sales_open_item_id_id_get(id)
        print("The response of SalesOpenItemApi->sales_open_item_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesOpenItemApi->sales_open_item_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SalesOpenItem**](SalesOpenItem.md)

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

