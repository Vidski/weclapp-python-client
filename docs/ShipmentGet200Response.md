# ShipmentGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Shipment]**](Shipment.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipment_get200_response import ShipmentGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentGet200Response from a JSON string
shipment_get200_response_instance = ShipmentGet200Response.from_json(json)
# print the JSON string representation of the object
print(ShipmentGet200Response.to_json())

# convert the object into a dict
shipment_get200_response_dict = shipment_get200_response_instance.to_dict()
# create an instance of ShipmentGet200Response from a dict
shipment_get200_response_from_dict = ShipmentGet200Response.from_dict(shipment_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


