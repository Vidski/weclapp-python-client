# openapi_client.TicketApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_count_get**](TicketApi.md#ticket_count_get) | **GET** /ticket/count | count ticket
[**ticket_get**](TicketApi.md#ticket_get) | **GET** /ticket | query ticket
[**ticket_id_id_create_public_page_post**](TicketApi.md#ticket_id_id_create_public_page_post) | **POST** /ticket/id/{id}/createPublicPage | 
[**ticket_id_id_delete**](TicketApi.md#ticket_id_id_delete) | **DELETE** /ticket/id/{id} | delete a ticket
[**ticket_id_id_disable_public_page_post**](TicketApi.md#ticket_id_id_disable_public_page_post) | **POST** /ticket/id/{id}/disablePublicPage | 
[**ticket_id_id_get**](TicketApi.md#ticket_id_id_get) | **GET** /ticket/id/{id} | query a specific ticket
[**ticket_id_id_link_sales_order_post**](TicketApi.md#ticket_id_id_link_sales_order_post) | **POST** /ticket/id/{id}/linkSalesOrder | 
[**ticket_id_id_put**](TicketApi.md#ticket_id_id_put) | **PUT** /ticket/id/{id} | update a ticket
[**ticket_id_id_unlink_sales_order_post**](TicketApi.md#ticket_id_id_unlink_sales_order_post) | **POST** /ticket/id/{id}/unlinkSalesOrder | 
[**ticket_post**](TicketApi.md#ticket_post) | **POST** /ticket | create a ticket


# **ticket_count_get**
> AccountingTransactionCountGet200Response ticket_count_get()

count ticket

count ticket

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
    api_instance = openapi_client.TicketApi(api_client)

    try:
        # count ticket
        api_response = api_instance.ticket_count_get()
        print("The response of TicketApi->ticket_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_count_get: %s\n" % e)
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

# **ticket_get**
> TicketGet200Response ticket_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)

query ticket

query ticket

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_get200_response import TicketGet200Response
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
    api_instance = openapi_client.TicketApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)
    additional_properties = 'additional_properties_example' # str |  (optional)

    try:
        # query ticket
        api_response = api_instance.ticket_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities, additional_properties=additional_properties)
        print("The response of TicketApi->ticket_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_get: %s\n" % e)
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
 **additional_properties** | **str**|  | [optional] 

### Return type

[**TicketGet200Response**](TicketGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticket response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_create_public_page_post**
> TicketIdIdCreatePublicPagePost200Response ticket_id_id_create_public_page_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_id_id_create_public_page_post200_response import TicketIdIdCreatePublicPagePost200Response
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.ticket_id_id_create_public_page_post(id, body)
        print("The response of TicketApi->ticket_id_id_create_public_page_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_create_public_page_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**TicketIdIdCreatePublicPagePost200Response**](TicketIdIdCreatePublicPagePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | createPublicPage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_delete**
> ticket_id_id_delete(id, dry_run=dry_run)

delete a ticket

delete a ticket

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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a ticket
        api_instance.ticket_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_delete: %s\n" % e)
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
**204** | ticket delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_disable_public_page_post**
> TicketIdIdCreatePublicPagePost200Response ticket_id_id_disable_public_page_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_id_id_create_public_page_post200_response import TicketIdIdCreatePublicPagePost200Response
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.ticket_id_id_disable_public_page_post(id, body)
        print("The response of TicketApi->ticket_id_id_disable_public_page_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_disable_public_page_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**TicketIdIdCreatePublicPagePost200Response**](TicketIdIdCreatePublicPagePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | disablePublicPage response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_get**
> Ticket ticket_id_id_get(id)

query a specific ticket

query a specific ticket

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket import Ticket
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific ticket
        api_response = api_instance.ticket_id_id_get(id)
        print("The response of TicketApi->ticket_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Ticket**](Ticket.md)

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

# **ticket_id_id_link_sales_order_post**
> TicketIdIdCreatePublicPagePost200Response ticket_id_id_link_sales_order_post(id, ticket_id_id_link_sales_order_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_id_id_create_public_page_post200_response import TicketIdIdCreatePublicPagePost200Response
from openapi_client.models.ticket_id_id_link_sales_order_post_request import TicketIdIdLinkSalesOrderPostRequest
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    ticket_id_id_link_sales_order_post_request = openapi_client.TicketIdIdLinkSalesOrderPostRequest() # TicketIdIdLinkSalesOrderPostRequest | 

    try:
        api_response = api_instance.ticket_id_id_link_sales_order_post(id, ticket_id_id_link_sales_order_post_request)
        print("The response of TicketApi->ticket_id_id_link_sales_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_link_sales_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_id_id_link_sales_order_post_request** | [**TicketIdIdLinkSalesOrderPostRequest**](TicketIdIdLinkSalesOrderPostRequest.md)|  | 

### Return type

[**TicketIdIdCreatePublicPagePost200Response**](TicketIdIdCreatePublicPagePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | linkSalesOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_put**
> Ticket ticket_id_id_put(id, ticket, dry_run=dry_run)

update a ticket

update ticket

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket import Ticket
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    ticket = openapi_client.Ticket() # Ticket | 
    dry_run = True # bool |  (optional)

    try:
        # update a ticket
        api_response = api_instance.ticket_id_id_put(id, ticket, dry_run=dry_run)
        print("The response of TicketApi->ticket_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket** | [**Ticket**](Ticket.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ticket update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_id_id_unlink_sales_order_post**
> TicketIdIdCreatePublicPagePost200Response ticket_id_id_unlink_sales_order_post(id, body)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket_id_id_create_public_page_post200_response import TicketIdIdCreatePublicPagePost200Response
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
    api_instance = openapi_client.TicketApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.ticket_id_id_unlink_sales_order_post(id, body)
        print("The response of TicketApi->ticket_id_id_unlink_sales_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_id_id_unlink_sales_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**TicketIdIdCreatePublicPagePost200Response**](TicketIdIdCreatePublicPagePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | unlinkSalesOrder response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_post**
> Ticket ticket_post(ticket, dry_run=dry_run)

create a ticket

create a ticket

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.ticket import Ticket
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
    api_instance = openapi_client.TicketApi(api_client)
    ticket = openapi_client.Ticket() # Ticket | 
    dry_run = True # bool |  (optional)

    try:
        # create a ticket
        api_response = api_instance.ticket_post(ticket, dry_run=dry_run)
        print("The response of TicketApi->ticket_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketApi->ticket_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket** | [**Ticket**](Ticket.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ticket create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

