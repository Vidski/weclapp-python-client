# VariantArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**primary_article_id** | **str** |  | [optional] 
**primary_article_number** | **str** |  | [optional] 
**variant_article_name** | **str** |  | [optional] 
**variant_article_number** | **str** |  | [optional] 
**variants** | [**List[VariantArticleVariantWithoutReference]**](VariantArticleVariantWithoutReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.variant_article import VariantArticle

# TODO update the JSON string below
json = "{}"
# create an instance of VariantArticle from a JSON string
variant_article_instance = VariantArticle.from_json(json)
# print the JSON string representation of the object
print(VariantArticle.to_json())

# convert the object into a dict
variant_article_dict = variant_article_instance.to_dict()
# create an instance of VariantArticle from a dict
variant_article_from_dict = VariantArticle.from_dict(variant_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


