# TaxResetSystemTaxesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**init_all_stores** | **bool** |  | 
**persons_third_country_free_tax** | **bool** |  | 
**tax_recipient_country** | **bool** |  | 

## Example

```python
from openapi_client.models.tax_reset_system_taxes_post_request import TaxResetSystemTaxesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxResetSystemTaxesPostRequest from a JSON string
tax_reset_system_taxes_post_request_instance = TaxResetSystemTaxesPostRequest.from_json(json)
# print the JSON string representation of the object
print(TaxResetSystemTaxesPostRequest.to_json())

# convert the object into a dict
tax_reset_system_taxes_post_request_dict = tax_reset_system_taxes_post_request_instance.to_dict()
# create an instance of TaxResetSystemTaxesPostRequest from a dict
tax_reset_system_taxes_post_request_from_dict = TaxResetSystemTaxesPostRequest.from_dict(tax_reset_system_taxes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


