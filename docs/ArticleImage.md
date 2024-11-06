# ArticleImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**main_image** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.article_image import ArticleImage

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleImage from a JSON string
article_image_instance = ArticleImage.from_json(json)
# print the JSON string representation of the object
print(ArticleImage.to_json())

# convert the object into a dict
article_image_dict = article_image_instance.to_dict()
# create an instance of ArticleImage from a dict
article_image_from_dict = ArticleImage.from_dict(article_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


