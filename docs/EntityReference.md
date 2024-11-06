# EntityReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.entity_reference import EntityReference

# TODO update the JSON string below
json = "{}"
# create an instance of EntityReference from a JSON string
entity_reference_instance = EntityReference.from_json(json)
# print the JSON string representation of the object
print(EntityReference.to_json())

# convert the object into a dict
entity_reference_dict = entity_reference_instance.to_dict()
# create an instance of EntityReference from a dict
entity_reference_from_dict = EntityReference.from_dict(entity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


