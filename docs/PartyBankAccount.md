# PartyBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**account_holder** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**credit_institute** | **str** |  | [optional] 
**party_id** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.party_bank_account import PartyBankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PartyBankAccount from a JSON string
party_bank_account_instance = PartyBankAccount.from_json(json)
# print the JSON string representation of the object
print(PartyBankAccount.to_json())

# convert the object into a dict
party_bank_account_dict = party_bank_account_instance.to_dict()
# create an instance of PartyBankAccount from a dict
party_bank_account_from_dict = PartyBankAccount.from_dict(party_bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


