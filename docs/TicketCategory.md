# TicketCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_ticket_category_id** | **str** |  | [optional] 
**pseudo_category** | **bool** |  | [optional] 
**published** | **bool** |  | [optional] 
**visible_in_customer_portal** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_category import TicketCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TicketCategory from a JSON string
ticket_category_instance = TicketCategory.from_json(json)
# print the JSON string representation of the object
print(TicketCategory.to_json())

# convert the object into a dict
ticket_category_dict = ticket_category_instance.to_dict()
# create an instance of TicketCategory from a dict
ticket_category_from_dict = TicketCategory.from_dict(ticket_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


