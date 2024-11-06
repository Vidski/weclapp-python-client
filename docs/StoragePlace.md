# StoragePlace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**barcode** | **str** |  | [optional] 
**blocked_for_resupply** | **bool** |  | [optional] 
**blocked_for_resupply_reason_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**field_number** | **int** |  | [optional] 
**level_number** | **int** |  | [optional] 
**storage_place_size_id** | **str** |  | [optional] 
**storage_place_type** | [**StoragePlaceType**](StoragePlaceType.md) |  | [optional] 
**shelf_id** | **str** |  | [optional] 
**shelf_storage_location_id** | **str** |  | [optional] 
**storage_location_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.storage_place import StoragePlace

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlace from a JSON string
storage_place_instance = StoragePlace.from_json(json)
# print the JSON string representation of the object
print(StoragePlace.to_json())

# convert the object into a dict
storage_place_dict = storage_place_instance.to_dict()
# create an instance of StoragePlace from a dict
storage_place_from_dict = StoragePlace.from_dict(storage_place_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


