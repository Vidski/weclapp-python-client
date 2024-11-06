# TicketPoolingGroupMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**ticket_pooling_group_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_pooling_group_member import TicketPoolingGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of TicketPoolingGroupMember from a JSON string
ticket_pooling_group_member_instance = TicketPoolingGroupMember.from_json(json)
# print the JSON string representation of the object
print(TicketPoolingGroupMember.to_json())

# convert the object into a dict
ticket_pooling_group_member_dict = ticket_pooling_group_member_instance.to_dict()
# create an instance of TicketPoolingGroupMember from a dict
ticket_pooling_group_member_from_dict = TicketPoolingGroupMember.from_dict(ticket_pooling_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


