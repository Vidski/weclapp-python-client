# CommentGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Comment]**](Comment.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_get200_response import CommentGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommentGet200Response from a JSON string
comment_get200_response_instance = CommentGet200Response.from_json(json)
# print the JSON string representation of the object
print(CommentGet200Response.to_json())

# convert the object into a dict
comment_get200_response_dict = comment_get200_response_instance.to_dict()
# create an instance of CommentGet200Response from a dict
comment_get200_response_from_dict = CommentGet200Response.from_dict(comment_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


