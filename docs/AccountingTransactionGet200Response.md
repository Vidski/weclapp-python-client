# AccountingTransactionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[AccountingTransaction]**](AccountingTransaction.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting_transaction_get200_response import AccountingTransactionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingTransactionGet200Response from a JSON string
accounting_transaction_get200_response_instance = AccountingTransactionGet200Response.from_json(json)
# print the JSON string representation of the object
print(AccountingTransactionGet200Response.to_json())

# convert the object into a dict
accounting_transaction_get200_response_dict = accounting_transaction_get200_response_instance.to_dict()
# create an instance of AccountingTransactionGet200Response from a dict
accounting_transaction_get200_response_from_dict = AccountingTransactionGet200Response.from_dict(accounting_transaction_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


