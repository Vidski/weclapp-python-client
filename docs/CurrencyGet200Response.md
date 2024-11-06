# CurrencyGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Currency]**](Currency.md) |  | [optional] 

## Example

```python
from openapi_client.models.currency_get200_response import CurrencyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyGet200Response from a JSON string
currency_get200_response_instance = CurrencyGet200Response.from_json(json)
# print the JSON string representation of the object
print(CurrencyGet200Response.to_json())

# convert the object into a dict
currency_get200_response_dict = currency_get200_response_instance.to_dict()
# create an instance of CurrencyGet200Response from a dict
currency_get200_response_from_dict = CurrencyGet200Response.from_dict(currency_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


