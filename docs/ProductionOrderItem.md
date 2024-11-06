# ProductionOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**actual_pick_date** | **int** |  | [optional] 
**actual_quantity** | **decimal.Decimal** |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**target_pick_date** | **int** |  | [optional] 
**target_quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.production_order_item import ProductionOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrderItem from a JSON string
production_order_item_instance = ProductionOrderItem.from_json(json)
# print the JSON string representation of the object
print(ProductionOrderItem.to_json())

# convert the object into a dict
production_order_item_dict = production_order_item_instance.to_dict()
# create an instance of ProductionOrderItem from a dict
production_order_item_from_dict = ProductionOrderItem.from_dict(production_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


