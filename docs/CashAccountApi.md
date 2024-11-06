# openapi_client.CashAccountApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cash_account_count_get**](CashAccountApi.md#cash_account_count_get) | **GET** /cashAccount/count | count cashAccount
[**cash_account_get**](CashAccountApi.md#cash_account_get) | **GET** /cashAccount | query cashAccount
[**cash_account_id_id_get**](CashAccountApi.md#cash_account_id_id_get) | **GET** /cashAccount/id/{id} | query a specific cashAccount
[**cash_account_id_id_put**](CashAccountApi.md#cash_account_id_id_put) | **PUT** /cashAccount/id/{id} | update a cashAccount
[**cash_account_post**](CashAccountApi.md#cash_account_post) | **POST** /cashAccount | create a cashAccount


# **cash_account_count_get**
> AccountingTransactionCountGet200Response cash_account_count_get()

count cashAccount

count cashAccount

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
    api_instance = openapi_client.CashAccountApi(api_client)

    try:
        # count cashAccount
        api_response = api_instance.cash_account_count_get()
        print("The response of CashAccountApi->cash_account_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashAccountApi->cash_account_count_get: %s\n" % e)
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

# **cash_account_get**
> CashAccountGet200Response cash_account_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query cashAccount

query cashAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.cash_account_get200_response import CashAccountGet200Response
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
    api_instance = openapi_client.CashAccountApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query cashAccount
        api_response = api_instance.cash_account_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of CashAccountApi->cash_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashAccountApi->cash_account_get: %s\n" % e)
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

[**CashAccountGet200Response**](CashAccountGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cashAccount response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_account_id_id_get**
> CashAccount cash_account_id_id_get(id)

query a specific cashAccount

query a specific cashAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.cash_account import CashAccount
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
    api_instance = openapi_client.CashAccountApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific cashAccount
        api_response = api_instance.cash_account_id_id_get(id)
        print("The response of CashAccountApi->cash_account_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashAccountApi->cash_account_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CashAccount**](CashAccount.md)

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

# **cash_account_id_id_put**
> CashAccount cash_account_id_id_put(id, cash_account, dry_run=dry_run)

update a cashAccount

update cashAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.cash_account import CashAccount
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
    api_instance = openapi_client.CashAccountApi(api_client)
    id = 'id_example' # str | 
    cash_account = openapi_client.CashAccount() # CashAccount | 
    dry_run = True # bool |  (optional)

    try:
        # update a cashAccount
        api_response = api_instance.cash_account_id_id_put(id, cash_account, dry_run=dry_run)
        print("The response of CashAccountApi->cash_account_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashAccountApi->cash_account_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cash_account** | [**CashAccount**](CashAccount.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CashAccount**](CashAccount.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cashAccount update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cash_account_post**
> CashAccount cash_account_post(cash_account, dry_run=dry_run)

create a cashAccount

create a cashAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.cash_account import CashAccount
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
    api_instance = openapi_client.CashAccountApi(api_client)
    cash_account = openapi_client.CashAccount() # CashAccount | 
    dry_run = True # bool |  (optional)

    try:
        # create a cashAccount
        api_response = api_instance.cash_account_post(cash_account, dry_run=dry_run)
        print("The response of CashAccountApi->cash_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashAccountApi->cash_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_account** | [**CashAccount**](CashAccount.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CashAccount**](CashAccount.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | cashAccount create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

