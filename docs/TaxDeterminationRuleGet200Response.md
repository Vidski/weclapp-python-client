# TaxDeterminationRuleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[TaxDeterminationRule]**](TaxDeterminationRule.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_determination_rule_get200_response import TaxDeterminationRuleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDeterminationRuleGet200Response from a JSON string
tax_determination_rule_get200_response_instance = TaxDeterminationRuleGet200Response.from_json(json)
# print the JSON string representation of the object
print(TaxDeterminationRuleGet200Response.to_json())

# convert the object into a dict
tax_determination_rule_get200_response_dict = tax_determination_rule_get200_response_instance.to_dict()
# create an instance of TaxDeterminationRuleGet200Response from a dict
tax_determination_rule_get200_response_from_dict = TaxDeterminationRuleGet200Response.from_dict(tax_determination_rule_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


