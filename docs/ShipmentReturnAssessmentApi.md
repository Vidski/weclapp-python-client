# openapi_client.ShipmentReturnAssessmentApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_return_assessment_count_get**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_count_get) | **GET** /shipmentReturnAssessment/count | count shipmentReturnAssessment
[**shipment_return_assessment_get**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_get) | **GET** /shipmentReturnAssessment | query shipmentReturnAssessment
[**shipment_return_assessment_id_id_delete**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_delete) | **DELETE** /shipmentReturnAssessment/id/{id} | delete a shipmentReturnAssessment
[**shipment_return_assessment_id_id_get**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_get) | **GET** /shipmentReturnAssessment/id/{id} | query a specific shipmentReturnAssessment
[**shipment_return_assessment_id_id_put**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_put) | **PUT** /shipmentReturnAssessment/id/{id} | update a shipmentReturnAssessment
[**shipment_return_assessment_post**](ShipmentReturnAssessmentApi.md#shipment_return_assessment_post) | **POST** /shipmentReturnAssessment | create a shipmentReturnAssessment


# **shipment_return_assessment_count_get**
> AccountingTransactionCountGet200Response shipment_return_assessment_count_get()

count shipmentReturnAssessment

count shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)

    try:
        # count shipmentReturnAssessment
        api_response = api_instance.shipment_return_assessment_count_get()
        print("The response of ShipmentReturnAssessmentApi->shipment_return_assessment_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_count_get: %s\n" % e)
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

# **shipment_return_assessment_get**
> ShipmentReturnAssessmentGet200Response shipment_return_assessment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query shipmentReturnAssessment

query shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query shipmentReturnAssessment
        api_response = api_instance.shipment_return_assessment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ShipmentReturnAssessmentApi->shipment_return_assessment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_get: %s\n" % e)
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
**200** | shipmentReturnAssessment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_assessment_id_id_delete**
> shipment_return_assessment_id_id_delete(id, dry_run=dry_run)

delete a shipmentReturnAssessment

delete a shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a shipmentReturnAssessment
        api_instance.shipment_return_assessment_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_id_id_delete: %s\n" % e)
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
**204** | shipmentReturnAssessment delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_assessment_id_id_get**
> ShipmentReturnDescription shipment_return_assessment_id_id_get(id)

query a specific shipmentReturnAssessment

query a specific shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific shipmentReturnAssessment
        api_response = api_instance.shipment_return_assessment_id_id_get(id)
        print("The response of ShipmentReturnAssessmentApi->shipment_return_assessment_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_id_id_get: %s\n" % e)
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

# **shipment_return_assessment_id_id_put**
> ShipmentReturnDescription shipment_return_assessment_id_id_put(id, shipment_return_description, dry_run=dry_run)

update a shipmentReturnAssessment

update shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)
    id = 'id_example' # str | 
    shipment_return_description = openapi_client.ShipmentReturnDescription() # ShipmentReturnDescription | 
    dry_run = True # bool |  (optional)

    try:
        # update a shipmentReturnAssessment
        api_response = api_instance.shipment_return_assessment_id_id_put(id, shipment_return_description, dry_run=dry_run)
        print("The response of ShipmentReturnAssessmentApi->shipment_return_assessment_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_id_id_put: %s\n" % e)
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
**200** | shipmentReturnAssessment update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_return_assessment_post**
> ShipmentReturnDescription shipment_return_assessment_post(shipment_return_description, dry_run=dry_run)

create a shipmentReturnAssessment

create a shipmentReturnAssessment

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
    api_instance = openapi_client.ShipmentReturnAssessmentApi(api_client)
    shipment_return_description = openapi_client.ShipmentReturnDescription() # ShipmentReturnDescription | 
    dry_run = True # bool |  (optional)

    try:
        # create a shipmentReturnAssessment
        api_response = api_instance.shipment_return_assessment_post(shipment_return_description, dry_run=dry_run)
        print("The response of ShipmentReturnAssessmentApi->shipment_return_assessment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentReturnAssessmentApi->shipment_return_assessment_post: %s\n" % e)
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
**201** | shipmentReturnAssessment create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

