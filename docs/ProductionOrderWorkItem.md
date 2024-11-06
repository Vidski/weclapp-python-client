# ProductionOrderWorkItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**book** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**manual_item** | **bool** |  | [optional] 
**position_number** | **int** |  | [optional] 
**short_description** | **str** |  | [optional] 
**status** | [**ProductionOrderItemStatus**](ProductionOrderItemStatus.md) |  | [optional] 
**target_end_date** | **int** |  | [optional] 
**target_order_time** | **int** |  | [optional] 
**target_start_date** | **int** |  | [optional] 
**time_type** | [**ProductionWorkScheduleItemTimeType**](ProductionWorkScheduleItemTimeType.md) |  | [optional] 
**unit_time** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.production_order_work_item import ProductionOrderWorkItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrderWorkItem from a JSON string
production_order_work_item_instance = ProductionOrderWorkItem.from_json(json)
# print the JSON string representation of the object
print(ProductionOrderWorkItem.to_json())

# convert the object into a dict
production_order_work_item_dict = production_order_work_item_instance.to_dict()
# create an instance of ProductionOrderWorkItem from a dict
production_order_work_item_from_dict = ProductionOrderWorkItem.from_dict(production_order_work_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


