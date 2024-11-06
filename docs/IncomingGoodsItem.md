# IncomingGoodsItem


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
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**purchase_order_item_id** | **str** |  | [optional] 
**return_assessment_id** | **str** |  | [optional] 
**return_assessment_name** | **str** |  | [optional] 
**return_description** | **str** |  | [optional] 
**return_error_id** | **str** |  | [optional] 
**return_error_name** | **str** |  | [optional] 
**return_reason_id** | **str** |  | [optional] 
**return_reason_name** | **str** |  | [optional] 
**return_rectification_id** | **str** |  | [optional] 
**return_rectification_name** | **str** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.incoming_goods_item import IncomingGoodsItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingGoodsItem from a JSON string
incoming_goods_item_instance = IncomingGoodsItem.from_json(json)
# print the JSON string representation of the object
print(IncomingGoodsItem.to_json())

# convert the object into a dict
incoming_goods_item_dict = incoming_goods_item_instance.to_dict()
# create an instance of IncomingGoodsItem from a dict
incoming_goods_item_from_dict = IncomingGoodsItem.from_dict(incoming_goods_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


