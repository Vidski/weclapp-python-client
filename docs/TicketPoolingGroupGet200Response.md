# TicketPoolingGroupGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketPoolingGroup]**](TicketPoolingGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_pooling_group_get200_response import TicketPoolingGroupGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketPoolingGroupGet200Response from a JSON string
ticket_pooling_group_get200_response_instance = TicketPoolingGroupGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketPoolingGroupGet200Response.to_json())

# convert the object into a dict
ticket_pooling_group_get200_response_dict = ticket_pooling_group_get200_response_instance.to_dict()
# create an instance of TicketPoolingGroupGet200Response from a dict
ticket_pooling_group_get200_response_from_dict = TicketPoolingGroupGet200Response.from_dict(ticket_pooling_group_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


