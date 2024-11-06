# openapi_client.ShipmentMethodApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_method_count_get**](ShipmentMethodApi.md#shipment_method_count_get) | **GET** /shipmentMethod/count | count shipmentMethod
[**shipment_method_get**](ShipmentMethodApi.md#shipment_method_get) | **GET** /shipmentMethod | query shipmentMethod
[**shipment_method_id_id_delete**](ShipmentMethodApi.md#shipment_method_id_id_delete) | **DELETE** /shipmentMethod/id/{id} | delete a shipmentMethod
[**shipment_method_id_id_get**](ShipmentMethodApi.md#shipment_method_id_id_get) | **GET** /shipmentMethod/id/{id} | query a specific shipmentMethod
[**shipment_method_id_id_put**](ShipmentMethodApi.md#shipment_method_id_id_put) | **PUT** /shipmentMethod/id/{id} | update a shipmentMethod
[**shipment_method_post**](ShipmentMethodApi.md#shipment_method_post) | **POST** /shipmentMethod | create a shipmentMethod


# **shipment_method_count_get**
> AccountingTransactionCountGet200Response shipment_method_count_get()

count shipmentMethod

count shipmentMethod

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
    api_instance = openapi_client.ShipmentMethodApi(api_client)

    try:
        # count shipmentMethod
        api_response = api_instance.shipment_method_count_get()
        print("The response of ShipmentMethodApi->shipment_method_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_count_get: %s\n" % e)
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

# **shipment_method_get**
> ShipmentMethodGet200Response shipment_method_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query shipmentMethod

query shipmentMethod

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_method_get200_response import ShipmentMethodGet200Response
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
    api_instance = openapi_client.ShipmentMethodApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query shipmentMethod
        api_response = api_instance.shipment_method_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ShipmentMethodApi->shipment_method_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_get: %s\n" % e)
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

[**ShipmentMethodGet200Response**](ShipmentMethodGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipmentMethod response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_method_id_id_delete**
> shipment_method_id_id_delete(id, dry_run=dry_run)

delete a shipmentMethod

delete a shipmentMethod

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
    api_instance = openapi_client.ShipmentMethodApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a shipmentMethod
        api_instance.shipment_method_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_id_id_delete: %s\n" % e)
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
**204** | shipmentMethod delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_method_id_id_get**
> ShipmentMethod shipment_method_id_id_get(id)

query a specific shipmentMethod

query a specific shipmentMethod

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_method import ShipmentMethod
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
    api_instance = openapi_client.ShipmentMethodApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific shipmentMethod
        api_response = api_instance.shipment_method_id_id_get(id)
        print("The response of ShipmentMethodApi->shipment_method_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

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

# **shipment_method_id_id_put**
> ShipmentMethod shipment_method_id_id_put(id, shipment_method, dry_run=dry_run)

update a shipmentMethod

update shipmentMethod

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_method import ShipmentMethod
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
    api_instance = openapi_client.ShipmentMethodApi(api_client)
    id = 'id_example' # str | 
    shipment_method = openapi_client.ShipmentMethod() # ShipmentMethod | 
    dry_run = True # bool |  (optional)

    try:
        # update a shipmentMethod
        api_response = api_instance.shipment_method_id_id_put(id, shipment_method, dry_run=dry_run)
        print("The response of ShipmentMethodApi->shipment_method_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shipment_method** | [**ShipmentMethod**](ShipmentMethod.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipmentMethod update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_method_post**
> ShipmentMethod shipment_method_post(shipment_method, dry_run=dry_run)

create a shipmentMethod

create a shipmentMethod

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_method import ShipmentMethod
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
    api_instance = openapi_client.ShipmentMethodApi(api_client)
    shipment_method = openapi_client.ShipmentMethod() # ShipmentMethod | 
    dry_run = True # bool |  (optional)

    try:
        # create a shipmentMethod
        api_response = api_instance.shipment_method_post(shipment_method, dry_run=dry_run)
        print("The response of ShipmentMethodApi->shipment_method_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentMethodApi->shipment_method_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_method** | [**ShipmentMethod**](ShipmentMethod.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | shipmentMethod create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

