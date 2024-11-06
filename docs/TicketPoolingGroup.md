# TicketPoolingGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ticket_categories** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**ticket_pooling_group_members** | [**List[TicketPoolingGroupMember]**](TicketPoolingGroupMember.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_pooling_group import TicketPoolingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TicketPoolingGroup from a JSON string
ticket_pooling_group_instance = TicketPoolingGroup.from_json(json)
# print the JSON string representation of the object
print(TicketPoolingGroup.to_json())

# convert the object into a dict
ticket_pooling_group_dict = ticket_pooling_group_instance.to_dict()
# create an instance of TicketPoolingGroup from a dict
ticket_pooling_group_from_dict = TicketPoolingGroup.from_dict(ticket_pooling_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


