# PaymentRunItemGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[PaymentRunItem]**](PaymentRunItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_run_item_get200_response import PaymentRunItemGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRunItemGet200Response from a JSON string
payment_run_item_get200_response_instance = PaymentRunItemGet200Response.from_json(json)
# print the JSON string representation of the object
print(PaymentRunItemGet200Response.to_json())

# convert the object into a dict
payment_run_item_get200_response_dict = payment_run_item_get200_response_instance.to_dict()
# create an instance of PaymentRunItemGet200Response from a dict
payment_run_item_get200_response_from_dict = PaymentRunItemGet200Response.from_dict(payment_run_item_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


