# ExternalConnectionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ExternalConnection]**](ExternalConnection.md) |  | [optional] 

## Example

```python
from openapi_client.models.external_connection_get200_response import ExternalConnectionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalConnectionGet200Response from a JSON string
external_connection_get200_response_instance = ExternalConnectionGet200Response.from_json(json)
# print the JSON string representation of the object
print(ExternalConnectionGet200Response.to_json())

# convert the object into a dict
external_connection_get200_response_dict = external_connection_get200_response_instance.to_dict()
# create an instance of ExternalConnectionGet200Response from a dict
external_connection_get200_response_from_dict = ExternalConnectionGet200Response.from_dict(external_connection_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


