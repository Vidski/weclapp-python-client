# TranslationValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.translation_value import TranslationValue

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationValue from a JSON string
translation_value_instance = TranslationValue.from_json(json)
# print the JSON string representation of the object
print(TranslationValue.to_json())

# convert the object into a dict
translation_value_dict = translation_value_instance.to_dict()
# create an instance of TranslationValue from a dict
translation_value_from_dict = TranslationValue.from_dict(translation_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


