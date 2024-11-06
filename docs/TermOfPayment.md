# TermOfPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**conditions** | [**List[TermOfPaymentCondition]**](TermOfPaymentCondition.md) |  | [optional] 
**datev_term_of_payment_number** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date_option** | [**DueDateOption**](DueDateOption.md) |  | [optional] 
**fixed_day** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_days** | **int** |  | [optional] 
**reference** | **str** |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.term_of_payment import TermOfPayment

# TODO update the JSON string below
json = "{}"
# create an instance of TermOfPayment from a JSON string
term_of_payment_instance = TermOfPayment.from_json(json)
# print the JSON string representation of the object
print(TermOfPayment.to_json())

# convert the object into a dict
term_of_payment_dict = term_of_payment_instance.to_dict()
# create an instance of TermOfPayment from a dict
term_of_payment_from_dict = TermOfPayment.from_dict(term_of_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


