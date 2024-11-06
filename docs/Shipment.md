# Shipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**commercial_language** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disable_email_template** | **bool** |  | [optional] 
**record_comment** | **str** |  | [optional] 
**record_free_text** | **str** |  | [optional] 
**record_opening** | **str** |  | [optional] 
**sent_to_recipient** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**recipient_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**sales_order_id** | **str** |  | [optional] 
**sales_order_number** | **str** |  | [optional] 
**sales_orders** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**status** | [**ShipmentStatusType**](ShipmentStatusType.md) |  | [optional] 
**status_history** | [**List[ShipmentStatus]**](ShipmentStatus.md) |  | [optional] 
**additional_delivery_information** | **str** |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**consolidation_storage_place_id** | **str** |  | [optional] 
**customer_purchase_order_number** | **str** |  | [optional] 
**declared_value_amount** | **decimal.Decimal** |  | [optional] 
**declared_value_amount_currency_id** | **str** |  | [optional] 
**declared_value_amount_currency_name** | **str** |  | [optional] 
**delivery_date** | **int** |  | [optional] 
**destination_storage_place_id** | **str** |  | [optional] 
**destination_warehouse_id** | **str** |  | [optional] 
**destination_warehouse_name** | **str** |  | [optional] 
**invoice_recipient_id** | **str** |  | [optional] 
**package_height** | **int** |  | [optional] 
**package_length** | **int** |  | [optional] 
**package_reference_number** | **str** |  | [optional] 
**package_return_tracking_number** | **str** |  | [optional] 
**package_return_tracking_url** | **str** |  | [optional] 
**package_tracking_number** | **str** |  | [optional] 
**package_tracking_url** | **str** |  | [optional] 
**package_weight** | **decimal.Decimal** |  | [optional] 
**package_width** | **int** |  | [optional] 
**picking_instructions** | **str** |  | [optional] 
**picks_complete** | **bool** |  | [optional] 
**purchase_orders** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**recipient_customer_number** | **str** |  | [optional] 
**recipient_party_id** | **str** |  | [optional] 
**recipient_supplier_number** | **str** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**sales_invoice_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**shipment_items** | [**List[ShipmentItem]**](ShipmentItem.md) |  | [optional] 
**shipment_method_id** | **str** |  | [optional] 
**shipment_method_name** | **str** |  | [optional] 
**shipment_number** | **str** |  | [optional] 
**shipment_type** | [**ShipmentOutType**](ShipmentOutType.md) |  | [optional] 
**shipped_from_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**shipping_carrier_id** | **str** |  | [optional] 
**shipping_carrier_name** | **str** |  | [optional] 
**shipping_date** | **int** |  | [optional] 
**shipping_labels_count** | **int** |  | [optional] 
**shipping_return_carrier_id** | **str** |  | [optional] 
**shipping_return_carrier_name** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.shipment import Shipment

# TODO update the JSON string below
json = "{}"
# create an instance of Shipment from a JSON string
shipment_instance = Shipment.from_json(json)
# print the JSON string representation of the object
print(Shipment.to_json())

# convert the object into a dict
shipment_dict = shipment_instance.to_dict()
# create an instance of Shipment from a dict
shipment_from_dict = Shipment.from_dict(shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


