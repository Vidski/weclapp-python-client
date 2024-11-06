# StorageLocationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[StorageLocation]**](StorageLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.storage_location_get200_response import StorageLocationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StorageLocationGet200Response from a JSON string
storage_location_get200_response_instance = StorageLocationGet200Response.from_json(json)
# print the JSON string representation of the object
print(StorageLocationGet200Response.to_json())

# convert the object into a dict
storage_location_get200_response_dict = storage_location_get200_response_instance.to_dict()
# create an instance of StorageLocationGet200Response from a dict
storage_location_get200_response_from_dict = StorageLocationGet200Response.from_dict(storage_location_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


