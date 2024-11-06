# FulfillmentProviderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[FulfillmentProvider]**](FulfillmentProvider.md) |  | [optional] 

## Example

```python
from openapi_client.models.fulfillment_provider_get200_response import FulfillmentProviderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentProviderGet200Response from a JSON string
fulfillment_provider_get200_response_instance = FulfillmentProviderGet200Response.from_json(json)
# print the JSON string representation of the object
print(FulfillmentProviderGet200Response.to_json())

# convert the object into a dict
fulfillment_provider_get200_response_dict = fulfillment_provider_get200_response_instance.to_dict()
# create an instance of FulfillmentProviderGet200Response from a dict
fulfillment_provider_get200_response_from_dict = FulfillmentProviderGet200Response.from_dict(fulfillment_provider_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


