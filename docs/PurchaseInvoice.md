# PurchaseInvoice


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
**booking_date** | **int** |  | [optional] 
**booking_text** | **str** |  | [optional] 
**cost_center_id** | **str** |  | [optional] 
**cost_center_number** | **str** |  | [optional] 
**credit_resets_order_state** | **bool** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**due_date** | **int** |  | [optional] 
**gross_prices** | **bool** |  | [optional] 
**import_sales_tax_amount** | **decimal.Decimal** |  | [optional] 
**import_sales_tax_id** | **str** |  | [optional] 
**internal_invoice_number** | **str** |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**invoice_date** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**preceding_purchase_invoice_id** | **str** |  | [optional] 
**pricing_date** | **int** |  | [optional] 
**purchase_invoice_items** | [**List[PurchaseInvoiceItem]**](PurchaseInvoiceItem.md) |  | [optional] 
**purchase_invoice_type** | [**PurchaseInvoiceType**](PurchaseInvoiceType.md) |  | [optional] 
**purchase_orders** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**sender_country_code** | **str** |  | [optional] 
**status** | [**PurchaseInvoiceStatusType**](PurchaseInvoiceStatusType.md) |  | [optional] 
**status_history** | [**List[PurchaseInvoiceStatusHistory]**](PurchaseInvoiceStatusHistory.md) |  | [optional] 
**supplier_habitual_exporter_letter_of_intent_id** | **str** |  | [optional] 
**vat_registration_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.purchase_invoice import PurchaseInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInvoice from a JSON string
purchase_invoice_instance = PurchaseInvoice.from_json(json)
# print the JSON string representation of the object
print(PurchaseInvoice.to_json())

# convert the object into a dict
purchase_invoice_dict = purchase_invoice_instance.to_dict()
# create an instance of PurchaseInvoice from a dict
purchase_invoice_from_dict = PurchaseInvoice.from_dict(purchase_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


