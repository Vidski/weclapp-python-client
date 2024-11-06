# StoragePlaceSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**segment_quantity** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.storage_place_size import StoragePlaceSize

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlaceSize from a JSON string
storage_place_size_instance = StoragePlaceSize.from_json(json)
# print the JSON string representation of the object
print(StoragePlaceSize.to_json())

# convert the object into a dict
storage_place_size_dict = storage_place_size_instance.to_dict()
# create an instance of StoragePlaceSize from a dict
storage_place_size_from_dict = StoragePlaceSize.from_dict(storage_place_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


