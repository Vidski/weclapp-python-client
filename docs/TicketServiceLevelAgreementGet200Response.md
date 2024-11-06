# TicketServiceLevelAgreementGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketServiceLevelAgreement]**](TicketServiceLevelAgreement.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_service_level_agreement_get200_response import TicketServiceLevelAgreementGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketServiceLevelAgreementGet200Response from a JSON string
ticket_service_level_agreement_get200_response_instance = TicketServiceLevelAgreementGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketServiceLevelAgreementGet200Response.to_json())

# convert the object into a dict
ticket_service_level_agreement_get200_response_dict = ticket_service_level_agreement_get200_response_instance.to_dict()
# create an instance of TicketServiceLevelAgreementGet200Response from a dict
ticket_service_level_agreement_get200_response_from_dict = TicketServiceLevelAgreementGet200Response.from_dict(ticket_service_level_agreement_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


