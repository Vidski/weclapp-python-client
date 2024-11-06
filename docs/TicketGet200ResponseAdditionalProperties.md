# TicketGet200ResponseAdditionalProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_time** | [**List[Duration]**](Duration.md) |  | [optional] 
**billable_time** | [**List[Duration]**](Duration.md) |  | [optional] 
**cost_of_services** | [**List[Amount]**](Amount.md) |  | [optional] 
**invoiceable_time** | [**List[Duration]**](Duration.md) |  | [optional] 
**process_time** | [**List[Duration]**](Duration.md) |  | [optional] 
**resolution_time** | [**List[Duration]**](Duration.md) |  | [optional] 
**response_time** | [**List[Duration]**](Duration.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_get200_response_additional_properties import TicketGet200ResponseAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TicketGet200ResponseAdditionalProperties from a JSON string
ticket_get200_response_additional_properties_instance = TicketGet200ResponseAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(TicketGet200ResponseAdditionalProperties.to_json())

# convert the object into a dict
ticket_get200_response_additional_properties_dict = ticket_get200_response_additional_properties_instance.to_dict()
# create an instance of TicketGet200ResponseAdditionalProperties from a dict
ticket_get200_response_additional_properties_from_dict = TicketGet200ResponseAdditionalProperties.from_dict(ticket_get200_response_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


