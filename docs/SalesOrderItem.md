# SalesOrderItem


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
**invoicing_type** | [**InvoicingType**](InvoicingType.md) |  | [optional] 
**manual_planned_working_time_per_unit** | **bool** |  | [optional] 
**planned_working_time_per_unit** | **int** |  | [optional] 
**service_item** | **bool** |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**ecommerce_order_item_id** | **str** |  | [optional] 
**invoiced_quantity** | **decimal.Decimal** |  | [optional] 
**pick_batch_number** | **str** |  | [optional] 
**pick_serial_numbers** | **List[str]** |  | [optional] 
**pick_storage_place_id** | **str** |  | [optional] 
**planned_shipping_date** | **int** |  | [optional] 
**returned_quantity** | **decimal.Decimal** |  | [optional] 
**shipped** | **bool** |  | [optional] 
**shipped_quantity** | **decimal.Decimal** |  | [optional] 
**tasks** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_item import SalesOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderItem from a JSON string
sales_order_item_instance = SalesOrderItem.from_json(json)
# print the JSON string representation of the object
print(SalesOrderItem.to_json())

# convert the object into a dict
sales_order_item_dict = sales_order_item_instance.to_dict()
# create an instance of SalesOrderItem from a dict
sales_order_item_from_dict = SalesOrderItem.from_dict(sales_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


