# CostCenter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**cost_center_group_id** | **str** |  | [optional] 
**cost_center_number** | **str** |  | [optional] 
**cost_center_type** | [**ProductionCostCenterType**](ProductionCostCenterType.md) |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_center import CostCenter

# TODO update the JSON string below
json = "{}"
# create an instance of CostCenter from a JSON string
cost_center_instance = CostCenter.from_json(json)
# print the JSON string representation of the object
print(CostCenter.to_json())

# convert the object into a dict
cost_center_dict = cost_center_instance.to_dict()
# create an instance of CostCenter from a dict
cost_center_from_dict = CostCenter.from_dict(cost_center_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


