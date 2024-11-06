# openapi_client.SepaDirectDebitMandateApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sepa_direct_debit_mandate_count_get**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_count_get) | **GET** /sepaDirectDebitMandate/count | count sepaDirectDebitMandate
[**sepa_direct_debit_mandate_get**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_get) | **GET** /sepaDirectDebitMandate | query sepaDirectDebitMandate
[**sepa_direct_debit_mandate_id_id_delete**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_delete) | **DELETE** /sepaDirectDebitMandate/id/{id} | delete a sepaDirectDebitMandate
[**sepa_direct_debit_mandate_id_id_get**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_get) | **GET** /sepaDirectDebitMandate/id/{id} | query a specific sepaDirectDebitMandate
[**sepa_direct_debit_mandate_id_id_put**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_put) | **PUT** /sepaDirectDebitMandate/id/{id} | update a sepaDirectDebitMandate
[**sepa_direct_debit_mandate_post**](SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_post) | **POST** /sepaDirectDebitMandate | create a sepaDirectDebitMandate


# **sepa_direct_debit_mandate_count_get**
> AccountingTransactionCountGet200Response sepa_direct_debit_mandate_count_get()

count sepaDirectDebitMandate

count sepaDirectDebitMandate

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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)

    try:
        # count sepaDirectDebitMandate
        api_response = api_instance.sepa_direct_debit_mandate_count_get()
        print("The response of SepaDirectDebitMandateApi->sepa_direct_debit_mandate_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_count_get: %s\n" % e)
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

# **sepa_direct_debit_mandate_get**
> SepaDirectDebitMandateGet200Response sepa_direct_debit_mandate_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query sepaDirectDebitMandate

query sepaDirectDebitMandate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sepa_direct_debit_mandate_get200_response import SepaDirectDebitMandateGet200Response
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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query sepaDirectDebitMandate
        api_response = api_instance.sepa_direct_debit_mandate_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of SepaDirectDebitMandateApi->sepa_direct_debit_mandate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_get: %s\n" % e)
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

[**SepaDirectDebitMandateGet200Response**](SepaDirectDebitMandateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | sepaDirectDebitMandate response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sepa_direct_debit_mandate_id_id_delete**
> sepa_direct_debit_mandate_id_id_delete(id, dry_run=dry_run)

delete a sepaDirectDebitMandate

delete a sepaDirectDebitMandate

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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a sepaDirectDebitMandate
        api_instance.sepa_direct_debit_mandate_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_id_id_delete: %s\n" % e)
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
**204** | sepaDirectDebitMandate delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sepa_direct_debit_mandate_id_id_get**
> SepaDirectDebitMandate sepa_direct_debit_mandate_id_id_get(id)

query a specific sepaDirectDebitMandate

query a specific sepaDirectDebitMandate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sepa_direct_debit_mandate import SepaDirectDebitMandate
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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific sepaDirectDebitMandate
        api_response = api_instance.sepa_direct_debit_mandate_id_id_get(id)
        print("The response of SepaDirectDebitMandateApi->sepa_direct_debit_mandate_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SepaDirectDebitMandate**](SepaDirectDebitMandate.md)

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

# **sepa_direct_debit_mandate_id_id_put**
> SepaDirectDebitMandate sepa_direct_debit_mandate_id_id_put(id, sepa_direct_debit_mandate, dry_run=dry_run)

update a sepaDirectDebitMandate

update sepaDirectDebitMandate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sepa_direct_debit_mandate import SepaDirectDebitMandate
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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)
    id = 'id_example' # str | 
    sepa_direct_debit_mandate = openapi_client.SepaDirectDebitMandate() # SepaDirectDebitMandate | 
    dry_run = True # bool |  (optional)

    try:
        # update a sepaDirectDebitMandate
        api_response = api_instance.sepa_direct_debit_mandate_id_id_put(id, sepa_direct_debit_mandate, dry_run=dry_run)
        print("The response of SepaDirectDebitMandateApi->sepa_direct_debit_mandate_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sepa_direct_debit_mandate** | [**SepaDirectDebitMandate**](SepaDirectDebitMandate.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SepaDirectDebitMandate**](SepaDirectDebitMandate.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | sepaDirectDebitMandate update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sepa_direct_debit_mandate_post**
> SepaDirectDebitMandate sepa_direct_debit_mandate_post(sepa_direct_debit_mandate, dry_run=dry_run)

create a sepaDirectDebitMandate

create a sepaDirectDebitMandate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sepa_direct_debit_mandate import SepaDirectDebitMandate
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
    api_instance = openapi_client.SepaDirectDebitMandateApi(api_client)
    sepa_direct_debit_mandate = openapi_client.SepaDirectDebitMandate() # SepaDirectDebitMandate | 
    dry_run = True # bool |  (optional)

    try:
        # create a sepaDirectDebitMandate
        api_response = api_instance.sepa_direct_debit_mandate_post(sepa_direct_debit_mandate, dry_run=dry_run)
        print("The response of SepaDirectDebitMandateApi->sepa_direct_debit_mandate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SepaDirectDebitMandateApi->sepa_direct_debit_mandate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sepa_direct_debit_mandate** | [**SepaDirectDebitMandate**](SepaDirectDebitMandate.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**SepaDirectDebitMandate**](SepaDirectDebitMandate.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | sepaDirectDebitMandate create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

