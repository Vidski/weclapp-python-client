# StoragePlaceTypeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_mixed_storing** | **bool** |  | [optional] 
**automatic_place_assignment** | **bool** |  | [optional] 
**multiple_places_per_base_article** | **bool** |  | [optional] 
**transportation_order_requires_free_segment** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.storage_place_type_settings import StoragePlaceTypeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlaceTypeSettings from a JSON string
storage_place_type_settings_instance = StoragePlaceTypeSettings.from_json(json)
# print the JSON string representation of the object
print(StoragePlaceTypeSettings.to_json())

# convert the object into a dict
storage_place_type_settings_dict = storage_place_type_settings_instance.to_dict()
# create an instance of StoragePlaceTypeSettings from a dict
storage_place_type_settings_from_dict = StoragePlaceTypeSettings.from_dict(storage_place_type_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


