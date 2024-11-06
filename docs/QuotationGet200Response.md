# QuotationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Quotation]**](Quotation.md) |  | [optional] 

## Example

```python
from openapi_client.models.quotation_get200_response import QuotationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QuotationGet200Response from a JSON string
quotation_get200_response_instance = QuotationGet200Response.from_json(json)
# print the JSON string representation of the object
print(QuotationGet200Response.to_json())

# convert the object into a dict
quotation_get200_response_dict = quotation_get200_response_instance.to_dict()
# create an instance of QuotationGet200Response from a dict
quotation_get200_response_from_dict = QuotationGet200Response.from_dict(quotation_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


