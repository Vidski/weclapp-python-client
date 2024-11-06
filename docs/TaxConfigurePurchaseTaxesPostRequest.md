# TaxConfigurePurchaseTaxesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 

## Example

```python
from openapi_client.models.tax_configure_purchase_taxes_post_request import TaxConfigurePurchaseTaxesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxConfigurePurchaseTaxesPostRequest from a JSON string
tax_configure_purchase_taxes_post_request_instance = TaxConfigurePurchaseTaxesPostRequest.from_json(json)
# print the JSON string representation of the object
print(TaxConfigurePurchaseTaxesPostRequest.to_json())

# convert the object into a dict
tax_configure_purchase_taxes_post_request_dict = tax_configure_purchase_taxes_post_request_instance.to_dict()
# create an instance of TaxConfigurePurchaseTaxesPostRequest from a dict
tax_configure_purchase_taxes_post_request_from_dict = TaxConfigurePurchaseTaxesPostRequest.from_dict(tax_configure_purchase_taxes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


