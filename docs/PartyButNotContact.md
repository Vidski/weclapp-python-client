# PartyButNotContact


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

## Example

```python
from openapi_client.models.party_but_not_contact import PartyButNotContact

# TODO update the JSON string below
json = "{}"
# create an instance of PartyButNotContact from a JSON string
party_but_not_contact_instance = PartyButNotContact.from_json(json)
# print the JSON string representation of the object
print(PartyButNotContact.to_json())

# convert the object into a dict
party_but_not_contact_dict = party_but_not_contact_instance.to_dict()
# create an instance of PartyButNotContact from a dict
party_but_not_contact_from_dict = PartyButNotContact.from_dict(party_but_not_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


