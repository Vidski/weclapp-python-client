# SalesOrderPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**amount** | **decimal.Decimal** |  | [optional] 
**position_number** | **int** |  | [optional] 
**sales_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_payment import SalesOrderPayment

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderPayment from a JSON string
sales_order_payment_instance = SalesOrderPayment.from_json(json)
# print the JSON string representation of the object
print(SalesOrderPayment.to_json())

# convert the object into a dict
sales_order_payment_dict = sales_order_payment_instance.to_dict()
# create an instance of SalesOrderPayment from a dict
sales_order_payment_from_dict = SalesOrderPayment.from_dict(sales_order_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


