# Contract


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
**additional_addresses** | [**List[ContractAdditionalAddress]**](ContractAdditionalAddress.md) |  | [optional] 
**authorization_unit_id** | **str** |  | [optional] 
**automatic_extension** | **bool** |  | [optional] 
**bill_until** | [**BillUntil**](BillUntil.md) |  | [optional] 
**billing_day** | **int** |  | [optional] 
**billing_target_invoice_status** | [**DesiredInvoiceStatusType**](DesiredInvoiceStatusType.md) |  | [optional] 
**billing_type** | [**ContractBillingType**](ContractBillingType.md) |  | [optional] 
**cancellation_date** | **int** |  | [optional] 
**cancellation_period_quantity** | **int** |  | [optional] 
**cancellation_period_softframe** | [**ContractSoftframe**](ContractSoftframe.md) |  | [optional] 
**cancellation_period_unit** | [**ContractUnitType**](ContractUnitType.md) |  | [optional] 
**commission** | **str** |  | [optional] 
**commission_sales_partners** | [**List[CommissionSalesPartner]**](CommissionSalesPartner.md) |  | [optional] 
**contract_cost_items** | [**List[ContractCostItem]**](ContractCostItem.md) |  | [optional] 
**contract_date** | **int** |  | [optional] 
**contract_items** | [**List[ContractItem]**](ContractItem.md) |  | [optional] 
**contract_number** | **str** |  | [optional] 
**contract_number_at_party** | **str** |  | [optional] 
**contract_status** | [**ContractStatus**](ContractStatus.md) |  | [optional] 
**correspondence_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**delivery_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**delivery_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**differing_correspondence_address** | **bool** |  | [optional] 
**differing_delivery_address** | **bool** |  | [optional] 
**differing_invoice_address** | **bool** |  | [optional] 
**end_date** | **int** |  | [optional] 
**extension_quantity** | **int** |  | [optional] 
**extension_unit** | [**ContractUnitType**](ContractUnitType.md) |  | [optional] 
**factoring** | **bool** |  | [optional] 
**invoice_address** | [**RecordAddress**](RecordAddress.md) |  | [optional] 
**invoice_recipient_id** | **str** |  | [optional] 
**latest_cancellation_warning_quantity** | **int** |  | [optional] 
**latest_cancellation_warning_unit** | [**ContractUnitType**](ContractUnitType.md) |  | [optional] 
**latest_possible_termination_date** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**next_contract_billing_date** | **int** |  | [optional] 
**non_standard_input_tax_id** | **str** |  | [optional] 
**order_number_at_customer** | **str** |  | [optional] 
**party_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**pricing_date** | **int** |  | [optional] 
**purchase_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**record_currency_id** | **str** |  | [optional] 
**record_currency_name** | **str** |  | [optional] 
**record_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**reminder_date** | **int** |  | [optional] 
**reminder_send_type** | [**ReminderSendType**](ReminderSendType.md) |  | [optional] 
**reminder_type** | [**CDBReminderType**](CDBReminderType.md) |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**sales_invoice_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**sales_order_email_addresses** | [**EmailAddresses**](EmailAddresses.md) |  | [optional] 
**start_date** | **int** |  | [optional] 
**template** | **bool** |  | [optional] 
**term_of_payment_id** | **str** |  | [optional] 
**termination_reason_id** | **str** |  | [optional] 
**ticket_service_level_agreement_id** | **str** |  | [optional] 
**types** | [**List[OnlyId]**](OnlyId.md) |  | [optional] 
**unlimited** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.contract import Contract

# TODO update the JSON string below
json = "{}"
# create an instance of Contract from a JSON string
contract_instance = Contract.from_json(json)
# print the JSON string representation of the object
print(Contract.to_json())

# convert the object into a dict
contract_dict = contract_instance.to_dict()
# create an instance of Contract from a dict
contract_from_dict = Contract.from_dict(contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


