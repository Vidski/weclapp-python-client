# CalendarEventAttendee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**attendee_status** | [**EventInvitationStatus**](EventInvitationStatus.md) |  | [optional] 
**calendar_event_id** | **str** |  | [optional] 
**event_permission** | [**EventRight**](EventRight.md) |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.calendar_event_attendee import CalendarEventAttendee

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventAttendee from a JSON string
calendar_event_attendee_instance = CalendarEventAttendee.from_json(json)
# print the JSON string representation of the object
print(CalendarEventAttendee.to_json())

# convert the object into a dict
calendar_event_attendee_dict = calendar_event_attendee_instance.to_dict()
# create an instance of CalendarEventAttendee from a dict
calendar_event_attendee_from_dict = CalendarEventAttendee.from_dict(calendar_event_attendee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


