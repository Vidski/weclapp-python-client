# BlanketPurchaseOrderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[BlanketPurchaseOrder]**](BlanketPurchaseOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.blanket_purchase_order_get200_response import BlanketPurchaseOrderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BlanketPurchaseOrderGet200Response from a JSON string
blanket_purchase_order_get200_response_instance = BlanketPurchaseOrderGet200Response.from_json(json)
# print the JSON string representation of the object
print(BlanketPurchaseOrderGet200Response.to_json())

# convert the object into a dict
blanket_purchase_order_get200_response_dict = blanket_purchase_order_get200_response_instance.to_dict()
# create an instance of BlanketPurchaseOrderGet200Response from a dict
blanket_purchase_order_get200_response_from_dict = BlanketPurchaseOrderGet200Response.from_dict(blanket_purchase_order_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


