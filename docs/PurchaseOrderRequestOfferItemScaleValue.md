# PurchaseOrderRequestOfferItemScaleValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **decimal.Decimal** |  | [optional] 
**scale** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_offer_item_scale_value import PurchaseOrderRequestOfferItemScaleValue

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestOfferItemScaleValue from a JSON string
purchase_order_request_offer_item_scale_value_instance = PurchaseOrderRequestOfferItemScaleValue.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestOfferItemScaleValue.to_json())

# convert the object into a dict
purchase_order_request_offer_item_scale_value_dict = purchase_order_request_offer_item_scale_value_instance.to_dict()
# create an instance of PurchaseOrderRequestOfferItemScaleValue from a dict
purchase_order_request_offer_item_scale_value_from_dict = PurchaseOrderRequestOfferItemScaleValue.from_dict(purchase_order_request_offer_item_scale_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


