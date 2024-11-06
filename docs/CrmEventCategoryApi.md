# openapi_client.CrmEventCategoryApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_event_category_count_get**](CrmEventCategoryApi.md#crm_event_category_count_get) | **GET** /crmEventCategory/count | count crmEventCategory
[**crm_event_category_get**](CrmEventCategoryApi.md#crm_event_category_get) | **GET** /crmEventCategory | query crmEventCategory
[**crm_event_category_id_id_delete**](CrmEventCategoryApi.md#crm_event_category_id_id_delete) | **DELETE** /crmEventCategory/id/{id} | delete a crmEventCategory
[**crm_event_category_id_id_get**](CrmEventCategoryApi.md#crm_event_category_id_id_get) | **GET** /crmEventCategory/id/{id} | query a specific crmEventCategory
[**crm_event_category_id_id_put**](CrmEventCategoryApi.md#crm_event_category_id_id_put) | **PUT** /crmEventCategory/id/{id} | update a crmEventCategory
[**crm_event_category_post**](CrmEventCategoryApi.md#crm_event_category_post) | **POST** /crmEventCategory | create a crmEventCategory


# **crm_event_category_count_get**
> AccountingTransactionCountGet200Response crm_event_category_count_get()

count crmEventCategory

count crmEventCategory

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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)

    try:
        # count crmEventCategory
        api_response = api_instance.crm_event_category_count_get()
        print("The response of CrmEventCategoryApi->crm_event_category_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_count_get: %s\n" % e)
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

# **crm_event_category_get**
> ArticleAccountingCodeGet200Response crm_event_category_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query crmEventCategory

query crmEventCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.article_accounting_code_get200_response import ArticleAccountingCodeGet200Response
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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query crmEventCategory
        api_response = api_instance.crm_event_category_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of CrmEventCategoryApi->crm_event_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_get: %s\n" % e)
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

[**ArticleAccountingCodeGet200Response**](ArticleAccountingCodeGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | crmEventCategory response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_event_category_id_id_delete**
> crm_event_category_id_id_delete(id, dry_run=dry_run)

delete a crmEventCategory

delete a crmEventCategory

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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a crmEventCategory
        api_instance.crm_event_category_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_id_id_delete: %s\n" % e)
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
**204** | crmEventCategory delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_event_category_id_id_get**
> CustomValue crm_event_category_id_id_get(id)

query a specific crmEventCategory

query a specific crmEventCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific crmEventCategory
        api_response = api_instance.crm_event_category_id_id_get(id)
        print("The response of CrmEventCategoryApi->crm_event_category_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CustomValue**](CustomValue.md)

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

# **crm_event_category_id_id_put**
> CustomValue crm_event_category_id_id_put(id, custom_value, dry_run=dry_run)

update a crmEventCategory

update crmEventCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)
    id = 'id_example' # str | 
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # update a crmEventCategory
        api_response = api_instance.crm_event_category_id_id_put(id, custom_value, dry_run=dry_run)
        print("The response of CrmEventCategoryApi->crm_event_category_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **custom_value** | [**CustomValue**](CustomValue.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomValue**](CustomValue.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | crmEventCategory update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crm_event_category_post**
> CustomValue crm_event_category_post(custom_value, dry_run=dry_run)

create a crmEventCategory

create a crmEventCategory

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.custom_value import CustomValue
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
    api_instance = openapi_client.CrmEventCategoryApi(api_client)
    custom_value = openapi_client.CustomValue() # CustomValue | 
    dry_run = True # bool |  (optional)

    try:
        # create a crmEventCategory
        api_response = api_instance.crm_event_category_post(custom_value, dry_run=dry_run)
        print("The response of CrmEventCategoryApi->crm_event_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CrmEventCategoryApi->crm_event_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_value** | [**CustomValue**](CustomValue.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**CustomValue**](CustomValue.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | crmEventCategory create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

