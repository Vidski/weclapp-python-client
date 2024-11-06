# PaymentRunItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**amount_discount** | **decimal.Decimal** |  | [optional] 
**amount_payment** | **decimal.Decimal** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 
**cleared** | **bool** |  | [optional] 
**conversion_rate** | **decimal.Decimal** |  | [optional] 
**conversion_rate_date** | **int** |  | [optional] 
**money_transaction** | [**MoneyTransaction**](MoneyTransaction.md) |  | [optional] 
**party_bank_account_id** | **str** |  | [optional] 
**payment_run_id** | **str** |  | [optional] 
**payment_run_payment_type** | [**PaymentRunPaymentType**](PaymentRunPaymentType.md) |  | [optional] 
**purchase_open_item_id** | **str** |  | [optional] 
**purpose** | **str** |  | [optional] 
**record_currency** | [**Currency**](Currency.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_run_item import PaymentRunItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRunItem from a JSON string
payment_run_item_instance = PaymentRunItem.from_json(json)
# print the JSON string representation of the object
print(PaymentRunItem.to_json())

# convert the object into a dict
payment_run_item_dict = payment_run_item_instance.to_dict()
# create an instance of PaymentRunItem from a dict
payment_run_item_from_dict = PaymentRunItem.from_dict(payment_run_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


