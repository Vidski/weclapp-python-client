# ArticleSupplySource


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
**article_prices** | [**List[ArticlePriceWithoutSalesChannel]**](ArticlePriceWithoutSalesChannel.md) |  | [optional] 
**dropshipping_possible** | **bool** |  | [optional] 
**procurement_lead_days** | **int** |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**supplier_number** | **str** |  | [optional] 
**supplier_stock_quantity** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.article_supply_source import ArticleSupplySource

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleSupplySource from a JSON string
article_supply_source_instance = ArticleSupplySource.from_json(json)
# print the JSON string representation of the object
print(ArticleSupplySource.to_json())

# convert the object into a dict
article_supply_source_dict = article_supply_source_instance.to_dict()
# create an instance of ArticleSupplySource from a dict
article_supply_source_from_dict = ArticleSupplySource.from_dict(article_supply_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


