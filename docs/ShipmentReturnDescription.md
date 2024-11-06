# ShipmentReturnDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**customer_return** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**supplier_return** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_return_description import ShipmentReturnDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentReturnDescription from a JSON string
shipment_return_description_instance = ShipmentReturnDescription.from_json(json)
# print the JSON string representation of the object
print(ShipmentReturnDescription.to_json())

# convert the object into a dict
shipment_return_description_dict = shipment_return_description_instance.to_dict()
# create an instance of ShipmentReturnDescription from a dict
shipment_return_description_from_dict = ShipmentReturnDescription.from_dict(shipment_return_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


