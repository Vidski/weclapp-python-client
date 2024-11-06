# AccountingTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**accounting_import_date** | **int** |  | [optional] 
**conversion_rate** | **decimal.Decimal** |  | [optional] 
**conversion_rate_date** | **int** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**external_record_number** | **str** |  | [optional] 
**internal_record_number** | **str** |  | [optional] 
**reverse_transaction** | **bool** |  | [optional] 
**status** | [**AccountingTransactionStatus**](AccountingTransactionStatus.md) |  | [optional] 
**transaction_date** | **int** |  | [optional] 
**transaction_details** | [**List[AccountingTransactionDetail]**](AccountingTransactionDetail.md) |  | [optional] 
**transaction_establish_date** | **int** |  | [optional] 
**transaction_number** | **str** |  | [optional] 
**type** | [**BookingType**](BookingType.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting_transaction import AccountingTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingTransaction from a JSON string
accounting_transaction_instance = AccountingTransaction.from_json(json)
# print the JSON string representation of the object
print(AccountingTransaction.to_json())

# convert the object into a dict
accounting_transaction_dict = accounting_transaction_instance.to_dict()
# create an instance of AccountingTransaction from a dict
accounting_transaction_from_dict = AccountingTransaction.from_dict(accounting_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


