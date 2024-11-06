# openapi_client.TaxApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_configure_purchase_taxes_post**](TaxApi.md#tax_configure_purchase_taxes_post) | **POST** /tax/configurePurchaseTaxes | 
[**tax_configure_sales_taxes_post**](TaxApi.md#tax_configure_sales_taxes_post) | **POST** /tax/configureSalesTaxes | 
[**tax_count_get**](TaxApi.md#tax_count_get) | **GET** /tax/count | count tax
[**tax_find_purchase_tax_get**](TaxApi.md#tax_find_purchase_tax_get) | **GET** /tax/findPurchaseTax | 
[**tax_find_sales_tax_get**](TaxApi.md#tax_find_sales_tax_get) | **GET** /tax/findSalesTax | 
[**tax_get**](TaxApi.md#tax_get) | **GET** /tax | query tax
[**tax_id_id_delete**](TaxApi.md#tax_id_id_delete) | **DELETE** /tax/id/{id} | delete a tax
[**tax_id_id_get**](TaxApi.md#tax_id_id_get) | **GET** /tax/id/{id} | query a specific tax
[**tax_id_id_put**](TaxApi.md#tax_id_id_put) | **PUT** /tax/id/{id} | update a tax
[**tax_post**](TaxApi.md#tax_post) | **POST** /tax | create a tax
[**tax_reset_system_taxes_post**](TaxApi.md#tax_reset_system_taxes_post) | **POST** /tax/resetSystemTaxes | 


# **tax_configure_purchase_taxes_post**
> ArchivedEmailIdIdRemoveReferencePost200Response tax_configure_purchase_taxes_post(tax_configure_purchase_taxes_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.tax_configure_purchase_taxes_post_request import TaxConfigurePurchaseTaxesPostRequest
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
    api_instance = openapi_client.TaxApi(api_client)
    tax_configure_purchase_taxes_post_request = openapi_client.TaxConfigurePurchaseTaxesPostRequest() # TaxConfigurePurchaseTaxesPostRequest | 

    try:
        api_response = api_instance.tax_configure_purchase_taxes_post(tax_configure_purchase_taxes_post_request)
        print("The response of TaxApi->tax_configure_purchase_taxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_configure_purchase_taxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_configure_purchase_taxes_post_request** | [**TaxConfigurePurchaseTaxesPostRequest**](TaxConfigurePurchaseTaxesPostRequest.md)|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configurePurchaseTaxes response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_configure_sales_taxes_post**
> ArchivedEmailIdIdRemoveReferencePost200Response tax_configure_sales_taxes_post(tax_configure_sales_taxes_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.tax_configure_sales_taxes_post_request import TaxConfigureSalesTaxesPostRequest
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
    api_instance = openapi_client.TaxApi(api_client)
    tax_configure_sales_taxes_post_request = openapi_client.TaxConfigureSalesTaxesPostRequest() # TaxConfigureSalesTaxesPostRequest | 

    try:
        api_response = api_instance.tax_configure_sales_taxes_post(tax_configure_sales_taxes_post_request)
        print("The response of TaxApi->tax_configure_sales_taxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_configure_sales_taxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_configure_sales_taxes_post_request** | [**TaxConfigureSalesTaxesPostRequest**](TaxConfigureSalesTaxesPostRequest.md)|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | configureSalesTaxes response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_count_get**
> AccountingTransactionCountGet200Response tax_count_get()

count tax

count tax

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
    api_instance = openapi_client.TaxApi(api_client)

    try:
        # count tax
        api_response = api_instance.tax_count_get()
        print("The response of TaxApi->tax_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_count_get: %s\n" % e)
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

# **tax_find_purchase_tax_get**
> TaxFindPurchaseTaxGet200Response tax_find_purchase_tax_get(recipient_country_code, dispatch_country_code=dispatch_country_code, tax_rate_type=tax_rate_type, party_type=party_type, debtor_creditor_code_id=debtor_creditor_code_id, product_code_id=product_code_id, var_date=var_date)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax_find_purchase_tax_get200_response import TaxFindPurchaseTaxGet200Response
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
    api_instance = openapi_client.TaxApi(api_client)
    recipient_country_code = 'recipient_country_code_example' # str | 
    dispatch_country_code = 'dispatch_country_code_example' # str |  (optional)
    tax_rate_type = 'tax_rate_type_example' # str |  (optional)
    party_type = 'party_type_example' # str |  (optional)
    debtor_creditor_code_id = 'debtor_creditor_code_id_example' # str |  (optional)
    product_code_id = 'product_code_id_example' # str |  (optional)
    var_date = 56 # int |  (optional)

    try:
        api_response = api_instance.tax_find_purchase_tax_get(recipient_country_code, dispatch_country_code=dispatch_country_code, tax_rate_type=tax_rate_type, party_type=party_type, debtor_creditor_code_id=debtor_creditor_code_id, product_code_id=product_code_id, var_date=var_date)
        print("The response of TaxApi->tax_find_purchase_tax_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_find_purchase_tax_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipient_country_code** | **str**|  | 
 **dispatch_country_code** | **str**|  | [optional] 
 **tax_rate_type** | **str**|  | [optional] 
 **party_type** | **str**|  | [optional] 
 **debtor_creditor_code_id** | **str**|  | [optional] 
 **product_code_id** | **str**|  | [optional] 
 **var_date** | **int**|  | [optional] 

### Return type

[**TaxFindPurchaseTaxGet200Response**](TaxFindPurchaseTaxGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | findPurchaseTax response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_find_sales_tax_get**
> TaxFindPurchaseTaxGet200Response tax_find_sales_tax_get(dispatch_country_code, recipient_country_code=recipient_country_code, tax_rate_type=tax_rate_type, party_type=party_type, debtor_creditor_code_id=debtor_creditor_code_id, product_code_id=product_code_id, valid_vat_id=valid_vat_id, var_date=var_date)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax_find_purchase_tax_get200_response import TaxFindPurchaseTaxGet200Response
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
    api_instance = openapi_client.TaxApi(api_client)
    dispatch_country_code = 'dispatch_country_code_example' # str | 
    recipient_country_code = 'recipient_country_code_example' # str |  (optional)
    tax_rate_type = 'tax_rate_type_example' # str |  (optional)
    party_type = 'party_type_example' # str |  (optional)
    debtor_creditor_code_id = 'debtor_creditor_code_id_example' # str |  (optional)
    product_code_id = 'product_code_id_example' # str |  (optional)
    valid_vat_id = True # bool |  (optional)
    var_date = 56 # int |  (optional)

    try:
        api_response = api_instance.tax_find_sales_tax_get(dispatch_country_code, recipient_country_code=recipient_country_code, tax_rate_type=tax_rate_type, party_type=party_type, debtor_creditor_code_id=debtor_creditor_code_id, product_code_id=product_code_id, valid_vat_id=valid_vat_id, var_date=var_date)
        print("The response of TaxApi->tax_find_sales_tax_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_find_sales_tax_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_country_code** | **str**|  | 
 **recipient_country_code** | **str**|  | [optional] 
 **tax_rate_type** | **str**|  | [optional] 
 **party_type** | **str**|  | [optional] 
 **debtor_creditor_code_id** | **str**|  | [optional] 
 **product_code_id** | **str**|  | [optional] 
 **valid_vat_id** | **bool**|  | [optional] 
 **var_date** | **int**|  | [optional] 

### Return type

[**TaxFindPurchaseTaxGet200Response**](TaxFindPurchaseTaxGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | findSalesTax response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_get**
> TaxGet200Response tax_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)

query tax

query tax

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax_get200_response import TaxGet200Response
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
    api_instance = openapi_client.TaxApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    serialize_nulls = True # bool |  (optional)
    sort = 'sort_example' # str |  (optional)
    properties = 'properties_example' # str |  (optional)
    include_referenced_entities = 'include_referenced_entities_example' # str |  (optional)

    try:
        # query tax
        api_response = api_instance.tax_get(page=page, page_size=page_size, serialize_nulls=serialize_nulls, sort=sort, properties=properties, include_referenced_entities=include_referenced_entities)
        print("The response of TaxApi->tax_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_get: %s\n" % e)
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

[**TaxGet200Response**](TaxGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tax response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_id_id_delete**
> tax_id_id_delete(id, dry_run=dry_run)

delete a tax

delete a tax

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
    api_instance = openapi_client.TaxApi(api_client)
    id = 'id_example' # str | 
    dry_run = True # bool |  (optional)

    try:
        # delete a tax
        api_instance.tax_id_id_delete(id, dry_run=dry_run)
    except Exception as e:
        print("Exception when calling TaxApi->tax_id_id_delete: %s\n" % e)
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
**204** | tax delete response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_id_id_get**
> Tax tax_id_id_get(id)

query a specific tax

query a specific tax

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax import Tax
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
    api_instance = openapi_client.TaxApi(api_client)
    id = 'id_example' # str | 

    try:
        # query a specific tax
        api_response = api_instance.tax_id_id_get(id)
        print("The response of TaxApi->tax_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Tax**](Tax.md)

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

# **tax_id_id_put**
> Tax tax_id_id_put(id, tax, dry_run=dry_run)

update a tax

update tax

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax import Tax
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
    api_instance = openapi_client.TaxApi(api_client)
    id = 'id_example' # str | 
    tax = openapi_client.Tax() # Tax | 
    dry_run = True # bool |  (optional)

    try:
        # update a tax
        api_response = api_instance.tax_id_id_put(id, tax, dry_run=dry_run)
        print("The response of TaxApi->tax_id_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_id_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tax** | [**Tax**](Tax.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Tax**](Tax.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tax update response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_post**
> Tax tax_post(tax, dry_run=dry_run)

create a tax

create a tax

### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.tax import Tax
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
    api_instance = openapi_client.TaxApi(api_client)
    tax = openapi_client.Tax() # Tax | 
    dry_run = True # bool |  (optional)

    try:
        # create a tax
        api_response = api_instance.tax_post(tax, dry_run=dry_run)
        print("The response of TaxApi->tax_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax** | [**Tax**](Tax.md)|  | 
 **dry_run** | **bool**|  | [optional] 

### Return type

[**Tax**](Tax.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | tax create response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_reset_system_taxes_post**
> ArchivedEmailIdIdRemoveReferencePost200Response tax_reset_system_taxes_post(tax_reset_system_taxes_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.archived_email_id_id_remove_reference_post200_response import ArchivedEmailIdIdRemoveReferencePost200Response
from openapi_client.models.tax_reset_system_taxes_post_request import TaxResetSystemTaxesPostRequest
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
    api_instance = openapi_client.TaxApi(api_client)
    tax_reset_system_taxes_post_request = openapi_client.TaxResetSystemTaxesPostRequest() # TaxResetSystemTaxesPostRequest | 

    try:
        api_response = api_instance.tax_reset_system_taxes_post(tax_reset_system_taxes_post_request)
        print("The response of TaxApi->tax_reset_system_taxes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxApi->tax_reset_system_taxes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_reset_system_taxes_post_request** | [**TaxResetSystemTaxesPostRequest**](TaxResetSystemTaxesPostRequest.md)|  | 

### Return type

[**ArchivedEmailIdIdRemoveReferencePost200Response**](ArchivedEmailIdIdRemoveReferencePost200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resetSystemTaxes response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

