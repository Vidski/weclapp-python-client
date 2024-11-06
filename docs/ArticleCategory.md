# ArticleCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_category_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.article_category import ArticleCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleCategory from a JSON string
article_category_instance = ArticleCategory.from_json(json)
# print the JSON string representation of the object
print(ArticleCategory.to_json())

# convert the object into a dict
article_category_dict = article_category_instance.to_dict()
# create an instance of ArticleCategory from a dict
article_category_from_dict = ArticleCategory.from_dict(article_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


