# CalendarGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Calendar]**](Calendar.md) |  | [optional] 

## Example

```python
from openapi_client.models.calendar_get200_response import CalendarGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarGet200Response from a JSON string
calendar_get200_response_instance = CalendarGet200Response.from_json(json)
# print the JSON string representation of the object
print(CalendarGet200Response.to_json())

# convert the object into a dict
calendar_get200_response_dict = calendar_get200_response_instance.to_dict()
# create an instance of CalendarGet200Response from a dict
calendar_get200_response_from_dict = CalendarGet200Response.from_dict(calendar_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


