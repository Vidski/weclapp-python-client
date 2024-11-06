# openapi_client.ArchivedEmailApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archived_email_count_get**](ArchivedEmailApi.md#archived_email_count_get) | **GET** /archivedEmail/count | count archivedEmail
[**archived_email_get**](ArchivedEmailApi.md#archived_email_get) | **GET** /archivedEmail | query archivedEmail
[**archived_email_id_id_get**](ArchivedEmailApi.md#archived_email_id_id_get) | **GET** /archivedEmail/id/{id} | query a specific archivedEmail
[**archived_email_id_id_remove_reference_post**](ArchivedEmailApi.md#archived_email_id_id_remove_reference_post) | **POST** /archivedEmail/id/{id}/removeReference | 


# **archived_email_count_get**
> AccountingTransactionCountGet200Response archived_email_count_get(entity_id, entity_name)

count archivedEmail

count archivedEmail

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
    api_instance = openapi_client.ArchivedEmailApi(api_client)
    entity_id = 'entity_id_example' # str | 
    entity_name = 'entity_name_example' # str | 

    try:
        # count archivedEmail
        api_response = api_instance.archived_email_count_get(entity_id, entity_name)
        print("The response of ArchivedEmailApi->archived_email_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivedEmailApi->archived_email_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **entity_name** | **str**|  | 

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

# **archived_email_get**
> ArchivedEmailGet200Response archived_email_get(entity_id, entity_name, page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query archivedEmail

query archivedEmail

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_get200_response import ArchivedEmailGet200Response
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
    api_instance = openapi_client.ArchivedEmailApi(api_client)
    entity_id = 'entity_id_example' # str | 
    entity_name = 'entity_name_example' # str | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query archivedEmail
        api_response = api_instance.archived_email_get(entity_id, entity_name, page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ArchivedEmailApi->archived_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivedEmailApi->archived_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 
 **entity_name** | **str**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **serialize_nulls** | **bool**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **properties** | **str**|  | [optional] 
 **include_referenced_entities** | **str**|  | [optional] 

### Return type

[**ArchivedEmailGet200Response**](ArchivedEmailGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | archivedEmail response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archived_email_id_id_get**
> ArchivedEmail archived_email_id_id_get(id)

query a specific archivedEmail

query a specific archivedEmail

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email import ArchivedEmail
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
    api_instance = openapi_client.ArchivedEmailApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific archivedEmail
        api_response = api_instance.archived_email_id_id_get(id)
        print("The response of ArchivedEmailApi->archived_email_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivedEmailApi->archived_email_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ArchivedEmail**](ArchivedEmail.md)

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

# **archived_email_id_id_remove_reference_post**
> ArchivedEmailIdIdRemoveReferencePost200Response archived_email_id_id_remove_reference_post(id, archived_email_id_id_remove_reference_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.archived_email_id_id_remove_reference_post_request import ArchivedEmailIdIdRemoveReferencePostRequest
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
    api_instance = openapi_client.ArchivedEmailApi(api_client)
    id = 'id_example' # str | 
    archived_email_id_id_remove_reference_post_request = openapi_client.ArchivedEmailIdIdRemoveReferencePostRequest() # ArchivedEmailIdIdRemoveReferencePostRequest | 

    try:
        api_response = api_instance.archived_email_id_id_remove_reference_post(id, archived_email_id_id_remove_reference_post_request)
        print("The response of ArchivedEmailApi->archived_email_id_id_remove_reference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArchivedEmailApi->archived_email_id_id_remove_reference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **archived_email_id_id_remove_reference_post_request** | [**ArchivedEmailIdIdRemoveReferencePostRequest**](ArchivedEmailIdIdRemoveReferencePostRequest.md)|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | removeReference response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

