# TicketServiceLevelAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**categories** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**customers** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**degree_of_performance** | **int** |  | [optional] 
**include_no_ticket_type** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rating_id** | **str** |  | [optional] 
**targets** | [**List[TicketServiceLevelAgreementTarget]**](TicketServiceLevelAgreementTarget.md) |  | [optional] 
**types** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**visible** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_service_level_agreement import TicketServiceLevelAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of TicketServiceLevelAgreement from a JSON string
ticket_service_level_agreement_instance = TicketServiceLevelAgreement.from_json(json)
# print the JSON string representation of the object
print(TicketServiceLevelAgreement.to_json())

# convert the object into a dict
ticket_service_level_agreement_dict = ticket_service_level_agreement_instance.to_dict()
# create an instance of TicketServiceLevelAgreement from a dict
ticket_service_level_agreement_from_dict = TicketServiceLevelAgreement.from_dict(ticket_service_level_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


