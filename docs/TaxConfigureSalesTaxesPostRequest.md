# TaxConfigureSalesTaxesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**persons_third_country_free_tax** | **bool** |  | 
**tax_eu_persons_recipient_country** | **bool** |  | 

## Example

```python
from openapi_client.models.tax_configure_sales_taxes_post_request import TaxConfigureSalesTaxesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxConfigureSalesTaxesPostRequest from a JSON string
tax_configure_sales_taxes_post_request_instance = TaxConfigureSalesTaxesPostRequest.from_json(json)
# print the JSON string representation of the object
print(TaxConfigureSalesTaxesPostRequest.to_json())

# convert the object into a dict
tax_configure_sales_taxes_post_request_dict = tax_configure_sales_taxes_post_request_instance.to_dict()
# create an instance of TaxConfigureSalesTaxesPostRequest from a dict
tax_configure_sales_taxes_post_request_from_dict = TaxConfigureSalesTaxesPostRequest.from_dict(tax_configure_sales_taxes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


