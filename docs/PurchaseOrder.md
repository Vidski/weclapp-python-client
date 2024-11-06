# PurchaseOrder


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
**currency_conversion_date** | **int** |  | [optional] 
**currency_conversion_rate** | **decimal.Decimal** |  | [optional] 
**gross_amount** | **decimal.Decimal** |  | [optional] 
**gross_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**header_discount** | **decimal.Decimal** |  | [optional] 
**header_surcharge** | **decimal.Decimal** |  | [optional] 
**net_amount** | **decimal.Decimal** |  | [optional] 
**net_amount_in_company_currency** | **decimal.Decimal** |  | [optional] 
**non_standard_tax_id** | **str** |  | [optional] 
**non_standard_tax_name** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**record_currency_id** | **str** |  | [optional] 
**record_currency_name** | **str** |  | [optional] 
**term_of_payment_id** | **str** |  | [optional] 
**term_of_payment_name** | **str** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**responsible_user_username** | **str** |  | [optional] 
**service_period_from** | **int** |  | [optional] 
**service_period_to** | **int** |  | [optional] 
**shipping_cost_items** | [**List[PurchaseShippingCostItem]**](PurchaseShippingCostItem.md) |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**supplier_number** | **str** |  | [optional] 
**advance_payment_status** | [**AdvancePaymentStatus**](AdvancePaymentStatus.md) |  | [optional] 
**commission** | **str** |  | [optional] 
**confirmation_number** | **str** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**external_purchase_order_number** | **str** |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**order_date** | **int** |  | [optional] 
**package_tracking_number** | **str** |  | [optional] 
**package_tracking_url** | **str** |  | [optional] 
**planned_delivery_date** | **int** |  | [optional] 
**planned_shipping_date** | **int** |  | [optional] 
**purchase_order_items** | [**List[PurchaseOrderItem]**](PurchaseOrderItem.md) |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**purchase_order_request_id** | **str** |  | [optional] 
**purchase_order_type** | [**SupplierOrderType**](SupplierOrderType.md) |  | [optional] 
**received** | **bool** |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**sales_order_id** | **str** |  | [optional] 
**sales_order_number** | **str** |  | [optional] 
**sender_country_code** | **str** |  | [optional] 
**shipment_method_id** | **str** |  | [optional] 
**shipment_method_name** | **str** |  | [optional] 
**shipping_carrier_id** | **str** |  | [optional] 
**status** | [**SupplierOrderStatusType**](SupplierOrderStatusType.md) |  | [optional] 
**status_history** | [**List[PurchaseOrderStatusHistory]**](PurchaseOrderStatusHistory.md) |  | [optional] 
**supplier_habitual_exporter_letter_of_intent_id** | **str** |  | [optional] 
**supplier_quotation_number** | **str** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_order import PurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrder from a JSON string
purchase_order_instance = PurchaseOrder.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrder.to_json())

# convert the object into a dict
purchase_order_dict = purchase_order_instance.to_dict()
# create an instance of PurchaseOrder from a dict
purchase_order_from_dict = PurchaseOrder.from_dict(purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


