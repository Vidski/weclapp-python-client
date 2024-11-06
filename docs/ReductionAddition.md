# ReductionAddition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**PriceConditionType**](PriceConditionType.md) |  | [optional] 
**value** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.reduction_addition import ReductionAddition

# TODO update the JSON string below
json = "{}"
# create an instance of ReductionAddition from a JSON string
reduction_addition_instance = ReductionAddition.from_json(json)
# print the JSON string representation of the object
print(ReductionAddition.to_json())

# convert the object into a dict
reduction_addition_dict = reduction_addition_instance.to_dict()
# create an instance of ReductionAddition from a dict
reduction_addition_from_dict = ReductionAddition.from_dict(reduction_addition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


