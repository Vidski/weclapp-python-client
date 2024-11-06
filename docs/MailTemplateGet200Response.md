# MailTemplateGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[MailTemplate]**](MailTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.mail_template_get200_response import MailTemplateGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailTemplateGet200Response from a JSON string
mail_template_get200_response_instance = MailTemplateGet200Response.from_json(json)
# print the JSON string representation of the object
print(MailTemplateGet200Response.to_json())

# convert the object into a dict
mail_template_get200_response_dict = mail_template_get200_response_instance.to_dict()
# create an instance of MailTemplateGet200Response from a dict
mail_template_get200_response_from_dict = MailTemplateGet200Response.from_dict(mail_template_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


