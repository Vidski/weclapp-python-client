# VariantArticleAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**attribute_options** | [**List[VariantArticleAttributeOption]**](VariantArticleAttributeOption.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.variant_article_attribute import VariantArticleAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of VariantArticleAttribute from a JSON string
variant_article_attribute_instance = VariantArticleAttribute.from_json(json)
# print the JSON string representation of the object
print(VariantArticleAttribute.to_json())

# convert the object into a dict
variant_article_attribute_dict = variant_article_attribute_instance.to_dict()
# create an instance of VariantArticleAttribute from a dict
variant_article_attribute_from_dict = VariantArticleAttribute.from_dict(variant_article_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


