# PurchaseRequisitionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[PurchaseRequisition]**](PurchaseRequisition.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_requisition_get200_response import PurchaseRequisitionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseRequisitionGet200Response from a JSON string
purchase_requisition_get200_response_instance = PurchaseRequisitionGet200Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseRequisitionGet200Response.to_json())

# convert the object into a dict
purchase_requisition_get200_response_dict = purchase_requisition_get200_response_instance.to_dict()
# create an instance of PurchaseRequisitionGet200Response from a dict
purchase_requisition_get200_response_from_dict = PurchaseRequisitionGet200Response.from_dict(purchase_requisition_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


