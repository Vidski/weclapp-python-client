# CustomAttributeDefinitionTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_text** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_translation import CustomAttributeDefinitionTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionTranslation from a JSON string
custom_attribute_definition_translation_instance = CustomAttributeDefinitionTranslation.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionTranslation.to_json())

# convert the object into a dict
custom_attribute_definition_translation_dict = custom_attribute_definition_translation_instance.to_dict()
# create an instance of CustomAttributeDefinitionTranslation from a dict
custom_attribute_definition_translation_from_dict = CustomAttributeDefinitionTranslation.from_dict(custom_attribute_definition_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


