# SalesInvoiceIdIdAddSalesOrdersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collective_invoice_position_print_type** | **str** |  | [optional] 
**sales_order_ids** | **List[str]** |  | 

## Example

```python
from openapi_client.models.sales_invoice_id_id_add_sales_orders_post_request import SalesInvoiceIdIdAddSalesOrdersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesInvoiceIdIdAddSalesOrdersPostRequest from a JSON string
sales_invoice_id_id_add_sales_orders_post_request_instance = SalesInvoiceIdIdAddSalesOrdersPostRequest.from_json(json)
# print the JSON string representation of the object
print(SalesInvoiceIdIdAddSalesOrdersPostRequest.to_json())

# convert the object into a dict
sales_invoice_id_id_add_sales_orders_post_request_dict = sales_invoice_id_id_add_sales_orders_post_request_instance.to_dict()
# create an instance of SalesInvoiceIdIdAddSalesOrdersPostRequest from a dict
sales_invoice_id_id_add_sales_orders_post_request_from_dict = SalesInvoiceIdIdAddSalesOrdersPostRequest.from_dict(sales_invoice_id_id_add_sales_orders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


