# TermOfPaymentCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_days** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.term_of_payment_condition import TermOfPaymentCondition

# TODO update the JSON string below
json = "{}"
# create an instance of TermOfPaymentCondition from a JSON string
term_of_payment_condition_instance = TermOfPaymentCondition.from_json(json)
# print the JSON string representation of the object
print(TermOfPaymentCondition.to_json())

# convert the object into a dict
term_of_payment_condition_dict = term_of_payment_condition_instance.to_dict()
# create an instance of TermOfPaymentCondition from a dict
term_of_payment_condition_from_dict = TermOfPaymentCondition.from_dict(term_of_payment_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


