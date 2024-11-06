# openapi_client.MailTemplateApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mail_template_count_get**](MailTemplateApi.md#mail_template_count_get) | **GET** /mailTemplate/count | count mailTemplate
[**mail_template_get**](MailTemplateApi.md#mail_template_get) | **GET** /mailTemplate | query mailTemplate
[**mail_template_id_id_delete**](MailTemplateApi.md#mail_template_id_id_delete) | **DELETE** /mailTemplate/id/{id} | delete a mailTemplate
[**mail_template_id_id_get**](MailTemplateApi.md#mail_template_id_id_get) | **GET** /mailTemplate/id/{id} | query a specific mailTemplate
[**mail_template_id_id_put**](MailTemplateApi.md#mail_template_id_id_put) | **PUT** /mailTemplate/id/{id} | update a mailTemplate
[**mail_template_post**](MailTemplateApi.md#mail_template_post) | **POST** /mailTemplate | create a mailTemplate


# **mail_template_count_get**
> AccountingTransactionCountGet200Response mail_template_count_get()

count mailTemplate

count mailTemplate

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
    api_instance = openapi_client.MailTemplateApi(api_client)

    try:
        # count mailTemplate
        api_response = api_instance.mail_template_count_get()
        print("The response of MailTemplateApi->mail_template_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_count_get: %s\n" % e)
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

# **mail_template_get**
> MailTemplateGet200Response mail_template_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query mailTemplate

query mailTemplate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.mail_template_get200_response import MailTemplateGet200Response
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
    api_instance = openapi_client.MailTemplateApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query mailTemplate
        api_response = api_instance.mail_template_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of MailTemplateApi->mail_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_get: %s\n" % e)
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

[**MailTemplateGet200Response**](MailTemplateGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mailTemplate response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_template_id_id_delete**
> mail_template_id_id_delete(id, dry_run=dry_run)

delete a mailTemplate

delete a mailTemplate

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
    api_instance = openapi_client.MailTemplateApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a mailTemplate
        api_instance.mail_template_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_id_id_delete: %s\n" % e)
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
**204** | mailTemplate delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_template_id_id_get**
> MailTemplate mail_template_id_id_get(id)

query a specific mailTemplate

query a specific mailTemplate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.mail_template import MailTemplate
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
    api_instance = openapi_client.MailTemplateApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific mailTemplate
        api_response = api_instance.mail_template_id_id_get(id)
        print("The response of MailTemplateApi->mail_template_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MailTemplate**](MailTemplate.md)

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

# **mail_template_id_id_put**
> MailTemplate mail_template_id_id_put(id, mail_template, dry_run=dry_run)

update a mailTemplate

update mailTemplate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.mail_template import MailTemplate
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
    api_instance = openapi_client.MailTemplateApi(api_client)
    id = 'id_example' # str | 
    mail_template = openapi_client.MailTemplate() # MailTemplate | 
    dry_run = True # bool |  (optional)

    try:
        # update a mailTemplate
        api_response = api_instance.mail_template_id_id_put(id, mail_template, dry_run=dry_run)
        print("The response of MailTemplateApi->mail_template_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **mail_template** | [**MailTemplate**](MailTemplate.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**MailTemplate**](MailTemplate.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | mailTemplate update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mail_template_post**
> MailTemplate mail_template_post(mail_template, dry_run=dry_run)

create a mailTemplate

create a mailTemplate

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.mail_template import MailTemplate
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
    api_instance = openapi_client.MailTemplateApi(api_client)
    mail_template = openapi_client.MailTemplate() # MailTemplate | 
    dry_run = True # bool |  (optional)

    try:
        # create a mailTemplate
        api_response = api_instance.mail_template_post(mail_template, dry_run=dry_run)
        print("The response of MailTemplateApi->mail_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailTemplateApi->mail_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_template** | [**MailTemplate**](MailTemplate.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**MailTemplate**](MailTemplate.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | mailTemplate create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

