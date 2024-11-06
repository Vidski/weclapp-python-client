# IncomingBooking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**confirmed_by_user_id** | **str** |  | [optional] 
**confirmed_date** | **int** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**storage_place_id** | **str** |  | [optional] 
**article_valuation_price** | **decimal.Decimal** |  | [optional] 
**book_into_warehouse** | **bool** |  | [optional] 
**confirmed_by_user_id_deprecated** | **str** |  | [optional] 
**confirmed_date_deprecated** | **int** |  | [optional] 
**confirmed_quantity_deprecated** | **decimal.Decimal** |  | [optional] 
**expiration_date** | **int** |  | [optional] 
**incoming_goods_item_id** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.incoming_booking import IncomingBooking

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingBooking from a JSON string
incoming_booking_instance = IncomingBooking.from_json(json)
# print the JSON string representation of the object
print(IncomingBooking.to_json())

# convert the object into a dict
incoming_booking_dict = incoming_booking_instance.to_dict()
# create an instance of IncomingBooking from a dict
incoming_booking_from_dict = IncomingBooking.from_dict(incoming_booking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


