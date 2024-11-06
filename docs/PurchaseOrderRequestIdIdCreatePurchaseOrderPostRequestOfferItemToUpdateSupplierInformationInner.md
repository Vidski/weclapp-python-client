# PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_or_update_article_supply_source** | **bool** |  | [optional] 
**offer_item_id** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**sales_order_item_id** | **int** |  | [optional] 
**update_information** | **bool** |  | [optional] 
**update_purchase_price** | [**PurchaseOrderRequestPurchasePriceUpdateMode**](PurchaseOrderRequestPurchasePriceUpdateMode.md) |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner import PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner from a JSON string
purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner_instance = PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner.to_json())

# convert the object into a dict
purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner_dict = purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner_instance.to_dict()
# create an instance of PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner from a dict
purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner_from_dict = PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner.from_dict(purchase_order_request_id_id_create_purchase_order_post_request_offer_item_to_update_supplier_information_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


