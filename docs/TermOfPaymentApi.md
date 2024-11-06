# openapi_client.TermOfPaymentApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**term_of_payment_count_get**](TermOfPaymentApi.md#term_of_payment_count_get) | **GET** /termOfPayment/count | count termOfPayment
[**term_of_payment_get**](TermOfPaymentApi.md#term_of_payment_get) | **GET** /termOfPayment | query termOfPayment
[**term_of_payment_id_id_delete**](TermOfPaymentApi.md#term_of_payment_id_id_delete) | **DELETE** /termOfPayment/id/{id} | delete a termOfPayment
[**term_of_payment_id_id_get**](TermOfPaymentApi.md#term_of_payment_id_id_get) | **GET** /termOfPayment/id/{id} | query a specific termOfPayment
[**term_of_payment_id_id_put**](TermOfPaymentApi.md#term_of_payment_id_id_put) | **PUT** /termOfPayment/id/{id} | update a termOfPayment
[**term_of_payment_post**](TermOfPaymentApi.md#term_of_payment_post) | **POST** /termOfPayment | create a termOfPayment


# **term_of_payment_count_get**
> AccountingTransactionCountGet200Response term_of_payment_count_get()

count termOfPayment

count termOfPayment

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
    api_instance = openapi_client.TermOfPaymentApi(api_client)

    try:
        # count termOfPayment
        api_response = api_instance.term_of_payment_count_get()
        print("The response of TermOfPaymentApi->term_of_payment_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_count_get: %s\n" % e)
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

# **term_of_payment_get**
> TermOfPaymentGet200Response term_of_payment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query termOfPayment

query termOfPayment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.term_of_payment_get200_response import TermOfPaymentGet200Response
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
    api_instance = openapi_client.TermOfPaymentApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query termOfPayment
        api_response = api_instance.term_of_payment_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TermOfPaymentApi->term_of_payment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_get: %s\n" % e)
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

[**TermOfPaymentGet200Response**](TermOfPaymentGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | termOfPayment response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **term_of_payment_id_id_delete**
> term_of_payment_id_id_delete(id, dry_run=dry_run)

delete a termOfPayment

delete a termOfPayment

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
    api_instance = openapi_client.TermOfPaymentApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a termOfPayment
        api_instance.term_of_payment_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_id_id_delete: %s\n" % e)
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
**204** | termOfPayment delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **term_of_payment_id_id_get**
> TermOfPayment term_of_payment_id_id_get(id)

query a specific termOfPayment

query a specific termOfPayment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.term_of_payment import TermOfPayment
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
    api_instance = openapi_client.TermOfPaymentApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific termOfPayment
        api_response = api_instance.term_of_payment_id_id_get(id)
        print("The response of TermOfPaymentApi->term_of_payment_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TermOfPayment**](TermOfPayment.md)

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

# **term_of_payment_id_id_put**
> TermOfPayment term_of_payment_id_id_put(id, term_of_payment, dry_run=dry_run)

update a termOfPayment

update termOfPayment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.term_of_payment import TermOfPayment
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
    api_instance = openapi_client.TermOfPaymentApi(api_client)
    id = 'id_example' # str | 
    term_of_payment = openapi_client.TermOfPayment() # TermOfPayment | 
    dry_run = True # bool |  (optional)

    try:
        # update a termOfPayment
        api_response = api_instance.term_of_payment_id_id_put(id, term_of_payment, dry_run=dry_run)
        print("The response of TermOfPaymentApi->term_of_payment_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **term_of_payment** | [**TermOfPayment**](TermOfPayment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TermOfPayment**](TermOfPayment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | termOfPayment update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **term_of_payment_post**
> TermOfPayment term_of_payment_post(term_of_payment, dry_run=dry_run)

create a termOfPayment

create a termOfPayment

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.term_of_payment import TermOfPayment
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
    api_instance = openapi_client.TermOfPaymentApi(api_client)
    term_of_payment = openapi_client.TermOfPayment() # TermOfPayment | 
    dry_run = True # bool |  (optional)

    try:
        # create a termOfPayment
        api_response = api_instance.term_of_payment_post(term_of_payment, dry_run=dry_run)
        print("The response of TermOfPaymentApi->term_of_payment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermOfPaymentApi->term_of_payment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_of_payment** | [**TermOfPayment**](TermOfPayment.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TermOfPayment**](TermOfPayment.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | termOfPayment create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

