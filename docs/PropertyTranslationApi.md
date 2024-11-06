# openapi_client.PropertyTranslationApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**property_translation_read_property_translations_get**](PropertyTranslationApi.md#property_translation_read_property_translations_get) | **GET** /propertyTranslation/readPropertyTranslations | 
[**property_translation_update_property_translations_post**](PropertyTranslationApi.md#property_translation_update_property_translations_post) | **POST** /propertyTranslation/updatePropertyTranslations | 


# **property_translation_read_property_translations_get**
> PropertyTranslationReadPropertyTranslationsGet200Response property_translation_read_property_translations_get(entity_name, entity_id, locale=locale, property_names=property_names)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.property_translation_read_property_translations_get200_response import PropertyTranslationReadPropertyTranslationsGet200Response
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
    api_instance = openapi_client.PropertyTranslationApi(api_client)
    entity_name = 'entity_name_example' # str | 
    entity_id = 'entity_id_example' # str | 
    locale = 'locale_example' # str |  (optional)
    property_names = ['property_names_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.property_translation_read_property_translations_get(entity_name, entity_id, locale=locale, property_names=property_names)
        print("The response of PropertyTranslationApi->property_translation_read_property_translations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyTranslationApi->property_translation_read_property_translations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_name** | **str**|  | 
 **entity_id** | **str**|  | 
 **locale** | **str**|  | [optional] 
 **property_names** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PropertyTranslationReadPropertyTranslationsGet200Response**](PropertyTranslationReadPropertyTranslationsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | readPropertyTranslations response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **property_translation_update_property_translations_post**
> PropertyTranslationReadPropertyTranslationsGet200Response property_translation_update_property_translations_post(property_translation_update_property_translations_post_request)



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.property_translation_read_property_translations_get200_response import PropertyTranslationReadPropertyTranslationsGet200Response
from openapi_client.models.property_translation_update_property_translations_post_request import PropertyTranslationUpdatePropertyTranslationsPostRequest
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
    api_instance = openapi_client.PropertyTranslationApi(api_client)
    property_translation_update_property_translations_post_request = openapi_client.PropertyTranslationUpdatePropertyTranslationsPostRequest() # PropertyTranslationUpdatePropertyTranslationsPostRequest | 

    try:
        api_response = api_instance.property_translation_update_property_translations_post(property_translation_update_property_translations_post_request)
        print("The response of PropertyTranslationApi->property_translation_update_property_translations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyTranslationApi->property_translation_update_property_translations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_translation_update_property_translations_post_request** | [**PropertyTranslationUpdatePropertyTranslationsPostRequest**](PropertyTranslationUpdatePropertyTranslationsPostRequest.md)|  | 

### Return type

[**PropertyTranslationReadPropertyTranslationsGet200Response**](PropertyTranslationReadPropertyTranslationsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | updatePropertyTranslations response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

