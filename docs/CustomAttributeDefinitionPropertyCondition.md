# CustomAttributeDefinitionPropertyCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_operator** | [**CustomAttributeDefinitionConditionOperator**](CustomAttributeDefinitionConditionOperator.md) |  | [optional] 
**property_name** | **str** |  | [optional] 
**property_type** | [**CustomAttributeDefinitionConditionType**](CustomAttributeDefinitionConditionType.md) |  | [optional] 
**property_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_property_condition import CustomAttributeDefinitionPropertyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionPropertyCondition from a JSON string
custom_attribute_definition_property_condition_instance = CustomAttributeDefinitionPropertyCondition.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionPropertyCondition.to_json())

# convert the object into a dict
custom_attribute_definition_property_condition_dict = custom_attribute_definition_property_condition_instance.to_dict()
# create an instance of CustomAttributeDefinitionPropertyCondition from a dict
custom_attribute_definition_property_condition_from_dict = CustomAttributeDefinitionPropertyCondition.from_dict(custom_attribute_definition_property_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


