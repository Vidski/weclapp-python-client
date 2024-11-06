# Lead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**custom_attributes** | [**List[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**addresses** | [**List[Address]**](Address.md) |  | [optional] 
**birth_date** | **int** |  | [optional] 
**company** | **str** |  | [optional] 
**company2** | **str** |  | [optional] 
**delivery_address_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**invoice_address_id** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile_phone1** | **str** |  | [optional] 
**online_accounts** | [**List[OnlineAccount]**](OnlineAccount.md) |  | [optional] 
**party_type** | [**PartyType**](PartyType.md) |  | [optional] 
**person_company** | **str** |  | [optional] 
**person_department_id** | **str** |  | [optional] 
**person_role_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**primary_address_id** | **str** |  | [optional] 
**salutation** | [**Salutation**](Salutation.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**title_id** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**commercial_language_id** | **str** |  | [optional] 
**contacts** | [**List[Contact]**](Contact.md) |  | [optional] 
**currency_id** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**primary_contact_id** | **str** |  | [optional] 
**sector_id** | **str** |  | [optional] 
**sector_name** | **str** |  | [optional] 
**annual_revenue** | **decimal.Decimal** |  | [optional] 
**company_size_id** | **str** |  | [optional] 
**company_size_name** | **str** |  | [optional] 
**customer_category_id** | **str** |  | [optional] 
**customer_category_name** | **str** |  | [optional] 
**parent_party_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**payment_method_name** | **str** |  | [optional] 
**responsible_user_id** | **str** |  | [optional] 
**responsible_user_username** | **str** |  | [optional] 
**shipment_method_id** | **str** |  | [optional] 
**shipment_method_name** | **str** |  | [optional] 
**term_of_payment_id** | **str** |  | [optional] 
**term_of_payment_name** | **str** |  | [optional] 
**vat_registration_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**lead_number** | **str** |  | [optional] 
**lead_rating_id** | **str** |  | [optional] 
**lead_rating_name** | **str** |  | [optional] 
**lead_source_id** | **str** |  | [optional] 
**lead_source_name** | **str** |  | [optional] 
**lead_status** | [**LeadStatus**](LeadStatus.md) |  | [optional] 
**lead_topics** | [**List[Entity]**](Entity.md) |  | [optional] 
**loss_description** | **str** |  | [optional] 
**loss_reason_id** | **str** |  | [optional] 
**loss_reason_name** | **str** |  | [optional] 
**old_lead_number** | **str** |  | [optional] 
**opt_in** | **bool** |  | [optional] 
**opt_in_letter** | **bool** |  | [optional] 
**opt_in_phone** | **bool** |  | [optional] 
**opt_in_sms** | **bool** |  | [optional] 
**responsible_user_fixed** | **bool** |  | [optional] 
**sales_channel** | [**DistributionChannel**](DistributionChannel.md) |  | [optional] 
**sales_stage_id** | **str** |  | [optional] 
**sales_stage_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.lead import Lead

# TODO update the JSON string below
json = "{}"
# create an instance of Lead from a JSON string
lead_instance = Lead.from_json(json)
# print the JSON string representation of the object
print(Lead.to_json())

# convert the object into a dict
lead_dict = lead_instance.to_dict()
# create an instance of Lead from a dict
lead_from_dict = Lead.from_dict(lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


