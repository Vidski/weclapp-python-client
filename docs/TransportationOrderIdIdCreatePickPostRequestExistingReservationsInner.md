# TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pick_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order_id_id_create_pick_post_request_existing_reservations_inner import TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner from a JSON string
transportation_order_id_id_create_pick_post_request_existing_reservations_inner_instance = TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner.to_json())

# convert the object into a dict
transportation_order_id_id_create_pick_post_request_existing_reservations_inner_dict = transportation_order_id_id_create_pick_post_request_existing_reservations_inner_instance.to_dict()
# create an instance of TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner from a dict
transportation_order_id_id_create_pick_post_request_existing_reservations_inner_from_dict = TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner.from_dict(transportation_order_id_id_create_pick_post_request_existing_reservations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


