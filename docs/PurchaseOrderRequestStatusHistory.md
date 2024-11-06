# PurchaseOrderRequestStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PurchaseOrderRequestStatusType**](PurchaseOrderRequestStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_status_history import PurchaseOrderRequestStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestStatusHistory from a JSON string
purchase_order_request_status_history_instance = PurchaseOrderRequestStatusHistory.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestStatusHistory.to_json())

# convert the object into a dict
purchase_order_request_status_history_dict = purchase_order_request_status_history_instance.to_dict()
# create an instance of PurchaseOrderRequestStatusHistory from a dict
purchase_order_request_status_history_from_dict = PurchaseOrderRequestStatusHistory.from_dict(purchase_order_request_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


