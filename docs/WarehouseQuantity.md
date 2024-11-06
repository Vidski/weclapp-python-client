# WarehouseQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **decimal.Decimal** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_quantity import WarehouseQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseQuantity from a JSON string
warehouse_quantity_instance = WarehouseQuantity.from_json(json)
# print the JSON string representation of the object
print(WarehouseQuantity.to_json())

# convert the object into a dict
warehouse_quantity_dict = warehouse_quantity_instance.to_dict()
# create an instance of WarehouseQuantity from a dict
warehouse_quantity_from_dict = WarehouseQuantity.from_dict(warehouse_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


