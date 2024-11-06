# TermOfPaymentGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TermOfPayment]**](TermOfPayment.md) |  | [optional] 

## Example

```python
from openapi_client.models.term_of_payment_get200_response import TermOfPaymentGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TermOfPaymentGet200Response from a JSON string
term_of_payment_get200_response_instance = TermOfPaymentGet200Response.from_json(json)
# print the JSON string representation of the object
print(TermOfPaymentGet200Response.to_json())

# convert the object into a dict
term_of_payment_get200_response_dict = term_of_payment_get200_response_instance.to_dict()
# create an instance of TermOfPaymentGet200Response from a dict
term_of_payment_get200_response_from_dict = TermOfPaymentGet200Response.from_dict(term_of_payment_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


