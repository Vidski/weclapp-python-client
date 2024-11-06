# PurchaseInvoiceStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PurchaseInvoiceStatusType**](PurchaseInvoiceStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_invoice_status_history import PurchaseInvoiceStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInvoiceStatusHistory from a JSON string
purchase_invoice_status_history_instance = PurchaseInvoiceStatusHistory.from_json(json)
# print the JSON string representation of the object
print(PurchaseInvoiceStatusHistory.to_json())

# convert the object into a dict
purchase_invoice_status_history_dict = purchase_invoice_status_history_instance.to_dict()
# create an instance of PurchaseInvoiceStatusHistory from a dict
purchase_invoice_status_history_from_dict = PurchaseInvoiceStatusHistory.from_dict(purchase_invoice_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


