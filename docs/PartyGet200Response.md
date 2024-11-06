# PartyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Party]**](Party.md) |  | [optional] 

## Example

```python
from openapi_client.models.party_get200_response import PartyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PartyGet200Response from a JSON string
party_get200_response_instance = PartyGet200Response.from_json(json)
# print the JSON string representation of the object
print(PartyGet200Response.to_json())

# convert the object into a dict
party_get200_response_dict = party_get200_response_instance.to_dict()
# create an instance of PartyGet200Response from a dict
party_get200_response_from_dict = PartyGet200Response.from_dict(party_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


