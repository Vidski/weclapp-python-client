# TransportationOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**destination_storage_place_id** | **str** |  | [optional] 
**internal_transport_reference_id** | **str** |  | [optional] 
**loading_equipment_article_id** | **str** |  | [optional] 
**loading_equipment_identifier_id** | **str** |  | [optional] 
**picks** | [**List[BasePickingBookRecord]**](BasePickingBookRecord.md) |  | [optional] 
**production_order_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**status** | [**TransportationOrderStatusType**](TransportationOrderStatusType.md) |  | [optional] 
**status_history** | [**List[TransportationOrderStatusHistory]**](TransportationOrderStatusHistory.md) |  | [optional] 
**transportation_order_number** | **str** |  | [optional] 
**transportation_order_type** | [**TransportationOrderType**](TransportationOrderType.md) |  | [optional] 

## Example

```python
from openapi_client.models.transportation_order import TransportationOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationOrder from a JSON string
transportation_order_instance = TransportationOrder.from_json(json)
# print the JSON string representation of the object
print(TransportationOrder.to_json())

# convert the object into a dict
transportation_order_dict = transportation_order_instance.to_dict()
# create an instance of TransportationOrder from a dict
transportation_order_from_dict = TransportationOrder.from_dict(transportation_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


