# AttendanceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Attendance]**](Attendance.md) |  | [optional] 

## Example

```python
from openapi_client.models.attendance_get200_response import AttendanceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceGet200Response from a JSON string
attendance_get200_response_instance = AttendanceGet200Response.from_json(json)
# print the JSON string representation of the object
print(AttendanceGet200Response.to_json())

# convert the object into a dict
attendance_get200_response_dict = attendance_get200_response_instance.to_dict()
# create an instance of AttendanceGet200Response from a dict
attendance_get200_response_from_dict = AttendanceGet200Response.from_dict(attendance_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


