# Ticket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**assigned_pooling_group_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**billable** | **bool** |  | [optional] 
**billable_status** | **bool** |  | [optional] 
**cc_email_addresses** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**contract_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disable_email_templates** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**entity_references** | [**List[EntityReference]**](EntityReference.md) |  | [optional] 
**finished_date** | **int** |  | [optional] 
**first_name** | **str** |  | [optional] 
**follow_up_date** | **int** |  | [optional] 
**invoicing_status** | [**BillableInvoiceStatus**](BillableInvoiceStatus.md) |  | [optional] 
**language** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**legacy_article_id** | **str** |  | [optional] 
**legacy_time_and_material_ticket** | **bool** |  | [optional] 
**mail2_ticket_id** | **str** |  | [optional] 
**mobile_phone_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**party_id** | **str** |  | [optional] 
**performance_recorded_status** | [**PerformanceRecordedStatus**](PerformanceRecordedStatus.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**public_page_expiration_date** | **int** |  | [optional] 
**public_page_uuid** | **str** |  | [optional] 
**resolved_your_issue** | **bool** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**room** | **str** |  | [optional] 
**sales_order_id** | **str** |  | [optional] 
**solution_due_date** | **int** |  | [optional] 
**subject** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**ticket_category_id** | **str** |  | [optional] 
**ticket_channel_id** | **str** |  | [optional] 
**ticket_number** | **str** |  | [optional] 
**ticket_priority_id** | **str** |  | [optional] 
**ticket_rating** | [**Rating**](Rating.md) |  | [optional] 
**ticket_rating_comment** | **str** |  | [optional] 
**ticket_rating_date** | **int** |  | [optional] 
**ticket_service_level_agreement_id** | **str** |  | [optional] 
**ticket_status_id** | **str** |  | [optional] 
**ticket_type_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print(Ticket.to_json())

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_from_dict = Ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


