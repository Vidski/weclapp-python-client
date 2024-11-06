# ShipmentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_method import ShipmentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMethod from a JSON string
shipment_method_instance = ShipmentMethod.from_json(json)
# print the JSON string representation of the object
print(ShipmentMethod.to_json())

# convert the object into a dict
shipment_method_dict = shipment_method_instance.to_dict()
# create an instance of ShipmentMethod from a dict
shipment_method_from_dict = ShipmentMethod.from_dict(shipment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


