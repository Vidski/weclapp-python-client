# ArticleAlternativeQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**minimum_order_quantity** | **decimal.Decimal** |  | [optional] 
**minimum_stock_quantity** | **decimal.Decimal** |  | [optional] 
**target_stock_quantity** | **decimal.Decimal** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.article_alternative_quantity import ArticleAlternativeQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleAlternativeQuantity from a JSON string
article_alternative_quantity_instance = ArticleAlternativeQuantity.from_json(json)
# print the JSON string representation of the object
print(ArticleAlternativeQuantity.to_json())

# convert the object into a dict
article_alternative_quantity_dict = article_alternative_quantity_instance.to_dict()
# create an instance of ArticleAlternativeQuantity from a dict
article_alternative_quantity_from_dict = ArticleAlternativeQuantity.from_dict(article_alternative_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


