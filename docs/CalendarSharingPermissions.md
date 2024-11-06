# CalendarSharingPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**permission_type** | [**CalendarSharingPermissionType**](CalendarSharingPermissionType.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.calendar_sharing_permissions import CalendarSharingPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarSharingPermissions from a JSON string
calendar_sharing_permissions_instance = CalendarSharingPermissions.from_json(json)
# print the JSON string representation of the object
print(CalendarSharingPermissions.to_json())

# convert the object into a dict
calendar_sharing_permissions_dict = calendar_sharing_permissions_instance.to_dict()
# create an instance of CalendarSharingPermissions from a dict
calendar_sharing_permissions_from_dict = CalendarSharingPermissions.from_dict(calendar_sharing_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


