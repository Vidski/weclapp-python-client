# PriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_unit_price** | **decimal.Decimal** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**end_date** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**reduction_addition_items** | [**List[PriceDataReductionAdditionItem]**](PriceDataReductionAdditionItem.md) |  | [optional] 
**start_date** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.price_data import PriceData

# TODO update the JSON string below
json = "{}"
# create an instance of PriceData from a JSON string
price_data_instance = PriceData.from_json(json)
# print the JSON string representation of the object
print(PriceData.to_json())

# convert the object into a dict
price_data_dict = price_data_instance.to_dict()
# create an instance of PriceData from a dict
price_data_from_dict = PriceData.from_dict(price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


