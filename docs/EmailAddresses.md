# EmailAddresses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc_addresses** | **str** |  | [optional] 
**cc_addresses** | **str** |  | [optional] 
**to_addresses** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_addresses import EmailAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddresses from a JSON string
email_addresses_instance = EmailAddresses.from_json(json)
# print the JSON string representation of the object
print(EmailAddresses.to_json())

# convert the object into a dict
email_addresses_dict = email_addresses_instance.to_dict()
# create an instance of EmailAddresses from a dict
email_addresses_from_dict = EmailAddresses.from_dict(email_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


