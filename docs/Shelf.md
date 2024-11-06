# Shelf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**short_identifier** | **str** |  | [optional] 
**storage_location_id** | **str** |  | [optional] 
**storage_places** | [**List[NestedStoragePlace]**](NestedStoragePlace.md) |  | [optional] 

## Example

```python
from openapi_client.models.shelf import Shelf

# TODO update the JSON string below
json = "{}"
# create an instance of Shelf from a JSON string
shelf_instance = Shelf.from_json(json)
# print the JSON string representation of the object
print(Shelf.to_json())

# convert the object into a dict
shelf_dict = shelf_instance.to_dict()
# create an instance of Shelf from a dict
shelf_from_dict = Shelf.from_dict(shelf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


