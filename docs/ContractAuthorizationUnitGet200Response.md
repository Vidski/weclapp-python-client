# ContractAuthorizationUnitGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ContractAuthorizationUnit]**](ContractAuthorizationUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_authorization_unit_get200_response import ContractAuthorizationUnitGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAuthorizationUnitGet200Response from a JSON string
contract_authorization_unit_get200_response_instance = ContractAuthorizationUnitGet200Response.from_json(json)
# print the JSON string representation of the object
print(ContractAuthorizationUnitGet200Response.to_json())

# convert the object into a dict
contract_authorization_unit_get200_response_dict = contract_authorization_unit_get200_response_instance.to_dict()
# create an instance of ContractAuthorizationUnitGet200Response from a dict
contract_authorization_unit_get200_response_from_dict = ContractAuthorizationUnitGet200Response.from_dict(contract_authorization_unit_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


