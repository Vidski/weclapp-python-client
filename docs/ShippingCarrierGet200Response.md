# ShippingCarrierGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ShippingCarrier]**](ShippingCarrier.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipping_carrier_get200_response import ShippingCarrierGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCarrierGet200Response from a JSON string
shipping_carrier_get200_response_instance = ShippingCarrierGet200Response.from_json(json)
# print the JSON string representation of the object
print(ShippingCarrierGet200Response.to_json())

# convert the object into a dict
shipping_carrier_get200_response_dict = shipping_carrier_get200_response_instance.to_dict()
# create an instance of ShippingCarrierGet200Response from a dict
shipping_carrier_get200_response_from_dict = ShippingCarrierGet200Response.from_dict(shipping_carrier_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


