# PaymentApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**amount_applied** | **decimal.Decimal** |  | [optional] 
**amount_applied_origin_currency** | **decimal.Decimal** |  | [optional] 
**amount_costs_of_monetary_traffic** | **decimal.Decimal** |  | [optional] 
**amount_discount_applied** | **decimal.Decimal** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**money_transaction_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.payment_application import PaymentApplication

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentApplication from a JSON string
payment_application_instance = PaymentApplication.from_json(json)
# print the JSON string representation of the object
print(PaymentApplication.to_json())

# convert the object into a dict
payment_application_dict = payment_application_instance.to_dict()
# create an instance of PaymentApplication from a dict
payment_application_from_dict = PaymentApplication.from_dict(payment_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


