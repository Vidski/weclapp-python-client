# SalesOrder


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
**advance_payment_amount** | **decimal.Decimal** |  | [optional] 
**advance_payment_status** | [**AdvancePaymentStatus**](AdvancePaymentStatus.md) |  | [optional] 
**availability** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**availability_for_all_warehouses** | [**DispositionInfoAvailabilityType**](DispositionInfoAvailabilityType.md) |  | [optional] 
**cash_account_id** | **str** |  | [optional] 
**customer_habitual_exporter_letter_of_intent_id** | **str** |  | [optional] 
**default_shipping_return_carrier_id** | **str** |  | [optional] 
**default_shipping_return_carrier_name** | **str** |  | [optional] 
**ecommerce_order** | [**EcommerceOrder**](EcommerceOrder.md) |  | [optional] 
**fulfillment_provider_id** | **str** |  | [optional] 
**invoice_recipient_id** | **str** |  | [optional] 
**invoiced** | **bool** |  | [optional] 
**only_services** | **bool** |  | [optional] 
**order_date** | **int** |  | [optional] 
**order_items** | [**List[SalesOrderItem]**](SalesOrderItem.md) |  | [optional] 
**order_number** | **str** |  | [optional] 
**order_number_at_customer** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**payments** | [**List[SalesOrderPayment]**](SalesOrderPayment.md) |  | [optional] 
**planned_project_end_date** | **int** |  | [optional] 
**planned_project_start_date** | **int** |  | [optional] 
**project_goals** | **str** |  | [optional] 
**project_members** | [**List[ProjectMembers]**](ProjectMembers.md) |  | [optional] 
**project_mode_active** | **bool** |  | [optional] 
**quotation_id** | **str** |  | [optional] 
**quotation_number** | **str** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**sales_order_payment_type** | [**SalesOrderPaymentType**](SalesOrderPaymentType.md) |  | [optional] 
**services_finished** | **bool** |  | [optional] 
**shipped** | **bool** |  | [optional] 
**shipping_labels_count** | **int** |  | [optional] 
**status** | [**OrderStatusType**](OrderStatusType.md) |  | [optional] 
**status_history** | [**List[SalesOrderStatusHistory]**](SalesOrderStatusHistory.md) |  | [optional] 
**template** | **bool** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sales_order import SalesOrder

# TODO update the JSON string below
json = "{}"
# create an instance of SalesOrder from a JSON string
sales_order_instance = SalesOrder.from_json(json)
# print the JSON string representation of the object
print(SalesOrder.to_json())

# convert the object into a dict
sales_order_dict = sales_order_instance.to_dict()
# create an instance of SalesOrder from a dict
sales_order_from_dict = SalesOrder.from_dict(sales_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


