# WarehouseStockMovement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_number_id** | **str** |  | [optional] 
**cost_center_id** | **str** |  | [optional] 
**incoming_goods_item_id** | **str** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**movement_note** | **str** |  | [optional] 
**movement_number** | **str** |  | [optional] 
**posting_date** | **int** |  | [optional] 
**production_order_id** | **str** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 
**serial_numbers** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**shipment_item_id** | **str** |  | [optional] 
**stock_movement_type** | [**StockMovementType**](StockMovementType.md) |  | [optional] 
**storage_place_id** | **str** |  | [optional] 
**transportation_order_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**valuation_price** | **decimal.Decimal** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement import WarehouseStockMovement

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovement from a JSON string
warehouse_stock_movement_instance = WarehouseStockMovement.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovement.to_json())

# convert the object into a dict
warehouse_stock_movement_dict = warehouse_stock_movement_instance.to_dict()
# create an instance of WarehouseStockMovement from a dict
warehouse_stock_movement_from_dict = WarehouseStockMovement.from_dict(warehouse_stock_movement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


