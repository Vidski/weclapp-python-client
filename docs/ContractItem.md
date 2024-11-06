# ContractItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**description** | **str** |  | [optional] 
**description_fixed** | **bool** |  | [optional] 
**manual_quantity** | **bool** |  | [optional] 
**parent_item_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**gross_amount** | **decimal.Decimal** |  | [optional] 
**gross_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**manual_unit_price** | **bool** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_for_statistics** | **decimal.Decimal** |  | [optional] 
**net_amount_for_statistics_in_company_currency** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**reduction_addition_items** | [**List[ReductionAdditionItem]**](ReductionAdditionItem.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_name** | **str** |  | [optional] 
**unit_price** | **decimal.Decimal** |  | [optional] 
**unit_price_in_company_currency** | **decimal.Decimal** |  | [optional] 
**add_page_break_before** | **bool** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**free_text_item** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**billing_group_id** | **str** |  | [optional] 
**commission_sales_partners** | [**List[CommissionSalesPartner]**](CommissionSalesPartner.md) |  | [optional] 
**cost_type_id** | **str** |  | [optional] 
**interval** | [**ContractChargeInterval**](ContractChargeInterval.md) |  | [optional] 
**interval_type** | [**ContractChargeIntervalType**](ContractChargeIntervalType.md) |  | [optional] 
**next_contract_billing_date** | **int** |  | [optional] 
**previous_contract_billing_date** | **int** |  | [optional] 
**service_period_from_date** | **int** |  | [optional] 
**service_period_to_date** | **int** |  | [optional] 
**type** | [**ContractChargeType**](ContractChargeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.contract_item import ContractItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContractItem from a JSON string
contract_item_instance = ContractItem.from_json(json)
# print the JSON string representation of the object
print(ContractItem.to_json())

# convert the object into a dict
contract_item_dict = contract_item_instance.to_dict()
# create an instance of ContractItem from a dict
contract_item_from_dict = ContractItem.from_dict(contract_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


