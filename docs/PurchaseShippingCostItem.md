# PurchaseShippingCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**gross_amount** | **decimal.Decimal** |  | [optional] 
**gross_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**manual_unit_price** | **bool** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**unit_price** | **decimal.Decimal** |  | [optional] 
**unit_price_in_company_currency** | **decimal.Decimal** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_shipping_cost_item import PurchaseShippingCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseShippingCostItem from a JSON string
purchase_shipping_cost_item_instance = PurchaseShippingCostItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseShippingCostItem.to_json())

# convert the object into a dict
purchase_shipping_cost_item_dict = purchase_shipping_cost_item_instance.to_dict()
# create an instance of PurchaseShippingCostItem from a dict
purchase_shipping_cost_item_from_dict = PurchaseShippingCostItem.from_dict(purchase_shipping_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


