# ArticlePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**last_modified_by_user_id** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**price** | **decimal.Decimal** |  | [optional] 
**price_scale_type** | [**PriceScaleType**](PriceScaleType.md) |  | [optional] 
**price_scale_value** | **decimal.Decimal** |  | [optional] 
**reduction_additions** | [**List[ReductionAddition]**](ReductionAddition.md) |  | [optional] 
**start_date** | **int** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.article_price import ArticlePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ArticlePrice from a JSON string
article_price_instance = ArticlePrice.from_json(json)
# print the JSON string representation of the object
print(ArticlePrice.to_json())

# convert the object into a dict
article_price_dict = article_price_instance.to_dict()
# create an instance of ArticlePrice from a dict
article_price_from_dict = ArticlePrice.from_dict(article_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


