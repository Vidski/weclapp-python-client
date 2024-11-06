# TicketStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**auto_change_days** | **int** |  | [optional] 
**auto_change_ticket_status_id** | **str** |  | [optional] 
**color** | [**TicketStatusColor**](TicketStatusColor.md) |  | [optional] 
**default_for_internal** | **bool** |  | [optional] 
**internal_ticket_status** | [**InternalTicketStatus**](InternalTicketStatus.md) |  | [optional] 
**name** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**target_status_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_status import TicketStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TicketStatus from a JSON string
ticket_status_instance = TicketStatus.from_json(json)
# print the JSON string representation of the object
print(TicketStatus.to_json())

# convert the object into a dict
ticket_status_dict = ticket_status_instance.to_dict()
# create an instance of TicketStatus from a dict
ticket_status_from_dict = TicketStatus.from_dict(ticket_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


