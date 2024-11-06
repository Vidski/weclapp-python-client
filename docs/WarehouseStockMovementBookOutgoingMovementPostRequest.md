# WarehouseStockMovementBookOutgoingMovementPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**cost_center_id** | **str** |  | [optional] 
**custom_attributes** | [**List[WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner]**](WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md) |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**movement_note** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**source_storage_place_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_outgoing_movement_post_request import WarehouseStockMovementBookOutgoingMovementPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookOutgoingMovementPostRequest from a JSON string
warehouse_stock_movement_book_outgoing_movement_post_request_instance = WarehouseStockMovementBookOutgoingMovementPostRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookOutgoingMovementPostRequest.to_json())

# convert the object into a dict
warehouse_stock_movement_book_outgoing_movement_post_request_dict = warehouse_stock_movement_book_outgoing_movement_post_request_instance.to_dict()
# create an instance of WarehouseStockMovementBookOutgoingMovementPostRequest from a dict
warehouse_stock_movement_book_outgoing_movement_post_request_from_dict = WarehouseStockMovementBookOutgoingMovementPostRequest.from_dict(warehouse_stock_movement_book_outgoing_movement_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


