# openapi_client.ProductionWorkScheduleApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**production_work_schedule_count_get**](ProductionWorkScheduleApi.md#production_work_schedule_count_get) | **GET** /productionWorkSchedule/count | count productionWorkSchedule
[**production_work_schedule_get**](ProductionWorkScheduleApi.md#production_work_schedule_get) | **GET** /productionWorkSchedule | query productionWorkSchedule
[**production_work_schedule_id_id_delete**](ProductionWorkScheduleApi.md#production_work_schedule_id_id_delete) | **DELETE** /productionWorkSchedule/id/{id} | delete a productionWorkSchedule
[**production_work_schedule_id_id_get**](ProductionWorkScheduleApi.md#production_work_schedule_id_id_get) | **GET** /productionWorkSchedule/id/{id} | query a specific productionWorkSchedule
[**production_work_schedule_id_id_put**](ProductionWorkScheduleApi.md#production_work_schedule_id_id_put) | **PUT** /productionWorkSchedule/id/{id} | update a productionWorkSchedule
[**production_work_schedule_post**](ProductionWorkScheduleApi.md#production_work_schedule_post) | **POST** /productionWorkSchedule | create a productionWorkSchedule


# **production_work_schedule_count_get**
> AccountingTransactionCountGet200Response production_work_schedule_count_get()

count productionWorkSchedule

count productionWorkSchedule

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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)

    try:
        # count productionWorkSchedule
        api_response = api_instance.production_work_schedule_count_get()
        print("The response of ProductionWorkScheduleApi->production_work_schedule_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_count_get: %s\n" % e)
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

# **production_work_schedule_get**
> ProductionWorkScheduleGet200Response production_work_schedule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query productionWorkSchedule

query productionWorkSchedule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule_get200_response import ProductionWorkScheduleGet200Response
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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query productionWorkSchedule
        api_response = api_instance.production_work_schedule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ProductionWorkScheduleApi->production_work_schedule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_get: %s\n" % e)
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

[**ProductionWorkScheduleGet200Response**](ProductionWorkScheduleGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionWorkSchedule response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_id_id_delete**
> production_work_schedule_id_id_delete(id, dry_run=dry_run)

delete a productionWorkSchedule

delete a productionWorkSchedule

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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a productionWorkSchedule
        api_instance.production_work_schedule_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_id_id_delete: %s\n" % e)
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
**204** | productionWorkSchedule delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_id_id_get**
> ProductionWorkSchedule production_work_schedule_id_id_get(id)

query a specific productionWorkSchedule

query a specific productionWorkSchedule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule import ProductionWorkSchedule
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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific productionWorkSchedule
        api_response = api_instance.production_work_schedule_id_id_get(id)
        print("The response of ProductionWorkScheduleApi->production_work_schedule_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProductionWorkSchedule**](ProductionWorkSchedule.md)

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

# **production_work_schedule_id_id_put**
> ProductionWorkSchedule production_work_schedule_id_id_put(id, production_work_schedule, dry_run=dry_run)

update a productionWorkSchedule

update productionWorkSchedule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule import ProductionWorkSchedule
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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)
    id = 'id_example' # str | 
    production_work_schedule = openapi_client.ProductionWorkSchedule() # ProductionWorkSchedule | 
    dry_run = True # bool |  (optional)

    try:
        # update a productionWorkSchedule
        api_response = api_instance.production_work_schedule_id_id_put(id, production_work_schedule, dry_run=dry_run)
        print("The response of ProductionWorkScheduleApi->production_work_schedule_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **production_work_schedule** | [**ProductionWorkSchedule**](ProductionWorkSchedule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionWorkSchedule**](ProductionWorkSchedule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | productionWorkSchedule update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **production_work_schedule_post**
> ProductionWorkSchedule production_work_schedule_post(production_work_schedule, dry_run=dry_run)

create a productionWorkSchedule

create a productionWorkSchedule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.production_work_schedule import ProductionWorkSchedule
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
    api_instance = openapi_client.ProductionWorkScheduleApi(api_client)
    production_work_schedule = openapi_client.ProductionWorkSchedule() # ProductionWorkSchedule | 
    dry_run = True # bool |  (optional)

    try:
        # create a productionWorkSchedule
        api_response = api_instance.production_work_schedule_post(production_work_schedule, dry_run=dry_run)
        print("The response of ProductionWorkScheduleApi->production_work_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductionWorkScheduleApi->production_work_schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_work_schedule** | [**ProductionWorkSchedule**](ProductionWorkSchedule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**ProductionWorkSchedule**](ProductionWorkSchedule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | productionWorkSchedule create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

