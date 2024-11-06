# TicketTypeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketType]**](TicketType.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_type_get200_response import TicketTypeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketTypeGet200Response from a JSON string
ticket_type_get200_response_instance = TicketTypeGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketTypeGet200Response.to_json())

# convert the object into a dict
ticket_type_get200_response_dict = ticket_type_get200_response_instance.to_dict()
# create an instance of TicketTypeGet200Response from a dict
ticket_type_get200_response_from_dict = TicketTypeGet200Response.from_dict(ticket_type_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


