# Warehouse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**default_consolidation_storage_place_id** | **str** |  | [optional] 
**default_production_storage_place_id** | **str** |  | [optional] 
**default_returns_storage_place_id** | **str** |  | [optional] 
**default_storage_place_id** | **str** |  | [optional] 
**direct_booking_internal_transport_reference_id** | **str** |  | [optional] 
**loading_equipment_storage_place** | [**MinimalStoragePlace**](MinimalStoragePlace.md) |  | [optional] 
**name** | **str** |  | [optional] 
**short_identifier** | **str** |  | [optional] 
**standard** | **bool** |  | [optional] 
**transit_storage_place** | [**MinimalStoragePlace**](MinimalStoragePlace.md) |  | [optional] 
**warehouse_type** | [**StoreType**](StoreType.md) |  | [optional] 

## Example

```python
from openapi_client.models.warehouse import Warehouse

# TODO update the JSON string below
json = "{}"
# create an instance of Warehouse from a JSON string
warehouse_instance = Warehouse.from_json(json)
# print the JSON string representation of the object
print(Warehouse.to_json())

# convert the object into a dict
warehouse_dict = warehouse_instance.to_dict()
# create an instance of Warehouse from a dict
warehouse_from_dict = Warehouse.from_dict(warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


