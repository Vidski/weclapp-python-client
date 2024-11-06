# CostCenterWithDistributionPercentage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**cost_center_id** | **str** |  | [optional] 
**cost_center_number** | **str** |  | [optional] 
**distribution_percentage** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.cost_center_with_distribution_percentage import CostCenterWithDistributionPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of CostCenterWithDistributionPercentage from a JSON string
cost_center_with_distribution_percentage_instance = CostCenterWithDistributionPercentage.from_json(json)
# print the JSON string representation of the object
print(CostCenterWithDistributionPercentage.to_json())

# convert the object into a dict
cost_center_with_distribution_percentage_dict = cost_center_with_distribution_percentage_instance.to_dict()
# create an instance of CostCenterWithDistributionPercentage from a dict
cost_center_with_distribution_percentage_from_dict = CostCenterWithDistributionPercentage.from_dict(cost_center_with_distribution_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


