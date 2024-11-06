# openapi_client.ShipmentReturnRectificationApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_return_rectification_count_get**](ShipmentReturnRectificationApi.md#shipment_return_rectification_count_get) | **GET** /shipmentReturnRectification/count | count shipmentReturnRectification
[**shipment_return_rectification_get**](ShipmentReturnRectificationApi.md#shipment_return_rectification_get) | **GET** /shipmentReturnRectification | query shipmentReturnRectification
[**shipment_return_rectification_id_id_delete**](ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_delete) | **DELETE** /shipmentReturnRectification/id/{id} | delete a shipmentReturnRectification
[**shipment_return_rectification_id_id_get**](ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_get) | **GET** /shipmentReturnRectification/id/{id} | query a specific shipmentReturnRectification
[**shipment_return_rectification_id_id_put**](ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_put) | **PUT** /shipmentReturnRectification/id/{id} | update a shipmentReturnRectification
[**shipment_return_rectification_post**](ShipmentReturnRectificationApi.md#shipment_return_rectification_post) | **POST** /shipmentReturnRectification | create a shipmentReturnRectification


# **shipment_return_rectification_count_get**
> AccountingTransactionCountGet200Response shipment_return_rectification_count_get()

count shipmentReturnRectification

count shipmentReturnRectification

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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)

    try:
        # count shipmentReturnRectification
        api_response = api_instance.shipment_return_rectification_count_get()
        print("The response of ShipmentReturnRectificationApi->shipment_return_rectification_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_count_get: %s\n" % e)
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

# **shipment_return_rectification_get**
> ShipmentReturnAssessmentGet200Response shipment_return_rectification_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query shipmentReturnRectification

query shipmentReturnRectification

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_return_assessment_get200_response import ShipmentReturnAssessmentGet200Response
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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query shipmentReturnRectification
        api_response = api_instance.shipment_return_rectification_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ShipmentReturnRectificationApi->shipment_return_rectification_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_get: %s\n" % e)
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

[**ShipmentReturnAssessmentGet200Response**](ShipmentReturnAssessmentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipmentReturnRectification response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_rectification_id_id_delete**
> shipment_return_rectification_id_id_delete(id, dry_run=dry_run)

delete a shipmentReturnRectification

delete a shipmentReturnRectification

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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a shipmentReturnRectification
        api_instance.shipment_return_rectification_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_id_id_delete: %s\n" % e)
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
**204** | shipmentReturnRectification delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_rectification_id_id_get**
> ShipmentReturnDescription shipment_return_rectification_id_id_get(id)

query a specific shipmentReturnRectification

query a specific shipmentReturnRectification

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_return_description import ShipmentReturnDescription
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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific shipmentReturnRectification
        api_response = api_instance.shipment_return_rectification_id_id_get(id)
        print("The response of ShipmentReturnRectificationApi->shipment_return_rectification_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ShipmentReturnDescription**](ShipmentReturnDescription.md)

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

# **shipment_return_rectification_id_id_put**
> ShipmentReturnDescription shipment_return_rectification_id_id_put(id, shipment_return_description, dry_run=dry_run)

update a shipmentReturnRectification

update shipmentReturnRectification

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_return_description import ShipmentReturnDescription
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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)
    id = 'id_example' # str | 
    shipment_return_description = openapi_client.ShipmentReturnDescription() # ShipmentReturnDescription | 
    dry_run = True # bool |  (optional)

    try:
        # update a shipmentReturnRectification
        api_response = api_instance.shipment_return_rectification_id_id_put(id, shipment_return_description, dry_run=dry_run)
        print("The response of ShipmentReturnRectificationApi->shipment_return_rectification_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shipment_return_description** | [**ShipmentReturnDescription**](ShipmentReturnDescription.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShipmentReturnDescription**](ShipmentReturnDescription.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shipmentReturnRectification update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_rectification_post**
> ShipmentReturnDescription shipment_return_rectification_post(shipment_return_description, dry_run=dry_run)

create a shipmentReturnRectification

create a shipmentReturnRectification

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.shipment_return_description import ShipmentReturnDescription
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
    api_instance = openapi_client.ShipmentReturnRectificationApi(api_client)
    shipment_return_description = openapi_client.ShipmentReturnDescription() # ShipmentReturnDescription | 
    dry_run = True # bool |  (optional)

    try:
        # create a shipmentReturnRectification
        api_response = api_instance.shipment_return_rectification_post(shipment_return_description, dry_run=dry_run)
        print("The response of ShipmentReturnRectificationApi->shipment_return_rectification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnRectificationApi->shipment_return_rectification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_return_description** | [**ShipmentReturnDescription**](ShipmentReturnDescription.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ShipmentReturnDescription**](ShipmentReturnDescription.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | shipmentReturnRectification create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

