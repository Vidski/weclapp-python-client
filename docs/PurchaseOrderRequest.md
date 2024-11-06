# PurchaseOrderRequest


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
**confirmation_deadline** | **int** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**planned_delivery_date** | **int** |  | [optional] 
**purchase_order_request_items** | [**List[PurchaseOrderRequestItem]**](PurchaseOrderRequestItem.md) |  | [optional] 
**purchase_order_request_number** | **str** |  | [optional] 
**purchase_order_request_offers** | [**List[PurchaseOrderRequestOffer]**](PurchaseOrderRequestOffer.md) |  | [optional] 
**purchase_order_request_type** | [**PurchaseOrderRequestType**](PurchaseOrderRequestType.md) |  | [optional] 
**quotation_id** | **str** |  | [optional] 
**quotation_number** | **str** |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**responsible_user_username** | **str** |  | [optional] 
**sales_order_id** | **str** |  | [optional] 
**sales_order_number** | **str** |  | [optional] 
**status** | [**PurchaseOrderRequestStatusType**](PurchaseOrderRequestStatusType.md) |  | [optional] 
**status_history** | [**List[PurchaseOrderRequestStatusHistory]**](PurchaseOrderRequestStatusHistory.md) |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order_request import PurchaseOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderRequest from a JSON string
purchase_order_request_instance = PurchaseOrderRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderRequest.to_json())

# convert the object into a dict
purchase_order_request_dict = purchase_order_request_instance.to_dict()
# create an instance of PurchaseOrderRequest from a dict
purchase_order_request_from_dict = PurchaseOrderRequest.from_dict(purchase_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


