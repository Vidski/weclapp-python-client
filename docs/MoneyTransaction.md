# MoneyTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**account_for_costs_of_monetary_traffic_id** | **str** |  | [optional] 
**account_for_costs_of_monetary_traffic_number** | **str** |  | [optional] 
**account_for_dunning_fee_id** | **str** |  | [optional] 
**account_for_dunning_fee_number** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**amount** | **decimal.Decimal** |  | [optional] 
**amount_discount** | **decimal.Decimal** |  | [optional] 
**cash_account_sheet_id** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**effective_date** | **int** |  | [optional] 
**external_record_number** | **str** |  | [optional] 
**origin** | [**MoneyTransactionSource**](MoneyTransactionSource.md) |  | [optional] 
**party_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**payment_tolerance_account_id** | **str** |  | [optional] 
**payment_tolerance_account_number** | **str** |  | [optional] 
**payment_type** | [**PaymentType**](PaymentType.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.money_transaction import MoneyTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyTransaction from a JSON string
money_transaction_instance = MoneyTransaction.from_json(json)
# print the JSON string representation of the object
print(MoneyTransaction.to_json())

# convert the object into a dict
money_transaction_dict = money_transaction_instance.to_dict()
# create an instance of MoneyTransaction from a dict
money_transaction_from_dict = MoneyTransaction.from_dict(money_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


