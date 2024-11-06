# SalesOrderStatusHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OrderStatusType**](OrderStatusType.md) |  | [optional] 
**status_date** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_status_history import SalesOrderStatusHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderStatusHistory from a JSON string
sales_order_status_history_instance = SalesOrderStatusHistory.from_json(json)
# print the JSON string representation of the object
print(SalesOrderStatusHistory.to_json())

# convert the object into a dict
sales_order_status_history_dict = sales_order_status_history_instance.to_dict()
# create an instance of SalesOrderStatusHistory from a dict
sales_order_status_history_from_dict = SalesOrderStatusHistory.from_dict(sales_order_status_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


