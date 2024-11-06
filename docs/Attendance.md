# Attendance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**end_time** | **int** |  | [optional] 
**start_time** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.attendance import Attendance

# TODO update the JSON string below
json = "{}"
# create an instance of Attendance from a JSON string
attendance_instance = Attendance.from_json(json)
# print the JSON string representation of the object
print(Attendance.to_json())

# convert the object into a dict
attendance_dict = attendance_instance.to_dict()
# create an instance of Attendance from a dict
attendance_from_dict = Attendance.from_dict(attendance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


