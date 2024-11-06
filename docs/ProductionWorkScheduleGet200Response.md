# ProductionWorkScheduleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ProductionWorkSchedule]**](ProductionWorkSchedule.md) |  | [optional] 

## Example

```python
from openapi_client.models.production_work_schedule_get200_response import ProductionWorkScheduleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionWorkScheduleGet200Response from a JSON string
production_work_schedule_get200_response_instance = ProductionWorkScheduleGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProductionWorkScheduleGet200Response.to_json())

# convert the object into a dict
production_work_schedule_get200_response_dict = production_work_schedule_get200_response_instance.to_dict()
# create an instance of ProductionWorkScheduleGet200Response from a dict
production_work_schedule_get200_response_from_dict = ProductionWorkScheduleGet200Response.from_dict(production_work_schedule_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


