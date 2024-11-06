# StorageLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**block_storage_places** | [**List[NestedStoragePlace]**](NestedStoragePlace.md) |  | [optional] 
**name** | **str** |  | [optional] 
**shelves** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**short_identifier** | **str** |  | [optional] 
**storage_place_type_settings_blocked** | [**StoragePlaceTypeSettings**](StoragePlaceTypeSettings.md) |  | [optional] 
**storage_place_type_settings_picking** | [**StoragePlaceTypeSettings**](StoragePlaceTypeSettings.md) |  | [optional] 
**storage_place_type_settings_stock** | [**StoragePlaceTypeSettings**](StoragePlaceTypeSettings.md) |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.storage_location import StorageLocation

# TODO update the JSON string below
json = "{}"
# create an instance of StorageLocation from a JSON string
storage_location_instance = StorageLocation.from_json(json)
# print the JSON string representation of the object
print(StorageLocation.to_json())

# convert the object into a dict
storage_location_dict = storage_location_instance.to_dict()
# create an instance of StorageLocation from a dict
storage_location_from_dict = StorageLocation.from_dict(storage_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


