# SalesStageHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**sales_stage_id** | **str** |  | [optional] 
**sales_stage_name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_stage_history import SalesStageHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SalesStageHistory from a JSON string
sales_stage_history_instance = SalesStageHistory.from_json(json)
# print the JSON string representation of the object
print(SalesStageHistory.to_json())

# convert the object into a dict
sales_stage_history_dict = sales_stage_history_instance.to_dict()
# create an instance of SalesStageHistory from a dict
sales_stage_history_from_dict = SalesStageHistory.from_dict(sales_stage_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


