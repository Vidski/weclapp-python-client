# PurchaseOrderRequestOfferItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**description** | **str** |  | [optional] 
**description_fixed** | **bool** |  | [optional] 
**manual_quantity** | **bool** |  | [optional] 
**parent_item_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**gross_amount** | **decimal.Decimal** |  | [optional] 
**gross_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**manual_unit_price** | **bool** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_for_statistics** | **decimal.Decimal** |  | [optional] 
**net_amount_for_statistics_in_company_currency** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**reduction_addition_items** | [**List[ReductionAdditionItem]**](ReductionAdditionItem.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_name** | **str** |  | [optional] 
**unit_price** | **decimal.Decimal** |  | [optional] 
**unit_price_in_company_currency** | **decimal.Decimal** |  | [optional] 
**accepted** | **bool** |  | [optional] 
**container_quantity** | **decimal.Decimal** |  | [optional] 
**min_quantity** | **decimal.Decimal** |  | [optional] 
**ordered_quantity** | **decimal.Decimal** |  | [optional] 
**procurement_lead_days** | **int** |  | [optional] 
**purchase_order_request_item_id** | **int** |  | [optional] 
**scale_type** | [**PriceScaleType**](PriceScaleType.md) |  | [optional] 
**scale_values** | [**List[PurchaseOrderRequestOfferItemScaleValue]**](PurchaseOrderRequestOfferItemScaleValue.md) |  | [optional] 
**supplier_article_number** | **str** |  | [optional] 
**use_supplier_article_number** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_offer_item import PurchaseOrderRequestOfferItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestOfferItem from a JSON string
purchase_order_request_offer_item_instance = PurchaseOrderRequestOfferItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestOfferItem.to_json())

# convert the object into a dict
purchase_order_request_offer_item_dict = purchase_order_request_offer_item_instance.to_dict()
# create an instance of PurchaseOrderRequestOfferItem from a dict
purchase_order_request_offer_item_from_dict = PurchaseOrderRequestOfferItem.from_dict(purchase_order_request_offer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


