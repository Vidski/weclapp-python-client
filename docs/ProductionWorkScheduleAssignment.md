# ProductionWorkScheduleAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**alternative** | **bool** |  | [optional] 
**article_id** | **str** |  | [optional] 
**production_work_schedule_id** | **str** |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.production_work_schedule_assignment import ProductionWorkScheduleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionWorkScheduleAssignment from a JSON string
production_work_schedule_assignment_instance = ProductionWorkScheduleAssignment.from_json(json)
# print the JSON string representation of the object
print(ProductionWorkScheduleAssignment.to_json())

# convert the object into a dict
production_work_schedule_assignment_dict = production_work_schedule_assignment_instance.to_dict()
# create an instance of ProductionWorkScheduleAssignment from a dict
production_work_schedule_assignment_from_dict = ProductionWorkScheduleAssignment.from_dict(production_work_schedule_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


