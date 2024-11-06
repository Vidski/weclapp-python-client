# PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | 
**offer_item_to_update_supplier_information** | [**List[PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner]**](PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner.md) |  | 
**sales_order_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_id_id_create_purchase_order_post_request import PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest from a JSON string
purchase_order_request_id_id_create_purchase_order_post_request_instance = PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest.to_json())

# convert the object into a dict
purchase_order_request_id_id_create_purchase_order_post_request_dict = purchase_order_request_id_id_create_purchase_order_post_request_instance.to_dict()
# create an instance of PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest from a dict
purchase_order_request_id_id_create_purchase_order_post_request_from_dict = PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest.from_dict(purchase_order_request_id_id_create_purchase_order_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


