# TicketAssignmentRuleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TicketAssignmentRule]**](TicketAssignmentRule.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_assignment_rule_get200_response import TicketAssignmentRuleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TicketAssignmentRuleGet200Response from a JSON string
ticket_assignment_rule_get200_response_instance = TicketAssignmentRuleGet200Response.from_json(json)
# print the JSON string representation of the object
print(TicketAssignmentRuleGet200Response.to_json())

# convert the object into a dict
ticket_assignment_rule_get200_response_dict = ticket_assignment_rule_get200_response_instance.to_dict()
# create an instance of TicketAssignmentRuleGet200Response from a dict
ticket_assignment_rule_get200_response_from_dict = TicketAssignmentRuleGet200Response.from_dict(ticket_assignment_rule_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


