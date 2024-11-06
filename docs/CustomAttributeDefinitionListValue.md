# CustomAttributeDefinitionListValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**default_value** | **bool** |  | [optional] 
**position_number** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_list_value import CustomAttributeDefinitionListValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionListValue from a JSON string
custom_attribute_definition_list_value_instance = CustomAttributeDefinitionListValue.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionListValue.to_json())

# convert the object into a dict
custom_attribute_definition_list_value_dict = custom_attribute_definition_list_value_instance.to_dict()
# create an instance of CustomAttributeDefinitionListValue from a dict
custom_attribute_definition_list_value_from_dict = CustomAttributeDefinitionListValue.from_dict(custom_attribute_definition_list_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


