# PaymentRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**payment_run_date** | **int** |  | [optional] 
**payment_run_items** | [**List[PaymentRunItem]**](PaymentRunItem.md) |  | [optional] 
**payment_run_number** | **str** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**total_amount** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.payment_run import PaymentRun

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRun from a JSON string
payment_run_instance = PaymentRun.from_json(json)
# print the JSON string representation of the object
print(PaymentRun.to_json())

# convert the object into a dict
payment_run_dict = payment_run_instance.to_dict()
# create an instance of PaymentRun from a dict
payment_run_from_dict = PaymentRun.from_dict(payment_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


