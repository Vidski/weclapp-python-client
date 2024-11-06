# TransportationOrderStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransportationOrderStatusType**](TransportationOrderStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order_status_history import TransportationOrderStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderStatusHistory from a JSON string
transportation_order_status_history_instance = TransportationOrderStatusHistory.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderStatusHistory.to_json())

# convert the object into a dict
transportation_order_status_history_dict = transportation_order_status_history_instance.to_dict()
# create an instance of TransportationOrderStatusHistory from a dict
transportation_order_status_history_from_dict = TransportationOrderStatusHistory.from_dict(transportation_order_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


