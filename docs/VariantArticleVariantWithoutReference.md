# VariantArticleVariantWithoutReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**attribute_options** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**position_number** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.variant_article_variant_without_reference import VariantArticleVariantWithoutReference

# TODO update the JSON string below
json = "{}"
# create an instance of VariantArticleVariantWithoutReference from a JSON string
variant_article_variant_without_reference_instance = VariantArticleVariantWithoutReference.from_json(json)
# print the JSON string representation of the object
print(VariantArticleVariantWithoutReference.to_json())

# convert the object into a dict
variant_article_variant_without_reference_dict = variant_article_variant_without_reference_instance.to_dict()
# create an instance of VariantArticleVariantWithoutReference from a dict
variant_article_variant_without_reference_from_dict = VariantArticleVariantWithoutReference.from_dict(variant_article_variant_without_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


