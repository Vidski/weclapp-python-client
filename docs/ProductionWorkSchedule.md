# ProductionWorkSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**description** | **str** |  | [optional] 
**status** | [**ProductionWorkScheduleStatus**](ProductionWorkScheduleStatus.md) |  | [optional] 
**work_schedule_items** | [**List[ProductionWorkScheduleItem]**](ProductionWorkScheduleItem.md) |  | [optional] 
**work_schedule_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.production_work_schedule import ProductionWorkSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionWorkSchedule from a JSON string
production_work_schedule_instance = ProductionWorkSchedule.from_json(json)
# print the JSON string representation of the object
print(ProductionWorkSchedule.to_json())

# convert the object into a dict
production_work_schedule_dict = production_work_schedule_instance.to_dict()
# create an instance of ProductionWorkSchedule from a dict
production_work_schedule_from_dict = ProductionWorkSchedule.from_dict(production_work_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


