# TaxDeterminationRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**accounting_code_id** | **str** |  | [optional] 
**customer_debtor_accounting_code_id** | **str** |  | [optional] 
**dispatch_country_code** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**party_type** | [**PartyType**](PartyType.md) |  | [optional] 
**recipient_country_code** | **str** |  | [optional] 
**sales** | **bool** |  | [optional] 
**start_date** | **int** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_rate_type** | [**TaxRateType**](TaxRateType.md) |  | [optional] 
**valid_vat_id** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.tax_determination_rule import TaxDeterminationRule

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDeterminationRule from a JSON string
tax_determination_rule_instance = TaxDeterminationRule.from_json(json)
# print the JSON string representation of the object
print(TaxDeterminationRule.to_json())

# convert the object into a dict
tax_determination_rule_dict = tax_determination_rule_instance.to_dict()
# create an instance of TaxDeterminationRule from a dict
tax_determination_rule_from_dict = TaxDeterminationRule.from_dict(tax_determination_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


