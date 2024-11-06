# openapi_client.AttendanceApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attendance_count_get**](AttendanceApi.md#attendance_count_get) | **GET** /attendance/count | count attendance
[**attendance_current_attendance_get**](AttendanceApi.md#attendance_current_attendance_get) | **GET** /attendance/currentAttendance | 
[**attendance_get**](AttendanceApi.md#attendance_get) | **GET** /attendance | query attendance
[**attendance_id_id_delete**](AttendanceApi.md#attendance_id_id_delete) | **DELETE** /attendance/id/{id} | delete a attendance
[**attendance_id_id_get**](AttendanceApi.md#attendance_id_id_get) | **GET** /attendance/id/{id} | query a specific attendance
[**attendance_id_id_put**](AttendanceApi.md#attendance_id_id_put) | **PUT** /attendance/id/{id} | update a attendance
[**attendance_log_off_post**](AttendanceApi.md#attendance_log_off_post) | **POST** /attendance/logOff | 
[**attendance_log_on_post**](AttendanceApi.md#attendance_log_on_post) | **POST** /attendance/logOn | 
[**attendance_post**](AttendanceApi.md#attendance_post) | **POST** /attendance | create a attendance


# **attendance_count_get**
> AccountingTransactionCountGet200Response attendance_count_get()

count attendance

count attendance

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
    api_instance = openapi_client.AttendanceApi(api_client)

    try:
        # count attendance
        api_response = api_instance.attendance_count_get()
        print("The response of AttendanceApi->attendance_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_count_get: %s\n" % e)
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

# **attendance_current_attendance_get**
> AttendanceCurrentAttendanceGet200Response attendance_current_attendance_get()



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance_current_attendance_get200_response import AttendanceCurrentAttendanceGet200Response
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
    api_instance = openapi_client.AttendanceApi(api_client)

    try:
        api_response = api_instance.attendance_current_attendance_get()
        print("The response of AttendanceApi->attendance_current_attendance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_current_attendance_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AttendanceCurrentAttendanceGet200Response**](AttendanceCurrentAttendanceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | currentAttendance response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_get**
> AttendanceGet200Response attendance_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query attendance

query attendance

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance_get200_response import AttendanceGet200Response
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
    api_instance = openapi_client.AttendanceApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query attendance
        api_response = api_instance.attendance_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of AttendanceApi->attendance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_get: %s\n" % e)
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

[**AttendanceGet200Response**](AttendanceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attendance response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_id_id_delete**
> attendance_id_id_delete(id, dry_run=dry_run)

delete a attendance

delete a attendance

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
    api_instance = openapi_client.AttendanceApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a attendance
        api_instance.attendance_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_id_id_delete: %s\n" % e)
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
**204** | attendance delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_id_id_get**
> Attendance attendance_id_id_get(id)

query a specific attendance

query a specific attendance

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance import Attendance
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
    api_instance = openapi_client.AttendanceApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific attendance
        api_response = api_instance.attendance_id_id_get(id)
        print("The response of AttendanceApi->attendance_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Attendance**](Attendance.md)

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

# **attendance_id_id_put**
> Attendance attendance_id_id_put(id, attendance, dry_run=dry_run)

update a attendance

update attendance

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance import Attendance
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
    api_instance = openapi_client.AttendanceApi(api_client)
    id = 'id_example' # str | 
    attendance = openapi_client.Attendance() # Attendance | 
    dry_run = True # bool |  (optional)

    try:
        # update a attendance
        api_response = api_instance.attendance_id_id_put(id, attendance, dry_run=dry_run)
        print("The response of AttendanceApi->attendance_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **attendance** | [**Attendance**](Attendance.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Attendance**](Attendance.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | attendance update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_log_off_post**
> AttendanceCurrentAttendanceGet200Response attendance_log_off_post(body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance_current_attendance_get200_response import AttendanceCurrentAttendanceGet200Response
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
    api_instance = openapi_client.AttendanceApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.attendance_log_off_post(body)
        print("The response of AttendanceApi->attendance_log_off_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_log_off_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**AttendanceCurrentAttendanceGet200Response**](AttendanceCurrentAttendanceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | logOff response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_log_on_post**
> AttendanceCurrentAttendanceGet200Response attendance_log_on_post(body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance_current_attendance_get200_response import AttendanceCurrentAttendanceGet200Response
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
    api_instance = openapi_client.AttendanceApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.attendance_log_on_post(body)
        print("The response of AttendanceApi->attendance_log_on_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_log_on_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**AttendanceCurrentAttendanceGet200Response**](AttendanceCurrentAttendanceGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | logOn response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attendance_post**
> Attendance attendance_post(attendance, dry_run=dry_run)

create a attendance

create a attendance

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.attendance import Attendance
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
    api_instance = openapi_client.AttendanceApi(api_client)
    attendance = openapi_client.Attendance() # Attendance | 
    dry_run = True # bool |  (optional)

    try:
        # create a attendance
        api_response = api_instance.attendance_post(attendance, dry_run=dry_run)
        print("The response of AttendanceApi->attendance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttendanceApi->attendance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance** | [**Attendance**](Attendance.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Attendance**](Attendance.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | attendance create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

