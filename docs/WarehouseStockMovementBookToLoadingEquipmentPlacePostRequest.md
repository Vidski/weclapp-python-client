# WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_attributes** | [**List[WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner]**](WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md) |  | [optional] 
**loading_equipment_article_id** | **str** |  | 
**movement_note** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | 
**source_internal_transport_reference_id** | **str** |  | [optional] 
**source_storage_place_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_to_loading_equipment_place_post_request import WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest from a JSON string
warehouse_stock_movement_book_to_loading_equipment_place_post_request_instance = WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest.to_json())

# convert the object into a dict
warehouse_stock_movement_book_to_loading_equipment_place_post_request_dict = warehouse_stock_movement_book_to_loading_equipment_place_post_request_instance.to_dict()
# create an instance of WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest from a dict
warehouse_stock_movement_book_to_loading_equipment_place_post_request_from_dict = WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest.from_dict(warehouse_stock_movement_book_to_loading_equipment_place_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


