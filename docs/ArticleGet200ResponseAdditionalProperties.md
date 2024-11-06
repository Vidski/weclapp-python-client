# ArticleGet200ResponseAdditionalProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_price** | [**List[Amount]**](Amount.md) |  | [optional] 
**current_sales_price** | [**List[PriceData]**](PriceData.md) |  | [optional] 
**pickable_stock_quantity** | **List[List[WarehouseQuantity]]** |  | [optional] 
**reserved_stock_quantity** | **List[List[WarehouseQuantity]]** |  | [optional] 
**total_stock_quantity** | **List[List[WarehouseQuantity]]** |  | [optional] 

## Example

```python
from openapi_client.models.article_get200_response_additional_properties import ArticleGet200ResponseAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ArticleGet200ResponseAdditionalProperties from a JSON string
article_get200_response_additional_properties_instance = ArticleGet200ResponseAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(ArticleGet200ResponseAdditionalProperties.to_json())

# convert the object into a dict
article_get200_response_additional_properties_dict = article_get200_response_additional_properties_instance.to_dict()
# create an instance of ArticleGet200ResponseAdditionalProperties from a dict
article_get200_response_additional_properties_from_dict = ArticleGet200ResponseAdditionalProperties.from_dict(article_get200_response_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


