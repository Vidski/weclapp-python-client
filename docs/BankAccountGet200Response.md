# BankAccountGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[BankAccount]**](BankAccount.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_account_get200_response import BankAccountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountGet200Response from a JSON string
bank_account_get200_response_instance = BankAccountGet200Response.from_json(json)
# print the JSON string representation of the object
print(BankAccountGet200Response.to_json())

# convert the object into a dict
bank_account_get200_response_dict = bank_account_get200_response_instance.to_dict()
# create an instance of BankAccountGet200Response from a dict
bank_account_get200_response_from_dict = BankAccountGet200Response.from_dict(bank_account_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


