# PurchaseOrderStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SupplierOrderStatusType**](SupplierOrderStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_status_history import PurchaseOrderStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderStatusHistory from a JSON string
purchase_order_status_history_instance = PurchaseOrderStatusHistory.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderStatusHistory.to_json())

# convert the object into a dict
purchase_order_status_history_dict = purchase_order_status_history_instance.to_dict()
# create an instance of PurchaseOrderStatusHistory from a dict
purchase_order_status_history_from_dict = PurchaseOrderStatusHistory.from_dict(purchase_order_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


