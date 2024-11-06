# CalendarEventGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CalendarEvent]**](CalendarEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.calendar_event_get200_response import CalendarEventGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventGet200Response from a JSON string
calendar_event_get200_response_instance = CalendarEventGet200Response.from_json(json)
# print the JSON string representation of the object
print(CalendarEventGet200Response.to_json())

# convert the object into a dict
calendar_event_get200_response_dict = calendar_event_get200_response_instance.to_dict()
# create an instance of CalendarEventGet200Response from a dict
calendar_event_get200_response_from_dict = CalendarEventGet200Response.from_dict(calendar_event_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


