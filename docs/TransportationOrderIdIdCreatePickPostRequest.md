# TransportationOrderIdIdCreatePickPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_number** | **str** |  | [optional] 
**existing_reservations** | [**List[TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner]**](TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner.md) |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**order_item_id** | **str** |  | [optional] 
**packaging_unit_base_article_id** | **str** |  | 
**quantity** | **decimal.Decimal** |  | 
**serial_numbers** | **List[str]** |  | [optional] 
**storage_place_id** | **str** |  | 

## Example

```python
from openapi_client.models.transportation_order_id_id_create_pick_post_request import TransportationOrderIdIdCreatePickPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrderIdIdCreatePickPostRequest from a JSON string
transportation_order_id_id_create_pick_post_request_instance = TransportationOrderIdIdCreatePickPostRequest.from_json(json)
# print the JSON string representation of the object
print(TransportationOrderIdIdCreatePickPostRequest.to_json())

# convert the object into a dict
transportation_order_id_id_create_pick_post_request_dict = transportation_order_id_id_create_pick_post_request_instance.to_dict()
# create an instance of TransportationOrderIdIdCreatePickPostRequest from a dict
transportation_order_id_id_create_pick_post_request_from_dict = TransportationOrderIdIdCreatePickPostRequest.from_dict(transportation_order_id_id_create_pick_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


