# SalesOrderGet200ResponseAdditionalProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booked_billable_work** | [**List[Duration]**](Duration.md) |  | [optional] 
**booked_work** | [**List[Duration]**](Duration.md) |  | [optional] 
**cost_of_services** | [**List[Amount]**](Amount.md) |  | [optional] 
**invoiceable_services** | [**List[Amount]**](Amount.md) |  | [optional] 
**invoiced_services** | [**List[Amount]**](Amount.md) |  | [optional] 
**not_invoiced_services** | [**List[Amount]**](Amount.md) |  | [optional] 
**planned_billable_effort** | [**List[Duration]**](Duration.md) |  | [optional] 
**planned_effort** | [**List[Duration]**](Duration.md) |  | [optional] 

## Example

```python
from openapi_client.models.sales_order_get200_response_additional_properties import SalesOrderGet200ResponseAdditionalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrderGet200ResponseAdditionalProperties from a JSON string
sales_order_get200_response_additional_properties_instance = SalesOrderGet200ResponseAdditionalProperties.from_json(json)
# print the JSON string representation of the object
print(SalesOrderGet200ResponseAdditionalProperties.to_json())

# convert the object into a dict
sales_order_get200_response_additional_properties_dict = sales_order_get200_response_additional_properties_instance.to_dict()
# create an instance of SalesOrderGet200ResponseAdditionalProperties from a dict
sales_order_get200_response_additional_properties_from_dict = SalesOrderGet200ResponseAdditionalProperties.from_dict(sales_order_get200_response_additional_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


