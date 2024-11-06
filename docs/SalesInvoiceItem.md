# SalesInvoiceItem


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
**commission_sales_partners** | [**List[CommissionSalesPartner]**](CommissionSalesPartner.md) |  | [optional] 
**manual_unit_cost** | **bool** |  | [optional] 
**service_period_from** | **int** |  | [optional] 
**service_period_to** | **int** |  | [optional] 
**unit_cost** | **decimal.Decimal** |  | [optional] 
**unit_cost_in_company_currency** | **decimal.Decimal** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**contract_item_id** | **str** |  | [optional] 
**cost_center_items** | [**List[CostCenterWithDistributionPercentage]**](CostCenterWithDistributionPercentage.md) |  | [optional] 
**credited_invoice_item_id** | **str** |  | [optional] 
**delivery_date** | **int** |  | [optional] 
**sales_invoice_item_relationship** | [**List[SalesInvoiceItemRelationship]**](SalesInvoiceItemRelationship.md) |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**shipping_date** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.sales_invoice_item import SalesInvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesInvoiceItem from a JSON string
sales_invoice_item_instance = SalesInvoiceItem.from_json(json)
# print the JSON string representation of the object
print(SalesInvoiceItem.to_json())

# convert the object into a dict
sales_invoice_item_dict = sales_invoice_item_instance.to_dict()
# create an instance of SalesInvoiceItem from a dict
sales_invoice_item_from_dict = SalesInvoiceItem.from_dict(sales_invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


