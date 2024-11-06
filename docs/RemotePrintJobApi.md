# openapi_client.RemotePrintJobApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_print_job_count_get**](RemotePrintJobApi.md#remote_print_job_count_get) | **GET** /remotePrintJob/count | count remotePrintJob
[**remote_print_job_create_print_job_with_document_post**](RemotePrintJobApi.md#remote_print_job_create_print_job_with_document_post) | **POST** /remotePrintJob/createPrintJobWithDocument | 
[**remote_print_job_get**](RemotePrintJobApi.md#remote_print_job_get) | **GET** /remotePrintJob | query remotePrintJob
[**remote_print_job_id_id_delete**](RemotePrintJobApi.md#remote_print_job_id_id_delete) | **DELETE** /remotePrintJob/id/{id} | delete a remotePrintJob
[**remote_print_job_id_id_get**](RemotePrintJobApi.md#remote_print_job_id_id_get) | **GET** /remotePrintJob/id/{id} | query a specific remotePrintJob
[**remote_print_job_id_id_put**](RemotePrintJobApi.md#remote_print_job_id_id_put) | **PUT** /remotePrintJob/id/{id} | update a remotePrintJob
[**remote_print_job_post**](RemotePrintJobApi.md#remote_print_job_post) | **POST** /remotePrintJob | create a remotePrintJob


# **remote_print_job_count_get**
> AccountingTransactionCountGet200Response remote_print_job_count_get()

count remotePrintJob

count remotePrintJob

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
    api_instance = openapi_client.RemotePrintJobApi(api_client)

    try:
        # count remotePrintJob
        api_response = api_instance.remote_print_job_count_get()
        print("The response of RemotePrintJobApi->remote_print_job_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_count_get: %s\n" % e)
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

# **remote_print_job_create_print_job_with_document_post**
> RemotePrintJobCreatePrintJobWithDocumentPost200Response remote_print_job_create_print_job_with_document_post(weclapp_os_id, printer_name, quantity, document_name, body, document_description=document_description)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.remote_print_job_create_print_job_with_document_post200_response import RemotePrintJobCreatePrintJobWithDocumentPost200Response
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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    weclapp_os_id = 'weclapp_os_id_example' # str | 
    printer_name = 'printer_name_example' # str | 
    quantity = 56 # int | 
    document_name = 'document_name_example' # str | 
    body = None # bytearray | 
    document_description = 'document_description_example' # str |  (optional)

    try:
        api_response = api_instance.remote_print_job_create_print_job_with_document_post(weclapp_os_id, printer_name, quantity, document_name, body, document_description=document_description)
        print("The response of RemotePrintJobApi->remote_print_job_create_print_job_with_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_create_print_job_with_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **weclapp_os_id** | **str**|  | 
 **printer_name** | **str**|  | 
 **quantity** | **int**|  | 
 **document_name** | **str**|  | 
 **body** | **bytearray**|  | 
 **document_description** | **str**|  | [optional] 

### Return type

[**RemotePrintJobCreatePrintJobWithDocumentPost200Response**](RemotePrintJobCreatePrintJobWithDocumentPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/pdf, image/jpeg, image/png
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPrintJobWithDocument response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_print_job_get**
> RemotePrintJobGet200Response remote_print_job_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query remotePrintJob

query remotePrintJob

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.remote_print_job_get200_response import RemotePrintJobGet200Response
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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query remotePrintJob
        api_response = api_instance.remote_print_job_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of RemotePrintJobApi->remote_print_job_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_get: %s\n" % e)
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

[**RemotePrintJobGet200Response**](RemotePrintJobGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | remotePrintJob response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_print_job_id_id_delete**
> remote_print_job_id_id_delete(id, dry_run=dry_run)

delete a remotePrintJob

delete a remotePrintJob

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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a remotePrintJob
        api_instance.remote_print_job_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_id_id_delete: %s\n" % e)
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
**204** | remotePrintJob delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_print_job_id_id_get**
> RemotePrintJob remote_print_job_id_id_get(id)

query a specific remotePrintJob

query a specific remotePrintJob

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.remote_print_job import RemotePrintJob
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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific remotePrintJob
        api_response = api_instance.remote_print_job_id_id_get(id)
        print("The response of RemotePrintJobApi->remote_print_job_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RemotePrintJob**](RemotePrintJob.md)

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

# **remote_print_job_id_id_put**
> RemotePrintJob remote_print_job_id_id_put(id, remote_print_job, dry_run=dry_run)

update a remotePrintJob

update remotePrintJob

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.remote_print_job import RemotePrintJob
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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    id = 'id_example' # str | 
    remote_print_job = openapi_client.RemotePrintJob() # RemotePrintJob | 
    dry_run = True # bool |  (optional)

    try:
        # update a remotePrintJob
        api_response = api_instance.remote_print_job_id_id_put(id, remote_print_job, dry_run=dry_run)
        print("The response of RemotePrintJobApi->remote_print_job_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **remote_print_job** | [**RemotePrintJob**](RemotePrintJob.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**RemotePrintJob**](RemotePrintJob.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | remotePrintJob update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_print_job_post**
> RemotePrintJob remote_print_job_post(remote_print_job, dry_run=dry_run)

create a remotePrintJob

create a remotePrintJob

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.remote_print_job import RemotePrintJob
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
    api_instance = openapi_client.RemotePrintJobApi(api_client)
    remote_print_job = openapi_client.RemotePrintJob() # RemotePrintJob | 
    dry_run = True # bool |  (optional)

    try:
        # create a remotePrintJob
        api_response = api_instance.remote_print_job_post(remote_print_job, dry_run=dry_run)
        print("The response of RemotePrintJobApi->remote_print_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemotePrintJobApi->remote_print_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_print_job** | [**RemotePrintJob**](RemotePrintJob.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**RemotePrintJob**](RemotePrintJob.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | remotePrintJob create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

