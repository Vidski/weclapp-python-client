# TicketCategoryGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketCategory]**](TicketCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_category_get200_response import TicketCategoryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCategoryGet200Response from a JSON string
ticket_category_get200_response_instance = TicketCategoryGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketCategoryGet200Response.to_json())

# convert the object into a dict
ticket_category_get200_response_dict = ticket_category_get200_response_instance.to_dict()
# create an instance of TicketCategoryGet200Response from a dict
ticket_category_get200_response_from_dict = TicketCategoryGet200Response.from_dict(ticket_category_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


