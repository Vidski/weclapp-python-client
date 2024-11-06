# Tax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**contra_account_id** | **str** |  | [optional] 
**contra_account_number** | **str** |  | [optional] 
**default_discount_account_id** | **str** |  | [optional] 
**default_discount_account_number** | **str** |  | [optional] 
**default_nominal_account_id** | **str** |  | [optional] 
**default_nominal_account_number** | **str** |  | [optional] 
**deposit_account_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_key** | [**TaxKey**](TaxKey.md) |  | [optional] 
**tax_type** | [**TaxType**](TaxType.md) |  | [optional] 
**tax_value** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.tax import Tax

# TODO update the JSON string below
json = "{}"
# create an instance of Tax from a JSON string
tax_instance = Tax.from_json(json)
# print the JSON string representation of the object
print(Tax.to_json())

# convert the object into a dict
tax_dict = tax_instance.to_dict()
# create an instance of Tax from a dict
tax_from_dict = Tax.from_dict(tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


