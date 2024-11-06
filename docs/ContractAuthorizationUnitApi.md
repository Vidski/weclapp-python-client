# openapi_client.ContractAuthorizationUnitApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_authorization_unit_count_get**](ContractAuthorizationUnitApi.md#contract_authorization_unit_count_get) | **GET** /contractAuthorizationUnit/count | count contractAuthorizationUnit
[**contract_authorization_unit_get**](ContractAuthorizationUnitApi.md#contract_authorization_unit_get) | **GET** /contractAuthorizationUnit | query contractAuthorizationUnit
[**contract_authorization_unit_id_id_get**](ContractAuthorizationUnitApi.md#contract_authorization_unit_id_id_get) | **GET** /contractAuthorizationUnit/id/{id} | query a specific contractAuthorizationUnit


# **contract_authorization_unit_count_get**
> AccountingTransactionCountGet200Response contract_authorization_unit_count_get()

count contractAuthorizationUnit

count contractAuthorizationUnit

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
    api_instance = openapi_client.ContractAuthorizationUnitApi(api_client)

    try:
        # count contractAuthorizationUnit
        api_response = api_instance.contract_authorization_unit_count_get()
        print("The response of ContractAuthorizationUnitApi->contract_authorization_unit_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAuthorizationUnitApi->contract_authorization_unit_count_get: %s\n" % e)
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

# **contract_authorization_unit_get**
> ContractAuthorizationUnitGet200Response contract_authorization_unit_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query contractAuthorizationUnit

query contractAuthorizationUnit

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.contract_authorization_unit_get200_response import ContractAuthorizationUnitGet200Response
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
    api_instance = openapi_client.ContractAuthorizationUnitApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query contractAuthorizationUnit
        api_response = api_instance.contract_authorization_unit_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of ContractAuthorizationUnitApi->contract_authorization_unit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAuthorizationUnitApi->contract_authorization_unit_get: %s\n" % e)
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

[**ContractAuthorizationUnitGet200Response**](ContractAuthorizationUnitGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | contractAuthorizationUnit response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contract_authorization_unit_id_id_get**
> ContractAuthorizationUnit contract_authorization_unit_id_id_get(id)

query a specific contractAuthorizationUnit

query a specific contractAuthorizationUnit

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.contract_authorization_unit import ContractAuthorizationUnit
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
    api_instance = openapi_client.ContractAuthorizationUnitApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific contractAuthorizationUnit
        api_response = api_instance.contract_authorization_unit_id_id_get(id)
        print("The response of ContractAuthorizationUnitApi->contract_authorization_unit_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractAuthorizationUnitApi->contract_authorization_unit_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ContractAuthorizationUnit**](ContractAuthorizationUnit.md)

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

