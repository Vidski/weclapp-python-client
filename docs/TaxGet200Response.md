# TaxGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Tax]**](Tax.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_get200_response import TaxGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TaxGet200Response from a JSON string
tax_get200_response_instance = TaxGet200Response.from_json(json)
# print the JSON string representation of the object
print(TaxGet200Response.to_json())

# convert the object into a dict
tax_get200_response_dict = tax_get200_response_instance.to_dict()
# create an instance of TaxGet200Response from a dict
tax_get200_response_from_dict = TaxGet200Response.from_dict(tax_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


