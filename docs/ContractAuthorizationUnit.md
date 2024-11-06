# ContractAuthorizationUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contract_authorization_unit import ContractAuthorizationUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAuthorizationUnit from a JSON string
contract_authorization_unit_instance = ContractAuthorizationUnit.from_json(json)
# print the JSON string representation of the object
print(ContractAuthorizationUnit.to_json())

# convert the object into a dict
contract_authorization_unit_dict = contract_authorization_unit_instance.to_dict()
# create an instance of ContractAuthorizationUnit from a dict
contract_authorization_unit_from_dict = ContractAuthorizationUnit.from_dict(contract_authorization_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


