# PurchaseRequisitionStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PurchaseRequisitionStatusType**](PurchaseRequisitionStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_requisition_status_history import PurchaseRequisitionStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseRequisitionStatusHistory from a JSON string
purchase_requisition_status_history_instance = PurchaseRequisitionStatusHistory.from_json(json)
# print the JSON string representation of the object
print(PurchaseRequisitionStatusHistory.to_json())

# convert the object into a dict
purchase_requisition_status_history_dict = purchase_requisition_status_history_instance.to_dict()
# create an instance of PurchaseRequisitionStatusHistory from a dict
purchase_requisition_status_history_from_dict = PurchaseRequisitionStatusHistory.from_dict(purchase_requisition_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


