# openapi_client.LoadingEquipmentIdentifierApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loading_equipment_identifier_count_get**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_count_get) | **GET** /loadingEquipmentIdentifier/count | count loadingEquipmentIdentifier
[**loading_equipment_identifier_get**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_get) | **GET** /loadingEquipmentIdentifier | query loadingEquipmentIdentifier
[**loading_equipment_identifier_id_id_delete**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_delete) | **DELETE** /loadingEquipmentIdentifier/id/{id} | delete a loadingEquipmentIdentifier
[**loading_equipment_identifier_id_id_get**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_get) | **GET** /loadingEquipmentIdentifier/id/{id} | query a specific loadingEquipmentIdentifier
[**loading_equipment_identifier_id_id_put**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_put) | **PUT** /loadingEquipmentIdentifier/id/{id} | update a loadingEquipmentIdentifier
[**loading_equipment_identifier_post**](LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_post) | **POST** /loadingEquipmentIdentifier | create a loadingEquipmentIdentifier


# **loading_equipment_identifier_count_get**
> AccountingTransactionCountGet200Response loading_equipment_identifier_count_get()

count loadingEquipmentIdentifier

count loadingEquipmentIdentifier

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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)

    try:
        # count loadingEquipmentIdentifier
        api_response = api_instance.loading_equipment_identifier_count_get()
        print("The response of LoadingEquipmentIdentifierApi->loading_equipment_identifier_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_count_get: %s\n" % e)
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

# **loading_equipment_identifier_get**
> LoadingEquipmentIdentifierGet200Response loading_equipment_identifier_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query loadingEquipmentIdentifier

query loadingEquipmentIdentifier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.loading_equipment_identifier_get200_response import LoadingEquipmentIdentifierGet200Response
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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query loadingEquipmentIdentifier
        api_response = api_instance.loading_equipment_identifier_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of LoadingEquipmentIdentifierApi->loading_equipment_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_get: %s\n" % e)
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

[**LoadingEquipmentIdentifierGet200Response**](LoadingEquipmentIdentifierGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loadingEquipmentIdentifier response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loading_equipment_identifier_id_id_delete**
> loading_equipment_identifier_id_id_delete(id, dry_run=dry_run)

delete a loadingEquipmentIdentifier

delete a loadingEquipmentIdentifier

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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a loadingEquipmentIdentifier
        api_instance.loading_equipment_identifier_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_id_id_delete: %s\n" % e)
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
**204** | loadingEquipmentIdentifier delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loading_equipment_identifier_id_id_get**
> LoadingEquipmentIdentifier loading_equipment_identifier_id_id_get(id)

query a specific loadingEquipmentIdentifier

query a specific loadingEquipmentIdentifier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.loading_equipment_identifier import LoadingEquipmentIdentifier
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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific loadingEquipmentIdentifier
        api_response = api_instance.loading_equipment_identifier_id_id_get(id)
        print("The response of LoadingEquipmentIdentifierApi->loading_equipment_identifier_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LoadingEquipmentIdentifier**](LoadingEquipmentIdentifier.md)

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

# **loading_equipment_identifier_id_id_put**
> LoadingEquipmentIdentifier loading_equipment_identifier_id_id_put(id, loading_equipment_identifier, dry_run=dry_run)

update a loadingEquipmentIdentifier

update loadingEquipmentIdentifier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.loading_equipment_identifier import LoadingEquipmentIdentifier
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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)
    id = 'id_example' # str | 
    loading_equipment_identifier = openapi_client.LoadingEquipmentIdentifier() # LoadingEquipmentIdentifier | 
    dry_run = True # bool |  (optional)

    try:
        # update a loadingEquipmentIdentifier
        api_response = api_instance.loading_equipment_identifier_id_id_put(id, loading_equipment_identifier, dry_run=dry_run)
        print("The response of LoadingEquipmentIdentifierApi->loading_equipment_identifier_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **loading_equipment_identifier** | [**LoadingEquipmentIdentifier**](LoadingEquipmentIdentifier.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**LoadingEquipmentIdentifier**](LoadingEquipmentIdentifier.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loadingEquipmentIdentifier update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loading_equipment_identifier_post**
> LoadingEquipmentIdentifier loading_equipment_identifier_post(loading_equipment_identifier, dry_run=dry_run)

create a loadingEquipmentIdentifier

create a loadingEquipmentIdentifier

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.loading_equipment_identifier import LoadingEquipmentIdentifier
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
    api_instance = openapi_client.LoadingEquipmentIdentifierApi(api_client)
    loading_equipment_identifier = openapi_client.LoadingEquipmentIdentifier() # LoadingEquipmentIdentifier | 
    dry_run = True # bool |  (optional)

    try:
        # create a loadingEquipmentIdentifier
        api_response = api_instance.loading_equipment_identifier_post(loading_equipment_identifier, dry_run=dry_run)
        print("The response of LoadingEquipmentIdentifierApi->loading_equipment_identifier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadingEquipmentIdentifierApi->loading_equipment_identifier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loading_equipment_identifier** | [**LoadingEquipmentIdentifier**](LoadingEquipmentIdentifier.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**LoadingEquipmentIdentifier**](LoadingEquipmentIdentifier.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | loadingEquipmentIdentifier create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

