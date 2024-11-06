# MailTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**bcc_email_addresses** | **str** |  | [optional] 
**cc_email_addresses** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**to_email_addresses** | **str** |  | [optional] 
**type** | [**TemplateType**](TemplateType.md) |  | [optional] 
**use_as_default** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.mail_template import MailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplate from a JSON string
mail_template_instance = MailTemplate.from_json(json)
# print the JSON string representation of the object
print(MailTemplate.to_json())

# convert the object into a dict
mail_template_dict = mail_template_instance.to_dict()
# create an instance of MailTemplate from a dict
mail_template_from_dict = MailTemplate.from_dict(mail_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


