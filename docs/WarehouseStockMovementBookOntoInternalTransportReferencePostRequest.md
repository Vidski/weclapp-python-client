# WarehouseStockMovementBookOntoInternalTransportReferencePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** |  | 
**base_article_quantity** | **decimal.Decimal** |  | 
**batch_number** | **str** |  | [optional] 
**book_from_loading_equipment_place** | **bool** |  | [optional] 
**book_loading_equipment_on_dissolve_of_preferred** | **bool** |  | [optional] 
**custom_attributes** | [**List[WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner]**](WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md) |  | [optional] 
**loading_equipment_article_id** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**movement_note** | **str** |  | [optional] 
**serial_numbers** | **List[str]** |  | [optional] 
**source_internal_transport_reference_id** | **str** |  | [optional] 
**source_storage_place_id** | **str** |  | [optional] 
**target_internal_transport_reference_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock_movement_book_onto_internal_transport_reference_post_request import WarehouseStockMovementBookOntoInternalTransportReferencePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStockMovementBookOntoInternalTransportReferencePostRequest from a JSON string
warehouse_stock_movement_book_onto_internal_transport_reference_post_request_instance = WarehouseStockMovementBookOntoInternalTransportReferencePostRequest.from_json(json)
# print the JSON string representation of the object
print(WarehouseStockMovementBookOntoInternalTransportReferencePostRequest.to_json())

# convert the object into a dict
warehouse_stock_movement_book_onto_internal_transport_reference_post_request_dict = warehouse_stock_movement_book_onto_internal_transport_reference_post_request_instance.to_dict()
# create an instance of WarehouseStockMovementBookOntoInternalTransportReferencePostRequest from a dict
warehouse_stock_movement_book_onto_internal_transport_reference_post_request_from_dict = WarehouseStockMovementBookOntoInternalTransportReferencePostRequest.from_dict(warehouse_stock_movement_book_onto_internal_transport_reference_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


