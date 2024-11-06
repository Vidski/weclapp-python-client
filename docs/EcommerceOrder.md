# EcommerceOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecommerce_id** | **str** |  | [optional] 
**external_connection_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ecommerce_order import EcommerceOrder

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceOrder from a JSON string
ecommerce_order_instance = EcommerceOrder.from_json(json)
# print the JSON string representation of the object
print(EcommerceOrder.to_json())

# convert the object into a dict
ecommerce_order_dict = ecommerce_order_instance.to_dict()
# create an instance of EcommerceOrder from a dict
ecommerce_order_from_dict = EcommerceOrder.from_dict(ecommerce_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


