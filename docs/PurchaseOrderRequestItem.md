# PurchaseOrderRequestItem


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
**deleted** | **bool** |  | [optional] 
**free_text_item** | **bool** |  | [optional] 
**price_scale_type** | [**PriceScaleType**](PriceScaleType.md) |  | [optional] 
**price_scale_values** | **List[decimal.Decimal]** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request_item import PurchaseOrderRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequestItem from a JSON string
purchase_order_request_item_instance = PurchaseOrderRequestItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequestItem.to_json())

# convert the object into a dict
purchase_order_request_item_dict = purchase_order_request_item_instance.to_dict()
# create an instance of PurchaseOrderRequestItem from a dict
purchase_order_request_item_from_dict = PurchaseOrderRequestItem.from_dict(purchase_order_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


