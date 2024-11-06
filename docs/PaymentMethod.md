# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**auto_clearing_account_transaction** | **bool** |  | [optional] 
**clearing_account_id** | **str** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**discount_value** | **decimal.Decimal** |  | [optional] 
**document_text** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**type** | [**PaymentMethodTypeKey**](PaymentMethodTypeKey.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_from_dict = PaymentMethod.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


