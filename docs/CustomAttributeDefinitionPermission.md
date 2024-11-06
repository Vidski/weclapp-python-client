# CustomAttributeDefinitionPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_date** | **int** |  | [optional] [readonly] 
**last_modified_date** | **int** |  | [optional] [readonly] 
**version** | **str** |  | [optional] 
**permission_type** | [**CustomAttributeDefinitionPermissionType**](CustomAttributeDefinitionPermissionType.md) |  | [optional] 
**user_role_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.custom_attribute_definition_permission import CustomAttributeDefinitionPermission

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionPermission from a JSON string
custom_attribute_definition_permission_instance = CustomAttributeDefinitionPermission.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionPermission.to_json())

# convert the object into a dict
custom_attribute_definition_permission_dict = custom_attribute_definition_permission_instance.to_dict()
# create an instance of CustomAttributeDefinitionPermission from a dict
custom_attribute_definition_permission_from_dict = CustomAttributeDefinitionPermission.from_dict(custom_attribute_definition_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


