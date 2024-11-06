# SalesOrderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**SalesOrderGet200ResponseAdditionalProperties**](SalesOrderGet200ResponseAdditionalProperties.md) |  | [optional] 
**result** | [**List[SalesOrder]**](SalesOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_get200_response import SalesOrderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderGet200Response from a JSON string
sales_order_get200_response_instance = SalesOrderGet200Response.from_json(json)
# print the JSON string representation of the object
print(SalesOrderGet200Response.to_json())

# convert the object into a dict
sales_order_get200_response_dict = sales_order_get200_response_instance.to_dict()
# create an instance of SalesOrderGet200Response from a dict
sales_order_get200_response_from_dict = SalesOrderGet200Response.from_dict(sales_order_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


