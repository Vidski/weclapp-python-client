# CalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**all_day_event** | **bool** |  | [optional] 
**attendees** | [**List[CalendarEventAttendee]**](CalendarEventAttendee.md) |  | [optional] 
**calendar_id** | **str** |  | [optional] 
**concerning_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**location** | **str** |  | [optional] 
**private_event** | **bool** |  | [optional] 
**recurring_event** | [**RecurringEvent**](RecurringEvent.md) |  | [optional] 
**references** | [**List[EntityReference]**](EntityReference.md) |  | [optional] 
**reminder_send_type** | [**ReminderSendType**](ReminderSendType.md) |  | [optional] 
**reminder_time** | **int** |  | [optional] 
**show_as** | [**FollowupBusyState**](FollowupBusyState.md) |  | [optional] 
**start_date** | **int** |  | [optional] 
**subject** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.calendar_event import CalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEvent from a JSON string
calendar_event_instance = CalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEvent.to_json())

# convert the object into a dict
calendar_event_dict = calendar_event_instance.to_dict()
# create an instance of CalendarEvent from a dict
calendar_event_from_dict = CalendarEvent.from_dict(calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


