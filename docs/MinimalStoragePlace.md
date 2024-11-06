# MinimalStoragePlace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.minimal_storage_place import MinimalStoragePlace

# TODO update the JSON string below
json = "{}"
# create an instance of MinimalStoragePlace from a JSON string
minimal_storage_place_instance = MinimalStoragePlace.from_json(json)
# print the JSON string representation of the object
print(MinimalStoragePlace.to_json())

# convert the object into a dict
minimal_storage_place_dict = minimal_storage_place_instance.to_dict()
# create an instance of MinimalStoragePlace from a dict
minimal_storage_place_from_dict = MinimalStoragePlace.from_dict(minimal_storage_place_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


