# ShipmentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ShipmentStatusType**](ShipmentStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_status import ShipmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentStatus from a JSON string
shipment_status_instance = ShipmentStatus.from_json(json)
# print the JSON string representation of the object
print(ShipmentStatus.to_json())

# convert the object into a dict
shipment_status_dict = shipment_status_instance.to_dict()
# create an instance of ShipmentStatus from a dict
shipment_status_from_dict = ShipmentStatus.from_dict(shipment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


