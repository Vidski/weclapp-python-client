# TicketServiceLevelAgreementTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_time_quantity** | **int** |  | [optional] 
**assignment_time_unit** | [**TicketServiceLevelAgreementUnit**](TicketServiceLevelAgreementUnit.md) |  | [optional] 
**business_holidays_id** | **int** |  | [optional] 
**business_hours_id** | **int** |  | [optional] 
**first_reply_time_quantity** | **int** |  | [optional] 
**first_reply_time_unit** | [**TicketServiceLevelAgreementUnit**](TicketServiceLevelAgreementUnit.md) |  | [optional] 
**notification** | **bool** |  | [optional] 
**priority_id** | **int** |  | [optional] 
**send_escalation_email** | **bool** |  | [optional] 
**solution_time_quantity** | **int** |  | [optional] 
**solution_time_unit** | [**TicketServiceLevelAgreementUnit**](TicketServiceLevelAgreementUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_service_level_agreement_target import TicketServiceLevelAgreementTarget

# TODO update the JSON string below
json = "{}"
# create an instance of TicketServiceLevelAgreementTarget from a JSON string
ticket_service_level_agreement_target_instance = TicketServiceLevelAgreementTarget.from_json(json)
# print the JSON string representation of the object
print(TicketServiceLevelAgreementTarget.to_json())

# convert the object into a dict
ticket_service_level_agreement_target_dict = ticket_service_level_agreement_target_instance.to_dict()
# create an instance of TicketServiceLevelAgreementTarget from a dict
ticket_service_level_agreement_target_from_dict = TicketServiceLevelAgreementTarget.from_dict(ticket_service_level_agreement_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


