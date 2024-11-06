# openapi_client.TicketAssignmentRuleApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_assignment_rule_count_get**](TicketAssignmentRuleApi.md#ticket_assignment_rule_count_get) | **GET** /ticketAssignmentRule/count | count ticketAssignmentRule
[**ticket_assignment_rule_get**](TicketAssignmentRuleApi.md#ticket_assignment_rule_get) | **GET** /ticketAssignmentRule | query ticketAssignmentRule
[**ticket_assignment_rule_id_id_delete**](TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_delete) | **DELETE** /ticketAssignmentRule/id/{id} | delete a ticketAssignmentRule
[**ticket_assignment_rule_id_id_get**](TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_get) | **GET** /ticketAssignmentRule/id/{id} | query a specific ticketAssignmentRule
[**ticket_assignment_rule_id_id_put**](TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_put) | **PUT** /ticketAssignmentRule/id/{id} | update a ticketAssignmentRule
[**ticket_assignment_rule_post**](TicketAssignmentRuleApi.md#ticket_assignment_rule_post) | **POST** /ticketAssignmentRule | create a ticketAssignmentRule


# **ticket_assignment_rule_count_get**
> AccountingTransactionCountGet200Response ticket_assignment_rule_count_get()

count ticketAssignmentRule

count ticketAssignmentRule

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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)

    try:
        # count ticketAssignmentRule
        api_response = api_instance.ticket_assignment_rule_count_get()
        print("The response of TicketAssignmentRuleApi->ticket_assignment_rule_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_count_get: %s\n" % e)
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

# **ticket_assignment_rule_get**
> TicketAssignmentRuleGet200Response ticket_assignment_rule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query ticketAssignmentRule

query ticketAssignmentRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_assignment_rule_get200_response import TicketAssignmentRuleGet200Response
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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query ticketAssignmentRule
        api_response = api_instance.ticket_assignment_rule_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TicketAssignmentRuleApi->ticket_assignment_rule_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_get: %s\n" % e)
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

[**TicketAssignmentRuleGet200Response**](TicketAssignmentRuleGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketAssignmentRule response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_assignment_rule_id_id_delete**
> ticket_assignment_rule_id_id_delete(id, dry_run=dry_run)

delete a ticketAssignmentRule

delete a ticketAssignmentRule

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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ticketAssignmentRule
        api_instance.ticket_assignment_rule_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_id_id_delete: %s\n" % e)
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
**204** | ticketAssignmentRule delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_assignment_rule_id_id_get**
> TicketAssignmentRule ticket_assignment_rule_id_id_get(id)

query a specific ticketAssignmentRule

query a specific ticketAssignmentRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_assignment_rule import TicketAssignmentRule
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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticketAssignmentRule
        api_response = api_instance.ticket_assignment_rule_id_id_get(id)
        print("The response of TicketAssignmentRuleApi->ticket_assignment_rule_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketAssignmentRule**](TicketAssignmentRule.md)

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

# **ticket_assignment_rule_id_id_put**
> TicketAssignmentRule ticket_assignment_rule_id_id_put(id, ticket_assignment_rule, dry_run=dry_run)

update a ticketAssignmentRule

update ticketAssignmentRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_assignment_rule import TicketAssignmentRule
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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)
    id = 'id_example' # str | 
    ticket_assignment_rule = openapi_client.TicketAssignmentRule() # TicketAssignmentRule | 
    dry_run = True # bool |  (optional)

    try:
        # update a ticketAssignmentRule
        api_response = api_instance.ticket_assignment_rule_id_id_put(id, ticket_assignment_rule, dry_run=dry_run)
        print("The response of TicketAssignmentRuleApi->ticket_assignment_rule_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_assignment_rule** | [**TicketAssignmentRule**](TicketAssignmentRule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketAssignmentRule**](TicketAssignmentRule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticketAssignmentRule update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_assignment_rule_post**
> TicketAssignmentRule ticket_assignment_rule_post(ticket_assignment_rule, dry_run=dry_run)

create a ticketAssignmentRule

create a ticketAssignmentRule

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_assignment_rule import TicketAssignmentRule
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
    api_instance = openapi_client.TicketAssignmentRuleApi(api_client)
    ticket_assignment_rule = openapi_client.TicketAssignmentRule() # TicketAssignmentRule | 
    dry_run = True # bool |  (optional)

    try:
        # create a ticketAssignmentRule
        api_response = api_instance.ticket_assignment_rule_post(ticket_assignment_rule, dry_run=dry_run)
        print("The response of TicketAssignmentRuleApi->ticket_assignment_rule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketAssignmentRuleApi->ticket_assignment_rule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_assignment_rule** | [**TicketAssignmentRule**](TicketAssignmentRule.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**TicketAssignmentRule**](TicketAssignmentRule.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ticketAssignmentRule create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

