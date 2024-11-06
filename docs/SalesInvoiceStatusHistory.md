# SalesInvoiceStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SalesInvoiceStatusType**](SalesInvoiceStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_invoice_status_history import SalesInvoiceStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SalesInvoiceStatusHistory from a JSON string
sales_invoice_status_history_instance = SalesInvoiceStatusHistory.from_json(json)
# print the JSON string representation of the object
print(SalesInvoiceStatusHistory.to_json())

# convert the object into a dict
sales_invoice_status_history_dict = sales_invoice_status_history_instance.to_dict()
# create an instance of SalesInvoiceStatusHistory from a dict
sales_invoice_status_history_from_dict = SalesInvoiceStatusHistory.from_dict(sales_invoice_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


