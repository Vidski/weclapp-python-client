# ArticlePriceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ArticlePrice]**](ArticlePrice.md) |  | [optional] 

## Example

```python
from openapi_client.models.article_price_get200_response import ArticlePriceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ArticlePriceGet200Response from a JSON string
article_price_get200_response_instance = ArticlePriceGet200Response.from_json(json)
# print the JSON string representation of the object
print(ArticlePriceGet200Response.to_json())

# convert the object into a dict
article_price_get200_response_dict = article_price_get200_response_instance.to_dict()
# create an instance of ArticlePriceGet200Response from a dict
article_price_get200_response_from_dict = ArticlePriceGet200Response.from_dict(article_price_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


