# CustomAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_definition_id** | **str** |  | [optional] 
**boolean_value** | **bool** |  | [optional] 
**date_value** | **int** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_references** | [**List[EntityReference]**](EntityReference.md) |  | [optional] 
**number_value** | **decimal.Decimal** |  | [optional] 
**selected_value_id** | **str** |  | [optional] 
**selected_values** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**string_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute import CustomAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttribute from a JSON string
custom_attribute_instance = CustomAttribute.from_json(json)
# print the JSON string representation of the object
print(CustomAttribute.to_json())

# convert the object into a dict
custom_attribute_dict = custom_attribute_instance.to_dict()
# create an instance of CustomAttribute from a dict
custom_attribute_from_dict = CustomAttribute.from_dict(custom_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


