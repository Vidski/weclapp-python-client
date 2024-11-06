# TicketStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketStatus]**](TicketStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_status_get200_response import TicketStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketStatusGet200Response from a JSON string
ticket_status_get200_response_instance = TicketStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketStatusGet200Response.to_json())

# convert the object into a dict
ticket_status_get200_response_dict = ticket_status_get200_response_instance.to_dict()
# create an instance of TicketStatusGet200Response from a dict
ticket_status_get200_response_from_dict = TicketStatusGet200Response.from_dict(ticket_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


