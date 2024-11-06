# SalesInvoice


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
**commission** | **str** |  | [optional] 
**commission_sales_partners** | [**List[CommissionSalesPartner]**](CommissionSalesPartner.md) |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_number** | **str** |  | [optional] 
**dispatch_country_code** | **str** |  | [optional] 
**factoring** | **bool** |  | [optional] 
**pricing_date** | **int** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**responsible_user_username** | **str** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**service_period_from** | **int** |  | [optional] 
**service_period_to** | **int** |  | [optional] 
**shipment_method_id** | **str** |  | [optional] 
**shipment_method_name** | **str** |  | [optional] 
**shipping_cost_items** | [**List[SalesShippingCostItem]**](SalesShippingCostItem.md) |  | [optional] 
**booking_date** | **int** |  | [optional] 
**booking_text** | **str** |  | [optional] 
**cancellation_date** | **int** |  | [optional] 
**cancellation_number** | **str** |  | [optional] 
**collective_invoice_position_print_type** | [**CollectiveInvoicePositionPrintType**](CollectiveInvoicePositionPrintType.md) |  | [optional] 
**commission_block** | **bool** |  | [optional] 
**credit_resets_order_state** | **bool** |  | [optional] 
**customer_habitual_exporter_letter_of_intent_id** | **str** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**delivery_date** | **int** |  | [optional] 
**direct_debit_file_created** | **bool** |  | [optional] 
**direct_debit_file_latest_date** | **int** |  | [optional] 
**due_date** | **int** |  | [optional] 
**dunning_block_date_until_date** | **int** |  | [optional] 
**dunning_block_note** | **str** |  | [optional] 
**dunning_block_state** | [**DunningBlockState**](DunningBlockState.md) |  | [optional] 
**invoice_date** | **int** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**order_number_at_customer** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**payment_status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**preceding_sales_invoice_id** | **str** |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**sales_invoice_items** | [**List[SalesInvoiceItem]**](SalesInvoiceItem.md) |  | [optional] 
**sales_invoice_type** | [**SalesInvoiceType**](SalesInvoiceType.md) |  | [optional] 
**sales_order_id** | **str** |  | [optional] 
**sales_order_number** | **str** |  | [optional] 
**sales_orders** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**sepa_direct_debit_mandate_id** | **str** |  | [optional] 
**shipping_date** | **int** |  | [optional] 
**status** | [**SalesInvoiceStatusType**](SalesInvoiceStatusType.md) |  | [optional] 
**status_history** | [**List[SalesInvoiceStatusHistory]**](SalesInvoiceStatusHistory.md) |  | [optional] 
**vat_registration_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_invoice import SalesInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of SalesInvoice from a JSON string
sales_invoice_instance = SalesInvoice.from_json(json)
# print the JSON string representation of the object
print(SalesInvoice.to_json())

# convert the object into a dict
sales_invoice_dict = sales_invoice_instance.to_dict()
# create an instance of SalesInvoice from a dict
sales_invoice_from_dict = SalesInvoice.from_dict(sales_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


