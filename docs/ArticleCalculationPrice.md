# ArticleCalculationPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_calculation_price_type** | [**ArticleCalculationPriceType**](ArticleCalculationPriceType.md) |  | [optional] 
**end_date** | **int** |  | [optional] 
**position_number** | **int** |  | [optional] 
**price** | **decimal.Decimal** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**start_date** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.article_calculation_price import ArticleCalculationPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleCalculationPrice from a JSON string
article_calculation_price_instance = ArticleCalculationPrice.from_json(json)
# print the JSON string representation of the object
print(ArticleCalculationPrice.to_json())

# convert the object into a dict
article_calculation_price_dict = article_calculation_price_instance.to_dict()
# create an instance of ArticleCalculationPrice from a dict
article_calculation_price_from_dict = ArticleCalculationPrice.from_dict(article_calculation_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


