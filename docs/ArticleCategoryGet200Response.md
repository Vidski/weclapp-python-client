# ArticleCategoryGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ArticleCategory]**](ArticleCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.article_category_get200_response import ArticleCategoryGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleCategoryGet200Response from a JSON string
article_category_get200_response_instance = ArticleCategoryGet200Response.from_json(json)
# print the JSON string representation of the object
print(ArticleCategoryGet200Response.to_json())

# convert the object into a dict
article_category_get200_response_dict = article_category_get200_response_instance.to_dict()
# create an instance of ArticleCategoryGet200Response from a dict
article_category_get200_response_from_dict = ArticleCategoryGet200Response.from_dict(article_category_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


