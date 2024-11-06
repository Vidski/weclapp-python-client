# WarehouseStockMovementBookIncomingMovementPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** |  | 
**article_valuation_price** | **decimal.Decimal** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_number_expiration_date** | **int** |  | [optional] 
**custom_attributes** | [**List[WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner]**](WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md) |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**movement_note** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | 
**serial_numbers** | **List[str]** |  | [optional] 
**target_storage_place_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_incoming_movement_post_request import WarehouseStockMovementBookIncomingMovementPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookIncomingMovementPostRequest from a JSON string
warehouse_stock_movement_book_incoming_movement_post_request_instance = WarehouseStockMovementBookIncomingMovementPostRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookIncomingMovementPostRequest.to_json())

# convert the object into a dict
warehouse_stock_movement_book_incoming_movement_post_request_dict = warehouse_stock_movement_book_incoming_movement_post_request_instance.to_dict()
# create an instance of WarehouseStockMovementBookIncomingMovementPostRequest from a dict
warehouse_stock_movement_book_incoming_movement_post_request_from_dict = WarehouseStockMovementBookIncomingMovementPostRequest.from_dict(warehouse_stock_movement_book_incoming_movement_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


