# openapi_client.ProductionWorkScheduleAssignmentApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**production_work_schedule_assignment_count_get**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_count_get) | **GET** /productionWorkScheduleAssignment/count | count productionWorkScheduleAssignment
[**production_work_schedule_assignment_get**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_get) | **GET** /productionWorkScheduleAssignment | query productionWorkScheduleAssignment
[**production_work_schedule_assignment_id_id_delete**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_delete) | **DELETE** /productionWorkScheduleAssignment/id/{id} | delete a productionWorkScheduleAssignment
[**production_work_schedule_assignment_id_id_get**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_get) | **GET** /productionWorkScheduleAssignment/id/{id} | query a specific productionWorkScheduleAssignment
[**production_work_schedule_assignment_id_id_put**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_put) | **PUT** /productionWorkScheduleAssignment/id/{id} | update a productionWorkScheduleAssignment
[**production_work_schedule_assignment_post**](ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_post) | **POST** /productionWorkScheduleAssignment | create a productionWorkScheduleAssignment


# **production_work_schedule_assignment_count_get**
> AccountingTransactionCountGet200Response production_work_schedule_assignment_count_get()

count productionWorkScheduleAssignment

count productionWorkScheduleAssignment

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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)

    try:
        # count productionWorkScheduleAssignment
        api_response = api_instance.production_work_schedule_assignment_count_get()
        print("The response of ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_count_get: %s\n" % e)
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

# **production_work_schedule_assignment_get**
> ProductionWorkScheduleAssignmentGet200Response production_work_schedule_assignment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query productionWorkScheduleAssignment

query productionWorkScheduleAssignment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule_assignment_get200_response import ProductionWorkScheduleAssignmentGet200Response
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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query productionWorkScheduleAssignment
        api_response = api_instance.production_work_schedule_assignment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_get: %s\n" % e)
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

[**ProductionWorkScheduleAssignmentGet200Response**](ProductionWorkScheduleAssignmentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionWorkScheduleAssignment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_assignment_id_id_delete**
> production_work_schedule_assignment_id_id_delete(id, dry_run=dry_run)

delete a productionWorkScheduleAssignment

delete a productionWorkScheduleAssignment

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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a productionWorkScheduleAssignment
        api_instance.production_work_schedule_assignment_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_id_id_delete: %s\n" % e)
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
**204** | productionWorkScheduleAssignment delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_assignment_id_id_get**
> ProductionWorkScheduleAssignment production_work_schedule_assignment_id_id_get(id)

query a specific productionWorkScheduleAssignment

query a specific productionWorkScheduleAssignment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule_assignment import ProductionWorkScheduleAssignment
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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific productionWorkScheduleAssignment
        api_response = api_instance.production_work_schedule_assignment_id_id_get(id)
        print("The response of ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProductionWorkScheduleAssignment**](ProductionWorkScheduleAssignment.md)

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

# **production_work_schedule_assignment_id_id_put**
> ProductionWorkScheduleAssignment production_work_schedule_assignment_id_id_put(id, production_work_schedule_assignment, dry_run=dry_run)

update a productionWorkScheduleAssignment

update productionWorkScheduleAssignment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule_assignment import ProductionWorkScheduleAssignment
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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)
    id = 'id_example' # str | 
    production_work_schedule_assignment = openapi_client.ProductionWorkScheduleAssignment() # ProductionWorkScheduleAssignment | 
    dry_run = True # bool |  (optional)

    try:
        # update a productionWorkScheduleAssignment
        api_response = api_instance.production_work_schedule_assignment_id_id_put(id, production_work_schedule_assignment, dry_run=dry_run)
        print("The response of ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **production_work_schedule_assignment** | [**ProductionWorkScheduleAssignment**](ProductionWorkScheduleAssignment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionWorkScheduleAssignment**](ProductionWorkScheduleAssignment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionWorkScheduleAssignment update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_assignment_post**
> ProductionWorkScheduleAssignment production_work_schedule_assignment_post(production_work_schedule_assignment, dry_run=dry_run)

create a productionWorkScheduleAssignment

create a productionWorkScheduleAssignment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule_assignment import ProductionWorkScheduleAssignment
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
    api_instance = openapi_client.ProductionWorkScheduleAssignmentApi(api_client)
    production_work_schedule_assignment = openapi_client.ProductionWorkScheduleAssignment() # ProductionWorkScheduleAssignment | 
    dry_run = True # bool |  (optional)

    try:
        # create a productionWorkScheduleAssignment
        api_response = api_instance.production_work_schedule_assignment_post(production_work_schedule_assignment, dry_run=dry_run)
        print("The response of ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleAssignmentApi->production_work_schedule_assignment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_work_schedule_assignment** | [**ProductionWorkScheduleAssignment**](ProductionWorkScheduleAssignment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionWorkScheduleAssignment**](ProductionWorkScheduleAssignment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | productionWorkScheduleAssignment create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

