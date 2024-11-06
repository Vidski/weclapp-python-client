# openapi_client.LedgerAccountApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ledger_account_count_get**](LedgerAccountApi.md#ledger_account_count_get) | **GET** /ledgerAccount/count | count ledgerAccount
[**ledger_account_get**](LedgerAccountApi.md#ledger_account_get) | **GET** /ledgerAccount | query ledgerAccount
[**ledger_account_id_id_delete**](LedgerAccountApi.md#ledger_account_id_id_delete) | **DELETE** /ledgerAccount/id/{id} | delete a ledgerAccount
[**ledger_account_id_id_get**](LedgerAccountApi.md#ledger_account_id_id_get) | **GET** /ledgerAccount/id/{id} | query a specific ledgerAccount
[**ledger_account_id_id_put**](LedgerAccountApi.md#ledger_account_id_id_put) | **PUT** /ledgerAccount/id/{id} | update a ledgerAccount
[**ledger_account_post**](LedgerAccountApi.md#ledger_account_post) | **POST** /ledgerAccount | create a ledgerAccount


# **ledger_account_count_get**
> AccountingTransactionCountGet200Response ledger_account_count_get()

count ledgerAccount

count ledgerAccount

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
    api_instance = openapi_client.LedgerAccountApi(api_client)

    try:
        # count ledgerAccount
        api_response = api_instance.ledger_account_count_get()
        print("The response of LedgerAccountApi->ledger_account_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_count_get: %s\n" % e)
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

# **ledger_account_get**
> LedgerAccountGet200Response ledger_account_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ledgerAccount

query ledgerAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ledger_account_get200_response import LedgerAccountGet200Response
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
    api_instance = openapi_client.LedgerAccountApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ledgerAccount
        api_response = api_instance.ledger_account_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of LedgerAccountApi->ledger_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_get: %s\n" % e)
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

[**LedgerAccountGet200Response**](LedgerAccountGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ledgerAccount response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_account_id_id_delete**
> ledger_account_id_id_delete(id, dry_run=dry_run)

delete a ledgerAccount

delete a ledgerAccount

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
    api_instance = openapi_client.LedgerAccountApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ledgerAccount
        api_instance.ledger_account_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_id_id_delete: %s\n" % e)
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
**204** | ledgerAccount delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_account_id_id_get**
> LedgerAccount ledger_account_id_id_get(id)

query a specific ledgerAccount

query a specific ledgerAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ledger_account import LedgerAccount
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
    api_instance = openapi_client.LedgerAccountApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ledgerAccount
        api_response = api_instance.ledger_account_id_id_get(id)
        print("The response of LedgerAccountApi->ledger_account_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LedgerAccount**](LedgerAccount.md)

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

# **ledger_account_id_id_put**
> LedgerAccount ledger_account_id_id_put(id, ledger_account, dry_run=dry_run)

update a ledgerAccount

update ledgerAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ledger_account import LedgerAccount
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
    api_instance = openapi_client.LedgerAccountApi(api_client)
    id = 'id_example' # str | 
    ledger_account = openapi_client.LedgerAccount() # LedgerAccount | 
    dry_run = True # bool |  (optional)

    try:
        # update a ledgerAccount
        api_response = api_instance.ledger_account_id_id_put(id, ledger_account, dry_run=dry_run)
        print("The response of LedgerAccountApi->ledger_account_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ledger_account** | [**LedgerAccount**](LedgerAccount.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ledgerAccount update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ledger_account_post**
> LedgerAccount ledger_account_post(ledger_account, dry_run=dry_run)

create a ledgerAccount

create a ledgerAccount

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ledger_account import LedgerAccount
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
    api_instance = openapi_client.LedgerAccountApi(api_client)
    ledger_account = openapi_client.LedgerAccount() # LedgerAccount | 
    dry_run = True # bool |  (optional)

    try:
        # create a ledgerAccount
        api_response = api_instance.ledger_account_post(ledger_account, dry_run=dry_run)
        print("The response of LedgerAccountApi->ledger_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerAccountApi->ledger_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_account** | [**LedgerAccount**](LedgerAccount.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ledgerAccount create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

