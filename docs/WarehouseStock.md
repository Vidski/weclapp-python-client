# WarehouseStock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_number_id** | **str** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**packaging_units** | [**List[PackagingUnit]**](PackagingUnit.md) |  | [optional] 
**picks** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 
**serial_numbers** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**storage_place_id** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.warehouse_stock import WarehouseStock

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseStock from a JSON string
warehouse_stock_instance = WarehouseStock.from_json(json)
# print the JSON string representation of the object
print(WarehouseStock.to_json())

# convert the object into a dict
warehouse_stock_dict = warehouse_stock_instance.to_dict()
# create an instance of WarehouseStock from a dict
warehouse_stock_from_dict = WarehouseStock.from_dict(warehouse_stock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


