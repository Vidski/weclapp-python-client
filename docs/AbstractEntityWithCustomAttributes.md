# AbstractEntityWithCustomAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 

## Example

```python
from openapi_client.models.abstract_entity_with_custom_attributes import AbstractEntityWithCustomAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractEntityWithCustomAttributes from a JSON string
abstract_entity_with_custom_attributes_instance = AbstractEntityWithCustomAttributes.from_json(json)
# print the JSON string representation of the object
print(AbstractEntityWithCustomAttributes.to_json())

# convert the object into a dict
abstract_entity_with_custom_attributes_dict = abstract_entity_with_custom_attributes_instance.to_dict()
# create an instance of AbstractEntityWithCustomAttributes from a dict
abstract_entity_with_custom_attributes_from_dict = AbstractEntityWithCustomAttributes.from_dict(abstract_entity_with_custom_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


