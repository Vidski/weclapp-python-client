# ConditionsForEntityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**CustomAttributeExtendableEntity**](CustomAttributeExtendableEntity.md) |  | [optional] 
**property_conditions** | [**List[CustomAttributeDefinitionPropertyCondition]**](CustomAttributeDefinitionPropertyCondition.md) |  | [optional] 

## Example

```python
from openapi_client.models.conditions_for_entity_type import ConditionsForEntityType

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionsForEntityType from a JSON string
conditions_for_entity_type_instance = ConditionsForEntityType.from_json(json)
# print the JSON string representation of the object
print(ConditionsForEntityType.to_json())

# convert the object into a dict
conditions_for_entity_type_dict = conditions_for_entity_type_instance.to_dict()
# create an instance of ConditionsForEntityType from a dict
conditions_for_entity_type_from_dict = ConditionsForEntityType.from_dict(conditions_for_entity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


