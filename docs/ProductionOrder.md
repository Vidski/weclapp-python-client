# ProductionOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**actual_end_date** | **int** |  | [optional] 
**actual_quantity** | **decimal.Decimal** |  | [optional] 
**actual_start_date** | **int** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**assembly_storage_place_id** | **str** |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**picking_instructions** | **str** |  | [optional] 
**picks_complete** | **bool** |  | [optional] 
**production_order_items** | [**List[ProductionOrderItem]**](ProductionOrderItem.md) |  | [optional] 
**production_order_number** | **str** |  | [optional] 
**status** | [**ProductionOrderStatusType**](ProductionOrderStatusType.md) |  | [optional] 
**status_history** | [**List[ProductionOrderStatusHistory]**](ProductionOrderStatusHistory.md) |  | [optional] 
**target_end_date** | **int** |  | [optional] 
**target_quantity** | **decimal.Decimal** |  | [optional] 
**target_start_date** | **int** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 
**work_items** | [**List[ProductionOrderWorkItem]**](ProductionOrderWorkItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.production_order import ProductionOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrder from a JSON string
production_order_instance = ProductionOrder.from_json(json)
# print the JSON string representation of the object
print(ProductionOrder.to_json())

# convert the object into a dict
production_order_dict = production_order_instance.to_dict()
# create an instance of ProductionOrder from a dict
production_order_from_dict = ProductionOrder.from_dict(production_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


