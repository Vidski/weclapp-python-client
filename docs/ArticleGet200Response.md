# ArticleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**ArticleGet200ResponseAdditionalProperties**](ArticleGet200ResponseAdditionalProperties.md) |  | [optional] 
**result** | [**List[Article]**](Article.md) |  | [optional] 

## Example

```python
from openapi_client.models.article_get200_response import ArticleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleGet200Response from a JSON string
article_get200_response_instance = ArticleGet200Response.from_json(json)
# print the JSON string representation of the object
print(ArticleGet200Response.to_json())

# convert the object into a dict
article_get200_response_dict = article_get200_response_instance.to_dict()
# create an instance of ArticleGet200Response from a dict
article_get200_response_from_dict = ArticleGet200Response.from_dict(article_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


