# FinancialYear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**periods** | [**List[Period]**](Period.md) |  | [optional] 
**status** | [**FinancialYearStatus**](FinancialYearStatus.md) |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.financial_year import FinancialYear

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialYear from a JSON string
financial_year_instance = FinancialYear.from_json(json)
# print the JSON string representation of the object
print(FinancialYear.to_json())

# convert the object into a dict
financial_year_dict = financial_year_instance.to_dict()
# create an instance of FinancialYear from a dict
financial_year_from_dict = FinancialYear.from_dict(financial_year_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


