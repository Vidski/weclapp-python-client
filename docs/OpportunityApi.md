# openapi_client.OpportunityApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**opportunity_count_get**](OpportunityApi.md#opportunity_count_get) | **GET** /opportunity/count | count opportunity
[**opportunity_get**](OpportunityApi.md#opportunity_get) | **GET** /opportunity | query opportunity
[**opportunity_id_id_delete**](OpportunityApi.md#opportunity_id_id_delete) | **DELETE** /opportunity/id/{id} | delete a opportunity
[**opportunity_id_id_get**](OpportunityApi.md#opportunity_id_id_get) | **GET** /opportunity/id/{id} | query a specific opportunity
[**opportunity_id_id_link_quotation_post**](OpportunityApi.md#opportunity_id_id_link_quotation_post) | **POST** /opportunity/id/{id}/linkQuotation | 
[**opportunity_id_id_put**](OpportunityApi.md#opportunity_id_id_put) | **PUT** /opportunity/id/{id} | update a opportunity
[**opportunity_post**](OpportunityApi.md#opportunity_post) | **POST** /opportunity | create a opportunity


# **opportunity_count_get**
> AccountingTransactionCountGet200Response opportunity_count_get()

count opportunity

count opportunity

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
    api_instance = openapi_client.OpportunityApi(api_client)

    try:
        # count opportunity
        api_response = api_instance.opportunity_count_get()
        print("The response of OpportunityApi->opportunity_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_count_get: %s\n" % e)
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

# **opportunity_get**
> OpportunityGet200Response opportunity_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query opportunity

query opportunity

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.opportunity_get200_response import OpportunityGet200Response
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
    api_instance = openapi_client.OpportunityApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query opportunity
        api_response = api_instance.opportunity_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of OpportunityApi->opportunity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_get: %s\n" % e)
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

[**OpportunityGet200Response**](OpportunityGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | opportunity response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opportunity_id_id_delete**
> opportunity_id_id_delete(id, dry_run=dry_run)

delete a opportunity

delete a opportunity

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
    api_instance = openapi_client.OpportunityApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a opportunity
        api_instance.opportunity_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_id_id_delete: %s\n" % e)
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
**204** | opportunity delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opportunity_id_id_get**
> Opportunity opportunity_id_id_get(id)

query a specific opportunity

query a specific opportunity

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.opportunity import Opportunity
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
    api_instance = openapi_client.OpportunityApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific opportunity
        api_response = api_instance.opportunity_id_id_get(id)
        print("The response of OpportunityApi->opportunity_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Opportunity**](Opportunity.md)

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

# **opportunity_id_id_link_quotation_post**
> OpportunityIdIdLinkQuotationPost200Response opportunity_id_id_link_quotation_post(id, opportunity_id_id_link_quotation_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.opportunity_id_id_link_quotation_post200_response import OpportunityIdIdLinkQuotationPost200Response
from openapi_client.models.opportunity_id_id_link_quotation_post_request import OpportunityIdIdLinkQuotationPostRequest
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
    api_instance = openapi_client.OpportunityApi(api_client)
    id = 'id_example' # str | 
    opportunity_id_id_link_quotation_post_request = openapi_client.OpportunityIdIdLinkQuotationPostRequest() # OpportunityIdIdLinkQuotationPostRequest | 

    try:
        api_response = api_instance.opportunity_id_id_link_quotation_post(id, opportunity_id_id_link_quotation_post_request)
        print("The response of OpportunityApi->opportunity_id_id_link_quotation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_id_id_link_quotation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **opportunity_id_id_link_quotation_post_request** | [**OpportunityIdIdLinkQuotationPostRequest**](OpportunityIdIdLinkQuotationPostRequest.md)|  | 

### Return type

[**OpportunityIdIdLinkQuotationPost200Response**](OpportunityIdIdLinkQuotationPost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | linkQuotation response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opportunity_id_id_put**
> Opportunity opportunity_id_id_put(id, opportunity, dry_run=dry_run)

update a opportunity

update opportunity

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.opportunity import Opportunity
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
    api_instance = openapi_client.OpportunityApi(api_client)
    id = 'id_example' # str | 
    opportunity = openapi_client.Opportunity() # Opportunity | 
    dry_run = True # bool |  (optional)

    try:
        # update a opportunity
        api_response = api_instance.opportunity_id_id_put(id, opportunity, dry_run=dry_run)
        print("The response of OpportunityApi->opportunity_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **opportunity** | [**Opportunity**](Opportunity.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | opportunity update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opportunity_post**
> Opportunity opportunity_post(opportunity, dry_run=dry_run)

create a opportunity

create a opportunity

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.opportunity import Opportunity
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
    api_instance = openapi_client.OpportunityApi(api_client)
    opportunity = openapi_client.Opportunity() # Opportunity | 
    dry_run = True # bool |  (optional)

    try:
        # create a opportunity
        api_response = api_instance.opportunity_post(opportunity, dry_run=dry_run)
        print("The response of OpportunityApi->opportunity_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityApi->opportunity_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **opportunity** | [**Opportunity**](Opportunity.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | opportunity create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

