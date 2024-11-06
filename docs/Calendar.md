# Calendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**caldav_account_id** | **str** |  | [optional] 
**calendar_color** | **str** |  | [optional] 
**calendar_key** | **str** |  | [optional] 
**calendar_sharing_permissions** | [**List[CalendarSharingPermissions]**](CalendarSharingPermissions.md) |  | [optional] 
**last_events_sync_token** | **str** |  | [optional] 
**mail_account_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**share_private_events** | **bool** |  | [optional] 
**synchronize** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.calendar import Calendar

# TODO update the JSON string below
json = "{}"
# create an instance of Calendar from a JSON string
calendar_instance = Calendar.from_json(json)
# print the JSON string representation of the object
print(Calendar.to_json())

# convert the object into a dict
calendar_dict = calendar_instance.to_dict()
# create an instance of Calendar from a dict
calendar_from_dict = Calendar.from_dict(calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


