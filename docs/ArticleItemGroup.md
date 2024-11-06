# ArticleItemGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**items** | [**List[ArticleItemGroupItem]**](ArticleItemGroupItem.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.article_item_group import ArticleItemGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleItemGroup from a JSON string
article_item_group_instance = ArticleItemGroup.from_json(json)
# print the JSON string representation of the object
print(ArticleItemGroup.to_json())

# convert the object into a dict
article_item_group_dict = article_item_group_instance.to_dict()
# create an instance of ArticleItemGroup from a dict
article_item_group_from_dict = ArticleItemGroup.from_dict(article_item_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


