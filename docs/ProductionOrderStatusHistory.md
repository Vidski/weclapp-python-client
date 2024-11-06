# ProductionOrderStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ProductionOrderStatusType**](ProductionOrderStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.production_order_status_history import ProductionOrderStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrderStatusHistory from a JSON string
production_order_status_history_instance = ProductionOrderStatusHistory.from_json(json)
# print the JSON string representation of the object
print(ProductionOrderStatusHistory.to_json())

# convert the object into a dict
production_order_status_history_dict = production_order_status_history_instance.to_dict()
# create an instance of ProductionOrderStatusHistory from a dict
production_order_status_history_from_dict = ProductionOrderStatusHistory.from_dict(production_order_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


