# ProductionOrderGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ProductionOrder]**](ProductionOrder.md) |  | [optional] 

## Example

```python
from openapi_client.models.production_order_get200_response import ProductionOrderGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrderGet200Response from a JSON string
production_order_get200_response_instance = ProductionOrderGet200Response.from_json(json)
# print the JSON string representation of the object
print(ProductionOrderGet200Response.to_json())

# convert the object into a dict
production_order_get200_response_dict = production_order_get200_response_instance.to_dict()
# create an instance of ProductionOrderGet200Response from a dict
production_order_get200_response_from_dict = ProductionOrderGet200Response.from_dict(production_order_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


