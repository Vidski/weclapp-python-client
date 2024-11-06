# openapi_client.ShippingCarrierApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipping_carrier_count_get**](ShippingCarrierApi.md#shipping_carrier_count_get) | **GET** /shippingCarrier/count | count shippingCarrier
[**shipping_carrier_get**](ShippingCarrierApi.md#shipping_carrier_get) | **GET** /shippingCarrier | query shippingCarrier
[**shipping_carrier_id_id_delete**](ShippingCarrierApi.md#shipping_carrier_id_id_delete) | **DELETE** /shippingCarrier/id/{id} | delete a shippingCarrier
[**shipping_carrier_id_id_get**](ShippingCarrierApi.md#shipping_carrier_id_id_get) | **GET** /shippingCarrier/id/{id} | query a specific shippingCarrier
[**shipping_carrier_id_id_put**](ShippingCarrierApi.md#shipping_carrier_id_id_put) | **PUT** /shippingCarrier/id/{id} | update a shippingCarrier
[**shipping_carrier_post**](ShippingCarrierApi.md#shipping_carrier_post) | **POST** /shippingCarrier | create a shippingCarrier


# **shipping_carrier_count_get**
> AccountingTransactionCountGet200Response shipping_carrier_count_get()

count shippingCarrier

count shippingCarrier

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
    api_instance = openapi_client.ShippingCarrierApi(api_client)

    try:
        # count shippingCarrier
        api_response = api_instance.shipping_carrier_count_get()
        print("The response of ShippingCarrierApi->shipping_carrier_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_count_get: %s\n" % e)
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

# **shipping_carrier_get**
> ShippingCarrierGet200Response shipping_carrier_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query shippingCarrier

query shippingCarrier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipping_carrier_get200_response import ShippingCarrierGet200Response
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
    api_instance = openapi_client.ShippingCarrierApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query shippingCarrier
        api_response = api_instance.shipping_carrier_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ShippingCarrierApi->shipping_carrier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_get: %s\n" % e)
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

[**ShippingCarrierGet200Response**](ShippingCarrierGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shippingCarrier response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipping_carrier_id_id_delete**
> shipping_carrier_id_id_delete(id, dry_run=dry_run)

delete a shippingCarrier

delete a shippingCarrier

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
    api_instance = openapi_client.ShippingCarrierApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a shippingCarrier
        api_instance.shipping_carrier_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_id_id_delete: %s\n" % e)
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
**204** | shippingCarrier delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipping_carrier_id_id_get**
> ShippingCarrier shipping_carrier_id_id_get(id)

query a specific shippingCarrier

query a specific shippingCarrier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipping_carrier import ShippingCarrier
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
    api_instance = openapi_client.ShippingCarrierApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific shippingCarrier
        api_response = api_instance.shipping_carrier_id_id_get(id)
        print("The response of ShippingCarrierApi->shipping_carrier_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ShippingCarrier**](ShippingCarrier.md)

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

# **shipping_carrier_id_id_put**
> ShippingCarrier shipping_carrier_id_id_put(id, shipping_carrier, dry_run=dry_run)

update a shippingCarrier

update shippingCarrier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipping_carrier import ShippingCarrier
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
    api_instance = openapi_client.ShippingCarrierApi(api_client)
    id = 'id_example' # str | 
    shipping_carrier = openapi_client.ShippingCarrier() # ShippingCarrier | 
    dry_run = True # bool |  (optional)

    try:
        # update a shippingCarrier
        api_response = api_instance.shipping_carrier_id_id_put(id, shipping_carrier, dry_run=dry_run)
        print("The response of ShippingCarrierApi->shipping_carrier_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shipping_carrier** | [**ShippingCarrier**](ShippingCarrier.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShippingCarrier**](ShippingCarrier.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shippingCarrier update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipping_carrier_post**
> ShippingCarrier shipping_carrier_post(shipping_carrier, dry_run=dry_run)

create a shippingCarrier

create a shippingCarrier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipping_carrier import ShippingCarrier
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
    api_instance = openapi_client.ShippingCarrierApi(api_client)
    shipping_carrier = openapi_client.ShippingCarrier() # ShippingCarrier | 
    dry_run = True # bool |  (optional)

    try:
        # create a shippingCarrier
        api_response = api_instance.shipping_carrier_post(shipping_carrier, dry_run=dry_run)
        print("The response of ShippingCarrierApi->shipping_carrier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingCarrierApi->shipping_carrier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_carrier** | [**ShippingCarrier**](ShippingCarrier.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShippingCarrier**](ShippingCarrier.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | shippingCarrier create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

