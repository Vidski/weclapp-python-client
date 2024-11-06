# SalesBillOfMaterialArticleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.sales_bill_of_material_article_item import SalesBillOfMaterialArticleItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesBillOfMaterialArticleItem from a JSON string
sales_bill_of_material_article_item_instance = SalesBillOfMaterialArticleItem.from_json(json)
# print the JSON string representation of the object
print(SalesBillOfMaterialArticleItem.to_json())

# convert the object into a dict
sales_bill_of_material_article_item_dict = sales_bill_of_material_article_item_instance.to_dict()
# create an instance of SalesBillOfMaterialArticleItem from a dict
sales_bill_of_material_article_item_from_dict = SalesBillOfMaterialArticleItem.from_dict(sales_bill_of_material_article_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


