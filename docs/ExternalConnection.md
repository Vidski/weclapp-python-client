# ExternalConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**connection_type** | [**ExternalConnectionType**](ExternalConnectionType.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.external_connection import ExternalConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalConnection from a JSON string
external_connection_instance = ExternalConnection.from_json(json)
# print the JSON string representation of the object
print(ExternalConnection.to_json())

# convert the object into a dict
external_connection_dict = external_connection_instance.to_dict()
# create an instance of ExternalConnection from a dict
external_connection_from_dict = ExternalConnection.from_dict(external_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


