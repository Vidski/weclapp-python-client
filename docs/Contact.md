# Contact


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
**customer_category_id** | **str** |  | [optional] 
**customer_category_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fix_phone2** | **str** |  | [optional] 
**mobile_phone2** | **str** |  | [optional] 
**opt_in** | **bool** |  | [optional] 
**opt_in_letter** | **bool** |  | [optional] 
**opt_in_phone** | **bool** |  | [optional] 
**opt_in_sms** | **bool** |  | [optional] 
**phone_home** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


