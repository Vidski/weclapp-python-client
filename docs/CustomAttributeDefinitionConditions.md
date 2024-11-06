# CustomAttributeDefinitionConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions_for_entity_type** | [**List[ConditionsForEntityType]**](ConditionsForEntityType.md) |  | [optional] 
**ignore_conditions_if_value_is_set** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_conditions import CustomAttributeDefinitionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionConditions from a JSON string
custom_attribute_definition_conditions_instance = CustomAttributeDefinitionConditions.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionConditions.to_json())

# convert the object into a dict
custom_attribute_definition_conditions_dict = custom_attribute_definition_conditions_instance.to_dict()
# create an instance of CustomAttributeDefinitionConditions from a dict
custom_attribute_definition_conditions_from_dict = CustomAttributeDefinitionConditions.from_dict(custom_attribute_definition_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


