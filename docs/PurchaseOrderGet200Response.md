# PurchaseOrderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[PurchaseOrder]**](PurchaseOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_get200_response import PurchaseOrderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGet200Response from a JSON string
purchase_order_get200_response_instance = PurchaseOrderGet200Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGet200Response.to_json())

# convert the object into a dict
purchase_order_get200_response_dict = purchase_order_get200_response_instance.to_dict()
# create an instance of PurchaseOrderGet200Response from a dict
purchase_order_get200_response_from_dict = PurchaseOrderGet200Response.from_dict(purchase_order_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


