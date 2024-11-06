# ArticleItemGroupItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.article_item_group_item import ArticleItemGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleItemGroupItem from a JSON string
article_item_group_item_instance = ArticleItemGroupItem.from_json(json)
# print the JSON string representation of the object
print(ArticleItemGroupItem.to_json())

# convert the object into a dict
article_item_group_item_dict = article_item_group_item_instance.to_dict()
# create an instance of ArticleItemGroupItem from a dict
article_item_group_item_from_dict = ArticleItemGroupItem.from_dict(article_item_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


