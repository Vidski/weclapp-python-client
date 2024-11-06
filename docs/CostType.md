# CostType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_type import CostType

# TODO update the JSON string below
json = "{}"
# create an instance of CostType from a JSON string
cost_type_instance = CostType.from_json(json)
# print the JSON string representation of the object
print(CostType.to_json())

# convert the object into a dict
cost_type_dict = cost_type_instance.to_dict()
# create an instance of CostType from a dict
cost_type_from_dict = CostType.from_dict(cost_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


