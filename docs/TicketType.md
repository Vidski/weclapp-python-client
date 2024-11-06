# TicketType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**article_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_type import TicketType

# TODO update the JSON string below
json = "{}"
# create an instance of TicketType from a JSON string
ticket_type_instance = TicketType.from_json(json)
# print the JSON string representation of the object
print(TicketType.to_json())

# convert the object into a dict
ticket_type_dict = ticket_type_instance.to_dict()
# create an instance of TicketType from a dict
ticket_type_from_dict = TicketType.from_dict(ticket_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


