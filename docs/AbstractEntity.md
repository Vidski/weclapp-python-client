# AbstractEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.abstract_entity import AbstractEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractEntity from a JSON string
abstract_entity_instance = AbstractEntity.from_json(json)
# print the JSON string representation of the object
print(AbstractEntity.to_json())

# convert the object into a dict
abstract_entity_dict = abstract_entity_instance.to_dict()
# create an instance of AbstractEntity from a dict
abstract_entity_from_dict = AbstractEntity.from_dict(abstract_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


