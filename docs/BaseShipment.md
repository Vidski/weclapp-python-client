# BaseShipment


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

## Example

```python
from openapi_client.models.base_shipment import BaseShipment

# TODO update the JSON string below
json = "{}"
# create an instance of BaseShipment from a JSON string
base_shipment_instance = BaseShipment.from_json(json)
# print the JSON string representation of the object
print(BaseShipment.to_json())

# convert the object into a dict
base_shipment_dict = base_shipment_instance.to_dict()
# create an instance of BaseShipment from a dict
base_shipment_from_dict = BaseShipment.from_dict(base_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


