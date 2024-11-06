# VariantArticleAttributeOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.variant_article_attribute_option import VariantArticleAttributeOption

# TODO update the JSON string below
json = "{}"
# create an instance of VariantArticleAttributeOption from a JSON string
variant_article_attribute_option_instance = VariantArticleAttributeOption.from_json(json)
# print the JSON string representation of the object
print(VariantArticleAttributeOption.to_json())

# convert the object into a dict
variant_article_attribute_option_dict = variant_article_attribute_option_instance.to_dict()
# create an instance of VariantArticleAttributeOption from a dict
variant_article_attribute_option_from_dict = VariantArticleAttributeOption.from_dict(variant_article_attribute_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


