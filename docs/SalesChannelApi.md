# openapi_client.SalesChannelApi

All URIs are relative to *https://localhost:80/webapp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_channel_active_sales_channels_get**](SalesChannelApi.md#sales_channel_active_sales_channels_get) | **GET** /salesChannel/activeSalesChannels | 


# **sales_channel_active_sales_channels_get**
> SalesChannelActiveSalesChannelsGet200Response sales_channel_active_sales_channels_get()



### Example

* Api Key Authentication (api-token):

```python
import openapi_client
from openapi_client.models.sales_channel_active_sales_channels_get200_response import SalesChannelActiveSalesChannelsGet200Response
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
    api_instance = openapi_client.SalesChannelApi(api_client)

    try:
        api_response = api_instance.sales_channel_active_sales_channels_get()
        print("The response of SalesChannelApi->sales_channel_active_sales_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesChannelApi->sales_channel_active_sales_channels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SalesChannelActiveSalesChannelsGet200Response**](SalesChannelActiveSalesChannelsGet200Response.md)

### Authorization

[api-token](../README.md#api-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | activeSalesChannels response |  -  |
**0** | error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

