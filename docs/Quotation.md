# Quotation


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
**default_shipping_carrier_id** | **str** |  | [optional] 
**default_shipping_carrier_name** | **str** |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**delivery_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**planned_delivery_date** | **int** |  | [optional] 
**planned_shipping_date** | **int** |  | [optional] 
**record_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**sales_invoice_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**active_version** | **bool** |  | [optional] 
**invoice_recipient_id** | **str** |  | [optional] 
**opportunity_id** | **str** |  | [optional] 
**opportunity_number** | **str** |  | [optional] 
**public_link** | **str** |  | [optional] 
**quotation_date** | **int** |  | [optional] 
**quotation_items** | [**List[QuotationItem]**](QuotationItem.md) |  | [optional] 
**quotation_number** | **str** |  | [optional] 
**quotation_type** | [**OfferOutType**](OfferOutType.md) |  | [optional] 
**quotation_version** | **int** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**rejection_reason** | **str** |  | [optional] 
**request_date** | **int** |  | [optional] 
**sales_order_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**sales_probability** | **int** |  | [optional] 
**sales_stage_history** | [**List[SalesStageHistory]**](SalesStageHistory.md) |  | [optional] 
**sales_stage_id** | **str** |  | [optional] 
**sales_stage_name** | **str** |  | [optional] 
**status** | [**OfferStatusType**](OfferStatusType.md) |  | [optional] 
**status_history** | [**List[QuotationStatusHistory]**](QuotationStatusHistory.md) |  | [optional] 
**template** | **bool** |  | [optional] 
**valid_from** | **int** |  | [optional] 
**valid_to** | **int** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quotation import Quotation

# TODO update the JSON string below
json = "{}"
# create an instance of Quotation from a JSON string
quotation_instance = Quotation.from_json(json)
# print the JSON string representation of the object
print(Quotation.to_json())

# convert the object into a dict
quotation_dict = quotation_instance.to_dict()
# create an instance of Quotation from a dict
quotation_from_dict = Quotation.from_dict(quotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


