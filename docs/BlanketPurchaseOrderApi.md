# openapi_client.BlanketPurchaseOrderApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blanket_purchase_order_count_get**](BlanketPurchaseOrderApi.md#blanket_purchase_order_count_get) | **GET** /blanketPurchaseOrder/count | count blanketPurchaseOrder
[**blanket_purchase_order_get**](BlanketPurchaseOrderApi.md#blanket_purchase_order_get) | **GET** /blanketPurchaseOrder | query blanketPurchaseOrder
[**blanket_purchase_order_id_id_delete**](BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_delete) | **DELETE** /blanketPurchaseOrder/id/{id} | delete a blanketPurchaseOrder
[**blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get**](BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get) | **GET** /blanketPurchaseOrder/id/{id}/downloadLatestBlanketPurchaseOrderPdf | 
[**blanket_purchase_order_id_id_generate_releases_post**](BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_generate_releases_post) | **POST** /blanketPurchaseOrder/id/{id}/generateReleases | 
[**blanket_purchase_order_id_id_get**](BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_get) | **GET** /blanketPurchaseOrder/id/{id} | query a specific blanketPurchaseOrder
[**blanket_purchase_order_id_id_put**](BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_put) | **PUT** /blanketPurchaseOrder/id/{id} | update a blanketPurchaseOrder
[**blanket_purchase_order_post**](BlanketPurchaseOrderApi.md#blanket_purchase_order_post) | **POST** /blanketPurchaseOrder | create a blanketPurchaseOrder


# **blanket_purchase_order_count_get**
> AccountingTransactionCountGet200Response blanket_purchase_order_count_get()

count blanketPurchaseOrder

count blanketPurchaseOrder

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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)

    try:
        # count blanketPurchaseOrder
        api_response = api_instance.blanket_purchase_order_count_get()
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_count_get: %s\n" % e)
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

# **blanket_purchase_order_get**
> BlanketPurchaseOrderGet200Response blanket_purchase_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query blanketPurchaseOrder

query blanketPurchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.blanket_purchase_order_get200_response import BlanketPurchaseOrderGet200Response
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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query blanketPurchaseOrder
        api_response = api_instance.blanket_purchase_order_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_get: %s\n" % e)
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

[**BlanketPurchaseOrderGet200Response**](BlanketPurchaseOrderGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blanketPurchaseOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blanket_purchase_order_id_id_delete**
> blanket_purchase_order_id_id_delete(id, dry_run=dry_run)

delete a blanketPurchaseOrder

delete a blanketPurchaseOrder

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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a blanketPurchaseOrder
        api_instance.blanket_purchase_order_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_id_id_delete: %s\n" % e)
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
**204** | blanketPurchaseOrder delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get**
> bytearray blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get(id)



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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get(id)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get: %s\n" % e)
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
**200** | downloadLatestBlanketPurchaseOrderPdf response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blanket_purchase_order_id_id_generate_releases_post**
> BlanketPurchaseOrderIdIdGenerateReleasesPost200Response blanket_purchase_order_id_id_generate_releases_post(id, blanket_purchase_order_id_id_generate_releases_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.blanket_purchase_order_id_id_generate_releases_post200_response import BlanketPurchaseOrderIdIdGenerateReleasesPost200Response
from openapi_client.models.blanket_purchase_order_id_id_generate_releases_post_request import BlanketPurchaseOrderIdIdGenerateReleasesPostRequest
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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    blanket_purchase_order_id_id_generate_releases_post_request = openapi_client.BlanketPurchaseOrderIdIdGenerateReleasesPostRequest() # BlanketPurchaseOrderIdIdGenerateReleasesPostRequest | 

    try:
        api_response = api_instance.blanket_purchase_order_id_id_generate_releases_post(id, blanket_purchase_order_id_id_generate_releases_post_request)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_id_id_generate_releases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_id_id_generate_releases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **blanket_purchase_order_id_id_generate_releases_post_request** | [**BlanketPurchaseOrderIdIdGenerateReleasesPostRequest**](BlanketPurchaseOrderIdIdGenerateReleasesPostRequest.md)|  | 

### Return type

[**BlanketPurchaseOrderIdIdGenerateReleasesPost200Response**](BlanketPurchaseOrderIdIdGenerateReleasesPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | generateReleases response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blanket_purchase_order_id_id_get**
> BlanketPurchaseOrder blanket_purchase_order_id_id_get(id)

query a specific blanketPurchaseOrder

query a specific blanketPurchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.blanket_purchase_order import BlanketPurchaseOrder
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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific blanketPurchaseOrder
        api_response = api_instance.blanket_purchase_order_id_id_get(id)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BlanketPurchaseOrder**](BlanketPurchaseOrder.md)

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

# **blanket_purchase_order_id_id_put**
> BlanketPurchaseOrder blanket_purchase_order_id_id_put(id, blanket_purchase_order, dry_run=dry_run)

update a blanketPurchaseOrder

update blanketPurchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.blanket_purchase_order import BlanketPurchaseOrder
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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    id = 'id_example' # str | 
    blanket_purchase_order = openapi_client.BlanketPurchaseOrder() # BlanketPurchaseOrder | 
    dry_run = True # bool |  (optional)

    try:
        # update a blanketPurchaseOrder
        api_response = api_instance.blanket_purchase_order_id_id_put(id, blanket_purchase_order, dry_run=dry_run)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **blanket_purchase_order** | [**BlanketPurchaseOrder**](BlanketPurchaseOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**BlanketPurchaseOrder**](BlanketPurchaseOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | blanketPurchaseOrder update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blanket_purchase_order_post**
> BlanketPurchaseOrder blanket_purchase_order_post(blanket_purchase_order, dry_run=dry_run)

create a blanketPurchaseOrder

create a blanketPurchaseOrder

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.blanket_purchase_order import BlanketPurchaseOrder
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
    api_instance = openapi_client.BlanketPurchaseOrderApi(api_client)
    blanket_purchase_order = openapi_client.BlanketPurchaseOrder() # BlanketPurchaseOrder | 
    dry_run = True # bool |  (optional)

    try:
        # create a blanketPurchaseOrder
        api_response = api_instance.blanket_purchase_order_post(blanket_purchase_order, dry_run=dry_run)
        print("The response of BlanketPurchaseOrderApi->blanket_purchase_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlanketPurchaseOrderApi->blanket_purchase_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blanket_purchase_order** | [**BlanketPurchaseOrder**](BlanketPurchaseOrder.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**BlanketPurchaseOrder**](BlanketPurchaseOrder.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | blanketPurchaseOrder create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

