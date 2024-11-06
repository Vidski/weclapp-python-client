# PriceDataReductionAdditionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** |  | [optional] 
**source** | [**RecordItemReductionAdditionSource**](RecordItemReductionAdditionSource.md) |  | [optional] 
**special_price_reduction** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**RecordItemReductionAdditionType**](RecordItemReductionAdditionType.md) |  | [optional] 
**value** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.price_data_reduction_addition_item import PriceDataReductionAdditionItem

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDataReductionAdditionItem from a JSON string
price_data_reduction_addition_item_instance = PriceDataReductionAdditionItem.from_json(json)
# print the JSON string representation of the object
print(PriceDataReductionAdditionItem.to_json())

# convert the object into a dict
price_data_reduction_addition_item_dict = price_data_reduction_addition_item_instance.to_dict()
# create an instance of PriceDataReductionAdditionItem from a dict
price_data_reduction_addition_item_from_dict = PriceDataReductionAdditionItem.from_dict(price_data_reduction_addition_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


