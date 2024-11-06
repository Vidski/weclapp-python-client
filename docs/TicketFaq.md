# TicketFaq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**answer** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**customers** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**position_number** | **int** |  | [optional] 
**question** | **str** |  | [optional] 
**ticket_categories** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**visibility** | [**TicketFaqVisibility**](TicketFaqVisibility.md) |  | [optional] 

## Example

```python
from openapi_client.models.ticket_faq import TicketFaq

# TODO update the JSON string below
json = "{}"
# create an instance of TicketFaq from a JSON string
ticket_faq_instance = TicketFaq.from_json(json)
# print the JSON string representation of the object
print(TicketFaq.to_json())

# convert the object into a dict
ticket_faq_dict = ticket_faq_instance.to_dict()
# create an instance of TicketFaq from a dict
ticket_faq_from_dict = TicketFaq.from_dict(ticket_faq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


