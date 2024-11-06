# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**account_holder** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**auto_sync** | **bool** |  | [optional] 
**automatic_processing** | [**MoneyTransactionProcessingStrategy**](MoneyTransactionProcessingStrategy.md) |  | [optional] 
**balance** | **decimal.Decimal** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**connection_failure** | **str** |  | [optional] 
**credit_institute** | **str** |  | [optional] 
**credit_institute_city** | **str** |  | [optional] 
**credit_institute_street** | **str** |  | [optional] 
**credit_institute_zip** | **str** |  | [optional] 
**credit_line** | **decimal.Decimal** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**different_sepa_creditor_identifier** | **str** |  | [optional] 
**enabled_for_electronic_payment_transactions** | **bool** |  | [optional] 
**iban** | **str** |  | [optional] 
**incidental_costs_of_monetary_traffic_account_id** | **str** |  | [optional] 
**incidental_costs_of_monetary_traffic_tax_id** | **str** |  | [optional] 
**last_download** | **int** |  | [optional] 
**primary** | **bool** |  | [optional] 
**qr_iban** | **str** |  | [optional] 
**qr_identifier** | **str** |  | [optional] 
**swift_bic** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_account import BankAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccount from a JSON string
bank_account_instance = BankAccount.from_json(json)
# print the JSON string representation of the object
print(BankAccount.to_json())

# convert the object into a dict
bank_account_dict = bank_account_instance.to_dict()
# create an instance of BankAccount from a dict
bank_account_from_dict = BankAccount.from_dict(bank_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


