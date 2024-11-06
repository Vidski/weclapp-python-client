# BlanketPurchaseOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**article_id** | **str** |  | [optional] 
**blanket_purchase_order_number** | **str** |  | [optional] 
**calculation_mode** | [**SpecialCalculationMode**](SpecialCalculationMode.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**commercial_language** | **str** |  | [optional] 
**confirmation_number** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**description** | **str** |  | [optional] 
**discount_percentage** | **decimal.Decimal** |  | [optional] 
**end_date** | **int** |  | [optional] 
**form_settings_from_distribution_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**header_discount** | **decimal.Decimal** |  | [optional] 
**header_surcharge** | **decimal.Decimal** |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**non_standard_tax_id** | **str** |  | [optional] 
**order_date** | **int** |  | [optional] 
**order_quantity** | **decimal.Decimal** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**recipient_country_code** | **str** |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**record_comment** | **str** |  | [optional] 
**record_currency_id** | **str** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**record_free_text** | **str** |  | [optional] 
**record_opening** | **str** |  | [optional] 
**releases** | [**List[Releases]**](Releases.md) |  | [optional] 
**residual_quantity** | **decimal.Decimal** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**sender_country_code** | **str** |  | [optional] 
**sent_to_recipient** | **bool** |  | [optional] 
**shipment_method_id** | **str** |  | [optional] 
**start_date** | **int** |  | [optional] 
**status** | [**BlanketPurchaseOrderStatusType**](BlanketPurchaseOrderStatusType.md) |  | [optional] 
**status_history** | [**List[BlanketPurchaseOrderStatusHistory]**](BlanketPurchaseOrderStatusHistory.md) |  | [optional] 
**supplier_blanket_purchase_order_number** | **str** |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**supplier_quotation_number** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**term_of_payment_id** | **str** |  | [optional] 
**unit_price** | **decimal.Decimal** |  | [optional] 
**use_manual_unit_price** | **bool** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blanket_purchase_order import BlanketPurchaseOrder

# TODO update the JSON string below
json = "{}"
# create an instance of BlanketPurchaseOrder from a JSON string
blanket_purchase_order_instance = BlanketPurchaseOrder.from_json(json)
# print the JSON string representation of the object
print(BlanketPurchaseOrder.to_json())

# convert the object into a dict
blanket_purchase_order_dict = blanket_purchase_order_instance.to_dict()
# create an instance of BlanketPurchaseOrder from a dict
blanket_purchase_order_from_dict = BlanketPurchaseOrder.from_dict(blanket_purchase_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


