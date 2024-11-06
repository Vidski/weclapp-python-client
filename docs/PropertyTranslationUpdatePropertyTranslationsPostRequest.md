# PropertyTranslationUpdatePropertyTranslationsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**entity_name** | **str** |  | 
**property_translations** | [**List[PropertyTranslationUpdatePropertyTranslationsPostRequestPropertyTranslationsInner]**](PropertyTranslationUpdatePropertyTranslationsPostRequestPropertyTranslationsInner.md) |  | 

## Example

```python
from openapi_client.models.property_translation_update_property_translations_post_request import PropertyTranslationUpdatePropertyTranslationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyTranslationUpdatePropertyTranslationsPostRequest from a JSON string
property_translation_update_property_translations_post_request_instance = PropertyTranslationUpdatePropertyTranslationsPostRequest.from_json(json)
# print the JSON string representation of the object
print(PropertyTranslationUpdatePropertyTranslationsPostRequest.to_json())

# convert the object into a dict
property_translation_update_property_translations_post_request_dict = property_translation_update_property_translations_post_request_instance.to_dict()
# create an instance of PropertyTranslationUpdatePropertyTranslationsPostRequest from a dict
property_translation_update_property_translations_post_request_from_dict = PropertyTranslationUpdatePropertyTranslationsPostRequest.from_dict(property_translation_update_property_translations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


