# IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_valuation_price** | **decimal.Decimal** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**book_into_warehouse** | **bool** |  | [optional] 
**confirmed_by_user_id** | **str** |  | [optional] 
**confirmed_by_user_id_deprecated** | **str** |  | [optional] 
**confirmed_date** | **int** |  | [optional] 
**confirmed_date_deprecated** | **int** |  | [optional] 
**confirmed_quantity_deprecated** | **decimal.Decimal** |  | [optional] 
**created_date** | **int** |  | [optional] 
**expiration_date** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**incoming_goods_item_id** | **str** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**last_modified_date** | **int** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**storage_place_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner import IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner from a JSON string
incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner_instance = IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner.from_json(json)
# print the JSON string representation of the object
print(IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner.to_json())

# convert the object into a dict
incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner_dict = incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner_instance.to_dict()
# create an instance of IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner from a dict
incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner_from_dict = IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner.from_dict(incoming_goods_id_id_update_incoming_bookings_post_request_incoming_bookings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


