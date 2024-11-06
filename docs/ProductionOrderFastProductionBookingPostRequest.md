# ProductionOrderFastProductionBookingPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**production_order_number** | **str** |  | 
**quantity** | **decimal.Decimal** |  | 

## Example

```python
from openapi_client.models.production_order_fast_production_booking_post_request import ProductionOrderFastProductionBookingPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionOrderFastProductionBookingPostRequest from a JSON string
production_order_fast_production_booking_post_request_instance = ProductionOrderFastProductionBookingPostRequest.from_json(json)
# print the JSON string representation of the object
print(ProductionOrderFastProductionBookingPostRequest.to_json())

# convert the object into a dict
production_order_fast_production_booking_post_request_dict = production_order_fast_production_booking_post_request_instance.to_dict()
# create an instance of ProductionOrderFastProductionBookingPostRequest from a dict
production_order_fast_production_booking_post_request_from_dict = ProductionOrderFastProductionBookingPostRequest.from_dict(production_order_fast_production_booking_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


