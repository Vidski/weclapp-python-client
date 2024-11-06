# TicketAssignmentRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**assigned_pooling_group_id** | **str** |  | [optional] 
**assignee_user_id** | **str** |  | [optional] 
**commercial_language** | **str** |  | [optional] 
**distribution_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**party_id** | **str** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**target_status_id** | **str** |  | [optional] 
**ticket_assignee_type** | [**TicketAssigneeType**](TicketAssigneeType.md) |  | [optional] 
**ticket_category_id** | **str** |  | [optional] 
**ticket_channel_id** | **str** |  | [optional] 
**ticket_priority_id** | **str** |  | [optional] 
**ticket_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_assignment_rule import TicketAssignmentRule

# TODO update the JSON string below
json = "{}"
# create an instance of TicketAssignmentRule from a JSON string
ticket_assignment_rule_instance = TicketAssignmentRule.from_json(json)
# print the JSON string representation of the object
print(TicketAssignmentRule.to_json())

# convert the object into a dict
ticket_assignment_rule_dict = ticket_assignment_rule_instance.to_dict()
# create an instance of TicketAssignmentRule from a dict
ticket_assignment_rule_from_dict = TicketAssignmentRule.from_dict(ticket_assignment_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


