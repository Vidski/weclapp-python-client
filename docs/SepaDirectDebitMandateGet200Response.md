# SepaDirectDebitMandateGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[SepaDirectDebitMandate]**](SepaDirectDebitMandate.md) |  | [optional] 

## Example

```python
from openapi_client.models.sepa_direct_debit_mandate_get200_response import SepaDirectDebitMandateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SepaDirectDebitMandateGet200Response from a JSON string
sepa_direct_debit_mandate_get200_response_instance = SepaDirectDebitMandateGet200Response.from_json(json)
# print the JSON string representation of the object
print(SepaDirectDebitMandateGet200Response.to_json())

# convert the object into a dict
sepa_direct_debit_mandate_get200_response_dict = sepa_direct_debit_mandate_get200_response_instance.to_dict()
# create an instance of SepaDirectDebitMandateGet200Response from a dict
sepa_direct_debit_mandate_get200_response_from_dict = SepaDirectDebitMandateGet200Response.from_dict(sepa_direct_debit_mandate_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


