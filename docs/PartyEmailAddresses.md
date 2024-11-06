# PartyEmailAddresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**bcc_addresses** | **str** |  | [optional] 
**cc_addresses** | **str** |  | [optional] 
**to_addresses** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.party_email_addresses import PartyEmailAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of PartyEmailAddresses from a JSON string
party_email_addresses_instance = PartyEmailAddresses.from_json(json)
# print the JSON string representation of the object
print(PartyEmailAddresses.to_json())

# convert the object into a dict
party_email_addresses_dict = party_email_addresses_instance.to_dict()
# create an instance of PartyEmailAddresses from a dict
party_email_addresses_from_dict = PartyEmailAddresses.from_dict(party_email_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


