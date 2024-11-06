# WarehouseStockMovementBookDirectStockTransferPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** |  | 
**batch_number** | **str** |  | [optional] 
**custom_attributes** | [**List[WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner]**](WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md) |  | [optional] 
**destination_storage_place_id** | **str** |  | 
**internal_transport_reference_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | 
**serial_numbers** | **List[str]** |  | [optional] 
**source_storage_place_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_direct_stock_transfer_post_request import WarehouseStockMovementBookDirectStockTransferPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookDirectStockTransferPostRequest from a JSON string
warehouse_stock_movement_book_direct_stock_transfer_post_request_instance = WarehouseStockMovementBookDirectStockTransferPostRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookDirectStockTransferPostRequest.to_json())

# convert the object into a dict
warehouse_stock_movement_book_direct_stock_transfer_post_request_dict = warehouse_stock_movement_book_direct_stock_transfer_post_request_instance.to_dict()
# create an instance of WarehouseStockMovementBookDirectStockTransferPostRequest from a dict
warehouse_stock_movement_book_direct_stock_transfer_post_request_from_dict = WarehouseStockMovementBookDirectStockTransferPostRequest.from_dict(warehouse_stock_movement_book_direct_stock_transfer_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


