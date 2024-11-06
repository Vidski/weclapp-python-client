# TicketGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**TicketGet200ResponseAdditionalProperties**](TicketGet200ResponseAdditionalProperties.md) |  | [optional] 
**result** | [**List[Ticket]**](Ticket.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_get200_response import TicketGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketGet200Response from a JSON string
ticket_get200_response_instance = TicketGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketGet200Response.to_json())

# convert the object into a dict
ticket_get200_response_dict = ticket_get200_response_instance.to_dict()
# create an instance of TicketGet200Response from a dict
ticket_get200_response_from_dict = TicketGet200Response.from_dict(ticket_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


