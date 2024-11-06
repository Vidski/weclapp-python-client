# AccountingTransactionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**amount** | **decimal.Decimal** |  | [optional] 
**debit_credit** | [**DebitCreditIndicator**](DebitCreditIndicator.md) |  | [optional] 
**description** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.accounting_transaction_detail import AccountingTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingTransactionDetail from a JSON string
accounting_transaction_detail_instance = AccountingTransactionDetail.from_json(json)
# print the JSON string representation of the object
print(AccountingTransactionDetail.to_json())

# convert the object into a dict
accounting_transaction_detail_dict = accounting_transaction_detail_instance.to_dict()
# create an instance of AccountingTransactionDetail from a dict
accounting_transaction_detail_from_dict = AccountingTransactionDetail.from_dict(accounting_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


