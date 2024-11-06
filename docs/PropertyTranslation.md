# PropertyTranslation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**values** | [**List[PropertyTranslationValue]**](PropertyTranslationValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.property_translation import PropertyTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyTranslation from a JSON string
property_translation_instance = PropertyTranslation.from_json(json)
# print the JSON string representation of the object
print(PropertyTranslation.to_json())

# convert the object into a dict
property_translation_dict = property_translation_instance.to_dict()
# create an instance of PropertyTranslation from a dict
property_translation_from_dict = PropertyTranslation.from_dict(property_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


