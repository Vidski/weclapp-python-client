# SalesOrderIdIdCreatePurchaseOrderPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_purchase_orders** | **bool** |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_id_id_create_purchase_order_post_request import SalesOrderIdIdCreatePurchaseOrderPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderIdIdCreatePurchaseOrderPostRequest from a JSON string
sales_order_id_id_create_purchase_order_post_request_instance = SalesOrderIdIdCreatePurchaseOrderPostRequest.from_json(json)
# print the JSON string representation of the object
print(SalesOrderIdIdCreatePurchaseOrderPostRequest.to_json())

# convert the object into a dict
sales_order_id_id_create_purchase_order_post_request_dict = sales_order_id_id_create_purchase_order_post_request_instance.to_dict()
# create an instance of SalesOrderIdIdCreatePurchaseOrderPostRequest from a dict
sales_order_id_id_create_purchase_order_post_request_from_dict = SalesOrderIdIdCreatePurchaseOrderPostRequest.from_dict(sales_order_id_id_create_purchase_order_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


