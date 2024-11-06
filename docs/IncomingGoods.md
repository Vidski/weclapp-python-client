# IncomingGoods


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
**customer_delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**customer_invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**delivery_note_number** | **str** |  | [optional] 
**incoming_goods_items** | [**List[IncomingGoodsItem]**](IncomingGoodsItem.md) |  | [optional] 
**incoming_goods_number** | **str** |  | [optional] 
**incoming_goods_type** | [**ShipmentInType**](ShipmentInType.md) |  | [optional] 
**invoice_recipient_id** | **str** |  | [optional] 
**purchase_order_id** | **str** |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**purchase_orders** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**related_shipment_id** | **str** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**return_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**sender_customer_number** | **str** |  | [optional] 
**sender_party_id** | **str** |  | [optional] 
**sender_supplier_number** | **str** |  | [optional] 
**source_warehouse_id** | **str** |  | [optional] 
**source_warehouse_name** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.incoming_goods import IncomingGoods

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingGoods from a JSON string
incoming_goods_instance = IncomingGoods.from_json(json)
# print the JSON string representation of the object
print(IncomingGoods.to_json())

# convert the object into a dict
incoming_goods_dict = incoming_goods_instance.to_dict()
# create an instance of IncomingGoods from a dict
incoming_goods_from_dict = IncomingGoods.from_dict(incoming_goods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


