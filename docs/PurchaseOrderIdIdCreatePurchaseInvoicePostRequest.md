# PurchaseOrderIdIdCreatePurchaseInvoicePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_existing_invoice_number** | **bool** |  | [optional] 
**invoice_date** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_type** | **str** |  | [optional] 
**is_gross** | **bool** |  | [optional] 
**payment_amount** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_id_id_create_purchase_invoice_post_request import PurchaseOrderIdIdCreatePurchaseInvoicePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderIdIdCreatePurchaseInvoicePostRequest from a JSON string
purchase_order_id_id_create_purchase_invoice_post_request_instance = PurchaseOrderIdIdCreatePurchaseInvoicePostRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderIdIdCreatePurchaseInvoicePostRequest.to_json())

# convert the object into a dict
purchase_order_id_id_create_purchase_invoice_post_request_dict = purchase_order_id_id_create_purchase_invoice_post_request_instance.to_dict()
# create an instance of PurchaseOrderIdIdCreatePurchaseInvoicePostRequest from a dict
purchase_order_id_id_create_purchase_invoice_post_request_from_dict = PurchaseOrderIdIdCreatePurchaseInvoicePostRequest.from_dict(purchase_order_id_id_create_purchase_invoice_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


