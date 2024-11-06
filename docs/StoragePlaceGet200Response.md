# StoragePlaceGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[StoragePlace]**](StoragePlace.md) |  | [optional] 

## Example

```python
from openapi_client.models.storage_place_get200_response import StoragePlaceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlaceGet200Response from a JSON string
storage_place_get200_response_instance = StoragePlaceGet200Response.from_json(json)
# print the JSON string representation of the object
print(StoragePlaceGet200Response.to_json())

# convert the object into a dict
storage_place_get200_response_dict = storage_place_get200_response_instance.to_dict()
# create an instance of StoragePlaceGet200Response from a dict
storage_place_get200_response_from_dict = StoragePlaceGet200Response.from_dict(storage_place_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


