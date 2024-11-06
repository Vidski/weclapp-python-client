# TicketIdIdLinkSalesOrderPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_order_id** | **int** |  | 
**task_id_to_order_item_id** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.ticket_id_id_link_sales_order_post_request import TicketIdIdLinkSalesOrderPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TicketIdIdLinkSalesOrderPostRequest from a JSON string
ticket_id_id_link_sales_order_post_request_instance = TicketIdIdLinkSalesOrderPostRequest.from_json(json)
# print the JSON string representation of the object
print(TicketIdIdLinkSalesOrderPostRequest.to_json())

# convert the object into a dict
ticket_id_id_link_sales_order_post_request_dict = ticket_id_id_link_sales_order_post_request_instance.to_dict()
# create an instance of TicketIdIdLinkSalesOrderPostRequest from a dict
ticket_id_id_link_sales_order_post_request_from_dict = TicketIdIdLinkSalesOrderPostRequest.from_dict(ticket_id_id_link_sales_order_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


