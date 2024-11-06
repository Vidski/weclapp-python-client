# PurchaseInvoiceItemRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**shipment_item_id** | **str** |  | [optional] 
**supplier_order_item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_invoice_item_relationship import PurchaseInvoiceItemRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInvoiceItemRelationship from a JSON string
purchase_invoice_item_relationship_instance = PurchaseInvoiceItemRelationship.from_json(json)
# print the JSON string representation of the object
print(PurchaseInvoiceItemRelationship.to_json())

# convert the object into a dict
purchase_invoice_item_relationship_dict = purchase_invoice_item_relationship_instance.to_dict()
# create an instance of PurchaseInvoiceItemRelationship from a dict
purchase_invoice_item_relationship_from_dict = PurchaseInvoiceItemRelationship.from_dict(purchase_invoice_item_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


