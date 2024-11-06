# ShipmentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**article_id** | **str** |  | [optional] 
**article_number** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**position_number** | **int** |  | [optional] 
**quantity** | **decimal.Decimal** |  | [optional] 
**description** | **str** |  | [optional] 
**description_fixed** | **bool** |  | [optional] 
**manual_quantity** | **bool** |  | [optional] 
**parent_item_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**add_page_break_before** | **bool** |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**free_text_item** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**purchase_order_item_id** | **str** |  | [optional] 
**return_assessment_id** | **str** |  | [optional] 
**return_assessment_name** | **str** |  | [optional] 
**return_description** | **str** |  | [optional] 
**return_error_id** | **str** |  | [optional] 
**return_error_name** | **str** |  | [optional] 
**return_reason_id** | **str** |  | [optional] 
**return_reason_name** | **str** |  | [optional] 
**return_rectification_id** | **str** |  | [optional] 
**return_rectification_name** | **str** |  | [optional] 
**sales_order_item_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment_item import ShipmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItem from a JSON string
shipment_item_instance = ShipmentItem.from_json(json)
# print the JSON string representation of the object
print(ShipmentItem.to_json())

# convert the object into a dict
shipment_item_dict = shipment_item_instance.to_dict()
# create an instance of ShipmentItem from a dict
shipment_item_from_dict = ShipmentItem.from_dict(shipment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


