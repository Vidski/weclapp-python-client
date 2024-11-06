# ContractCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_fixed** | **bool** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**interval** | [**ContractChargeInterval**](ContractChargeInterval.md) |  | [optional] 
**interval_type** | [**ContractChargeIntervalType**](ContractChargeIntervalType.md) |  | [optional] 
**manual_unit_price** | **bool** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**note** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**service_period_from** | **int** |  | [optional] 
**service_period_to** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_price** | **decimal.Decimal** |  | [optional] 
**unit_price_in_company_currency** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.contract_cost_item import ContractCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCostItem from a JSON string
contract_cost_item_instance = ContractCostItem.from_json(json)
# print the JSON string representation of the object
print(ContractCostItem.to_json())

# convert the object into a dict
contract_cost_item_dict = contract_cost_item_instance.to_dict()
# create an instance of ContractCostItem from a dict
contract_cost_item_from_dict = ContractCostItem.from_dict(contract_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


