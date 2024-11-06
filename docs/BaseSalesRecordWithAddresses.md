# BaseSalesRecordWithAddresses


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

## Example

```python
from openapi_client.models.base_sales_record_with_addresses import BaseSalesRecordWithAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of BaseSalesRecordWithAddresses from a JSON string
base_sales_record_with_addresses_instance = BaseSalesRecordWithAddresses.from_json(json)
# print the JSON string representation of the object
print(BaseSalesRecordWithAddresses.to_json())

# convert the object into a dict
base_sales_record_with_addresses_dict = base_sales_record_with_addresses_instance.to_dict()
# create an instance of BaseSalesRecordWithAddresses from a dict
base_sales_record_with_addresses_from_dict = BaseSalesRecordWithAddresses.from_dict(base_sales_record_with_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


