# Article


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**fixed_purchase_quantity** | **decimal.Decimal** |  | [optional] 
**internal_note** | **str** |  | [optional] 
**manufacturer_part_number** | **str** |  | [optional] 
**match_code** | **str** |  | [optional] 
**minimum_purchase_quantity** | **decimal.Decimal** |  | [optional] 
**name** | **str** |  | [optional] 
**short_description1** | **str** |  | [optional] 
**short_description2** | **str** |  | [optional] 
**tax_rate_type** | [**TaxRateType**](TaxRateType.md) |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**accounting_code_id** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**apply_cash_discount** | **bool** |  | [optional] 
**article_alternative_quantities** | [**List[ArticleAlternativeQuantity]**](ArticleAlternativeQuantity.md) |  | [optional] 
**article_calculation_prices** | [**List[ArticleCalculationPrice]**](ArticleCalculationPrice.md) |  | [optional] 
**article_category_id** | **str** |  | [optional] 
**article_gross_weight** | **decimal.Decimal** |  | [optional] 
**article_height** | **decimal.Decimal** |  | [optional] 
**article_images** | [**List[ArticleImage]**](ArticleImage.md) |  | [optional] 
**article_length** | **decimal.Decimal** |  | [optional] 
**article_net_weight** | **decimal.Decimal** |  | [optional] 
**article_prices** | [**List[ArticlePriceWithoutArticleReference]**](ArticlePriceWithoutArticleReference.md) |  | [optional] 
**article_type** | [**ArticleType**](ArticleType.md) |  | [optional] 
**article_width** | **decimal.Decimal** |  | [optional] 
**available_for_sales_channels** | [**List[DistributionChannel]**](DistributionChannel.md) |  | [optional] 
**available_in_sale** | **bool** |  | [optional] 
**average_delivery_time** | **int** |  | [optional] 
**barcode** | **str** |  | [optional] 
**batch_number_required** | **bool** |  | [optional] 
**bill_of_material_part_delivery_possible** | **bool** |  | [optional] 
**catalog_code** | **str** |  | [optional] 
**commission_rate** | **decimal.Decimal** |  | [optional] 
**contract_billing_cycle** | [**ContractChargeInterval**](ContractChargeInterval.md) |  | [optional] 
**contract_billing_mode** | [**ContractChargeIntervalType**](ContractChargeIntervalType.md) |  | [optional] 
**country_of_origin_code** | **str** |  | [optional] 
**customer_article_numbers** | [**List[CustomerSpecificArticleAttributes]**](CustomerSpecificArticleAttributes.md) |  | [optional] 
**customs_description** | **str** |  | [optional] 
**customs_tariff_number** | **str** |  | [optional] 
**customs_tariff_number_id** | **str** |  | [optional] 
**default_loading_equipment_identifier_id** | **str** |  | [optional] 
**default_price_calculation_type** | [**CalculationType**](CalculationType.md) |  | [optional] 
**default_storage_places** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**define_individual_task_templates** | **bool** |  | [optional] 
**expense_account_id** | **str** |  | [optional] 
**expense_account_number** | **str** |  | [optional] 
**expiration_days** | **int** |  | [optional] 
**invoicing_type** | [**InvoicingType**](InvoicingType.md) |  | [optional] 
**launch_date** | **int** |  | [optional] 
**loading_equipment_article_id** | **str** |  | [optional] 
**long_text** | **str** |  | [optional] 
**low_level_code** | **int** |  | [optional] 
**manufacturer_id** | **str** |  | [optional] 
**manufacturer_name** | **str** |  | [optional] 
**margin_calculation_price_type** | [**MarginCalculationPriceType**](MarginCalculationPriceType.md) |  | [optional] 
**minimum_stock_quantity** | **decimal.Decimal** |  | [optional] 
**packaging_quantity** | **int** |  | [optional] 
**packaging_unit_base_article_id** | **str** |  | [optional] 
**packaging_unit_parent_article_id** | **str** |  | [optional] 
**planned_working_time_per_unit** | **int** |  | [optional] 
**price_calculation_parameters** | [**List[PriceCalculationParameter]**](PriceCalculationParameter.md) |  | [optional] 
**primary_supply_source_id** | **str** |  | [optional] 
**procurement_lead_days** | **int** |  | [optional] 
**producer_type** | **str** |  | [optional] 
**production_article** | **bool** |  | [optional] 
**production_bill_of_material_items** | [**List[BillOfMaterial]**](BillOfMaterial.md) |  | [optional] 
**purchase_cost_center_id** | **str** |  | [optional] 
**purchase_cost_center_number** | **str** |  | [optional] 
**quantity_conversions** | [**List[QuantityConversion]**](QuantityConversion.md) |  | [optional] 
**rating_id** | **str** |  | [optional] 
**rating_name** | **str** |  | [optional] 
**record_item_group_name** | **str** |  | [optional] 
**safety_stock_days** | **int** |  | [optional] 
**sales_bill_of_material_items** | [**List[SalesBillOfMaterialArticleItem]**](SalesBillOfMaterialArticleItem.md) |  | [optional] 
**sales_cost_center_id** | **str** |  | [optional] 
**sales_cost_center_number** | **str** |  | [optional] 
**sell_by_date** | **int** |  | [optional] 
**sell_from_date** | **int** |  | [optional] 
**serial_number_required** | **bool** |  | [optional] 
**show_on_delivery_note** | **bool** |  | [optional] 
**status_id** | **str** |  | [optional] 
**supply_sources** | [**List[SupplySource]**](SupplySource.md) |  | [optional] 
**support_until_date** | **int** |  | [optional] 
**system_code** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**target_stock_quantity** | **decimal.Decimal** |  | [optional] 
**use_available_for_sales_channels** | **bool** |  | [optional] 
**use_sales_bill_of_material_item_prices** | **bool** |  | [optional] 
**use_sales_bill_of_material_item_prices_for_purchase** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.article import Article

# TODO update the JSON string below
json = "{}"
# create an instance of Article from a JSON string
article_instance = Article.from_json(json)
# print the JSON string representation of the object
print(Article.to_json())

# convert the object into a dict
article_dict = article_instance.to_dict()
# create an instance of Article from a dict
article_from_dict = Article.from_dict(article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


