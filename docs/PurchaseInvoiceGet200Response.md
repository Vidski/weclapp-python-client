# PurchaseInvoiceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[PurchaseInvoice]**](PurchaseInvoice.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_invoice_get200_response import PurchaseInvoiceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInvoiceGet200Response from a JSON string
purchase_invoice_get200_response_instance = PurchaseInvoiceGet200Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseInvoiceGet200Response.to_json())

# convert the object into a dict
purchase_invoice_get200_response_dict = purchase_invoice_get200_response_instance.to_dict()
# create an instance of PurchaseInvoiceGet200Response from a dict
purchase_invoice_get200_response_from_dict = PurchaseInvoiceGet200Response.from_dict(purchase_invoice_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


