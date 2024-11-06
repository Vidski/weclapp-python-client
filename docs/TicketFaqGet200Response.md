# TicketFaqGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketFaq]**](TicketFaq.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_faq_get200_response import TicketFaqGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketFaqGet200Response from a JSON string
ticket_faq_get200_response_instance = TicketFaqGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketFaqGet200Response.to_json())

# convert the object into a dict
ticket_faq_get200_response_dict = ticket_faq_get200_response_instance.to_dict()
# create an instance of TicketFaqGet200Response from a dict
ticket_faq_get200_response_from_dict = TicketFaqGet200Response.from_dict(ticket_faq_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


