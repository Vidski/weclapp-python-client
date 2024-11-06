# PurchaseOrderRequestGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[PurchaseOrderRequest]**](PurchaseOrderRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_get200_response import PurchaseOrderRequestGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestGet200Response from a JSON string
purchase_order_request_get200_response_instance = PurchaseOrderRequestGet200Response.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestGet200Response.to_json())

# convert the object into a dict
purchase_order_request_get200_response_dict = purchase_order_request_get200_response_instance.to_dict()
# create an instance of PurchaseOrderRequestGet200Response from a dict
purchase_order_request_get200_response_from_dict = PurchaseOrderRequestGet200Response.from_dict(purchase_order_request_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


