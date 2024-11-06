# UserCurrentUserGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**User**](User.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_current_user_get200_response import UserCurrentUserGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserCurrentUserGet200Response from a JSON string
user_current_user_get200_response_instance = UserCurrentUserGet200Response.from_json(json)
# print the JSON string representation of the object
print(UserCurrentUserGet200Response.to_json())

# convert the object into a dict
user_current_user_get200_response_dict = user_current_user_get200_response_instance.to_dict()
# create an instance of UserCurrentUserGet200Response from a dict
user_current_user_get200_response_from_dict = UserCurrentUserGet200Response.from_dict(user_current_user_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


