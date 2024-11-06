# ReductionAdditionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** |  | [optional] 
**source** | [**RecordItemReductionAdditionSource**](RecordItemReductionAdditionSource.md) |  | [optional] 
**type** | [**RecordItemReductionAdditionType**](RecordItemReductionAdditionType.md) |  | [optional] 
**value** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.reduction_addition_item import ReductionAdditionItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReductionAdditionItem from a JSON string
reduction_addition_item_instance = ReductionAdditionItem.from_json(json)
# print the JSON string representation of the object
print(ReductionAdditionItem.to_json())

# convert the object into a dict
reduction_addition_item_dict = reduction_addition_item_instance.to_dict()
# create an instance of ReductionAdditionItem from a dict
reduction_addition_item_from_dict = ReductionAdditionItem.from_dict(reduction_addition_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


