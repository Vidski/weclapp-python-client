# WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_definition_id** | **str** |  | [optional] 
**boolean_value** | **bool** |  | [optional] 
**date_value** | **int** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**entity_references** | [**List[EntityReference]**](EntityReference.md) |  | [optional] 
**number_value** | **decimal.Decimal** |  | [optional] 
**selected_value_id** | **str** |  | [optional] 
**selected_values** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**string_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner import WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner from a JSON string
warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner_instance = WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.to_json())

# convert the object into a dict
warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner_dict = warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner_instance.to_dict()
# create an instance of WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner from a dict
warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner_from_dict = WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.from_dict(warehouse_stock_movement_book_direct_stock_transfer_post_request_custom_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


