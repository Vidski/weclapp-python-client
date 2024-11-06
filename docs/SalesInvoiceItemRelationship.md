# SalesInvoiceItemRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performance_record_item_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**sales_invoice_item_id** | **str** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 
**shipment_item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_invoice_item_relationship import SalesInvoiceItemRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of SalesInvoiceItemRelationship from a JSON string
sales_invoice_item_relationship_instance = SalesInvoiceItemRelationship.from_json(json)
# print the JSON string representation of the object
print(SalesInvoiceItemRelationship.to_json())

# convert the object into a dict
sales_invoice_item_relationship_dict = sales_invoice_item_relationship_instance.to_dict()
# create an instance of SalesInvoiceItemRelationship from a dict
sales_invoice_item_relationship_from_dict = SalesInvoiceItemRelationship.from_dict(sales_invoice_item_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


