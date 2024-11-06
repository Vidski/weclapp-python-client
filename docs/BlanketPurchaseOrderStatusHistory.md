# BlanketPurchaseOrderStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**BlanketPurchaseOrderStatusType**](BlanketPurchaseOrderStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blanket_purchase_order_status_history import BlanketPurchaseOrderStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of BlanketPurchaseOrderStatusHistory from a JSON string
blanket_purchase_order_status_history_instance = BlanketPurchaseOrderStatusHistory.from_json(json)
# print the JSON string representation of the object
print(BlanketPurchaseOrderStatusHistory.to_json())

# convert the object into a dict
blanket_purchase_order_status_history_dict = blanket_purchase_order_status_history_instance.to_dict()
# create an instance of BlanketPurchaseOrderStatusHistory from a dict
blanket_purchase_order_status_history_from_dict = BlanketPurchaseOrderStatusHistory.from_dict(blanket_purchase_order_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


