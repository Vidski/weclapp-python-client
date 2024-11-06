# SalesStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**probability** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.sales_stage import SalesStage

# TODO update the JSON string below
json = "{}"
# create an instance of SalesStage from a JSON string
sales_stage_instance = SalesStage.from_json(json)
# print the JSON string representation of the object
print(SalesStage.to_json())

# convert the object into a dict
sales_stage_dict = sales_stage_instance.to_dict()
# create an instance of SalesStage from a dict
sales_stage_from_dict = SalesStage.from_dict(sales_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


