# openapi_client.PurchaseRequisitionApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_requisition_count_get**](PurchaseRequisitionApi.md#purchase_requisition_count_get) | **GET** /purchaseRequisition/count | count purchaseRequisition
[**purchase_requisition_delete_all_requisitions_post**](PurchaseRequisitionApi.md#purchase_requisition_delete_all_requisitions_post) | **POST** /purchaseRequisition/deleteAllRequisitions | 
[**purchase_requisition_get**](PurchaseRequisitionApi.md#purchase_requisition_get) | **GET** /purchaseRequisition | query purchaseRequisition
[**purchase_requisition_id_id_get**](PurchaseRequisitionApi.md#purchase_requisition_id_id_get) | **GET** /purchaseRequisition/id/{id} | query a specific purchaseRequisition
[**purchase_requisition_id_id_put**](PurchaseRequisitionApi.md#purchase_requisition_id_id_put) | **PUT** /purchaseRequisition/id/{id} | update a purchaseRequisition
[**purchase_requisition_start_material_planning_run_post**](PurchaseRequisitionApi.md#purchase_requisition_start_material_planning_run_post) | **POST** /purchaseRequisition/startMaterialPlanningRun | 


# **purchase_requisition_count_get**
> AccountingTransactionCountGet200Response purchase_requisition_count_get()

count purchaseRequisition

count purchaseRequisition

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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)

    try:
        # count purchaseRequisition
        api_response = api_instance.purchase_requisition_count_get()
        print("The response of PurchaseRequisitionApi->purchase_requisition_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_count_get: %s\n" % e)
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

# **purchase_requisition_delete_all_requisitions_post**
> purchase_requisition_delete_all_requisitions_post(body)



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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)
    body = None # object | 

    try:
        api_instance.purchase_requisition_delete_all_requisitions_post(body)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_delete_all_requisitions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deleteAllRequisitions response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_requisition_get**
> PurchaseRequisitionGet200Response purchase_requisition_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query purchaseRequisition

query purchaseRequisition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_requisition_get200_response import PurchaseRequisitionGet200Response
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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query purchaseRequisition
        api_response = api_instance.purchase_requisition_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of PurchaseRequisitionApi->purchase_requisition_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_get: %s\n" % e)
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

[**PurchaseRequisitionGet200Response**](PurchaseRequisitionGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseRequisition response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_requisition_id_id_get**
> PurchaseRequisition purchase_requisition_id_id_get(id)

query a specific purchaseRequisition

query a specific purchaseRequisition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_requisition import PurchaseRequisition
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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific purchaseRequisition
        api_response = api_instance.purchase_requisition_id_id_get(id)
        print("The response of PurchaseRequisitionApi->purchase_requisition_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PurchaseRequisition**](PurchaseRequisition.md)

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

# **purchase_requisition_id_id_put**
> PurchaseRequisition purchase_requisition_id_id_put(id, purchase_requisition, dry_run=dry_run)

update a purchaseRequisition

update purchaseRequisition

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.purchase_requisition import PurchaseRequisition
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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)
    id = 'id_example' # str | 
    purchase_requisition = openapi_client.PurchaseRequisition() # PurchaseRequisition | 
    dry_run = True # bool |  (optional)

    try:
        # update a purchaseRequisition
        api_response = api_instance.purchase_requisition_id_id_put(id, purchase_requisition, dry_run=dry_run)
        print("The response of PurchaseRequisitionApi->purchase_requisition_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purchase_requisition** | [**PurchaseRequisition**](PurchaseRequisition.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**PurchaseRequisition**](PurchaseRequisition.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | purchaseRequisition update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_requisition_start_material_planning_run_post**
> JobAbortGet200Response purchase_requisition_start_material_planning_run_post(purchase_requisition_start_material_planning_run_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.job_abort_get200_response import JobAbortGet200Response
from openapi_client.models.purchase_requisition_start_material_planning_run_post_request import PurchaseRequisitionStartMaterialPlanningRunPostRequest
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
    api_instance = openapi_client.PurchaseRequisitionApi(api_client)
    purchase_requisition_start_material_planning_run_post_request = openapi_client.PurchaseRequisitionStartMaterialPlanningRunPostRequest() # PurchaseRequisitionStartMaterialPlanningRunPostRequest | 

    try:
        api_response = api_instance.purchase_requisition_start_material_planning_run_post(purchase_requisition_start_material_planning_run_post_request)
        print("The response of PurchaseRequisitionApi->purchase_requisition_start_material_planning_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseRequisitionApi->purchase_requisition_start_material_planning_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_requisition_start_material_planning_run_post_request** | [**PurchaseRequisitionStartMaterialPlanningRunPostRequest**](PurchaseRequisitionStartMaterialPlanningRunPostRequest.md)|  | 

### Return type

[**JobAbortGet200Response**](JobAbortGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | startMaterialPlanningRun response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

