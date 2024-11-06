# CustomAttributeDefinitionGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[CustomAttributeDefinition]**](CustomAttributeDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_get200_response import CustomAttributeDefinitionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionGet200Response from a JSON string
custom_attribute_definition_get200_response_instance = CustomAttributeDefinitionGet200Response.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionGet200Response.to_json())

# convert the object into a dict
custom_attribute_definition_get200_response_dict = custom_attribute_definition_get200_response_instance.to_dict()
# create an instance of CustomAttributeDefinitionGet200Response from a dict
custom_attribute_definition_get200_response_from_dict = CustomAttributeDefinitionGet200Response.from_dict(custom_attribute_definition_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


