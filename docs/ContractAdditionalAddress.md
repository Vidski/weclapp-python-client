# ContractAdditionalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contract_additional_address import ContractAdditionalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAdditionalAddress from a JSON string
contract_additional_address_instance = ContractAdditionalAddress.from_json(json)
# print the JSON string representation of the object
print(ContractAdditionalAddress.to_json())

# convert the object into a dict
contract_additional_address_dict = contract_additional_address_instance.to_dict()
# create an instance of ContractAdditionalAddress from a dict
contract_additional_address_from_dict = ContractAdditionalAddress.from_dict(contract_additional_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


