# ArchivedEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**bcc_addresses** | **List[str]** |  | [optional] 
**body** | **str** |  | [optional] 
**cc_addresses** | **List[str]** |  | [optional] 
**from_address** | **str** |  | [optional] 
**message_identifier** | **str** |  | [optional] 
**received_date** | **int** |  | [optional] 
**reply_to_address** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**to_addresses** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.archived_email import ArchivedEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivedEmail from a JSON string
archived_email_instance = ArchivedEmail.from_json(json)
# print the JSON string representation of the object
print(ArchivedEmail.to_json())

# convert the object into a dict
archived_email_dict = archived_email_instance.to_dict()
# create an instance of ArchivedEmail from a dict
archived_email_from_dict = ArchivedEmail.from_dict(archived_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


