# UserRoleGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[UserRole]**](UserRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_role_get200_response import UserRoleGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleGet200Response from a JSON string
user_role_get200_response_instance = UserRoleGet200Response.from_json(json)
# print the JSON string representation of the object
print(UserRoleGet200Response.to_json())

# convert the object into a dict
user_role_get200_response_dict = user_role_get200_response_instance.to_dict()
# create an instance of UserRoleGet200Response from a dict
user_role_get200_response_from_dict = UserRoleGet200Response.from_dict(user_role_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


