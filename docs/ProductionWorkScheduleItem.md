# ProductionWorkScheduleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**cost_center_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**multiple_human_operation** | **int** |  | [optional] 
**multiple_machine_operation** | **int** |  | [optional] 
**position_number** | **int** |  | [optional] 
**production_work_schedule_id** | **str** |  | [optional] 
**quantity_base** | **int** |  | [optional] 
**setup_time** | **decimal.Decimal** |  | [optional] 
**short_description** | **str** |  | [optional] 
**time_type** | [**ProductionWorkScheduleItemTimeType**](ProductionWorkScheduleItemTimeType.md) |  | [optional] 
**time_unit** | [**TimeUnit**](TimeUnit.md) |  | [optional] 
**unit_time** | **decimal.Decimal** |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.production_work_schedule_item import ProductionWorkScheduleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionWorkScheduleItem from a JSON string
production_work_schedule_item_instance = ProductionWorkScheduleItem.from_json(json)
# print the JSON string representation of the object
print(ProductionWorkScheduleItem.to_json())

# convert the object into a dict
production_work_schedule_item_dict = production_work_schedule_item_instance.to_dict()
# create an instance of ProductionWorkScheduleItem from a dict
production_work_schedule_item_from_dict = ProductionWorkScheduleItem.from_dict(production_work_schedule_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


