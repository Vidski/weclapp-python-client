# ShippingCarrier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**internal_shipping_carrier** | [**InternalShippingCarrier**](InternalShippingCarrier.md) |  | [optional] 
**name** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**tracking_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipping_carrier import ShippingCarrier

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCarrier from a JSON string
shipping_carrier_instance = ShippingCarrier.from_json(json)
# print the JSON string representation of the object
print(ShippingCarrier.to_json())

# convert the object into a dict
shipping_carrier_dict = shipping_carrier_instance.to_dict()
# create an instance of ShippingCarrier from a dict
shipping_carrier_from_dict = ShippingCarrier.from_dict(shipping_carrier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


