# openapi_client.RecordEmailingRuleApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_emailing_rule_count_get**](RecordEmailingRuleApi.md#record_emailing_rule_count_get) | **GET** /recordEmailingRule/count | count recordEmailingRule
[**record_emailing_rule_get**](RecordEmailingRuleApi.md#record_emailing_rule_get) | **GET** /recordEmailingRule | query recordEmailingRule
[**record_emailing_rule_id_id_delete**](RecordEmailingRuleApi.md#record_emailing_rule_id_id_delete) | **DELETE** /recordEmailingRule/id/{id} | delete a recordEmailingRule
[**record_emailing_rule_id_id_get**](RecordEmailingRuleApi.md#record_emailing_rule_id_id_get) | **GET** /recordEmailingRule/id/{id} | query a specific recordEmailingRule
[**record_emailing_rule_id_id_put**](RecordEmailingRuleApi.md#record_emailing_rule_id_id_put) | **PUT** /recordEmailingRule/id/{id} | update a recordEmailingRule
[**record_emailing_rule_post**](RecordEmailingRuleApi.md#record_emailing_rule_post) | **POST** /recordEmailingRule | create a recordEmailingRule


# **record_emailing_rule_count_get**
> AccountingTransactionCountGet200Response record_emailing_rule_count_get()

count recordEmailingRule

count recordEmailingRule

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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)

    try:
        # count recordEmailingRule
        api_response = api_instance.record_emailing_rule_count_get()
        print("The response of RecordEmailingRuleApi->record_emailing_rule_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_count_get: %s\n" % e)
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

# **record_emailing_rule_get**
> RecordEmailingRuleGet200Response record_emailing_rule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query recordEmailingRule

query recordEmailingRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.record_emailing_rule_get200_response import RecordEmailingRuleGet200Response
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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query recordEmailingRule
        api_response = api_instance.record_emailing_rule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of RecordEmailingRuleApi->record_emailing_rule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_get: %s\n" % e)
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

[**RecordEmailingRuleGet200Response**](RecordEmailingRuleGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | recordEmailingRule response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_emailing_rule_id_id_delete**
> record_emailing_rule_id_id_delete(id, dry_run=dry_run)

delete a recordEmailingRule

delete a recordEmailingRule

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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a recordEmailingRule
        api_instance.record_emailing_rule_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_id_id_delete: %s\n" % e)
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
**204** | recordEmailingRule delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_emailing_rule_id_id_get**
> RecordEmailingRule record_emailing_rule_id_id_get(id)

query a specific recordEmailingRule

query a specific recordEmailingRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.record_emailing_rule import RecordEmailingRule
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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific recordEmailingRule
        api_response = api_instance.record_emailing_rule_id_id_get(id)
        print("The response of RecordEmailingRuleApi->record_emailing_rule_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RecordEmailingRule**](RecordEmailingRule.md)

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

# **record_emailing_rule_id_id_put**
> RecordEmailingRule record_emailing_rule_id_id_put(id, record_emailing_rule, dry_run=dry_run)

update a recordEmailingRule

update recordEmailingRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.record_emailing_rule import RecordEmailingRule
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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)
    id = 'id_example' # str | 
    record_emailing_rule = openapi_client.RecordEmailingRule() # RecordEmailingRule | 
    dry_run = True # bool |  (optional)

    try:
        # update a recordEmailingRule
        api_response = api_instance.record_emailing_rule_id_id_put(id, record_emailing_rule, dry_run=dry_run)
        print("The response of RecordEmailingRuleApi->record_emailing_rule_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **record_emailing_rule** | [**RecordEmailingRule**](RecordEmailingRule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**RecordEmailingRule**](RecordEmailingRule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | recordEmailingRule update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_emailing_rule_post**
> RecordEmailingRule record_emailing_rule_post(record_emailing_rule, dry_run=dry_run)

create a recordEmailingRule

create a recordEmailingRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.record_emailing_rule import RecordEmailingRule
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
    api_instance = openapi_client.RecordEmailingRuleApi(api_client)
    record_emailing_rule = openapi_client.RecordEmailingRule() # RecordEmailingRule | 
    dry_run = True # bool |  (optional)

    try:
        # create a recordEmailingRule
        api_response = api_instance.record_emailing_rule_post(record_emailing_rule, dry_run=dry_run)
        print("The response of RecordEmailingRuleApi->record_emailing_rule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordEmailingRuleApi->record_emailing_rule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_emailing_rule** | [**RecordEmailingRule**](RecordEmailingRule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**RecordEmailingRule**](RecordEmailingRule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | recordEmailingRule create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

